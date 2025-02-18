import imaplib
import email

# Set up the IMAP connection
mail = imaplib.IMAP4_SSL('jump.msk')
mail.login('ivan.ivanov', '1')
mail.select('inbox')

# Search for all email messages in the inbox
status, data = mail.search(None, 'ALL')

# Iterate through each email message and print its contents
for num in data[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    email_message = email.message_from_bytes(data[0][1])
    print('From:', email_message['From'])
    print('Subject:', email_message['Subject'])
    print('Date:', email_message['Date'])
    print('Body:', email_message.get_payload())
    print()

# Close the connection
mail.close()
mail.logout()