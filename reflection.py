from flask import Flask
import datetime

app = Flask(__name__)

myReflections = {}

myReflections["78"] = {"link": "https://www.google.com", "Reflection": "I'm not sure what the point is in this lesson, but i'll do it anyway."}
myReflections["79"] = {"link": "https://www.google.com", "Reflection": "Hav'nt done this one yet"}

@app.route('/<pageNumber>')
def index(pageNumber):
    page = ""
    f = open("template/reflection.html","r")
    page = f.read()
    f.close()
    page = page.replace("{day}", pageNumber)
    page = page.replace("{link}", myReflections[pageNumber]["link"])
    page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"] )
    return page

if __name__ == "__main__":
    app.run(debug=False)