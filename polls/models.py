from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class SmallObjectsManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(width__lt=200)

class Image(models.Model):
    width = models.IntegerField(null=False)
    height = models.IntegerField(null=False)

    objects = models.Manager()
    small_objects = SmallObjectsManager()

    def __str__(self):
        return "Image(width={}, height={})".format(self.width, self.height)