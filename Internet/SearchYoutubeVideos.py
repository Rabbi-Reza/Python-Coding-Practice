
import urllib.request
import re

import webbrowser

# import cgi
#
#
# form = cgi.FieldStorage()
#
# search_key_2 = form.getvalue("search_key")
# print(search_key_2)

search_key = input("Enter what are you looking for in Youtube ? \n==> ")

search_key_mod = search_key.replace(' ','+')

html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_key_mod)
video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())

print("Video url :  https://www.youtube.com/watch?v=" + video_id[0])

output_url = "https://www.youtube.com/watch?v=" + video_id[0]

webbrowser.open(output_url)
