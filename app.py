from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fart'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite.db'
app.config['SQLALCHEMY_BINDS'] = {'testDB' : 'sqlite:///test_mysite.db'}


app.debug = True
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


db = SQLAlchemy(app)
app.app_context().push()

migrate = Migrate(app, db)

class Projects(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    demo_url = db.Column(db.Text, nullable=True)
    






@app.route('/')
@app.route("/home")
def homepage():
    return render_template('HomeIndex.html')


@app.route('/resume')
def resume():
    return render_template('ResumeIndex.html')




@app.route('/portfolio')
def portfolio():
    projects = Projects.query.all()    
    return render_template('PortfolioIndex.html', projects=projects)

@app.route('/project_info_<int:proj_id>')
def show_project_info(proj_id):
    project = Projects.query.get_or_404(proj_id)
    
    return render_template('/project_info.html', project=project)


