from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route('/home')
def homepage():
    return render_template('HomeIndex.html')

@app.route('/resume')
def resume():
    return render_template('ResumeIndex.html')


if __name__ == "__main__":
    app.run(debug=True)