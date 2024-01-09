import smtplib
from email.message import EmailMessage
from user_info import MY_EMAIL, PASSWORD_KEY, FIDE_ID, EMAIL_SERVER

def send_email(email, tournament_name, rating):
    # SMTP Server and port no for email server
    email_server = EMAIL_SERVER
    email_port = 587

    # Starting connection
    my_server = smtplib.SMTP(email_server, email_port)
    my_server.ehlo()
    my_server.starttls()
        
    # Login with your email and password
    my_server.login(MY_EMAIL, PASSWORD_KEY)
    msg = EmailMessage()
    msg.set_content(f'''                                     
    Labdien!

    Nosūtu savu pieteikumu uz {tournament_name}:

    Vārds: (vārds)
    Uzvārds: (uzvārds)
    FIDE ID: {FIDE_ID}
    Reitings: {rating}
    Sporta klase/tituls: (sporta klase)
    Pilsēta/klubs: (pilsēta)

    Ar cieņu
    (vārds uzvārds)

    Šī ziņa tika sagatavota un nosūtīta automātiski.
                ''')

    msg['Subject'] = tournament_name
    msg['From'] = MY_EMAIL
    msg['To'] = email
    msg['CC'] = MY_EMAIL

    my_server.send_message(msg)