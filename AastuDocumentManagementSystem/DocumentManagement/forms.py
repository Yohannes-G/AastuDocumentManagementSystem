from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# from bootstrap_daterangepicker import widgets, fields
from .models import  Office, Type, User,MyProfile


def formGenerator(tpe, cls='', placeholder='', value=''):
    return forms.CharField(widget=forms.TextInput(attrs={
        'class': cls,
        'type': tpe,
        'placeholder': placeholder,
        'value': value
    }), label='')


def get_type():
    """ GET Type SELECTION """
    all_countries = [('-----', 'Select a Type')]
    all_data = [type_name.type_name for type_name in Type.objects.all().exclude(type_name='admin')]
    #print("all_data", all_data)
    for x in all_data:
        y = (x, x)
        all_countries.append(y)
    return all_countries


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class SignInForm(forms.Form):
    username = formGenerator('text', 'user', 'Username')
    password = formGenerator('password', 'lock', 'Password')
    submit = formGenerator('submit', value="Login to your account")


class TypeForm(forms.Form):
    type_name = formGenerator('text', 'user', 'type')
    submit = formGenerator('submit', value='Create type')


class OfficeForm(forms.Form):
    office = formGenerator('text', 'user', 'office')
    submit = formGenerator('submit', value='Create Office')


class ReplyMessageForm(forms.Form):
    cc_type_name = forms.ChoiceField(choices=get_type(),
                                     widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'id_cc_type'})
    )

    # cc_office = forms.ChoiceField(
    #     choices=(('Electrical Engineering', 'Electrical Engineering'),
    #              (' Mechanical Engineering', 'Mechanical Engineering')),
    #     widget=forms.Select(attrs={
    #         'class': 'form-control1',
    #     }, ), label=''
    # )
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'user',
        'placeholder': 'description',
    }), label='')

    file = forms.FileField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'file',
    }
    ), label='')

    submit = formGenerator('submit', value="Send File")


class SendMessageForm(forms.Form):
    type_name = forms.ChoiceField(choices=get_type(),
                                  widget=forms.Select(
                                      attrs={'class': 'form-control', 'id': 'id_type'})
                                  )
    cc_type_name = forms.ChoiceField(choices=get_type(),
                                     widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'id_cc_type'})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'user',
        'placeholder': 'description',
    }), label='')

    file = forms.FileField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'file',
    }
    ), label='')

    submit = formGenerator('submit', value="Send File")

    field_order = ['type_name', 'office']

class NewPasswordForm(forms.Form):
    password = formGenerator('password', 'lock', 'Password')
    conf_password = formGenerator('password', 'lock', 'Confirm Password')
    submit = formGenerator('submit', value="Submit")


class SignUPForm(forms.Form, forms.ModelForm):
    first_name = formGenerator('text', 'user', 'First Name')
    last_name = formGenerator('text', 'user', 'Last Name')
    type_name = forms.ChoiceField(choices=get_type(),
                                  widget=forms.Select(
                                      attrs={'class': 'form-control', 'id': 'id_type'}),
                                  label='Select User Type'
                                  )
    submit = formGenerator('submit', value="Save User")

    class Meta:
        model = User
        fields = ['type_name']

class UpdateUserForm(forms.Form, forms.ModelForm):
    username = formGenerator('text', 'user', 'Username')
    submit = formGenerator('submit', value="Save")
    class Meta:
        model = User
        fields = ['username']

class ProfileForm(forms.Form, forms.ModelForm):
    profile_image = forms.ImageField()
    submit = formGenerator('submit', value="Save")

    class Meta:
        model = MyProfile
        fields = ['profile_image']
