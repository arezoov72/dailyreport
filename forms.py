from django import forms
from .models import reportdetails



class TopicForm(forms.ModelForm):
    class Meta:
        model = reportdetails
        fields = ['comment']
        labels = {'comment': 'public'}
        public = forms.BooleanField(required=False)