from django import forms
from .models import ContactForm


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={"class": "form-control custom-input"}),
    )
    customer_name = forms.CharField(
        max_length=64,
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control custom-input"}),
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={"class": "form-control custom-textarea", "rows": 5}
        ),
    )


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["customer_email", "customer_name", "message"]
