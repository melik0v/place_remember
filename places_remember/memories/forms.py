from django import forms
from .models import Memory, Image
from django.forms import inlineformset_factory


class AddMemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ["name", "description", "place", "user_id"]
        # fields = '__all__'
        widgets = {"place": forms.HiddenInput(), "user_id": forms.HiddenInput()}


ImageFormset = inlineformset_factory(
    Memory, Image, extra=1, can_delete=False, fields=["image"], form=AddMemoryForm
)
