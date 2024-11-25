from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Film


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
	


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Film
        exclude = ("user",)

    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Title", "class":"form-control"}), label="")
    release_year = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Year Released", "class":"form-control"}), label="")
    director = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Director", "class":"form-control"}), label="")
    genre = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Genre", "class":"form-control"}), label="")
    language = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Language", "class":"form-control"}), label="")
    duration_mins = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Duration", "class":"form-control"}), label="")
    production_company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Production Company", "class":"form-control"}), label="")
    sypnosis = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sypnosis", "class":"form-control"}), label="")

class STATUS(forms.Form):
	status_choices = ( 
    ("TO WATCH", "TO WATCH"), 
    ("WATCHING", "WATCHING"), 
    ("WATCHED", "WATCHED"), 
    ("REWATCHED", "REWATCHED"), 
)	
status = forms.CharField()
category = forms.ChoiceField(choices=STATUS)

class RATING(forms.Form):
	rating_choices =(
          ("1", "1"),
          ("2", "2"),
          ("3", "3"),
          ("4", "4"),
          ("5", "5"),
    )
rating: forms.CharField()
category= forms.ChoiceField(choices=RATING)
	
