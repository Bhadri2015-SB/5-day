from celery import Celery
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# load_dotenv()


celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def send_email_background(email: str):
    print(f"Sending email to {email}...")
    time.sleep(5)
    print(f"Email to {email} sent!")
    return f"Email sent to {email}"
# def send_email_background(email: str, reset_link: str):
#     sender_email = os.getenv("EMAIL_USERNAME")
#     sender_password = os.getenv("EMAIL_PASSWORD")

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = email
#     message["Subject"] = "Password Reset Request"

#     body = f"""
#     <p>checking mail</p>
#     <p>If you did not request this, please ignore this email.</p>
#     """
#     message.attach(MIMEText(body, "html"))

#     try:
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()  # Upgrade the connection to secure
#             server.login(sender_email, sender_password)
#             server.sendmail(sender_email, email, message.as_string())
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Error sending email: {e}")
