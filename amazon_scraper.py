import bs4
import html5lib
import requests
product=input()
url="https://www.amazon.in/s?k="
url+=product
r=requests.get(url)
soup=bs4.BeautifulSoup(r.content)
classhtml=soup.findAll('div',{'class':'a-section aok-relative s-image-fixed-height'})
for idx,allclass in enumerate(classhtml):
    with open("amazon_{}_images{}.jpg".format(product,idx),"wb") as f:
        imgurl=allclass.img.attrs['src']
        imgresponse=requests.get(imgurl)
        f.write(imgresponse.content)