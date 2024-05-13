import tempfile
import urllib
from io import BytesIO
import base64

from PIL import Image
from flask import Flask
from send_email_function import send_email, send_report, send_idCard
from flask_cors import CORS, cross_origin
import random
from flask import request, jsonify
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from send_email_function import send_idCard  # Import your send_email function here
import pdfkit
import imgkit
app = Flask(__name__)
CORS(app)


@cross_origin()
@app.route('/sendotp', methods=['POST'])
def send_email_route():
    rn = random.randrange(100000, 1000000)
    print(rn)
    data = request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    send_to_email = data.get('send_to_email')
    subject = "Otp Verification"
    message = "Hi " + data.get('name') + " this is your otp " + str(rn)
    password = "pjjn laiz iqvb ybbd"

    result = send_email(sender_email, send_to_email, subject, message, password, rn)

    return jsonify({"message": result,
                    "otp": str(rn)}), 200


@app.route('/reportManager', methods=['POST'])
def report_manager_add_employee():
    data = request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    password = "pjjn laiz iqvb ybbd"
    name = data.get('name')
    mail = data.get('mail')
    managerEmail = data.get('managerEmail')
    subject = "New Employee Added"
    mobile = data.get('mobile')
    message = name + " will work under you and is mobile number is " + str(mobile) + " and is email is " + str(mail);
    result = send_report(sender_email, managerEmail, subject, message, password)
    return jsonify({"message": result,
                    }), 200

@cross_origin()
@app.route('/sendidcard', methods=['POST'])
def send_id_card():
    data = request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    password = "pjjn laiz iqvb ybbd"
    employee_name = data['employeeName']
    employee_position = data['position']
    employee_email = data['email']
    employee_mobile = data['phoneNumber']
    company = data['company']
    profile_image_base64 = data["profileImage"]
    subject = f"Hi {employee_name}, here is your Access Card. Carry the Access Card Everywhere in the office. Welcome to the {company} family."

    try:
        # Construct HTML email content with ID card template
        html_content = f"""
        <html>
        <head><title>ID Card</title></head>
        <body>
            <h1>ID Card</h1>
            <img src='data:image/jpeg;base64,{profile_image_base64}' width='200'>
            <p>Name: {employee_name}</p>
            <p>Position: {employee_position}</p>
            <p>Email: {employee_email}</p>
            <p>Mobile: {employee_mobile}</p>
            <p>Company: {company}</p>
        </body>
        </html>
        """

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = employee_email
        msg['Subject'] = subject

        # Attach HTML content as email body
        msg.attach(MIMEText(html_content, 'html'))

        # Send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
