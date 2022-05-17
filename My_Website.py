from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fart'

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

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)