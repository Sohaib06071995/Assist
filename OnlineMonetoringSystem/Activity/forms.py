from django import forms
from .models import Pending_Activity,Comments_Activity
from django_select2.forms import *
from Dictionary.models import *
from django.contrib.auth.models import User
import select2.fields
import select2.models
from datetime import date
import datetime
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)
from datetimewidget.widgets import DateWidget

ACTIVITY_TYPE = [
('pending','Pending'),
('ongoing','Ongoing'),
('completed','Completed'),
('submitted','Submitted'),
]
dateTimeOptions = {
'format': 'dd/mm/yyyy',
'autoclose': True,

}

class ActivitiesForm(forms.ModelForm):


    # Assigned_To = select2.fields.ChoiceField(
    #     choices=User.objects.all(),
    #     overlay="Choose an author...")
    # Assigned_To = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=Select2MultipleWidget)
    Active_Description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Active Description', }))
    Exceting_Agency = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Exceting Agency',}))
    Associated_with = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Associated With',}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput(
    # attrs={
    #     'placeholder': 'Confirm Password',
    # }
    # ))
    Assigned_Date = forms.DateField(input_formats=['%d-%m-%Y'])
    Assigned_Date = forms.DateField(initial=datetime.date.today ,disabled=True)


    Deadline = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'placeholder': 'Closing Date: DD/MM/YYYY',
                                    'class': 'datetime-input'
                                }))
    Status = forms.ChoiceField(choices=ACTIVITY_TYPE,required=False,widget=Select2Widget(attrs={'placeholder': 'Activity Type',}))
    class Meta:
        model = Pending_Activity
        fields = ('Active_Description',
        'Assigned_To',
        'Activity_Type',
        'Exceting_Agency',
        'Action_Required',
        'Assigned_Date',
        'Deadline',
        'Associated_with',
        'Status',

        )
        widgets = {
                    'Status': Select2Widget,
                    'Activity_Type':Select2Widget,
                    'Action_Required':Select2Widget,
                }

class Dashboard_Comment_Form(forms.ModelForm):
    class Meta:
        model = Comments_Activity
        fields = ('comment',)
        widgets = {
                    'comment': forms.TextInput(attrs={
                    'id': 'post-text',
                    'Required': True,
                    'placeholder': 'Type Your Comment here',

                    }),
                }
        labels = {
                        'comment': ('')
        }
        def clean_last_modified_by(self):
            if not self.cleaned_data['commented_by']:
                return User()
            return self.cleaned_data['commented_by']

class ProgressForm(forms.ModelForm):

    class Meta:
        model = Pending_Activity
        fields = ('Progress','Progress_Date')
        widgets = {
    #NOT Use localization and set a default format
    'Progress_Date': DateWidget(options = dateTimeOptions)
    }
