import requests
import os


url = "http://automation:9001/listfull/my-dd-course?keys=%7B%22title%22%3A1%2C%22key%22%3A1%7D"
rs = requests.get(url)
data = rs.json()

folder = "./course"
folderimg = "./imgs"
for f in [folder, folderimg]:
    if not os.path.exists(f):
        os.mkdir(f)


titles = [i for i in data if i['title'].startswith("200. course/")]

url = "http://automation:9001/get/my-dd-course"

courses = []

for t in titles:
    title = t['title'][len("200. course/"):]
    key = t['key']
    rs = requests.get(url+"/"+key)
    data = rs.json()
    code = data['code']
    thumbpath = ""
    for line in code.split("\n"):
        if line.startswith("![](http://automation") and line.endswith("?rt=img)"):
            link = line.strip()[len("![]("):-1]
            linkid = link.split("/")[-1].split("?")[0]
            thumbpath = f".{folderimg}/{linkid}.png"
            break
    title = title.replace(">", "_")

    courses.append({
        "title": title,
        "thumbpath": thumbpath,
    })

colsize = 2
md = "|||\n"
md += "|-|-|\n"
for idx, c in enumerate(courses):
    c['title'] = c['title'].encode('ascii', 'replace').decode()
    title = c['title']
    img = c['thumbpath']
    print(c)
    md += f"|![]({img})"

    if idx != 0 and idx%colsize == 0:
        md += "|\n"

with open("course-grid.md", "w") as f:
    f.write(md)
