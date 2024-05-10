from flask import Flask, request, jsonify
from send_email_function import send_email

app = Flask(__name__)


@app.route('/sendotp', methods=['POST'])
def send_email_route():
    data = request.get_json()
    sender_email = "rithikmanagement@gmail.com"
    send_to_email = data.get('send_to_email')
    subject = data.get('subject')
    message = data.get('message')
    password = "pjjn laiz iqvb ybbd"

    send_email(sender_email, send_to_email, subject, message, password)

    return jsonify({"message": "Email sent successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
