##from urllib.request import urlopen
#url = "https://investor.vanguard.com/search/?query=FLR"
#page = urlopen(url)
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")
#print(html)

import re
import urllib.request
response = urllib.request.urlopen('https://investor.vanguard.com/search/?query=FLR')
html = response.read()
text = html.decode()
re.findall('(.*?)',text)
print(text)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')