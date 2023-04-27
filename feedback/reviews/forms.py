from django import forms 

# review form class

class ReviewForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100, error_messages= {
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name!"
    })
