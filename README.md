# 🔐 OTP-Based Login Demo App

This is a simple OTP-based login system built using **Flask (Python)** for demo and academic purposes. The OTP is sent to the user (simulated by printing it in the terminal), and expires after 1 minute.

---

## 📌 Features

- ✅ Email input with format validation
- ✅ Random 6-digit OTP generation
- ✅ OTP expiry logic (1-minute timeout)
- ✅ Flash messages for success, errors & expiry
- ✅ Clean and modern UI using Bootstrap
- ✅ No external email services required (for demo use only)

---

## 📈 Sequence Diagram

The following diagram shows the step-by-step flow of how OTP-based login works in this application:

<img width="1024" height="1024" alt="Sequence Diagram" src="https://github.com/user-attachments/assets/f3166061-6f4c-45e1-8db3-a250a984d552" />

- The user enters their email.
- The system generates a random OTP.
- The OTP is stored temporarily and displayed in the terminal.
- The user enters the OTP on the verify page within the given timestamp.
- If the user enters the OTP after the given timestamp, the OTP gets invalid and the user need to generate a new one.
- If the OTP is correct, the login is successful.


## 🚀 How to Run

1. **Install Flask (if not already)**  
   ```bash
   pip install flask

2. **Run the app**
   ```
   python app.py
   ```

3. **Open in browser:**
Navigate to: http://localhost:5000

4. Check terminal output for OTP after submitting the email.

## 🖼️ Screenshots
<img width="1920" height="1011" alt="1" src="https://github.com/user-attachments/assets/3aec0f26-c39d-496a-a365-4277a95c2859" />

<img width="1918" height="1011" alt="2" src="https://github.com/user-attachments/assets/21e1949b-1a4d-4638-8010-5db4bb93c772" />

<img width="882" height="248" alt="3" src="https://github.com/user-attachments/assets/59566302-e86a-464c-96df-e8bb7ef39073" />

<img width="1920" height="978" alt="4" src="https://github.com/user-attachments/assets/6770d3c6-db76-479b-82aa-cf4fd03ac011" />

<img width="1920" height="1007" alt="5" src="https://github.com/user-attachments/assets/608de548-2484-4602-b383-d769c392d547" />



## 📁 Project Structure

```
├── app.py
├── templates/
│   ├── index.html
│   └── verify.html
└── README.md
```

## ✅ Use Cases

1. College project demos

2. Learning basic Flask apps

3. Simple security flow demonstration

## ⚠️ Disclaimer
This app is intended for demo/educational use only. It does not actually send emails, and is not secure for production use.

## 📧 Author

**By S Kantha Sishanth**
