from django import forms
from .models import Action,Activity


class ActionsForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('Actions',)



class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('Activities',)

        
