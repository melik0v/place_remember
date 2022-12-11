from django import forms
from .models import Memory, Image
from django.forms import inlineformset_factory


class AddMemoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Memory
        fields = ["name", "description", "place", "user_id"]
        # fields = '__all__'
        widgets = {"place": forms.HiddenInput()}


ImageFormset = inlineformset_factory(
    Memory, Image, extra=1, can_delete=False, fields=["image"], form=AddMemoryForm
)
