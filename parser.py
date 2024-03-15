import requests
from bs4 import BeautifulSoup

url = "https://stopgame.ru/"
request = requests.get(url)
print(request.status_code)

soup = BeautifulSoup(request.text,"html.parser")

with open("links.txt", "w+",encoding="UTF-8") as file3:
    links = soup.find_all("a")
    print(f"ССЫЛКИ {'-'*100} \n{links}")
    file3.write(f"{links}")
print("_" * 100)
with open("image.txt", "w+",encoding="UTF-8") as file2:
    image = soup.find_all("img")
    print(f"КАРТИНКИ {'_'*85} \n{image}")
    file2.write(f"{image}")
with open("class.txt", "w+",encoding="UTF-8") as file1:
    clas = soup.find_all(class_=True)
    #print(f"КЛАССЫ {'_' * 85} \n{clas}")
    file1.write(f"{clas}")

with open("text.txt", "w+",encoding="UTF-8") as file:
    file.write(soup.text)

