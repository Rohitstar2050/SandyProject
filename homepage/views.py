from django.shortcuts import render,redirect
from .models import contactdata
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def sendMail(name,email,msg):
    mail_content = '''Filled details are mentioned below:
                      Name:'''+name+'''
                      Email ID:'''+email+'''
                      Message:'''+msg+'''
                      
                      Note:do not reply this is system generated mail.
                    
    '''
    # The mail addresses and password
    sender_address = 'pnitech20@gmail.com'
    sender_pass = '882838916388'
    receiver_address = 'pnitech20@gmail.com'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Mail from Webserver PNI TECH'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def blog(request):
    return render(request,'blog.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    # validate={}
    # validate['validation'] = 'none'
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactsubmit(request):
    name=request.POST['name']
    email = request.POST['email']
    msg= request.POST['msg']
    validate={}

    if name!="" and email!="":
        validate['validationpass']=True
        ref=contactdata(name=name,emailid=email,msg=msg)
        ref.save()
        sendMail(name,email,msg)
        return render(request,'contact.html',validate)
        # return redirect('contact')
    else:
        validate['validationfail'] =True
        return render(request,'contact.html',validate)
