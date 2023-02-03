from django.db import models

class Layer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название слоя")