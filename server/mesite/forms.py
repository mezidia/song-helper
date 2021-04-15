from django.forms import Form, Textarea, CharField, TextInput


class MainForm(Form):
    text = CharField(label='Your description',
                     required=True,
                     widget=Textarea(attrs={
                         'class': 'form-control',
                         'placeholder': 'Write your description here',
                         'rows': 3,
                     }))


class AddForm(Form):
    song_id = CharField(label='ID of song',
                        required=True,
                        widget=TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Write Spotify ID of song. For example, 4Km5HrUvYTaSUfiSGPJeQR',
                        }))
