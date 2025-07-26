from django import forms

class userForm(forms.Form):
    username=forms.ChoiceField()
    pwd=forms.ChoiceField()
