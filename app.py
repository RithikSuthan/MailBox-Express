from flask import Flask
from send_email_function import send_email, send_report, send_idCard
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
    profile_image_path = data["profileImage"]
    pdf_filename = f'{employee_name}_id_card.pdf'
    subject="Hi "+employee_name+(" ,Here it is your Access Card .Carry the Access Card Everywhere in the office "
                                 " .Welcome to the ")+company+"  family."
    try:
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFillColorRGB(0.8, 0.8, 0.8)  # Light gray background color
        c.rect(0, 0, letter[0], letter[1], fill=True)  # Background color fill
        c.setStrokeColorRGB(0, 0, 0)  # Black border color
        c.rect(10, 10, letter[0] - 20, letter[1] - 20)  # Border around the ID card
        if profile_image_path!="":
            profile_image = ImageReader(profile_image_path)
        else:
            profile_image = ImageReader("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png")
        c.drawImage(profile_image, 50, letter[1] - 250, width=200, height=200, mask='auto')
        c.setFont("Helvetica-Bold", 16)
        c.setFillColorRGB(0, 0, 0)  # Black color for text
        c.drawString(280, letter[1] - 100, f'Name: {employee_name}')
        c.drawString(280, letter[1] - 130, f'Position: {employee_position}')
        c.drawString(280, letter[1] - 160, f'Email: {employee_email}')
        c.drawString(280, letter[1] - 190, f'Mobile: {employee_mobile}')
        c.drawString(280, letter[1] - 220, f'Company: {company}')
        c.save()
        result = send_idCard(pdf_filename, sender_email, employee_email, "Access Card", subject, password)
        return jsonify({"message": result}), 200
    except Exception as e:
        print("Error")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
