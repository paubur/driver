from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ForumPost(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    # context
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ForumPostAnswer(models.Model):
    description = models.TextField()
    # context
    forumpost = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id