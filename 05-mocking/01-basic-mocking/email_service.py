import smtplib

def send_welcome_email(recipient_email, message):
    try:
        # Simulate connecting to an SMTP server
        smtp_server = smtplib.SMTP('smtp.example.com', 587)
        smtp_server.starttls()
        smtp_server.login("user@example.com", "password")
        smtp_server.sendmail("sender@example.com", recipient_email, message)
        smtp_server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False