from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,IntegerField,DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)

class AddForm(FlaskForm):

    name = StringField('Name of the Employee')
    team = StringField('Team Name------------')
    skills = StringField('Skills Learning---------')
    learning_status = StringField('Learning Status--------')
    submit = SubmitField('Add Employee')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Employee to Remove:')
    submit = SubmitField('Remove Employee')

class UpdForm(FlaskForm):

    id = IntegerField('Id Number of Employee to Update')
    learning_status = StringField('Updated learning status------------')
    submit = SubmitField('Update Skill')

class AddJobAbendForm(FlaskForm):

    jobname = StringField('Job Name')
    issue_type = RadioField('Choose Issue Type:', choices=[('Pricing','Pricing'),('DataIssue','DataIssue'),('Contention','Contention'),('FTPIssue','FTPIssue'),('TableOverflowIssue','TableOverflowIssue'),('Program Issue','Program Issue'),('Storage Issue','Storage Issue'),('DBA Issue','DBA Issue'),('Other','Other')])
    is_install_issue = BooleanField('Is this Install Issue ?')
    stepname = StringField('Step Name')
    progname = StringField('Program Name')
    issue_desc = TextAreaField()
    issue_res = TextAreaField()
    inc_ticket = StringField('Incident Ticket')
    time_lost = StringField('Time Lost')
    submit = SubmitField('Add Jobabend')

class DelJobAbendForm(FlaskForm):

    id = IntegerField('Id Number of Job to Remove:')
    submit = SubmitField('Remove JobAbend')
