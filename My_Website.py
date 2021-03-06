from flask import Flask, render_template, request
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

# @app.route('/contact')
# def contact():
#     return render_template('ContactIndex.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        #do something with this result. Maybe write it to an excel spreadsheet with OpenPyXL
    return render_template('contact.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)