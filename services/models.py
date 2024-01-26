from django.db import models

class Fixture(models.Model): 
    STATUS_CHOICES = [
        ('won✅', 'Won✅'), 
        ('Lost❌', 'Lost❌'),
        ('N/A', 'N/A'),
    ]
    outcome=models.CharField(choices=STATUS_CHOICES,
                             max_length=100,
                             default='N/A')
    team1=models.CharField(max_length=100)
    team2=models.CharField(max_length=100)
    League=models.CharField(max_length=100,default='EPL')
    tip=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.team1} vs {self.team2}   results - {self.outcome}'
