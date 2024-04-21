from django.db import models
from users.models import CustomUser 
from iha.models import IHA

class UserRentIhaHistory(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    startDate = models.DateField()
    finishDate = models.DateField()
    startTime = models.TimeField()
    finishTime = models.TimeField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.iha.brand.name} - {self.startDate} - {self.finishDate}"
