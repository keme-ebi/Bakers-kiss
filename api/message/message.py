"""
sends messages to user
"""
from flask import current_app
from flask_mail import Message


def send_email(subject, message, recipient):
    """
    sends message to an email
    Args:
        message(str): The body of the message
        recipient: recipient email
    """
    msg = Message(
        subject=subject,
        recipients=[recipient],
    )
    msg.body = message
    current_app.mail.send(msg)