from django import forms


class TerminalForm(forms.Form):
    command = forms.CharField()
