from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'subject': forms.Select(attrs={
                'class': 'form-control custom-select',
            })
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].choices = [('', 'Select Subject...')] + list(Contact.SUBJECT_CHOICES)
        self.fields['subject'].initial = ''
        self.fields['subject'].required = True
