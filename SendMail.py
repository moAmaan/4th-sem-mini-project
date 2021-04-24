# import files
import AudioToText
import GetAudio
import GetCredentials
import ToAudio
# Get credentails
(username, password, contact) = GetCredentials.GetCredentials('send')

# Record message
GetAudio.GetAudio()

# Convert to text
msg = AudioToText.AudioToText()

# Send mail
import smtplib
from email.mime.text import MIMEText
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465


from_addr = username
to_addrs = contact

message = MIMEText(msg)
message['subject'] = ("Voiced mail System")
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
ToAudio.Confirm()
server.quit()