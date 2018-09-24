from django import forms
from .models import User_Account
from django.forms import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
    attrs={
        'placeholder': 'Password',
    }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
    attrs={
        'placeholder': 'Confirm Password',
    }
    ))
    username = forms.CharField(label="Full Name",widget=forms.TextInput(
    attrs={
        'placeholder': 'Full Name',
    }
    ))
    class Meta:
        model = User
        fields = ('username','password','confirm_password')


    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.required = True
    #
    #     password_field = self.fields['password']
    #     password_field.validators.append(MinLengthValidator(limit_value=8))



    def save(self, commit=True):
        MIN_LENGTH = 8
        user = super(UserForm, self).save(commit=False)
        user.password = self.cleaned_data['password']
        user.confirm_password = self.cleaned_data['confirm_password']
        # user.username = self.cleaned_data['username']
        # user.email = self.cleaned_data['email']


        if user.password and user.confirm_password:

            if user.password != user.confirm_password:
                raise forms.ValidationError('password_mismatch')
                print("password mismach")
            else:
                if len(user.password) < MIN_LENGTH:
                    raise forms.ValidationError("password should have atleast %d charachters" %MIN_LENGTH)
                if user.password.isdigit():
                    print("ONLY DIGIT")
                    raise forms.ValidationError("password should not contain only digit")
        else:
            raise forms.ValidationError('password_mismatch')
        if commit:
            user.save()
        return user




class UserProfileInfoForm(forms.ModelForm):
    position_title = forms.CharField(widget=forms.TextInput(
    attrs={
        'placeholder': 'Position Title'
    }
    ))
    user_name = forms.CharField(label="username",widget=forms.TextInput(
    attrs={
        'placeholder': 'example@gmail.com',
        'class': 'control-group'
    }
    ))
    class Meta:
        model = User_Account
        fields = ('position_title','user_type','user_name')



# class ActivitiesForm(forms.ModelForm):
#     class Meta:
#         model = Activity
#         fields = ('Activities',)
