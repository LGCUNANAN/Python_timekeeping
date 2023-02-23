from django.db import models

class Position(models.Model):
    status_id = models.CharField(max_length=1)
    Position = models.TextField()
    def __str__(self):
        return self.Position

class Employee(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.CharField(max_length=100)
    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.firstname


