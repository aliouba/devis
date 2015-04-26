from django import forms
class UserAuthLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}))
    class Meta:
        widgets = {
            "email":forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}),
            "password":forms.TextInput(attrs={'placeholder':'Mot de Passe ','class':'form-control'}),
        }
	    
