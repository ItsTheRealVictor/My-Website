from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def homepage():
    return render_template('HomeIndex.html')


@app.route('/resume')
def resume():
    return render_template('ResumeIndex.html')

@app.route('/contact')
def contact():
    return render_template('ContactIndex.html')


if __name__ == "__main__":
    app.run(debug=True)