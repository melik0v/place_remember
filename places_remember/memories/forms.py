from django import forms
from .widgets import CustomClearableFileInput
from .models import Memory, Image
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError


class AddMemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ["name", "description", "place", "user_id"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    # 'style': 'max-width: 300px;',
                    "placeholder": "Название",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    # 'style': 'max-width: 300px;',
                    "placeholder": "Описание",
                }
            ),
            "place": forms.HiddenInput(),
            "user_id": forms.HiddenInput(),
        }

    def clean_place(self):
        place = self.cleaned_data["place"]
        if not place:
            raise ValidationError("Выберите место на карте")
        return place


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        image = forms.ImageField()
        fields = "__all__"
        widgets = {
            "image": CustomClearableFileInput,
            "delete": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "type": "checkbox",
                    "value": "",
                }
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         print(field)


ImageFormset = inlineformset_factory(
    Memory, Image, extra=3, max_num=6, can_delete=True, fields=["image"], form=ImageForm
)
