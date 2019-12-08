from django.db import models

# Create your models here.

class Pizzas(models.Model):
    values = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.values



class Topping(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    