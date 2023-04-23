from flask import Flask, render_template, request, jsonify, make_response, session, url_for, redirect, flash, Markup
from urllib.request import urlopen
import simplejson

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
