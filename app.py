from flask import Flask, redirect, request
import datetime

app = Flask(__name__,static_url_path="/static")  

@app.route("/")
def index():
    today = datetime.date.today()
    page = f"""<html><body><h1>{today}\t<a href="/home">Home page</a><h1>
    <h2><a href="/portfolio">Portfolio</a><h/2>
    </body></html>"""
    return page


@app.route("/home")
def home():
    page ="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Charlies portfolio</title>
    <link href="static/css/style.css" rel="stylesheet" type="text/css">
</head>
<body>
    <h1>A portfolio of my favourite projects</h1>
    <h2>Pizza shop order program</h2>
    <p>I enjoyed making this program, it included most of the knowledge i have learnt through 100 days of code. It works by taking taking an order in and working out how much the total is at the end. Once the order is done, it can be deleted from the database.</p>
    <img src="static/images/pizzaShopOne.png">
    <img src="static/images/pizzaShopTwo.png">
    <h2>Log in system</h2>
    <p>Another project i enjoyed is the one i did about a log in system. This program saves the password in a seperate file and hashes the password. This makes the password harder to figure out if it found by hackers.</p>
    <img src="static/images/logInHashing.png">
    <h2>Graphic novel</h2>
    <p>This one was fun, i used one of the first fps games i ever played and used some of the images to make a small graphic novel. I used the tkinter library to make this program work. </p> 
    <img src="static/images/graphicNovelSS.png">
    <ol>
        <li>This is </li>
        <li>an ordered</li>
        <li>list</li>
    </ol>
    <p class="blurb"><a href="https://www.w3schools.com/html/html_lists.asp">For more info</a>: ordered lists and unordered lists</p>
    <ul>
        <li>This is</li>
        <li>an unordered</li>
        <li>list</li>
    </ul>
    <p class="blurb"><a href="/home">Home</a> | <a href="/portfolio">Portfolio</a> | <a href="/form">Form</a></p>
    <p>©2025 charliesportfolio</p>
</body>
</html>
"""
    return page

@app.route("/w3")
def redirectPg():
    return redirect ("https://www.w3schools.com/html/default.asp")

@app.route('/portfolio')
def port():
    myName = "Chuck"
    title = "Pool party"
    text = "This is my favourite because it includes nearly everything i know form 100 days of code."
    link = "/home"
    image = "pizzaShopOne.png"
    imageTwo = "beers.jpg"
    page = ""
    f = open("template/portfolio.html")
    page = f.read()
    f.close()
    page = page.replace("{name}", myName)
    page = page.replace("{title}", title)
    page = page.replace("{text}", text )
    page = page.replace("{link}", link)
    page = page.replace("{image}", image)
    page = page.replace("{imageTwo}", imageTwo)
    return page

@app.route("/process", methods=["POST"])
def process():
    page = ""
    form = request.form
    if form["City"] == "London":
        page += f"You're alright {form['username']}"
    else:
        page += f"You've picked wrong, {form['username']}"
    return page

@app.route('/form')
def form():
    page = ""
    f = open("template/form.html")
    page = f.read()
    f.close()
    return page

@app.route('/get', methods=["GET"])
def get():
    return request.args 
#If you type in this http://127.0.0.1:5000/get?name=bob&age=77 
#this will return a webpage with two variables
    

if __name__ == "__main__":
    app.run(debug=False)