#!/usr/bin/env python
"""
Script to fetch citation counts from Google Scholar and store them in _data/citations.yml
This script is designed to be run by a GitHub Action.

The papers are keyed by a stable title-based slug (not by Google Scholar paper ID),
because paper IDs change when you delete and re-add papers on Google Scholar.
The scholar_id is still stored as a field for reference and URL building.
"""

import os
import re
import yaml
import time
import random
from datetime import datetime
from scholarly import scholarly

# Configuration
SCHOLAR_USER_ID = "-9_KI-wAAAAJ"  # Your Google Scholar ID
OUTPUT_FILE = "_data/citations.yml"
MAX_RETRIES = 3

# Create data directory if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)


def slugify(title):
    """
    Generate a URL-friendly slug from a paper title.
    Mimics Jekyll's `slugify` filter (default mode):
    - lowercase
    - replace sequences of non-word characters with a single hyphen
    - collapse multiple consecutive hyphens
    - strip leading/trailing hyphens
    
    Jekyll's implementation in Ruby:
      string.downcase.gsub(/[^\w]/, '-').gsub(/-+/, '-').gsub(/^-|-$/, '')
    """
    # Convert to lowercase
    slug = title.lower()
    # Replace any sequence of non-word characters (not a-z, 0-9, or _) with a single hyphen
    slug = re.sub(r'[^a-z0-9_]+', '-', slug)
    # Collapse multiple consecutive hyphens into one
    slug = re.sub(r'-+', '-', slug)
    # Strip leading/trailing hyphens
    slug = slug.strip('-')
    return slug

def get_scholar_citations():
    """
    Fetch citation data from Google Scholar for all papers by the specified author.
    Papers are keyed by title slug (stable) rather than Google Scholar paper ID (volatile).
    """
    print(f"Fetching citations for Google Scholar ID: {SCHOLAR_USER_ID}")
    
    # Initialize citation data structure
    citation_data = {
        'metadata': {
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        'papers': {}  # Keyed by title slug for stability
    }
    
    # Try to load existing data to preserve citation counts for papers
    # that might not be fetched this time (e.g. due to rate limiting)
    existing_papers = {}
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f:
                existing_data = yaml.safe_load(f)
                if existing_data and isinstance(existing_data, dict):
                    if 'papers' in existing_data and existing_data['papers'] is not None:
                        existing_papers = existing_data['papers']
                        print(f"Loaded {len(existing_papers)} existing paper entries")
        except Exception as e:
            print(f"Warning: Could not read existing citation data: {e}")

    # Fetch author data with retries
    author_data = None
    for attempt in range(MAX_RETRIES):
        try:
            author = scholarly.search_author_id(SCHOLAR_USER_ID)
            print("Try to fetch author id: " + SCHOLAR_USER_ID)
            author_data = scholarly.fill(author)
            break
        except Exception as e:
            wait_time = (2 ** attempt) + random.uniform(0, 1)  # Exponential backoff
            print(f"Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying in {wait_time:.1f} seconds...")
                time.sleep(wait_time)
            else:
                print("All retries failed. Using existing data if available.")
                # Return existing data on total failure
                if existing_papers:
                    citation_data['papers'] = existing_papers
                    citation_data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    citation_data['metadata']['note'] = 'Data NOT updated - fetch failed'
                return citation_data
    
    if not author_data:
        print("Could not fetch author data")
        if existing_papers:
            citation_data['papers'] = existing_papers
        return citation_data
        
    # Process publications
    if 'publications' in author_data:
        for pub in author_data['publications']:
            try:
                # Get publication ID (the volatile Google Scholar paper ID)
                pub_id = None
                if 'author_pub_id' in pub and pub['author_pub_id']:
                    pub_id = pub['author_pub_id']
                elif 'pub_id' in pub and pub['pub_id']:
                    pub_id = pub['pub_id']
                
                # Strip the user ID prefix if present (e.g. "-9_KI-wAAAAJ:XXXX" -> "XXXX")
                # This matches the format used in papers.bib's google_scholar_id field
                short_pub_id = pub_id or ''
                if short_pub_id and ':' in short_pub_id:
                    short_pub_id = short_pub_id.split(':', 1)[1]
                
                # Get publication metadata
                title = "Unknown Title"
                year = "Unknown Year"
                citations = 0
                
                if 'bib' in pub:
                    if 'title' in pub['bib']:
                        title = pub['bib']['title']
                    if 'pub_year' in pub['bib']:
                        year = pub['bib']['pub_year']
                
                if 'num_citations' in pub:
                    citations = pub['num_citations']
                
                # Generate stable key from title slug
                title_slug = slugify(title)
                if not title_slug:
                    # Fallback: use pub_id if title slug is empty
                    title_slug = pub_id or f"unknown-{hash(title) % 10000}"
                
                print(f"Found: {title} ({year}) - Citations: {citations} -> slug: {title_slug}")
                
                # Store citation data keyed by title slug (stable)
                citation_data['papers'][title_slug] = {
                    'title': title,
                    'year': year,
                    'citations': citations,
                    'scholar_id': short_pub_id,  # Paper ID only, no user prefix
                }
                
            except Exception as e:
                print(f"Error processing publication: {str(e)}")
    else:
        print("No publications found in author data")
    
    # Save to YAML file
    try:
        with open(OUTPUT_FILE, 'w') as f:
            yaml.dump(citation_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"Citation data saved to {OUTPUT_FILE} ({len(citation_data['papers'])} papers)")
    except Exception as e:
        print(f"Error saving citation data: {str(e)}")
    
    return citation_data

if __name__ == "__main__":
    get_scholar_citations()
