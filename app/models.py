from django.db import models
class Tag(models.Model):
    tag1 = models.CharField(max_length=256)
    tag2 = models.CharField(max_length=256)
    tag3 = models.CharField(max_length=256)
    tag4 = models.CharField(max_length=256)
    tag5 = models.CharField(max_length=256)
class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    number = models.IntegerField()
    answers = models.IntegerField()
    counting_tags = models.IntegerField()
    tag_names = models.ForeignKey(Tag, on_delete=models.PROTECT)
    text_answers = models.TextField()
    counting_answers = models.IntegerField()
