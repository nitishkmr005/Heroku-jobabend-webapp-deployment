import os
from forms import  AddForm , DelForm, UpdForm, AddJobAbendForm,DelJobAbendForm
from flask import Flask, render_template, url_for, redirect,session
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY']='topsecret'
app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI']='postgres://whqhrtdctwhafc:f86cd62cac832bbe62e56a5619edd98651fd535036dfd3a6a8d5fa5dabc5b7dc@ec2-34-202-7-83.compute-1.amazonaws.com:5432/dc1c9fppm57ngk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
#Migrate(app,db)

# Emp table
class Abend(db.Model):

    __tablename__ = 't_abend'

    id               = db.Column(db.Integer,primary_key = True)
    jobname          = db.Column(db.Text)
    issue_type       = db.Column(db.Text)
    is_install_issue = db.Column(db.Text)
    stepname         = db.Column(db.Text)
    progname         = db.Column(db.Text)
    issue_desc       = db.Column(db.Text)
    issue_res        = db.Column(db.Text)
    inc_ticket       = db.Column(db.Text)
    time_lost        = db.Column(db.Text)

    def __init__(self,jobname,issue_type,is_install_issue,stepname,progname,issue_desc,issue_res,inc_ticket,time_lost):

       self.jobname          = jobname
       self.issue_type       = issue_type
       self.is_install_issue = is_install_issue
       self.stepname         = stepname
       self.progname         = progname
       self.issue_desc       = issue_desc
       self.issue_res        = issue_res
       self.inc_ticket       = inc_ticket
       self.time_lost        = time_lost

    def __repr__(self):
        return f"Id : {self.id} | Job_Name : {self.jobname} |  Issue_Type : {self.issue_type} | Install_Issue? : {self.is_install_issue} | Step_Name : {self.stepname} | Program_Name : {self.progname} | Issue_Desc : {self.issue_desc} | Issue_Resolution : {self.issue_res} | INC Ticket : {self.inc_ticket} | Time_Lost : {self.time_lost}."

class Emp(db.Model):

    __tablename__ = 't_emp'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    team = db.Column(db.Text)
    skills = db.Column(db.Text)
    learning_status = db.Column(db.Text)

    def __init__(self,name,team,skills,learning_status):
        self.name = name
        self.team = team
        self.skills = skills
        self.learning_status = learning_status

    def __repr__(self):
        return f"Id : {self.id} | Employee : {self.name} |  Team : {self.team} | Skills : {self.skills} | Status : {self.learning_status}."

############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_emp():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        team = form.team.data
        skills = form.skills.data
        learning_status = form.learning_status.data

        # Add new Emp to database
        new_emp = Emp(name,team,skills,learning_status)
        db.session.add(new_emp)
        db.session.commit()

        return redirect(url_for('list_emp'))

    return render_template('add.html',form=form)

@app.route('/update', methods=['GET', 'POST'])
def upd_emp():

    form = UpdForm()

    if form.validate_on_submit():
        id = form.id.data
        emp_u = Emp.query.get(id)
        emp_u.learning_status = form.learning_status.data
        db.session.add(emp_u)
        db.session.commit()

        return redirect(url_for('list_emp'))
    return render_template('update.html',form=form)

@app.route('/list')
def list_emp():
    # Grab a list of employess from database.
    employees = Emp.query.all()
    return render_template('list.html', employees=employees)

@app.route('/delete', methods=['GET', 'POST'])
def del_emp():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        emp_d = Emp.query.get(id)
        db.session.delete(emp_d)
        db.session.commit()

        return redirect(url_for('list_emp'))
    return render_template('delete.html',form=form)

@app.route('/addjob', methods=['GET', 'POST'])
def add_job():

    form = AddJobAbendForm()

    if form.validate_on_submit():

        jobname         = form.jobname.data
        issue_type      = form.issue_type.data
        is_install_issue   = form.is_install_issue.data
        stepname        = form.stepname.data
        progname        = form.progname.data
        issue_desc      = form.issue_desc.data
        issue_res       = form.issue_res.data
        inc_ticket      = form.inc_ticket.data
        time_lost       = form.time_lost.data

        # Add new Emp to database
        new_jobabend = Abend(jobname,issue_type,is_install_issue,stepname,progname,issue_desc,issue_res,inc_ticket,time_lost)
        db.session.add(new_jobabend)
        db.session.commit()

        return redirect(url_for('abend_list'))

    return render_template('addjob.html',form=form)

@app.route('/deletejob', methods=['GET', 'POST'])
def delete_job():

    form = DelJobAbendForm()

    if form.validate_on_submit():
        id = form.id.data
        job_d = Abend.query.get(id)
        db.session.delete(job_d)
        db.session.commit()

        return redirect(url_for('abend_list'))
    return render_template('deletejob.html',form=form)

@app.route('/abendlist')
def abend_list():
    # Grab a list of employess from database.
    jobs = Abend.query.all()
    return render_template('abendlist.html', jobs=jobs)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=Flase)
