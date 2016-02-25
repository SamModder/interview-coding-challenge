from bs4 import BeautifulSoup
import requests
import requests.exceptions
import re
import urllib


emails = []
website = requests.get("http://www.mit.edu/")



#find links
soup = BeautifulSoup(website.text,"html.parser")

links = soup.find_all("a")



for link in links:
	link = link.get('href')
	print ("processing " + link)
	try:
        	webpagedata = requests.get(link)
    	# ignore pages with errors
    	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
       
        	continue
	#look for emails
	pattern = re.compile(r"\w+-?\w+@\w+\.\w+")
	emails.extend(re.findall(pattern, webpagedata.text))
	
emails = list(set(emails))

print "\nFound these emails:"
for email in emails:
	print "\n", email
