#!/usr/bin/python
import re
import sys
import urllib2
import signal
from bs4 import BeautifulSoup

# Constants
url = "https://stackoverflow.com"
so_search_url = "https://stackoverflow.com/search?q="
answer_block_class = "post-text"
result_div_class = "result-link"
number_of_threads = 4

# Vars
all_links = []
search_string = ""
class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'


def handler(signum, frame):
	print "\nGot a CTRL+C. \nExiting now."
	sys.exit()

signal.signal(signal.SIGINT, handler)

# Check for arguments:
if len(sys.argv) < 2:
	print "Need something to search for..."
	sys.exit()

# Build search query
for item in sys.argv[1:]:
	search_string += item + "+"
search_string = search_string[:-1]

# Getting the initial search
text = urllib2.urlopen(so_search_url + search_string).read()
soup = BeautifulSoup(text)

# Get the class 'result-link' from the item
data = soup.findAll(name="div", attrs={'class': result_div_class})
for div in data:
	links = div.findAll('a')
	for a in links:
		# Extract links and add to issue
		all_links.append(url + a['href'])

# Check
if number_of_threads == 0:
	print(color.RED + "Nothing found..." + color.END)
	sys.exit(0)

# Get the actual answers:
for i in range(1, number_of_threads, 1):

	text = urllib2.urlopen(all_links[i]).read()
	soup = BeautifulSoup(text)

	title = soup.find(name="h1", attrs={'itemprop': "name"})
	print "\n" + color.BOLD + "Thread: " + title.string + color.END
	print color.RED + str(all_links[i])
	print "-----------------------------------------------------------"+ color.END

	data = soup.findAll(name="div", attrs={'class': answer_block_class})

	for elem in data:
		all_text = elem.findAll(name="p")
		all_codes = elem.findAll(name="code")
		for each in all_codes:
			print color.BLUE + "Code Snippet\n--------------" + color.END
			print each.string

	raw_input("Press a key to see the next.")
