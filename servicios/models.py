from django.db import models

class Servicios(models.Model):
    CONDITION_CHOICES = (
        ('aquatica', 'aquatica'),
        ('no aquatica', 'no aquatica'),
    )

    nombre = models.CharField(max_length=30)
    duracion = models.CharField(max_length=15)
    maestro = models.CharField(max_length=30)
    condition = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} - {self.duracion}'