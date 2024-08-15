
from django.db import models

class ExcelFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='excel/', default=None)

    def __str__(self):
        return self.name