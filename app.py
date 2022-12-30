from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Project, User
from forms import AddProjectForm, UserForm
from SECRETS import python_anywhere_DB_PASSWORD

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fart'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

#this is when using the site from pythonanywhere
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://TheRealVictor:{python_anywhere_DB_PASSWORD}@TheRealVictor.mysql.pythonanywhere-services.com/TheRealVictor$my_website"
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299


# This is for using/developing the site at home
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/my_website"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# This is for using/developing the site at home
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/my_website"

app.debug = False
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
app.app_context().push()

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('HomeIndex.html')


@app.route('/resume')
def resume():
    return render_template('ResumeIndex.html')

@app.route('/portfolio')
def show_portfolio():
    projects = Project.query.all()
    return render_template('PortfolioIndex.html', projects=projects)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        new_user = User.register(username, password)
        
        db.session.add(new_user)
        
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        
        db.session.commit()        
        
        return redirect('/')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = UserForm()
    
    if form.validate_on_submit:
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username, password)
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/')
        else:
            form.username.errors = ['INVALID USERNAME/PASSWORD']
            
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    session.pop('username')
    return redirect('/')

@app.route('/projects', methods=['GET', 'POST'])
def portfolio():
    projects = Project.query.all()
    form = AddProjectForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        demo_url = form.demo_url.data
        
        new_proj = Project(title=title,
                            description=description,
                            demo_url=demo_url)
        
        db.session.add(new_proj)
        db.session.commit()
        
        return redirect('/portfolio')
    
    
    return render_template('add_project.html', projects=projects, form=form)




@app.route('/projects/<int:proj_id>')
def show_project_info(proj_id):
    project = Project.query.get_or_404(proj_id)
    
    return render_template('project_info.html', project=project)

@app.route('/projects/<int:proj_id>', methods=['POST'])
def delete_project(proj_id):
    project = Project.query.get_or_404(proj_id)
    db.session.delete(project)
    db.session.commit()
    
    return redirect('/portfolio')
    


@app.route('/projects/integral_approximator')
def integrals():
    return render_template('includes/projects/integral_approximator.html')
# if __name__ == "__main__":
#     app.run(debug=True)
