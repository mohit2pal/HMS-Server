from flask import Flask, request
from flask_cors import CORS
import os
from flask_mail import Mail, Message

from dotenv import load_dotenv

load_dotenv()

mail_username = os.environ.get('MAIL_USERNAME')
mail_password = os.environ.get('MAIL_PASSWORD')

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
CORS(app)

mail = Mail(app)


@app.route("/")
def index():
    return "This is HMS-Server"


@app.route('/send-email', methods=["POST"])
def send_email():
    if request.method == "POST":
        data = request.form

        subject = data["subject"]
        recipient = data["recipient"]
        body = data["body"]

        if not (subject and recipient and body):
            return 'Invalid request. Please provide subject, recipient, and body parameters.'

        msg = Message(subject=subject, sender=mail_username, recipients=[recipient])
        msg.body = body
        mail.send(msg)

        return 'Email sent successfully!'


if __name__ == '__main__':
    app.run()
