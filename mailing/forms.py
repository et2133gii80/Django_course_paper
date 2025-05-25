# flake8: noqa
from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from .models import AttemptMailing, Mailing, Message, ReceiveMail


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, label="Тема письма")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    recipients = forms.CharField(widget=forms.Textarea, label="Получатели (через запятую)")


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        #exclude = ("set_is_active", "owner", "first_sending", "end_sending")


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:

        model = Message
        fields = "__all__"


class ReceiveMailForm(StyleFormMixin, ModelForm):

    class Meta:

        model = ReceiveMail
        fields = "__all__"
        exclude = ("can_blocking_client", "owner")


class ReceiveMailModeratorForm(StyleFormMixin, ModelForm):
    class Meta:

        model = ReceiveMail
        fields = "__all__"


class MailingModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"
