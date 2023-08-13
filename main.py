import requests
import sys
import re
args=(sys.argv[1:])
youtube=re.compile(r"^(?:(?:https?:)?\/\/)?(?:www\.)?youtube\.com\/watch\?v=[A-Za-z0-9-_]{11}")
match=youtube.search(args[0])
if not match:
    print("in male youtube nist")
    exit()
link=args[0]
id=link.split("=")
final=(f"https://img.youtube.com/vi/{id[1]}/maxresdefault.jpg")
name="thumbnail.jpg"
response=requests.get(final)
if response.status_code==200:
    with open(name,"wb")as file:
        file.write(response.content)
