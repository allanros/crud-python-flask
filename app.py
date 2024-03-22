from flask import Flask

# __name__ = __main__
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1><br><a href='/about'>About</a>"

@app.route("/about")
def about():
    return "<h1>Página Sobre</h1><br><a href='/'>Home</a>"

if __name__ == "__main__":
    app.run(debug=True)