from django.db import models


class Survey(models.Model):
    question = models.CharField(blank=True, null=True, max_length=250)


class Choices(models.Model):
    choicefield = models.CharField(max_length=20)
    rel = models.ForeignKey(
        Survey, on_delete=models.CASCADE, default=1)
