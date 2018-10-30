from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello World"
@app.route("/hi/<name>")
def hello_name(name):
    return "Hello %s" %name
@app.route("/hi/about/<name>")
def hi(name):
    return "Hello %d" %name
if __name__=="__main__":
    app.run(debug=True)
