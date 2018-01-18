
import urllib.request
import random
from urllib.request import urlretrieve
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def getURL(site,tag):

	tag = tag.replace(" ","+")
	url = rl+"/search?q=%s&search_image="%tag
	#url = "https://alpha.wallhaven.cc/search?q=water+fall&search_image="
	store = requests.get(url)
	soup = BeautifulSoup(store.content,"html.parser")
	links = soup.find_all("a")
	finallist=[]
	for link in links :
		s = str(link)
	
		if "wallpaper"  in s:
			#print(link.get("href"))
			#urllib.request.urlretrieve(link.get("href").jpg, "grub.jpg")
			finallist.append((link.get("href")))
			#finallist.append((link.get("href")))
	#print(finallist)
	a =random.choice(finallist)
	if a[len(a)-7  ]=="/":
		b = a[len(a)-6:]
	else:
		b=  a[len(a)-16:len(a)-10]
	#print(b)
	sss ="https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.png"%b
	#print(sss)
	#print(asdf)
	#..................................................everything below this is to download the file but it isn't working yet
	#asdf = asdf+".jpg"									
	#urllib.request.urlopen(asdf, "grub.jpg")
	urllib.request.urlretrieve(sss, "local-filename.png")
	'''resource = urllib.request.urlopen("https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-612125.jpg")
	output = open("file01.jpg","wb")
	output.write(resource.read())
	output.close()'''
	#urllib.urlretrieve(asdf,"grubimg.jpg")
	#data = urllib.request.urlretrieve("https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-612125.jpg")
	return
rl = input("enter the website url   'the code is made to work for https://alpha.wallhaven.cc'   ")
tag = input("enter the topic/tag")
getURL(rl,tag)
