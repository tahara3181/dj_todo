from django.db import models


PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    auther = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY,
    )
    progress = models.PositiveSmallIntegerField()
    duedate = models.DateField()
    complete = models.BooleanField()

    def __str__(self):
        return self.title
