from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["barry"] = {"email": "baz@b.com", "password": "baz"}
logins["lea"] = {"email": "lea@l.com", "password": "Leah"}
logins["mike"] = {"email": "mike@m.com", "password": "mikey"}

@app.route("/login", methods = ["POST"])
def login():
    form = request.form
    isThere = False
    details = {}
    try:
        details = logins[form["username"]]
        isThere = True
    except:
        return "username, email or password incorrect"
    if form["email"] == details["email"] and form["password"] == details["password"]:
        return f"Hi {form["username"]}, you are logged in"
    else:
        return "username, email or password incorrect"

@app.route('/')
def index():
    page = """<form method="post" action="/login">
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <button type="submit">login</button>
    </form>
    """
    return page

if __name__ == "__main__":
    app.run(debug=False)