from django.db import models

# Create your models here.


# class User(models.Model):
#     UserName = models.CharField(max_length=255)
#     Email = models.EmailField(unique=True)
#     Password = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.UserName}"


class Cart(models.Model):
    UserID = models.CharField(max_length=255)
    ProductID = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.UserID}"


class Orders(models.Model):
    OrederID = models.CharField(max_length=255)
    UserID = models.CharField(max_length=255)
    ProductID = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.OrderID}"
