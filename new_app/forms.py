from django import forms


class PageForm(forms.Form):
    key = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Certificate Number'})
    )
    CHOICES = [
    ('selection', '----Select event----'),
    ('codex-dec', 'CodeX December'),
    ('bov', 'Battle Of Vars'),
    ]
    event = forms.TypedChoiceField(
    choices=CHOICES,
    )
    event.widget.attrs.update({'placeholder':'Event'})
