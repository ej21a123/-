
from flask import Flask,render_template,url_for

app = Flask(__name__,static_folder='./templates/IMGs')

@app.route('/')
def index():
    return render_template("index.html") 
    #return "Hello World"
if __name__ == '__main__':
    app.run()
