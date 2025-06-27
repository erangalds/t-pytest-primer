import pytest
import smtplib # <--- Add this line
from email_service import send_welcome_email

def test_send_welcome_email_success(mocker):
    # Mock the smtplib.SMTP class and its methods
    mock_smtp_class = mocker.patch('email_service.smtplib.SMTP')

    # Configure the mock instance that will be returned when SMTP is called
    mock_smtp_instance = mock_smtp_class.return_value
    mock_smtp_instance.starttls.return_value = None
    mock_smtp_instance.login.return_value = None
    mock_smtp_instance.sendmail.return_value = None
    mock_smtp_instance.quit.return_value = None

    result = send_welcome_email("test@example.com", "Welcome!")

    # Assert that the mocked methods were called as expected
    mock_smtp_class.assert_called_once_with('smtp.example.com', 587)
    mock_smtp_instance.starttls.assert_called_once()
    mock_smtp_instance.login.assert_called_once_with("user@example.com", "password")
    mock_smtp_instance.sendmail.assert_called_once_with("sender@example.com", "test@example.com", "Welcome!")
    mock_smtp_instance.quit.assert_called_once()
    assert result is True

def test_send_welcome_email_failure(mocker):
    # Mock the sendmail method to raise an exception
    mock_smtp_class = mocker.patch('email_service.smtplib.SMTP')
    mock_smtp_instance = mock_smtp_class.return_value
    mock_smtp_instance.sendmail.side_effect = smtplib.SMTPException("Connection error")

    result = send_welcome_email("test@example.com", "Welcome!")

    assert result is False
    mock_smtp_instance.sendmail.assert_called_once() # Still called, but raised an exception