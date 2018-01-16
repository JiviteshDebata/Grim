
import urllib
import random
#from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
rl = input("enter the website url   'the code is made to work for https://alpha.wallhaven.cc'")
tag = input("enter the topic/tag")
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
		finallist.append(str(link.get("href")))
		#finallist.append((link.get("href")))
#print(finallist)
asdf =random.choice(finallist)
print(asdf)
#..................................................everything below this is to download the file but it isn't working yet
#asdf = asdf+".jpg"									
#urllib.request.urlopen(asdf, "grub.jpg")
'''resource = urllib.request.urlopen(asdf)
output = open("file01.jpg","wb")
output.write(resource.read())
output.close()'''
#urllib.urlretrieve(asdf,"grubimg.jpg")