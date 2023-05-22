from django import forms

from members.models import Member, TERMS_AGREE_NAME


class MemberForm(forms.ModelForm):
    terms_agree = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input me-2'}),
        required=False,
        label=TERMS_AGREE_NAME,
        label_suffix='')

    class Meta:
        model = Member
        fields = ('__all__')

    def clean_terms_agree(self):
        agreed = self.cleaned_data.get('terms_agree')

        if agreed:
            return agreed

        raise forms.ValidationError(
            'Необходимо принять условия политики конфиденциальности!'
        )
