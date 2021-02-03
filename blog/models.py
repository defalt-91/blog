from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk': self.pk})
