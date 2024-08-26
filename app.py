import io

from flask import Flask
from send_email_function import send_email, send_report, send_idCard, send_email_remainder
from flask_cors import CORS, cross_origin
import random
from flask import request, jsonify
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from send_email_function import send_idCard  # Import your send_email function here
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

    result = send_email(sender_email, send_to_email, subject, message, password)

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

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
    profile_image_path = data['profileImage']  # Path to profile image
    print("Employee Name:", employee_name)
    print("Employee Position:", employee_position)
    print("Employee Email:", employee_email)
    print("Employee Mobile:", employee_mobile)
    print("Company:", company)
    print("profile_image_path:", profile_image_path)
    html_content = """
        <div style="border: 2px solid #000; border-radius: 10px; max-width: 400px; margin: 0 auto; padding: 20px; background-color: #fff; font-family: Arial, sans-serif;">
            <div style="text-align: center; margin-top: 20px;">
                <h2 style="margin: 5px 0;">{employee_name}</h2>
                <p style="margin: 5px 0; font-size: 16px; color: #555;">{employee_position}</p>
            </div>
            <hr style="border-top: 2px solid #000; margin: 20px 0;">
            <div style="margin-bottom: 10px;">
                <p style="margin: 5px 0;"><strong>Email:</strong> {employee_email}</p>
                <p style="margin: 5px 0;"><strong>Mobile:</strong> {employee_mobile}</p>
                <p style="margin: 5px 0;"><strong>Company:</strong> {company}</p>
            </div>
            <div style="text-align: center;">
                <img style="height: 100px; width: 100px;" src="https://cdn.vectorstock.com/i/500p/00/35/letter-s-leaf-logo-vector-45880035.jpg" alt="Company Logo">
            </div>
        </div>
    """.format(profile_image_path=data['profileImage'],
               employee_name=employee_name,
               employee_position=employee_position,
               employee_email=employee_email,
               employee_mobile=employee_mobile,
               company=company)

    # Sending email
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = employee_email
        msg['Subject'] = f"Hi {employee_name}, Here is your Access Card"
        msg.attach(MIMEText(html_content, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, employee_email, msg.as_string())
        server.quit()

        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# def send_id_card():
#     data = request.get_json()
#     sender_email = "rithikmanagement@gmail.com"
#     password = "pjjn laiz iqvb ybbd"
#     employee_name = data['employeeName']
#     employee_position = data['position']
#     employee_email = data['email']
#     employee_mobile = data['phoneNumber']
#     company = data['company']
#     # profile_image_path = data["profileImage"]
#     profile_image_path = "logo.JPG"
#     pdf_filename = f'{employee_name}_id_card.pdf'
#     subject="Hi "+employee_name+(" ,Here it is your Access Card .Carry the Access Card Everywhere in the office "
#                                  " .Welcome to the ")+company+"  family."
#     try:
#         c = canvas.Canvas(pdf_filename, pagesize=letter)
#         c.setFillColorRGB(0.8, 0.8, 0.8)  # Light gray background color
#         c.rect(0, 0, letter[0], letter[1], fill=True)  # Background color fill
#         c.setStrokeColorRGB(0, 0, 0)  # Black border color
#         c.rect(10, 10, letter[0] - 20, letter[1] - 20)  # Border around the ID card
#         if profile_image_path!="":
#             profile_image = ImageReader(profile_image_path)
#         else:
#             profile_image = ImageReader("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png")
#         c.drawImage(profile_image, 50, letter[1] - 250, width=200, height=200, mask='auto')
#         c.setFont("Helvetica-Bold", 16)
#         c.setFillColorRGB(0, 0, 0)  # Black color for text
#         c.drawString(280, letter[1] - 100, f'Name: {employee_name}')
#         c.drawString(280, letter[1] - 130, f'Position: {employee_position}')
#         c.drawString(280, letter[1] - 160, f'Email: {employee_email}')
#         c.drawString(280, letter[1] - 190, f'Mobile: {employee_mobile}')
#         c.drawString(280, letter[1] - 220, f'Company: {company}')
#         c.save()
#         result = send_idCard(pdf_filename, sender_email, employee_email, "Access Card", subject, password)
#         return jsonify({"message": result}), 200
#     except Exception as e:
#         print("Error")
#         return jsonify({"error": str(e)}), 500

@cross_origin()
@app.route("/sendRemainder",methods=['POST'])
def sendRemainder():
    data=request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    send_to_email = data.get('mail')
    subject = data.get('subject')
    message = data.get('message')
    password = "pjjn laiz iqvb ybbd"
    print(send_to_email)
    result = send_email_remainder(sender_email, send_to_email, subject, message, password)
    return jsonify({"message": result}), 200


@cross_origin()
@app.route("/sendforgetPassword",methods=['POST'])
def sendforgetPassword():
    data=request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    send_to_email = data.get('mail')
    subject = data.get('subject')
    message = data.get('message')
    password = "pjjn laiz iqvb ybbd"
    print(send_to_email)
    result = send_email_remainder(sender_email, send_to_email, subject, message, password)
    return jsonify({"message": result}), 200

@app.route("/contact",methods=['POST'])
def getContact():
    data=request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    send_to_email = "rithiksuthan123@gmail.com"
    subject = "Message from Portfolio from "+data.get('from_name')
    message = data.get('message')+" .Further contact at "+data.get('email_id')
    password = "pjjn laiz iqvb ybbd"
    result = send_email_remainder(sender_email, send_to_email, subject, message, password)
    return jsonify({"message": "Mail Sent Successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
