import urllib
import re

emails = []

website = urllib.urlopen("http://www.mit.edu/")
webData = website.read()

print "Please wait...this may take a few minutes"

#find all links on website
links = re.findall('"(http://.*?)"', webData)

#identify emails based on pattern
pattern = re.compile("\w+-?\w+@\w+\.\w+")

for link in links:
	webpage = urllib.urlopen(link)
	webpageData = webpage.read()
	emails.extend(re.findall(pattern, webpageData))
	
emails = list(set(emails))

#Display emails
print "Found these emails:"
for email in emails:
	print "\n", email
