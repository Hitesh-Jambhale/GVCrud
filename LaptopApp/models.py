from django.db import models


class Laptop1(models.Model):
    company = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    ram = models.PositiveIntegerField()
    rom = models.PositiveIntegerField()
    price = models.FloatField()
    weight = models.FloatField()
    Processor = models.CharField(max_length=35)

    def __str__(self):
        return str(self.id)
