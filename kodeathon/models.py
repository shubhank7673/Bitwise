from django.db import models

class kodeathon(models.Model):
    isActive = models.BooleanField()
    TeamEvent = models.BooleanField(default=False)
    contestName = models.CharField(max_length=20)
    sheetName = models.CharField(max_length=60)
    def __str__(self):
        return self.contestName
