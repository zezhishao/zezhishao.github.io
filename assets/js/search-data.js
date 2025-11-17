// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "GitHub repositories",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-people",
          title: "People",
          description: "members of the lab or group",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-patchstg-is-accepted-by-kdd-25-sparkles",
          title: 'PatchSTG is accepted by KDD’25!:sparkles:',
          description: "",
          section: "News",},{id: "news-basicts-is-accepted-by-tkde-sparkles",
          title: 'BasicTS+ is accepted by TKDE!:sparkles:',
          description: "",
          section: "News",},{id: "news-one-commentary-about-spatial-temporal-large-models-for-science-is-accepted-by-the-innovation-if-25-7-sparkles",
          title: 'One commentary about Spatial-Temporal Large Models for Science is accepted by The Innovation...',
          description: "",
          section: "News",},{id: "news-ginar-is-accepted-by-tkde-sparkles",
          title: 'GinAR+ is accepted by TKDE!:sparkles:',
          description: "",
          section: "News",},{id: "news-one-amazing-review-about-decision-intelligence-is-accepted-by-the-innovation-if-25-7-sparkles",
          title: 'One amazing review about Decision Intelligence is accepted by The Innovation (IF: 25.7)!...',
          description: "",
          section: "News",},{id: "news-review-of-foundation-model-and-decision-intelligence-is-selected-as-cover-paper",
          title: 'Review of Foundation Model and Decision Intelligence is selected as Cover Paper!',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_0512/";
            },},{id: "news-hutformer-is-accepted-by-commtr-if-14-5-sparkles",
          title: 'HUTFormer is accepted by COMMTR (IF: 14.5)!:sparkles:',
          description: "",
          section: "News",},{id: "news-two-papers-blast-and-merlin-are-accepted-by-kdd-25-sparkles",
          title: 'Two papers, BLAST and Merlin, are accepted by KDD’25!:sparkles:',
          description: "",
          section: "News",},{id: "news-one-tutorial-about-mts-heterogeneity-has-been-accepted-by-sstd-2025",
          title: 'One Tutorial about MTS heterogeneity has been Accepted by SSTD 2025！',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_0709/";
            },},{id: "news-one-tkde-paper-about-mts-heterogeneity-has-entered-esi-high-cited-papers",
          title: 'One TKDE paper about MTS heterogeneity has entered ESI high cited papers!',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_0715/";
            },},{id: "news-sta-gann-is-accepted-by-cikm-25-sparkles",
          title: 'STA-GANN is accepted by CIKM’25!:sparkles:',
          description: "",
          section: "News",},{id: "news-three-papers-selective-learning-stella-and-smartraj2-are-accepted-by-neurips-25-sparkles",
          title: 'Three papers, Selective Learning, STELLA, and SMARTraj2, are accepted by NeurIPS’25!:sparkles:',
          description: "",
          section: "News",},{id: "news-apt-is-accepted-by-aaai-25-sparkles",
          title: 'APT is accepted by AAAI’25!:sparkles:',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=-9_KI-wAAAAJ", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/zezhishao", "_blank");
        },
      },{
        id: 'social-dblp',
        title: 'DBLP',
        section: 'Socials',
        handler: () => {
          window.open("https://dblp.org/pid/291/7158.html", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0002-0815-2768", "_blank");
        },
      },{
        id: 'social-semanticscholar',
        title: 'Semantic Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://www.semanticscholar.org/author/2088909840", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%73%68%61%6F%7A%65%7A%68%69@%69%63%74.%61%63.%63%6E", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
