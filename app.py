from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Projects
from forms import AddProjectForm
import sshtunnel
import mysql.connector
from SECRETS import python_anywhere_PASSWORD, my_SQL_pwd, python_anywhere_DB_PASSWORD

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fart'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0
 

with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username='TheRealVictor', ssh_password=python_anywhere_PASSWORD, remote_bind_address=('TheRealVictor.mysql.pythonanywhere-services.com', 3306)) as tunnel:
    connection = mysql.connector.connect(
        user='TheRealVictor',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='TheRealVictor$my_website'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://TheRealVictor:{python_anywhere_DB_PASSWORD}@127.0.0.1:{tunnel.local_bind_port}/TheRealVictor$my_website'

connection.close()
# else:
    
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:victordb@localhost/my_website'



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
    projects = Projects.query.all()
    return render_template('PortfolioIndex.html', projects=projects)




@app.route('/projects', methods=['GET', 'POST'])
def portfolio():
    projects = Projects.query.all()
    form = AddProjectForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        demo_url = form.demo_url.data
        
        new_proj = Projects(title=title,
                            description=description,
                            demo_url=demo_url)
        
        db.session.add(new_proj)
        db.session.commit()
        
        return redirect('/portfolio')
    
    
    return render_template('add_project.html', projects=projects, form=form)




@app.route('/projects/<int:proj_id>')
def show_project_info(proj_id):
    project = Projects.query.get_or_404(proj_id)
    
    return render_template('project_info.html', project=project)


@app.route('/projects/integral_approximator')
def integrals():
    return render_template('includes/projects/integral_approximator.html')
# if __name__ == "__main__":
#     app.run(debug=True)
