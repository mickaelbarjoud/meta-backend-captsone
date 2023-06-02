from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255,blank=False, db_index=True)
    no_of_guests = models.SmallIntegerField(blank=False)
    booking_date = models.DateTimeField(blank=False, db_index=True)

    def __str__(self) -> str:
        return self.name + ' - ' + str(self.booking_date)

class Menu(models.Model):
    title = models.CharField(max_length=255,unique=True, db_index=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=False, db_index=True)
    inventory = models.SmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
