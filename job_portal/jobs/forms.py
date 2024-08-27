from django import forms
from .models import CustomUser
from .models import Job

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'domain', 'is_experienced', 'resume']
        widgets = {
            'password': forms.PasswordInput(),
        }
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'location', 'role', 'average_package', 'is_for_experienced']