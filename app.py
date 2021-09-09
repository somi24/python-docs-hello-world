from flask import Flask, render_template,  request, url_for, flash, redirect
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testscript'

@app.route('/unsubscribed')
def unsubscribe():
	return render_template ('unsubscribed.html')
    
@app.route('/',methods = ('GET','POST'))   
def index():
    if request.method == 'POST':
        email = request.form['Email']
    
        if not email:
            flash('Email address is required!')
        else:
            server = 'advanced-analytics-srvr.database.windows.net'
            database = 'sqldbanalytics'
            username = 'sqldbadmin'
            password = '123Welcome123@@'   
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            cursordh = cnxn.cursor()
            cursordh.execute ("INSERT [dbo].[custom_email_test]  (unsubscribe_date,email_address) values (Getdate(),?)", email )
            cnxn.commit()
            return redirect(url_for('unsubscribed'))
      
    return render_template ('index.html')




