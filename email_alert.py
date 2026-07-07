import smtplib
from email.message import EmailMessage


SENDER_EMAIL = "ishitachandra0508@gmail.com"
APP_PASSWORD = "hrfkzsbhbwnitcog"

RECEIVER_EMAIL = SENDER_EMAIL  # You can change this to any email address you want to receive the alerts


def send_email(image_path, confidence):

    msg = EmailMessage()

    msg["Subject"] = "🚨 AI Surveillance Alert"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    msg.set_content(
        f"""
Person detected!

Confidence : {confidence:.2f}

Check the attached image.
"""
    )

    with open(image_path, "rb") as file:
        image_data = file.read()

    msg.add_attachment(
        image_data,
        maintype="image",
        subtype="jpeg",
        filename=image_path.split("/")[-1]
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(SENDER_EMAIL, APP_PASSWORD)

        smtp.send_message(msg)