from flask import Flask, request, jsonify
from send_email_function import send_email, send_report
from flask_cors import CORS, cross_origin
import random
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
    message = "Hi "+data.get('name')+" this is your otp "+str(rn)
    password = "pjjn laiz iqvb ybbd"

    result=send_email(sender_email, send_to_email, subject, message, password,rn)

    return jsonify({"message": result,
                    "otp":str(rn)}), 200


@app.route('/reportManager',methods=['POST'])
def report_manager_add_employee():
    data=request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    password = "pjjn laiz iqvb ybbd"
    name=data.get('name')
    mail=data.get('email')
    managerEmail=data.get('managerEmail')
    subject="New Employee Added"
    mobile=data.get('mobile')
    message=name+" will work under you and is mobile number is "+str(mobile)+" and is email is "+str(mail);
    print(data)
    result = send_report(sender_email, managerEmail, subject, message, password)
    return jsonify({"message": result,
                    }), 200


if __name__ == '__main__':
    app.run(debug=True)
