#Importing required libraries and modules.
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

count = 0
def Start():
    global count
    search = input("Enter Your Search for:")
    print("Downloading...Please wait!")
    params = {"q": search}
    dir_name = search.replace(" ","-").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a",{"class":"thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Downloading ", item.attrs["href"])
            title =item.attrs["href"].split("/")[-1]
            try:
                img =Image.open(BytesIO(img_obj.content))
                img.save("./"+ dir_name + "/" + title, img.format)
                count = count + 1
            except:
                print("Sorry! This Image could not be saved.")
        except:
            print("Sorry! could not request Image from Server.")
    print()      
    print("Download Finished."+ str(count) + " Files Downloaded.")
    Start()
    
Start()