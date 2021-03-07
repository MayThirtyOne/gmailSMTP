#!/usr/bin/env python
# coding: utf-8

# In[28]:


import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from datetime import date
import sys


# In[29]:


with open('config.json') as f:
    config=json.load(f)


# In[30]:


message = MIMEMultipart()
body = config['body']
message["From"] = config['sender_email_alias']
message["Subject"] = config['subject']
recp = config['receiver_email'].replace(" ", "").strip().split(",")


# In[31]:



the_date = str(today.strftime("%B %d, %Y"))
argument_1 = sys.argv[1]
argument_2 = sys.argv[2]
body = the_date + " " + argument_1 + " " + argument_2 +" "
message.attach(MIMEText(body, "plain"))


# In[32]:


if config['file_attachment_mode'] == 'True':
    filename = config['default_attachment_name']
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)


# In[ ]:





# In[33]:


# Log in to server using secure context and send email
text = message.as_string()
context = ssl.create_default_context()
with smtplib.SMTP_SSL(config['smtp'], config['port'], context=context) as server:
    server.login(config['sender_email'], config['password'])
    server.sendmail(config['sender_email'], recp, text)


# In[ ]:





# In[ ]:




