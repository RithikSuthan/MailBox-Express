from flask import Flask, request, jsonify
from send_email_function import send_email
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

    send_email(sender_email, send_to_email, subject, message, password,rn)

    return jsonify({"message": "Email sent successfully",
                    "otp":str(rn)}), 200


if __name__ == '__main__':
    app.run(debug=True)
