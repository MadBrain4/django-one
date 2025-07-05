from django import forms

class CreateNewTaskForm(forms.Form):
    name = forms.CharField(label="Task Name", max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, label="Description", required=False)
