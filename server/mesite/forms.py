from django.forms import Form, Textarea, CharField


class InputForm(Form):
    text = CharField(label='Your description',
                     required=True,
                     widget=Textarea(attrs={
                         'class': 'form-control',
                         'placeholder': 'Your description',
                         'rows': 3,
                     }))
