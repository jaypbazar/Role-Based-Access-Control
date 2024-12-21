from flask import Flask, request, session, redirect, render_template, url_for, flash
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
from backend import *

app = Flask(__name__)
app.secret_key = '@SE_S3cr3t_K3y!'
app.config['REMEMBER_COOKIE_REFRESH_EACH_REQUEST'] = False
app.config['WTF_CSRF_TIME_LIMIT'] = 3600
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
csrf = CSRFProtect(app)

'''
Sample Accounts:

Admin 1
    ID: 221008049  
    Password: Adm1nP@ssw0rd

Student 1
    ID: 2023123456
    Password: M@ri4Cl@r@2024!

Student 2
    ID: 2023126789
    Password: @ng3laMar!e2024#

Student 3
    ID: 2023987654
    Password: J0s3phL!u1s2024@

Employee 1
    ID: 12345678
    Password: J0hnM!cha3l2024#

Employee 2
    ID: 98765432
    Password: Chr!st!n3J0y2024#
'''

@app.route('/')
@nocache
def index():
    session['no_of_available_lots'] = 0
    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = "SELECT * FROM parking_lots"

        cursor.execute(query) 

        lots = []
        for row in cursor.fetchall():
            lots.append({
                'name': row[0],
                'coords': [[row[1], row[2]], [row[3], row[4]]],
                'status': row[5]
            })
            if row[5] == 'available':
                session['no_of_available_lots'] += 1

    except Exception as e:
        print(f"Index Error: {e}")
        lots = []
        color = '#6aff00'

    if session.get('no_of_available_lots') > 2: 
        color = '#34ff12'
    elif session.get('no_of_available_lots') > 0:
        color = '#ffff00'
    else: 
        color = '#ff2828'

    return render_template("index.html", parkingLots=lots, available_lots=session.get('no_of_available_lots'), color=color)

@app.route('/about')
@nocache
def about():
    return render_template('about.html')

@app.route('/terms')
@nocache
def terms():
    return render_template('terms.html')

@app.route('/login', methods=["GET", "POST"])
@nocache
def login():
    if 'user_id' in session:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        user_id = request.form.get('id')
        password = encrypt(request.form.get('password'))
        
        try:
            conn = connectSQL()
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE ID = %s AND Password = %s"
            values = (user_id, password)

            cursor.execute(query, values)

            user = cursor.fetchone()

            if user:
                session['user_id'] = user[0]
                session['username'] = f"{user[1]} {user[3]}"
                session['role'] = user[4]

                if session.get('role') == "admin":
                    return redirect(url_for('adminPanel'))

                return(redirect(url_for('index')))
            else:
                session.clear()
                flash("Wrong email or password. Please try again.", "danger")

            cursor.close()
            conn.close()

        except Exception as e:
            session.clear()
            flash("Login failed. Please try again.", "danger")
            print(f"Login Error: {e}")
    
    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
@nocache
def signup():
    if 'user_id' in session:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        user_id = request.form.get("id")
        firstname = request.form.get("fname")
        middlename = request.form.get("mname")
        lastname = request.form.get("lname")
        role = request.form.get("role")
        contact = request.form.get("contact")
        email = request.form.get("email")
        password = encrypt(request.form.get("password"))

        validate_duplicate("ID", user_id)
        validate_duplicate("CspcEmail", email)

        try:
            conn = connectSQL()
            cursor = conn.cursor()

            query = "INSERT INTO users (ID, FirstName, MiddleName, LastName, Role, CspcEmail, PhoneNumber, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (user_id, firstname, middlename, lastname, role, email, contact, password)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            flash("Registered successfully.", "success")
            return render_template("login.html")

        except Exception as e:
            print(f"Signup Error: {e}")
            flash("Sign up error. Please try again.", "danger")
                
    return render_template('signup.html')

@app.route('/booking', methods=["POST", "GET"])
@nocache
def booking():
    if 'user_id' in session:
        parkingLot = request.form.get('parkingSpace')
        bookingDate = request.form.get('reservationDate')
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')

        try:
            conn = connectSQL()
            cursor = conn.cursor()

            query = "INSERT INTO bookings VALUES(%s, %s, %s, %s, %s)"
            values = (parkingLot, bookingDate, startTime, endTime, session.get('user_id'))

            cursor.execute(query, values)
            conn.commit()

            query = "UPDATE parking_lots SET status = %s WHERE name = %s"
            values = ('reserved', parkingLot)
            
            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()
            
        except Exception as e:
            flash("Reservation failed. Try again.", "danger")
            print(f"Booking Error: {e}")

        flash("Reserved Successfully.", "success")
        return redirect(url_for("index"))

    return redirect(url_for("index"))

