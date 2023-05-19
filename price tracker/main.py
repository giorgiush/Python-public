from bs4 import BeautifulSoup
import requests


headers = {"Accept-Language":"en-US,en;q=0.9", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

response = requests.get(headers=headers, url="https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTSSR2/ref=sr_1_1_sspa?crid=1AWAC2EIBBQZE&keywords=ninja%2Brice%2Bcooker&qid=1676171288&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5T0VJM0UxSVBSSFEmZW5jcnlwdGVkSWQ9QTAxNjQyNTFGNEVBNjNZSllDUDgmZW5jcnlwdGVkQWRJZD1BMDc5NjkyMzkzMkJUWUpFVlBCVSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")
contents = response.text

soup = BeautifulSoup(contents, "lxml")
print(soup.find(name="span", class_="a-offscreen").text)