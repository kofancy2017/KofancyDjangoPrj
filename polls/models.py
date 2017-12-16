import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(verbose_name="问题",max_length=500)

    pub_date = models.DateTimeField(verbose_name="发布日期")


    def __str__(self):
        return  self.question_text

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = verbose_name


    def was_published_recently(self):
        #return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(verbose_name="选项",max_length=1000)
    votes = models.IntegerField(verbose_name="投票数",default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "选项"
        verbose_name_plural = verbose_name


