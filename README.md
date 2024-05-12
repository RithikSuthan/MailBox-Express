# MailBox-Express

MailBox-Express is a platform for generating OTPs (One-Time Passwords) and sending them via email. It is developed using Flask and SMTP, and it is deployed on Google Cloud Platform.

## Overview

MailBox-Express simplifies the process of generating and sending OTPs via email. It provides a RESTful API endpoint `/sendotp` where clients can send POST requests with recipient email addresses. Upon receiving a request, MailBox-Express generates a random OTP and sends it to the specified email address.

The platform is built using Flask, a lightweight web framework for Python, and it leverages SMTP (Simple Mail Transfer Protocol) for sending emails. It is deployed on Google Cloud Platform (GCP) using Google App Engine.

## Usage

To use MailBox-Express, clients can send POST requests to the `/sendotp` endpoint with the following payload:

```json
Modify JSON according to your needs
{
  "send_to_email": "recipient@example.com",
  "name": "Recipient Name"  
}
```

Upon successful processing of the request, MailBox-Express sends an email to the specified recipient containing the OTP.

## Deployment

MailBox-Express is deployed on Google Cloud Platform (GCP) using Google App Engine. The deployment process involves configuring the `app.yaml` file with the runtime settings and deploying the Flask application using the `gcloud app deploy` command.

To deploy MailBox-Express on Google App Engine:

1. Ensure that you have the Google Cloud SDK installed and configured on your local machine.
2. Update the `app.yaml` file with the appropriate runtime settings and configurations.
3. Run the command `gcloud app deploy` in the project directory to deploy the application to Google App Engine.

## Local Development

To run MailBox-Express locally for development or testing purposes:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file using pip.
3. Run the Flask application locally using the command `python app.py`.
4. Access the application in your web browser at `[https://mailboxexpress.el.r.appspot.com](https://mailboxexpress.el.r.appspot.com)`.

## Contributing

Contributions to MailBox-Express are welcome! If you encounter any issues, have feature requests, or would like to contribute code, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
