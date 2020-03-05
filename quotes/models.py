from django.db import models

class Mystockdb(models.Model):
	myticker = models.CharField(max_length=10)
	myprice = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=4)
	myowned = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

def __str__(self):
	return self.myticker


