from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    user={'usernmae':'Dhiraj'}
    posts=[
        {
            'author':{'username':'Daniel'},
            'body':'Beautiful day in Srilanka!'
        },
        {
            'author':{'username':'Aman'},
            'body':'Tiger Zinda he movie is so cool!'
        }
    ]
    return render_template('index.html',user=user,posts=posts)
if __name__=="__main__":
    app.run(debug=True)
