from django import forms

from todo_list.models import Task


class DeadlineForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
