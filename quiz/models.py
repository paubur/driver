from django.contrib.auth.models import User
from django.db import models
from tagging.fields import TagField

# Create your models here.

class Advice(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    tags = TagField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title


class Quiz(models.Model):
    question = models.CharField(max_length=256)
    answer_1 = models.CharField(max_length=512)
    answer_2 = models.CharField(max_length=512)
    answer_3 = models.CharField(max_length=512)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through='QuizResults', related_name='users')

    def __str__(self):
        return self.question


class QuizResults(models.Model):
    results = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to_quiz')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_to_user')


    def __str__(self):
        return self.id

# models.py
# class Person(models.Model):
#
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Case(models.Model):
#
#     summary = models.TextField()
#     litigants = models.ManyToManyField(Person, through='Litigant'  )
#
#     def __str__(self):
#         return 'Case %s' % (self.id)
#
# class Litigant(models.Model):
#
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_to_case')
#     case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='case_to_person')
#     role = models.TextField()

