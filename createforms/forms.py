from django import forms

class Studentform(forms.Form):

    name = forms.CharField( max_length=50) 
    email = forms.EmailField(label = "E-mail")
    category = forms.ChoiceField(choices = [('question', 'Question'),('other','Other')])  
    subject = forms.CharField(required = False)
    body = forms.CharField(widget=forms.Textarea)