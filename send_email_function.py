import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from getpass import getpass


def send_email(sender_email, send_to_email, subject, msg, password):
    result=""
    try:
        message = f"Subject: {subject}\n\n{msg}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Fix typo here
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to_email, message)
        server.quit()
        print("\nOTP sent successfully")
        result="OTP sent successfully"
    except Exception as e:
        print("\nEmail failed to send:", e)
        result="Email failed to send"
    return result

def send_email_remainder(sender_email, send_to_email, subject, msg, password):
    result=""
    try:
        message = f"Subject: {subject}\n\n{msg}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Fix typo here
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to_email, message)
        server.quit()
        print("\nEmail sent successfully")
        result="Email sent successfully"
    except Exception as e:
        print("\nEmail failed to send:", e)
        result="Email failed to send"
    return result


def send_report(sender_email, send_to_email, subject, msg, password):
    result=""
    try:
        message = f"Subject: {subject}\n\n{msg}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Fix typo here
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to_email, message)
        server.quit()
        print("\nReport sent successfully")
        result="Report sent successfully"
    except Exception as e:
        print("\nEmail failed to send:", e)
        result="Email failed to send"
    return result

def send_idCard(pdf_filename, sender_email, send_to_email, subject, msg, password):
    result = ""
    try:
        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = send_to_email
        message['Subject'] = subject

        # Attach the PDF file
        with open(pdf_filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {pdf_filename}')
            message.attach(part)

        # Add the message body
        message.attach(MIMEText(msg, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to_email, message.as_string())
        server.quit()

        print("\nReport sent successfully")
        result = "Report sent successfully"
    except Exception as e:
        print("\nEmail failed to send:", e)
        result = "Email failed to send"
    return result

# sender_email = "rithikmanagement@gmail.com"
# send_to_email = "rithiksuthan123@gmail.com"
# subject = "Mail Check"
# message = "hi da"
# password = "pjjn laiz iqvb ybbd"
#
# send_email(sender_email, send_to_email, subject, message, password)