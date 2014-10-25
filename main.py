#!/usr/bin/python

import os
import urllib2
import json
import sys , getopt
import re



def download_song_from_list(track_info):
	title = re.sub("\W+","_",track_info["title"])
	print "Downloading: "+track_info["title"]+"."+track_info["original_format"]
	command ="curl -# -L --user-agent 'Mozilla/5.0' -o "+title+"."+track_info["original_format"]+" "+track_info["stream_url"]+"?client_id=b45b1aa10f1ac2941910a7f0d10f8e28" 
	os.system(command)

def download_song(url):
	client_id = "d547390094416db503b228c531022ae8"
	resolver_url = "https://api.soundcloud.com/resolve.json?url="+url+"&client_id="+client_id
	request = urllib2.Request(resolver_url)
	response = urllib2.urlopen(request)
	result = response.read()
	json_result = json.loads(result)
	title = re.sub("\W+","_",json_result["title"])
	print "Downloading: "+json_result["title"]+"."+json_result["original_format"]
	command ="curl -# -L --user-agent 'Mozilla/5.0' -o "+title+"."+json_result["original_format"]+" "+json_result["stream_url"]+"?client_id=b45b1aa10f1ac2941910a7f0d10f8e28" 
	os.system(command)

def download_list(url):
	client_id = "d547390094416db503b228c531022ae8"
	resolver_url = "https://api.soundcloud.com/resolve.json?url="+url+"&client_id="+client_id
	request = urllib2.Request(resolver_url)
	response = urllib2.urlopen(request)
	result = response.read()
	json_result = json.loads(result)
	tracks = json_result["tracks"]
	for track in tracks:
		download_song_from_list(track)


def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hl:s:")
	except getopt.GetoptError:
		print "For downloading a song: $python main.py -s <url>"
		print "For downloading a list: $python main.py -l <url>" 
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-s":
			download_song(arg)
		elif opt == "-h":
			print "For downloading a song: $python main.py -s <url>"
			print "For downloading a list: $python main.py -l <url>"
		elif opt == "-l":
			download_list(arg)
if __name__=="__main__":
	main(sys.argv[1:])



