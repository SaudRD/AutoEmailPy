import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#your email and passowrd
Email = ''
Password = ''

def send_email(text="email body", sbject='test',from_email='Eng. Saud Alardi <saudalardi@outlook.sa', to_emails=None):
    assert isinstance(to_emails, list)

    #here am using Smtp for outlook, you can use Gmail "smtp.gmail.com" but you need to auth less security from email settings.
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = sbject

    html = """\
    <html>
    <head></head>
    <body>
    <p>
    Greeting Recruiters,
    <br>        <br>
    How you doing? I hope you well.
    <br>        <br>
    <b>
    •	I’m a Computer Engineer graduated First honor class with a GPA of 4.97/5 <br>
    •	I had Internship at Aramco and got a recommendation for Information Security Specialist. <br>
    •	I have a lot of knowledge in Network, Cyber Security and programming as well. <br>
    </b>
    <br>
    I have attached my C.V. and Aramco Recommendation letter for your consideration.
    Kindly take a look.
    <br>
    <br>
    Regards.
    </p>
    </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    #Here the attachemnt you can do with loops if you have more    
    pdf1 = "Aramco Cert Complete.pdf"
    with open(pdf1, "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(pdf1))
    msg.attach(attach)
  
    
    server.ehlo()
    server.starttls()
    server.login(Email,Password)
    server.sendmail(from_email,to_emails,msg.as_string())

#Here am just usting the to emails attrpiute to send for 1 email.
send_email(to_emails=['saudalardi@outlook.sa'])