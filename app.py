from flask import Flask, render_template, request, redirect, flash, url_for
import random
import re
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'

otp_storage = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            flash('Invalid email format. Please enter a valid email.', 'danger')
            return redirect(url_for('index'))

        otp = str(random.randint(100000, 999999))
        otp_storage[email] = {
            'otp': otp,
            'timestamp': datetime.now()
        }

        print(f"OTP for {email} is {otp}") 
        flash('OTP generated successfully! (Check terminal)', 'success')
        return redirect('/verify?email=' + email)

    return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    email = request.args.get('email')
    if request.method == 'POST':
        user_otp = request.form['otp']
        record = otp_storage.get(email)

        if record:
            valid_otp = record['otp']
            timestamp = record['timestamp']
            expiry_time = timestamp + timedelta(seconds=60)

            if datetime.now() > expiry_time:
                flash('OTP expired. Please generate a new one.', 'danger')
                otp_storage.pop(email, None) 
                return redirect('/')

            if user_otp == valid_otp:
                flash('OTP Verified Successfully!', 'success')
            else:
                flash('Invalid OTP. Try again.', 'danger')
        else:
            flash('No OTP found for this email.', 'danger')

        return redirect('/')

    return render_template('verify.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)