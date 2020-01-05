import img2pdf, requests, os, time
from PIL import Image 
from io import BytesIO
import urllib.request
from bs4 import BeautifulSoup
manga_url = 'https://mangakakalot.com/manga/gk919264' # spectify your url here
vol_chapter_urls = []
img_urls = []
imgs = []
def get_vol_chapter_urls():
	response = requests.get(manga_url)
	soup = BeautifulSoup(response.text, 'html.parser')
	chapters = soup.find("div", class_="chapter-list").find_all("div", class_="row")
	for i in range(len(chapters)):
		if(chapters[i].find("a").getText()[:5] == "Vol.1"): #specify your volume here
			vol_chapter_urls.append(chapters[i].find("a").get('href'))

get_vol_chapter_urls()
vol_chapter_urls.reverse()

def get_image_urls():
	for i in range(len(vol_chapter_urls)):
		response = requests.get(vol_chapter_urls[i])
		soup = BeautifulSoup(response.text, 'html.parser')
		m = soup.find("div", id='vungdoc').find_all("img")
		for y in range(len(m)):
			a = m[y].get('src')
			img_urls.append(a)
get_image_urls()

# for m in range(len(img_urls)):
# 	with open(str(m)+'.jpg', 'wb') as handler:
# 		handler.write(requests.get(img_urls[m]).content)

file = open("YOUR_PDF.pdf", "wb")
for l in range(len(img_urls)):
	# print(img_urls[l])
	req = urllib.request.Request(img_urls[l], headers={'User-Agent': 'Mozilla/5.0'}) # so server wont reject our request
	image = (urllib.request.urlopen(req))
	imgs.append(image)
pdf_bytes = img2pdf.convert(imgs)  
file.write(pdf_bytes)
image.close() 
file.close() 
print("Successfully made pdf file")
