from flask import Flask
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/hello/<jp>/<int:num>')
def hello_jp(jp, num):
    return " Hello Jp, almost there! " * num


@app.route('/greeting/<greetings>/<int:num>')
def loving_it(greetings, num):
    return "I am loving it! "* num
    

# @app.route('/almost/<string:almost>/<int:num>')
# def almost_there(almost,num):
#     return f"Almost there!{almost * 80}"

@app.route('/farewell/<string:blue_sky>/<int:num>')
def good_bye(blue_sky,num):
    return "Godbye sky" + blue_sky * num 


if __name__=="__main__":
    app.run(debug=True, port = 5001)


