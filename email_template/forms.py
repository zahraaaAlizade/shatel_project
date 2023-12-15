from django import forms


class EmailForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
