from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

# add a function that will allow to change the published data from blank to curect date

    def publish(self):
        self.published_date - timezone.now()
        self.save()

#string method to display the name of something in the terminal in case is needed
    def __str__(self):
        return self.title
    