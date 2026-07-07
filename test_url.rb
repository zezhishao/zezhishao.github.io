page_url = "/zh/people/index.html"
puts page_url.sub(%r{^/zh}, "")
puts page_url.sub(%r{^/(zh|en)}, "")
