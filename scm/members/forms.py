from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy

from members.models import Member, TERMS_AGREE_NAME


class MemberForm(forms.ModelForm):
    terms_agree = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input me-2'}),
        required=False,
        label_suffix='')

    class Meta:
        model = Member
        fields = ('__all__')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        link = reverse_lazy("core:policy")
        self.fields['terms_agree'].label = mark_safe(
            f'<a href="{link}" target="_blank">{TERMS_AGREE_NAME}</a>')

    def clean_terms_agree(self):
        agreed = self.cleaned_data.get('terms_agree')

        if agreed:
            return agreed

        raise forms.ValidationError(
            'Необходимо принять условия политики конфиденциальности!'
        )
