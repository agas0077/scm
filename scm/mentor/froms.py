from django import forms

from mentor.models import Mentee, Mentor, DESCRIPTION_NAME

DESCRIPTION_PLACEHOLDER = ('Укажите ваши ожидания от учстия в ментроской '
                           'программе.')


class SignUpBaseForm(forms.ModelForm):
    description = forms.CharField(label=DESCRIPTION_NAME,
                                  widget=forms.Textarea(attrs={
                                      'placeholder': DESCRIPTION_PLACEHOLDER,
                                      'class': 'form-control',
                                      'rows': '10',
                                  }))

    class Meta:
        fields = ('description', )


class SignUpMenteeForm(SignUpBaseForm):
    class Meta(SignUpBaseForm.Meta):
        model = Mentee


class SignUpMentorForm(SignUpBaseForm):
    class Meta(SignUpBaseForm.Meta):
        model = Mentor
