from django import forms


class UnsubscribeForm(forms.Form):
    """Unsubscribe form."""
    email = forms.EmailField()
