from django import forms


class UrlParserForm(forms.Form):
    url = forms.URLField(required=True)
