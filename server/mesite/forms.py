from django.forms import Form, Textarea, CharField


class InputForm(Form):
    text = CharField(label='Your description',
                     required=True,
                     widget=Textarea(attrs={
                         'class': 'form-control',
                         'placeholder': 'Write your description here',
                         'rows': 3,
                     }))
