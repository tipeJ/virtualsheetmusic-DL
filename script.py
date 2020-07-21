from bs4 import BeautifulSoup
import requests
import urllib
import os

target_url = input("Enter Target URL:")

r = requests.get(target_url)

parsed_html = BeautifulSoup(r.text)
id_element = parsed_html.find(id="s_id")
id = id_element['value']

url_token_element = parsed_html.find(id="audioselect").find_all('option')
url_token_list = url_token_element[0]['value'].split('/')
url_token = url_token_list[len(url_token_list)-3] + '/' + url_token_list[len(url_token_list)-2]
print(url_token)

pageCountElement = parsed_html.find(id="navbarpg")
pageCount = pageCountElement.text.strip().replace("Page  of ", "")

directory = url_token.replace("/", " - ")
try:
    os.stat(directory)
except:
    os.mkdir(directory)

for i in range(1, int(pageCount) + 1):
    url = "https://media.virtualsheetmusic.com/imgprev/%s/%s/%s.svg" % (id, url_token, str(i))
    print("Downloading: %s" % i)
    hdr = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
    }
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('Connection', 'keep-alive'),
        ('Referer', 'https://www.virtualsheetmusic.com/')
    ]
    urllib.request.install_opener(opener)
    filename = "%s/sheet %s.svg" % (directory, str(i))
    urllib.request.urlretrieve(url, filename)
    
print("Downloads finished!")