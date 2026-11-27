"""
Create a `crawler.py` file and define the skeleton of the crawling algorithm:
Crawl (=get and parse) all HTML pages on a certain server
that can directly or indirectly be reached from a start URL
by following links on the pages.
Do not follow links to URLs on other servers and only process HTML responses.
Test the crawler with a simple website, e.g., https://info.cern.ch/hypertext/WWW/TheProject.html
"""

# Crawling algorithm

# Initialize stack with start URL
# While stack is not empty:
    # Pop first URL
    # If not visited recently:
        # Get the content
        # Analyse it and updates the index
        # Analyse it, find links to other websites and add links to stack (push)
        # Update visited lst
