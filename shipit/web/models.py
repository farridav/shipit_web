from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
