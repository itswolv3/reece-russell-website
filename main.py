from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

title = "Reece Russell"


@app.route("/")
def home():
    return render_template("index.html", title=title)


@app.route("/cv")
def download_cv():

    return send_file("./static/pdf/Reece Russell CV.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run()