@app.route('/update_booking', methods=["POST"])
@nocache
def update_booking():
    parkingLotName = request.form.get('lot_name')
    bookingDate = request.form.get('booking_date')
    startTime = request.form.get('time_start')
    endTime = request.form.get('time_end')

    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = "UPDATE bookings SET bookingDate = %s, timeStarted = %s, timeEnded = %s WHERE lotName = %s"
        values = (bookingDate, startTime, endTime, parkingLotName)

        cursor.execute(query, values)
        conn.commit()

        flash("Reservation updated successfully.", "success")

        cursor.close()
        conn.close()
    
    except Exception as e:
        flash("Error updating reservation.", "danger")
        print(f"Reservation Update Error: {e}")

    return redirect(url_for('adminPanel'))

@app.route('/delete_booking', methods=["POST"])
@nocache
def delete_booking():
    parkingLotName = request.form.get('lotName')

    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = "DELETE FROM bookings WHERE lotName = %s"
        values = (parkingLotName,)

        cursor.execute(query, values)
        conn.commit()

        query = "UPDATE parking_lots SET status = %s WHERE name = %s"
        values = ('available', parkingLotName)

        cursor.execute(query, values)
        conn.commit()

        flash("Reservation removed successfully.", "success")

        cursor.close()
        conn.close()

    except Exception as e:
        flash("Error in deleting reservation.", "danger")
        print(f"Booking Deletion Error: {e}")
    
    return redirect(url_for('adminPanel'))

@app.route('/logout')
@nocache
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))

@app.route('/adminPanel')
@nocache
def adminPanel():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            try:
                conn = connectSQL()
                cursor = conn.cursor()

                query = "SELECT * FROM parking_lots"
                cursor.execute(query) 

                lots = cursor.fetchall()

                query = "SELECT * FROM bookings"
                cursor.execute(query)

                bookings = cursor.fetchall()

            except Exception as e:
                print(f"Admin Panel Error: {e}")
                
            return render_template('adminPanel.html', parkingLots=lots, reservations=bookings)
        
        flash("Access denied! Only admins are allowed.", "danger")
        return redirect(url_for("index"))
    
    flash("You must log in first.", "danger")
    return redirect(url_for("login"))

@app.route('/update_status', methods=["POST"])
@nocache
def update_status():
    lotName = request.form.get('lot_name')
    status = request.form.get('status')

    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = "UPDATE parking_lots SET status = %s WHERE name = %s"
        values = (status, lotName)

        cursor.execute(query, values)
        conn.commit()

        flash("Parking status updated successfully.", "success")

        cursor.close()
        conn.close()

    except Exception as e:
        flash("Error updating details. Try again.", "danger")
        print(f"Update Error: {e}")

    return redirect(url_for('adminPanel'))

@app.route('/manage_users', methods=["POST", "GET"])
@nocache
def manage_users():
    if session.get('role') != 'admin':
        flash("Access denied! Only admins are allowed.", "danger")
        return redirect(url_for('index'))
    
    try:
        conn = connectSQL()

        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE Role = 'student' OR Role = 'employee'"

        cursor.execute(query)

        session['user_list'] = cursor.fetchall()

        query = "SELECT * FROM users WHERE Role = 'admin'"

        cursor.execute(query)

        session['admin_list'] = cursor.fetchall()
        
        cursor.close()
        conn.close()

    except Exception as e:
        flash("Error getting users from database.", "danger")
        print(f"User Management Error: {e}")

    return render_template('userManagement.html')

@app.route('/delete_user', methods=["POST"])
@nocache
def delete_user():
    userID = request.form.get('user_id')

    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE ID = %s"
        values = (userID,)

        cursor.execute(query, values)
        conn.commit()

        flash("User deleted successfully.", "success")
        
        cursor.close()
        conn.close()

    except Exception as e:
        flash("Error deleting user.", "danger")
        print(f"User Deletion Error: {e}")

    return redirect(url_for("manage_users"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)