from django import forms
from .models import Contact,HireEnquiry





class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
       
       
class HireEnquiryForm(forms.ModelForm):
    class Meta:
        model = HireEnquiry
        fields = "__all__"