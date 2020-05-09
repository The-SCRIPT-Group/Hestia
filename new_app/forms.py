from django import forms


class PageForm(forms.Form):
    key = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Certificate Number'})
    )
