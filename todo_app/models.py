from django.db import models as M


class ToDo(M.Model):
    completed = M.BooleanField(default=False)
    description = M.CharField(max_length=512)
