from flask import Flask as F, render_template as rt
app=F(__name__)

@app.route('/')
def index():
    return rt("index.html")