"""passbook flows logout forms"""
from django import forms

from passbook.stages.user_logout.models import UserLogoutStage


class UserLogoutStageForm(forms.ModelForm):
    """Form to create/edit UserLogoutStage instances"""

    class Meta:

        model = UserLogoutStage
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(),
        }
