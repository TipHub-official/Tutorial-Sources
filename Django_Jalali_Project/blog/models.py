from django.db import models
from django_jalali.db import models as jmodels


class Article(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
