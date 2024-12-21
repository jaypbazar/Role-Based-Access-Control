from flask import flash, redirect, url_for, make_response
from functools import wraps
import mysql.connector, hashlib

def connectSQL() -> object:
    '''
A function to connect to mysql database.

Returns:
    - a connection from the mysql database
    '''
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "se_database"
    )

def encrypt(password: str) -> str:
    '''
A function that hash the passed argument usring sha-256 hashing.

Parameters:
    password - the password of user to be encrypted

Returns:
    - the encrypted password 
    '''
    return hashlib.sha256(password.encode()).hexdigest()

def validate_duplicate(column_name: str, data: str) -> None:
    '''
A function that validates the user input from a form for its uniqueness
    
Parameters:
    column_name - the name of the table column from the database
    
    data - the current value to validate
    
Returns:
    redirect() - redirects the user to same page then display error message if duplicate
    '''
    
    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = f"SELECT {column_name} FROM users"
        cursor.execute(query)

        data = data.lower()
        list = [row[0].lower() for row in cursor.fetchall()]

        cursor.close()
        print(data)
        print(list)

        if data in list: 
            flash(f"Error: {column_name} already exists!", "danger")
            return redirect(url_for('signup'))

    except Exception as e:
        print(f"Database Error: {e}")

def is_admin(user_id: str) -> bool:
    '''
A function that check if the user is an admin

Parameters:
    user_id - the id of user to check

Returns:
    true - if user is admin otherwise false
    '''
    try:
        conn = connectSQL()
        cursor = conn.cursor()

        query = "SELECT ID FROM users WHERE Role = 'admin'"
        cursor.execute(query)

        admin_ids = []
        for row in cursor.fetchall():
            admin_ids.append(row[0])

        print(admin_ids)

        return user_id in admin_ids

    except Exception as e:
        print(f"Admin Check Error: {e}")

    return False

def nocache(view):
    '''
A decorator that prevents caching of view functions by adding cache control headers
    
Parameters:
    view - the Flask view function to be decorated
    
Returns:
    decorated function - the original view function wrapped with cache control headers
    '''
    @wraps(view)  # Preserve the original function's metadata
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return no_cache
