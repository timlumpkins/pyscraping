#contact!
from lxml import html
import requests

job_page = requests.get('http://stlouis.craigslist.org/search/jjj?query=python')
job_tree = html.fromstring(job_page.text)

#This will create a list of listings:
job_listings = job_tree.xpath('//div/div/p/span/span[@class="pl"]/a/text()')
raw_job_url = job_tree.xpath('//div/div/p/span/span[@class="pl"]/a/@href')

#fixing the URLs to display correctly if they don't start with http
job_url = []
for url in raw_job_url:
    if url.startswith('/'):
        job_url.append("http://stlouis.craigslist.org" + url)
    else:
        job_url.append(url) 

#This prints the titles of the job posts
print str(len(job_listings)) + ' Job Listings:\n', '\n'.join(job_listings)

#This adds a new line and prints the corresponding URLs
print '\n' + str(len(job_listings)) + ' Job URLs:\n', '\n'.join(job_url)
