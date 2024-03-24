from django.utils import timezone
from django import forms
from .models import Profile
from django import forms
from .models import todo

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['task', 'description', 'due_date']
        widgets = {
                'due_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S'),  # Custom input format
            }  
    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date is None:
            # Set a default value if due_date is None
            due_date = timezone.now()  # Set it to the current date/time
        return due_date 