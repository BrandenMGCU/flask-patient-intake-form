from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            therapist TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home route that displays the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name'].strip()
    last_name = request.form['last_name'].strip()
    dob = request.form['dob']
    therapist = request.form['therapist'].strip()

    errors = []

    # Basic validation
    if not first_name:
        errors.append("First name is required.")

    if not last_name:
        errors.append("Last name is required.")

    if not dob:
        errors.append("Date of birth is required.")

    if not therapist:
        errors.append("Therapist name is required.")


    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        if dob_date >= datetime.today():
            errors.append("Date of birth must be in the past.")
    except ValueError:
        errors.append("Invalid date format. Use YYYY-MM-DD.")

    if errors:
        return render_template("form.html", errors=errors)

    # Insert into SQLite database
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute
    ('''
        INSERT INTO patients (first_name, last_name, dob, therapist)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, dob, therapist))
    conn.commit()
    conn.close()

    # Show confirmation page
    return render_template(
        'confirmation.html',
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        therapist=therapist
    )

# Start the Flask server
if __name__ == '__main__':
    init_db()  # Ensure DB is ready
    app.run(debug=True)