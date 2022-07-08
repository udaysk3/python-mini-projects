import smtplib
from email.mime.text import MIMEText
import email

your_email = "gfgscliet@gmail.com"
your_password = "qqrjopcfbrtjfvri"

names = ['S.Madhu Sudan', 'G.sai pavan', 'MANDALA GOWTHAM KUMAR', 'KOTESWARA RAO PAKEERI', 'MERAGANA VENKATARAMANA'
        , 'Hashita Pusapati', 'PASALA TEJA', 'BALI DHANUNJAYA RAO', 'Rali Venkata Siddardha']
emails = ['madhusudhanpatnaik20033@gmail.com', 'pavangsn143@gmail.com', 'gowthamandala2003@gmail.com','santhuaspirer@gmail.com'
            ,'venkymeragana@gmail.com','pusapatihashita012@gmail.com', 'teja.pasala948@gmail.com','burluudaysantoshkumar3@gmail.com', '20kd1a0509@lendi.org', 'rvsidhardha@hotmail.com']

emails2 = ['burluudaysantoshkumar3@gmail.com', 'hemanthkumar8251@gmail.com']

message = '''
Subject: Interview Invitation Mail\n

Hello, This is a reminder that your interview is scheduled between 7-8 pm today. You are requested to join through this google-meet link: https://meet.google.com/adz-gzxc-hbj.

You have to join this meet only when you receive an invitation message from any one of the admins of GFGSCLIET. 

For any queries: 
send reply to this email.

Thank You.
Regards:
Team GFGSCLIET
'''

msg = email.message.EmailMessage()
msg['Subject'] = "Interview Invitation Mail"
msg['From'] = your_email
msg['To'] = emails
msg.set_content(message)

with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()
    s.login(your_email, your_password)
    s.send_message(msg)

# for dest in emails2:
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(your_email, your_password)
#     s.sendmail(your_email, dest, message)
#     s.quit()
#     print("message sent to "+dest)
       