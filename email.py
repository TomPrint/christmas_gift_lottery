import random
from email.message import EmailMessage
import smtplib

email_sender = 'sendersemial@gmail.com'
email_password ='yourpasswordhere'

# your participants and email addresses here
emails = {"Tomek": "email1@email.com", "Kuba": "email2@email.com",
          "Iwona": "email3@email.com", "Malwina": "email4@email.com",
          "Gosia": "email5@email.com", "Staszek":"email6@email.com"}

# get_names function joins two lists and creates a dictionary through 'dict comprehension',
# excluding drawing oneself from the list, i.e Tomek : Tomek.
# while loop allows to return a dictionary of pairs, after loop returns six records (unique pairs)
def get_names():
    names = ["Tomek", 'Kuba', "Iwona", "Malwina", "Gosia", "Staszek"]
    while True:
        random.shuffle(names)
        pairs = {key: value for key, value in zip(names, names[1:] + names[:1])}
        if len(pairs) == len(names):
            return pairs

person = get_names()
print (person) # to check the get_names result

# Set up the SMTP server for sender's email, i.e. gmail email.
server = smtplib.SMTP('smtp.gmail.com', 465)
server.starttls()
server.login(email_sender, email_password)

# Send an email to each participant with the information about the person they need to buy a gift for
for name, email in emails.items():
    message = EmailMessage()
    message['From'] = email_sender
    message['To'] = email
    message['Subject'] = "Christmas gift exchange"
    message.set_content(f" Merry Christmas {name},\n Santa's lottery has chosen that this year you buy a gift for {person[name]}.\n Best Regards,\n Your Dear Santa")
    server.send_message(message)

server.quit()
