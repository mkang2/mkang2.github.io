import smtplib
from email.message import EmailMessage
from urllib.parse import urlparse
import os

# Get email server credentials from environment variables
email_address = os.environ['EMAIL_ADDRESS']
email_password = os.environ['EMAIL_PASSWORD']

# Parse the website domain from the referrer URL
referrer = os.environ.get('HTTP_REFERER')
if referrer:
    domain = urlparse(referrer).hostname
else:
    domain = ''

# Get form data from POST request
name = os.environ['QUERY_STRING'].split('&')[0].split('=')[1]
email = os.environ['QUERY_STRING'].split('&')[1].split('=')[1]
message = os.environ['QUERY_STRING'].split('&')[2].split('=')[1]

# Create email message
msg = EmailMessage()
msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")
msg['Subject'] = f"New message from {domain}"
msg['From'] = email_address
msg['To'] = email_address

# Send email using SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.send_message(msg)

# Redirect user to thank you page
print("Location: thankyou.html\n\n")
