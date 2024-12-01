from django.db import models



class Vitamin(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    """ 
    price is per unit available
    in usd
    """
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 3, decimal_places = 2, blank = False)
    vitamins = models.ManyToManyField(Vitamin, blank = True, related_name = "fruits")
    image = models.ImageField(upload_to = "fruit_images/") # Directory to store images

    def __str__(self):
        return self.name

