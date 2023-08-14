from flask import Flask, render_template, request

app = Flask(__name__,template_folder = "template")
# returns the html template on /signup route.
@app.route("/signup")
def signup():
    return render_template("signup.html")
# route to connect to db.
@app.route("/signup", methods=["POST"])
def signup_post():
    username = request.form["username"]
    password = request.form["password"]

    if username == "" or password == "":
        return "Please enter a username and password."

    # Save the user to the database

    return "Signup successful!"

if __name__ == "__main__":
    app.run(debug=True)
