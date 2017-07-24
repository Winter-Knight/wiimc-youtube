#!/usr/bin/python

import cgi
form = cgi.FieldStorage()

import re
import httplib
import urllib
import subprocess
import sys
import os

# IMPORTANT: This directory must exist, and the web user must have full access to it
media_dir = "/var/www/media/"

if ("query" not in form and "watch" not in form):
	print("Content-type: text/plain\n")
	print("No search query entered.")
	exit

if ("watch" in form):
	watch = str(form["watch"].value)
	outfile = media_dir + watch + ".mp4"
	subprocess.call(["youtube-dl", "-f", "18", "-o", outfile, "https://www.youtube.com/watch?v=" + watch], stdout = open("/dev/null", "w"))
	print("Content-type: video/mp4")
	print("Content-Length: " + str(os.path.getsize(outfile)) + "\n")
	f = open(outfile)
	while (True):
		chunk = f.read(1048576)
		if (len(chunk) == 0):
			f.close()
			break
		sys.stdout.write(chunk)
	exit


query = str(form["query"].value)

conn = httplib.HTTPSConnection("www.youtube.com")
conn.request("GET", "/results?search_query=" + urllib.quote(query))
res = conn.getresponse()
ytlines = res.read().split("\n")
conn.close()

names = []
urls = []
for i in ytlines:
	m = re.search('/watch\?v=[^"]*"[^>]*title="[^"]*"', i)
	if (m):
		if (re.search('ypc-badge', i)):
			continue
		m = i[m.start():m.end()]
		names.append(re.sub('/watch\?v=([^"]*)".*title="([^"]*)".*', r'\2', m))
		urls.append(re.sub('/watch\?v=([^"]*)".*title="([^"]*)".*', r'\1', m))

print("Content-type: text/plain\n")
for i,j in zip(names, urls):
	print("youtube.py?watch=" + j + "&videoname=/" + i)
