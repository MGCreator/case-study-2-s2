from flask import Flask, redirect, render_template, url_for, request, redirect, flash, session, abort
import uuid
from datetime import datetime
import pyodbc
from flask_recaptcha import ReCaptcha

COMPLETED = True
NOT_COMPLETED = False
CORRECT = False
INCORRECT = True

driver_name = 'SQL Server'
server_name = 'DESKTOP-KB055QI'
database_name = 'flaskDemo'

#uid=<username>
#pwd=<password>

connection_string = f"""
    DRIVER={{{driver_name}}};
    SERVER={server_name};
    DATABASE={database_name};
    Trust_Connection=yes;
    """

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    # to make captcha to work you need your own keys. You can find them here https://www.google.com/recaptcha/admin/create
    RECAPTCHA_SITE_KEY = '',
    RECAPTCHA_SECRET_KEY = ''
))

recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.config['SECREY_KEY'] = str(uuid.uuid4().hex)


query_insert = "INSERT INTO ProjectFlask (first_name, last_name, email, mobile, home_address, department, position, salary, hire_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"


@app.route('/', methods=['POST', 'GET'])
def index():
    
    if not session.get('logged_in'):
        return redirect('/login/')
    else:
        if request.method == 'POST':
            task_content = request.form['content']

            date_for_task1 = datetime.utcnow()

            try:

                with pyodbc.connect(connection_string) as conx:
                    cursor = conx.cursor()
                    cursor.execute(query_insert, task_content, date_for_task1)

                return redirect('/')
            except:
                return 'There was an issue with commiting in database'

        else:
            with pyodbc.connect(connection_string) as conx:
                    cursor = conx.cursor()

                    cursor.execute("SELECT * FROM ProjectFlask")
                    tasks = cursor.fetchall()
                    #print(tasks)
                    count = 0
                    for task in tasks:
                        count +=1
                        
                        print(task)
                        break
                    #flash("Welcome")
                    return render_template('index.html', tasks=tasks, count=count)


@app.route('/delete/<int:id>/')
def delete(id):
    if not session.get('logged_in'):
        return redirect('/login/')
    else:
        with pyodbc.connect(connection_string) as conx:
            cursor = conx.cursor()
            try:
                task_to_delete = cursor.execute("DELETE FROM ProjectFlask WHERE id=?", id)
                return redirect('/')
            except:
                return 'There was problem with deleting the task'


@app.route('/update/<int:id>/', methods=['POST', 'GET'])
def update(id):
    if not session.get('logged_in'):
        return redirect('/login/')
    else:
        with pyodbc.connect(connection_string) as conx:
            cursor = conx.cursor()
            selected_task = cursor.execute("SELECT first_name, last_name, email, mobile, home_address, department, position, salary FROM ProjectFlask WHERE id=?", id)
            selected_task = cursor.fetchall()

        if request.method == 'POST':

            with pyodbc.connect(connection_string) as conx:
                cursor = conx.cursor()
                try:
                    fname = request.form.get("fname")
                    print(4)
                    lname = request.form.get('lname')
                    email = request.form.get('email')
                    mobile = request.form.get('mobile')
                    addr = request.form.get('addr')
                    dprt = request.form.get('dprt')
                    posit = request.form.get('posit')
                    salary = request.form.get('salary')
                    cursor.execute("UPDATE ProjectFlask SET first_name=?, last_name=?, email=?, mobile=?, home_address=?, department=?, position=?, salary=? FROM ProjectFlask WHERE id=?", fname, lname, email, mobile, addr, dprt, posit, salary, id)
                    return redirect('/')
                except:
                    return 'There was problem with updating the task'

        elif request.method == 'GET':
            with pyodbc.connect(connection_string) as conx:
                cursor = conx.cursor()
                selected_task = cursor.execute("SELECT id, first_name, last_name, email, mobile, home_address, department, position, salary FROM ProjectFlask WHERE id=?", id)
                selected_task = cursor.fetchall()
                return render_template('update.html', task=selected_task)


@app.route('/add/', methods=['POST', 'GET'])
def gfg():
    if not session.get('logged_in'):
        return redirect('/login/')
    else:
        if request.method == 'POST':
            hire_date = datetime.utcnow()
            print(1)

            with pyodbc.connect(connection_string) as conx:
                cursor = conx.cursor()
                print(2)
                try:
                    print(3)
                    fname = request.form.get("fname")
                    print(4)
                    lname = request.form.get('lname')
                    email = request.form.get('email')
                    mobile = request.form.get('mobile')
                    addr = request.form.get('addr')
                    dprt = request.form.get('dprt')
                    posit = request.form.get('posit')
                    salary = request.form.get('salary')
                    print(fname)
                    cursor.execute(query_insert, fname, lname, email, mobile, addr, dprt, posit, salary, hire_date)
                    return redirect('/')
                except:
                    return 'There was problem with adding the information.'

        elif request.method == 'GET':
            return render_template('add.html')

credentials = CORRECT
is_captcha_completed = True

@app.route('/login/', methods=['POST', 'GET'])
def login():
    
    global credentials
    global is_captcha_completed
    
    if request.method == 'POST':
        if request.form['password'] == 'Admin-08' and request.form['username'] == 'admin' and recaptcha.verify():
            session['logged_in'] = True
            credentials = CORRECT
            is_captcha_completed = COMPLETED
            return redirect('/')
        else:
            if request.form['password'] == 'Admin-08' and request.form['username'] == 'admin':
                credentials = CORRECT
            else:
                credentials = INCORRECT
            # print("recpatcha.verify: " + str(recaptcha.verify()))
            # if recaptcha.verify():
            #     is_captcha_completed = True
            # elif not recaptcha.verify():
            #     is_captcha_completed = NOT_COMPLETED
            # print("bool: " + str(is_captcha_completed))
            # flash('Wrong credentials!')
            return redirect('/login')
    elif request.method == 'GET':
        return render_template('login.html', credentials=credentials, is_captcha_completed=is_captcha_completed)


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = str(uuid.uuid4().hex)
    app.run(host="0.0.0.0")
    