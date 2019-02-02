from flask import Flask, render_template
from altml import altmlfile

app = Flask(__name__)

@app.route("/")
def test():
    a = 3
    return altmlfile("test.altml", a=a)

app.run(debug=True)