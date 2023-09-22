import os
import smtplib
import sys
# import getpass
import time

def mail(sender_mail, sender_psd, adressee_mail, message, subject = 'mail_from_De_Evil', color = 1):
    smtp_server = 'smtp.gmail.com'
    port = 587
    #Login:
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        if smtp_server == "smtp.gmail.com":
            server.starttls()
            server.login(sender_mail, sender_psd)
    # Sending:
        for i in range(1, int(color)+1):
            message = 'From: ' + str(sender_mail) + '\nSubject: ' + str(subject) + '\n' + str(message)
            server.sendmail(sender_mail, adressee_mail, message)
            print ("\033[94m \033[97m Email \033[92mSENT\033[97m :\033[93m",i)
            sys.stdout.flush()
        server.quit()
        print ('\033[93m \033[97m All \033[97mMessage was\033[92m sent\033[97m ') 


    except smtplib.SMTPAuthenticationError:
        print(" ")
        print("\033[94m \033[91mError \033[97m:") 
        print ('\033[94m \033[97mThe \033[93musername \033[97mor \033[93mpassword\033[97myou entered is incorrect.')
        print ("\033[94m \033[91mCheck if the Options of 'Applications are less secure' is enabled\nCheck at https://myaccount.google.com/lesssecureapps")
        sys.exit()

#MAIN
# user = input('\033[92mYour \033[92mGmail\033[97m :\033[94m ')
# Password = getpass.getpass('\033[92mYour \033[92mPassword\033[97m :\033[94m ')
# sender = input('\n\033[91mTo Victim \033[91mEmail\033[97m : \033[94m')
# message = input('\033[92mYour \033[92mMessage\033[97m : \033[94m')
# subject = input('\nSubject of the mail : ')
# color = int(input('\n\033[92mNumber of \033[92msend\033[97m : \033[94m'))
# mail(user, Password, sender, message, subject, color)
