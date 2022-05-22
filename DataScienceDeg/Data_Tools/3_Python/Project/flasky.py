from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello!")
    return 'Hello, World!'

@app.route('/mini/<id>',methods=["GET"])
def getuser(id):
    return "Your username is " + id

app.run()