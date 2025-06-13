import requests
import os


url = "http://automation:9001/listfull/my-dd-course?keys=%7B%22title%22%3A1%2C%22key%22%3A1%7D"
rs = requests.get(url)
data = rs.json()

folder = "./course"
if not os.path.exists(folder):
    os.mkdir(folder)


titles = [i for i in data if i['title'].startswith("200. course/")]

url = "http://automation:9001/get/my-dd-course"

for t in titles:
    title = t['title'][len("200. course/"):]
    key = t['key']
    rs = requests.get(url+"/"+key)
    data = rs.json()
    filepath = os.path.join(folder, title+".md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data['code'])

