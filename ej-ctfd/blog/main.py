from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/notice/<urlWEB>")
def notice(urlWEB):
    print(urlWEB)
    with open("website.json") as jsonFile:
        webs = json.load(jsonFile)
        jsonFile.close()
    title = None
    url = None
    text = None
    title1 = None
    url1 = None
    title2 = None
    url2 = None
    title3 = None
    url3 = None
    for i in webs["URLS"]:
        if i["url"] == urlWEB:
            url = i["url"]
            title = i["titulo"]
            text = i["texto"]
            url1 = i["url1"]
            title1 = i["titulo1"]
            url2 = i["url2"]
            title2 = i["titulo2"]
            url3 = i["url3"]
            title3 = i["titulo3"]
    return render_template("post.html", url=url, text=text,title=title,url1=url1,title1=title1,url2=url2,title2=title2,url3=url3,title3=title3);

@app.route("/")
def main():
    return render_template("index.html");

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8002")
