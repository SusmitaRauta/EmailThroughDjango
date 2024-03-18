from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
class SendMailForm(forms.Form):
    subject=forms.CharField(label='Enter subject',max_length=100)
    message=forms.CharField(label="Enter Message",max_length=100)
    mailid=forms.EmailField(label='Enter mailid')
class ComposeForm(forms.Form):
    subject=forms.CharField(label='Enter subject',max_length=100)
    body=forms.CharField(label='Enter message',max_length=100)
    to=forms.EmailField(label='Eneter Emailid')
    attachment=forms.FileField(label="Attached File",max_length=100)
    
    def __init__(self, *args, **kwargs):
        super(ComposeForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'class': 'form-control'})
        self.fields['to'].widget.attrs.update({'class': 'form-control'})
        self.fields['attachment'].widget.attrs.update({'class': 'form-control'})