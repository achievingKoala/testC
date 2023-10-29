from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    sender_address = 'lkw_create@outlook.com'
    sender_pass = os.environ.get('SENDER_PASS')
    print('----', sender_pass)
    receiver_address = request.form['email']
    mail_content = request.form['content']
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.office365.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    return 'Mail Sent'

if __name__ == '__main__':
    app.run(debug=True)