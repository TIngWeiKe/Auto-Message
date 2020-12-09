from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} {self.name} {self.is_removed}"
