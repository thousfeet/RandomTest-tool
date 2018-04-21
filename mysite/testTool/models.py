from django.db import models

class students(models.Model):
    stuId = models.CharField(max_length=9)
    gitAddr = models.CharField(max_length=200)
    matchId = models.IntegerField(default=0)
    score = models.IntegerField(null=True)
    reason = models.TextField(null=True)
    def __str__(self):
        return self.stuId
