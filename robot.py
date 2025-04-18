from flask import Flask, request

app = Flask(__name__)

@app.route("/robot", methods=["POST"])  
def robot():
    form = request.form
    if form.get('metal') == "Yes":  
        return "You're a robot!"
    elif "error" in form.get("infinity").lower():  
        return "You're a robot!"
    elif form.get("food") == "synthetic oil":  
        return "You're a robot!"
    else:
        return "Hello human"

@app.route('/')
def index():
    page = ""
    try:
        with open("template/robot.html", "r") as f:
            page = f.read()
    except FileNotFoundError:
        return "Error: robot.html not found."
    return page

@app.route('/language', methods = ["GET"])
def lang(): #This function changes output on webpage depending on en/es
    data = request.args
    if data == {}:
        return "Nothing here"
    elif data["lang"]=="en": #http://127.0.0.1:5000/language?lang=en
        return "Welcome to the english webpage"
    elif data["lang"]=="es": #http://127.0.0.1:5000/language?lang=es
        return "bienvenido a la pagina web en espanol"
        
if __name__ == "__main__":
    app.run(debug=False)