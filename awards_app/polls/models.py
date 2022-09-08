import datetime
from polymorphic.models import PolymorphicModel

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date.date() >= timezone.now() - datetime.timedelta(days=1)


class Choice(PolymorphicModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


class LongChoice(Choice):
    long_choice_text = models.CharField(max_length=1000)


class ChoicePoly(PolymorphicModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

class LongChoicePoly(ChoicePoly):
    long_choice_text = models.CharField(max_length=1000)