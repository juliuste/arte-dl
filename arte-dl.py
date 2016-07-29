# encoding: utf-8

import feedparser
import youtube_dl
import os.path

config = {
	'feed': 'http://www.arte.tv/papi/tvguide-flow/feeds/videos/de.xml?type=ARTE_PLUS_SEVEN&player=true',
	'categories': ['Dokumentation', 'Dokumentationsreihe'],
	'list-path': 'id.list'
}


ids = []

if os.path.exists(config['list-path']) and os.path.isfile(config['list-path']):
	f = open(config['list-path'], 'r')
	for line in f:
		ids.append(line.strip())
	f.close()

mediathek = feedparser.parse(config['feed'])['items']

downloadLinks = []

for sendung in mediathek:
	if ((sendung['category'] in config['categories']) or (len(config['categories'])==0)) and not (sendung['link'] in ids):
		downloadLinks.append(sendung['link'])

print('Scanning complete. '+str(len(downloadLinks))+' Video(s) will be downloaded.')

ids.extend(downloadLinks)

f = open(config['list-path'], 'w')
for i in ids:
	f.write(i+"\n")
f.close()

if len(downloadLinks)>0:
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(downloadLinks)

print('Done. Downloaded '+str(len(downloadLinks))+' Video(s).')