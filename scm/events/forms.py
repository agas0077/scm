from django import forms

from events.models import EventMember


class EventSignUpForm(forms.ModelForm):

    class Meta:
        model = EventMember
        fields = ('__all__')
