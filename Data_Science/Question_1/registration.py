from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

app = Flask(__name__, static_url_path='/static')

# MySQL Configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '1234'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'registration_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def registration_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password = generate_password_hash(request.form['password'])

        # Insert data into MySQL table
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
