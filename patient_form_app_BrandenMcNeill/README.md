# Pediatric Therapy Clinic - Patient Intake App Submission
**Submitted by:** Branden McNeill
**Date:** 06-29-2025

## Overview

This is a simple Flask web application built as part of a mini screening project. It allows staff to enter patient details (First Name, Last Name, Date of Birth, Therapist Name) via a web form. The data is validated and stored in a SQLite database, and a confirmation page is shown after submission.

---

## Features

- Basic Flask backend without extra frameworks
- Form with required fields: Patient First Name, Last Name, Date of Birth, Therapist Name
- Server-side validation (no empty fields, DOB must be in the past)
- SQLite database integration
- Confirmation page displaying submitted data
- Clean folder structure with templates and static folders

---

## Add-On Questions

### 1. How does your app handle form validation? What happens if a required field is missing or the date is in the future?

My app checks each form field after submission. If any required fields are missing or the date of birth is invalid or in the future, it adds specific error messages to a list. These errors are shown on the form page so the user can correct them before submitting again.

### 2. If we wanted to extend the app to support therapist logins, how would you structure that?

I would add a `therapists` table in the database with the fields `id`, `name`, `email`, and `password_hash`. Login sessions would be handled using Flask’s session management, with hashed passwords for security. I’d separate authentication routes (`/login`, `/register`) and protect the patient intake routes to only logged-in therapists. For scalability, I would organize the code into Flask Blueprints.

### 3. How would you deploy this app to a HIPAA-compliant cloud environment?

I’d deploy on a HIPAA-compliant cloud provider like AWS, Google Cloud, or Azure, using secure services (e.g., AWS Elastic Beanstalk, RDS with encryption). I’d enforce HTTPS, restrict access with firewalls, setup roles, and ensure logging is secure and auditable. I’d also sign any necessary agreements with the provider and avoid storing information in plain text.

### 4. Where would you place the code that initializes the database and why?

The database initialization code is in a function called `init_db()`, which is called only when the app is run directly (`if __name__ == '__main__':`). This keeps initialization separate from route handling, avoids accidental re-initialization when importing, and keeps the code modular and clean.

---

## How to Run

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
