from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message',
            'rows': 4
        })
    )
    
    # Optional: Custom validation for fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "example.com" in email:
            raise forms.ValidationError("Emails from 'example.com' are not allowed.")
        return email

