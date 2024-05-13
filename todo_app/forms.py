from django import forms as F


class TaskForm(F.Form):
    description = F.CharField(label="Task Description", max_length=512)
