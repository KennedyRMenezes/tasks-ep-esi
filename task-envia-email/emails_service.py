from flask import Flask, request
import importlib

envia_email = importlib.import_module("envia-email")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def send_email():
    data = request.get_json()
    sender = data['sender']
    subject = data['subject']
    recipients = data['recipients']
    message = data['message']
    deadline = "2024-12-12"
    link = "link..."

    envia_email.Email.envia_email(subject, sender, recipients, deadline, link)

    return f"Email has been sent!"

if __name__ == "__main__":
    app.run(debug=True)