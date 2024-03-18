from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
from django.shortcuts import render
from django.core.mail import EmailMessage
from emailapp.forms  import SendMailForm,ComposeForm
from EmailThroughDjango import settings
from django.http import HttpResponse

# Create your views here.

def SendSimpleEmail(request):
    if request.method=='POST':
        form=SendMailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            msg=form.cleaned_data['message']
            mail=form.cleaned_data['mailid']
            rec=send_mail(subject,msg,"user@gmail.com",[mail])
            return render(request,"message.html")
    else:
        form=SendMailForm()
        return render(request,"mailbox.html",{'form':form})
def SendEmailWithAttach(request):
    if request.method=='POST':
        form=ComposeForm(request.POST,request.FILES)
        print("POST data:", request.POST)  # Debugging statement
        print("FILES data:", request.FILES)
        if form.is_valid():
            subj=form.cleaned_data['subject']
            bd=form.cleaned_data['body']
            to=form.cleaned_data['to']
            attfile=request.FILES.get('attachment')
            print("Attachment:", attfile)
            email=EmailMessage(subj,bd,settings.EMAIL_HOST_USER,[to])
            # fd=open(attfile,'r')
            # email.attach(attfile,fd.read(),'text/plain')
            email.attach(attfile.name, attfile.read(), attfile.content_type)
            email.send()
            return render (request,"message.html")
    else:
        form=ComposeForm()
    return render(request,'mailbox.html',{'form':form})
def SendMassEmail(request):
    msq1=("Hello","How are you",settings.EMAIL_HOST_USER,['user@gmail.com'])
    msq2=('Hy','Django class is started',settings.EMAIL_HOST_USER,['receiver@gmail.com'])
    messages = [msq1, msq2]
    rec=send_mass_mail(messages,fail_silently=False)
    return HttpResponse("%s" %rec)