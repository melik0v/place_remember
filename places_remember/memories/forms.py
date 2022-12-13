from django import forms

# from django.forms import BaseInlineFormSet
from .models import Memory, Image
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError


class AddMemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ["name", "description", "place", "user_id"]
        widgets = {"place": forms.HiddenInput(), "user_id": forms.HiddenInput()}

    def clean_place(self):
        place = self.cleaned_data["place"]
        if not place:
            raise ValidationError("Выберите место на карте")
        return place


ImageFormset = inlineformset_factory(
    Memory, Image, extra=1, can_delete=True, fields=["image"], form=AddMemoryForm
)
