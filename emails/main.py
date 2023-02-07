"""
This function is a basic way to send Email using SendGrid API. Note: No security features are provided here.For testing enclose the sender,reciever, subject and message in a JSON object in Postman .
"""

def send_mail(request, sender=None):
    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    print("Hello")
    from flask import abort
    request_json = request.get_json(silent=True)
    print(request_json)
    parameters = ('sender', 'receiver', 'subject', 'message ')
    sender, receiver, subject, message = '', '', '', ''
    if request_json and 'sender' in request_json and 'receiver' in request_json and 'subject' in request_json and 'message' in request_json:
        print("inside if")
        sender = request_json['sender']
        receiver = request_json['receiver']
        subject = request_json['subject']
        message = request_json['message']
    else:
        print("Error occured")
        abort(400)
    print(message)
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        return 'OK', 200
    except Exception as e:
        return e, 400, "error occured"
