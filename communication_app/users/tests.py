# users/tests.py

from django.test import TestCase

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms




class UserCreationFormTest(TestCase):

    def test_is_form_valid(self):
        data = {
            'username': 'someuser',
            'password1': 'somepassword123',
            'password2': 'somepassword123',
        }

        form = UserCreationForm(data)

        self.assertTrue(form.is_valid())

    def test_form_fields(self):

        data = {
            'username': 'someuser',
            'password1': 'somepassword123',
            'password2': 'somepassword123',
        }

        form = UserCreationForm(data)

        if form.is_valid():
            self.assertEquals(data['username'],form.cleaned_data['username'])
            self.assertEquals(data['password1'],form.cleaned_data['password1'])
            self.assertEquals(data['password2'],form.cleaned_data['password2'])

    def test_weak_password(self):

        data = {
            'username': 'someuser',
            'password1': 'password',
            'password2': 'password',
        }

        form = UserCreationForm(data)

        self.assertFalse(form.is_valid())


    def test_form_with_email_field(self):
        
        class UserRegisterForm(UserCreationForm):
            email = forms.EmailField(required=True, label='Email')

            class Meta:
                model = User
                fields = ['username', 'email', 'password1', 'password2']

        data = {
            'username': 'someuser',
            'email': 'someemail@test.com',
            'password1': 'somepassword123',
            'password2': 'somepassword123',
        }

        form = UserRegisterForm(data)

        self.assertTrue(form.is_valid())

class AuthenticationFormTest(TestCase):

    def test_valid_user(self):

        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        # create test user 
        user = User.objects.create(username=data['username'], email='test@test.com', is_active=True)
        user.set_password(data['password'])
        user.save()

        # authenticate new user 
        form = AuthenticationForm(None, data)

        self.assertTrue(form.is_valid())

        print(form.errors)


    def test_invalid_user(self):

        data = {
            'username': 'some_user_that_doesnt_exist',
            'password': 'password',
        }

        form = AuthenticationForm(None, data)

        self.assertFalse(form.is_valid())
