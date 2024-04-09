import os

from flask import Flask, render_template
from flask_mail import Mail, Message



app = Flask(__name__) 
app.config['MAIL_SERVER'] = 'smpt.yahoo.com'
app.config["MAIL_PORT"] = "465"
app.config["MAIL_USERNAME"] = "adelle_xx@yahoo.co.uk" 
app.config["MAIL_PASSWORD"] = os.environ.get('PASSWORD')
app.config["MAIL_USE_TLS"] = "False"
app.config["MAIL_USE_SSL"] = "True"
mail = Mail(app)
  
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/contactform")
def contactform():
    return render_template("contactform.html")





if __name__== "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)