from django import forms
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy

from members.models import Member, TERMS_AGREE_NAME


class MemberForm(forms.ModelForm):
    terms_agree = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input me-2'}),
        required=True,
        label_suffix='')

    class Meta:
        model = Member
        fields = ('__all__')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        link = reverse_lazy("core:policy")
        label = (f'<a href="{link}" class="link-light fw-bold"'
                 f' target="_blank">{TERMS_AGREE_NAME}</a>')
        self.fields['terms_agree'].label = mark_safe(label)

    def clean_terms_agree(self):
        agreed = self.cleaned_data.get('terms_agree')

        if not agreed:
            raise forms.ValidationError(
                'Необходимо принять условия политики конфиденциальности!'
            )

        return agreed

    def clean_telegram(self):
        telegram = self.cleaned_data.get('telegram')

        if telegram[0] != '@':
            return f'@{telegram}'

        return telegram
