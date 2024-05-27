import mysql.connector
import re

# Connect to the database
connection = mysql.connector.connect(host="localhost", user="root", password="", database="Login_Signup_db")

if connection.is_connected():
    print('Connected successfully')
else:
    print('Failed to connect')

# Function to register a new user
def register_user(name, username, password, email):
    # Check if the password is at least 8 characters long and contains at least one unique character
    if len(password) < 8 or len(set(password)) == len(password):
        return "Password must be at least 8 characters long and contain at least one unique character."

    # Check if the username is at least 6 characters long and contains at least 3 characters and 3 numbers
    if len(username) < 6 or not re.match(r'^[a-zA-Z0-9]{6,}$', username):
        return "Username must be at least 6 characters long and contain at least 3 characters and 3 numbers."

    # Check if the user already exists
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s OR username = %s", (email, username))
    if cursor.fetchone():
        return "User already exists."

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (name, username, password, email) VALUES (%s, %s, %s, %s)", (name, username, password, email))
    connection.commit()
    return "User registered successfully."

# Function to log in a user
def login_user(username, password):
    # Check if the user exists
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        return "Invalid username or password."

    # Check if the password is correct
    if user[3] != password:
        return "Invalid username or password."

    return "Login successful."

# Close the database connection
connection.close()