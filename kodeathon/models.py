from django.db import models

class kodeathon(models.Model):
    isActive = models.BooleanField()
    TeamEvent = models.BooleanField(default=False)
    contestName = models.CharField(max_length=20)
    sheetName = models.CharField(max_length=60)
    def __str__(self):
        return self.contestName
class livekod(models.Model):
    isActive = models.BooleanField(default=False)
    bgUrl = models.TextField(default='none')
    name = models.CharField(max_length=20)
    Q1 = models.TextField()
    Q2 = models.TextField()
    Q3 = models.TextField()
    Q4 = models.TextField()
    Q5 = models.TextField()
    Q6 = models.TextField()
    def __str__(self):
        return 'Livenow'
