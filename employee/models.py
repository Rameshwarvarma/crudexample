from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'








