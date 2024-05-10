import smtplib
from getpass import getpass

def send_email(sender_email, send_to_email, subject, msg, password,rn):
    try:
        message = f"Subject: {subject}\n\n{msg}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Fix typo here
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to_email, message)
        server.quit()
        print("\nEmail sent successfully")
    except Exception as e:
        print("\nEmail failed to send:", e)

# sender_email = "rithikmanagement@gmail.com"
# send_to_email = "rithiksuthan123@gmail.com"
# subject = "Mail Check"
# message = "hi da"
# password = "pjjn laiz iqvb ybbd"
#
# send_email(sender_email, send_to_email, subject, message, password)
