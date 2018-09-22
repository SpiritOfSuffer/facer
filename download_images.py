from bs4 import BeautifulSoup
import urllib.request
import os
import time

URL = "https://2ch.hk/soc/res/4647830.html"

def get_html():
    with urllib.request.urlopen(URL) as url:
        html = url.read()
        return html

def get_imgs(html):
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.findAll("div", {"class":"image-link"})
    print("Collecting images...")

    for div in divs:
        fileUrl = "https://2ch.hk" + div.a['href']

        if fileUrl.endswith(".png") or fileUrl.endswith(".jpg") or fileUrl.endswith(".gif"):
            urllib.request.urlretrieve(fileUrl, fileUrl.split("/", 6)[6])
            print(fileUrl.split("/", 6)[6] + " was saved successfully.")
        time.sleep(1)
    print("Done!")



def main():
    html = get_html()
    get_imgs(html)


if __name__ == "__main__":
    main()
