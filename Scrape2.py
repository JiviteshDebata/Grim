
import random

import requests
from bs4 import BeautifulSoup

def getURL(site,tag):

	tag = tag.replace(" ","+")
	url = rl+"/search?q=%s&search_image="%tag
	
	store = requests.get(url)
	soup = BeautifulSoup(store.content,"html.parser")
	links = soup.find_all("a")
	finallist=[]
	for link in links :
		s = str(link)
	
		if "wallpaper"  in s:
			
			finallist.append((link.get("href")))
			
	a =random.choice(finallist)
	if a[len(a)-7  ]=="/":
		b = a[len(a)-6:]
	else:
		b=  a[len(a)-16:len(a)-10]
	ppp ="https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg"%b
	rr = requests.get(ppp, allow_redirects=True)
	open('grub.jpg', 'wb').write(rr.content)
	
	
rl = input("enter the website url   https://alpha.wallhaven.cc   ")
tag = input("enter the topic/tag")
getURL(rl,tag)