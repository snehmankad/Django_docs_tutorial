from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.TextField(max_length=200)
    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_vote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
