import smtplib 
import email
from email.message import EmailMessage
from user_info import MY_EMAIL, PASSWORD_KEY, FIDE_ID

def send_email(email, tournament_name, rating):
    # SMTP Server and port no for inbox.lv
    inbox_server= "mail.inbox.lv"
    inbox_port= 587

    # Starting connection
    my_server = smtplib.SMTP(inbox_server, inbox_port)
    my_server.ehlo()
    my_server.starttls()
        
    # Login with your email and password
    my_server.login(MY_EMAIL, PASSWORD_KEY)
    msg = EmailMessage()
    msg.set_content(f'''                                     
    Labdien!

    Nosūtu savu pieteikumu uz {tournament_name}:

    Vārds: (vards)
    Uzvārds: (uzvards)
    FIDE ID: {FIDE_ID}
    Reitings: {rating}
    Sporta klase/tituls: (sporta klase)
    Pilsēta/klubs: (pilseta)

    Ar cieņu
    (vards uzvards)

    Šī ziņa tika sagatavota un nosūtīta automātiski.
                ''')

    msg['Subject'] = tournament_name
    msg['From'] = MY_EMAIL
    msg['To'] = email
    msg['CC'] = MY_EMAIL

    my_server.send_message(msg)
    print('Mail Sent to', msg['To'], msg['CC'], msg['Subject'])