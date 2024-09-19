from flask import Flask, render_template
app = Flask(__name__)

@app.route ("/")
@app.route ("/klaud")
def klaud():
    return render_template("klaud.html")



if __name__== '__main__':
    app.run(debug=True)