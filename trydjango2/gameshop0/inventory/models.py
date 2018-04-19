from django.db import models
from django.contrib.auth.models import User 

class Customer(models.Model):

        name = models.CharField(max_length = 264)
        email = models.EmailField(max_length = 264 , unique = True )
        phone_num = models.IntegerField( unique = True )


        def __str__(self):
            return self.email

class Game(models.Model):
        game_name = models.CharField(max_length = 100 )
        game_type = models.CharField(max_length = 100 )


        def __str__(self):
            return "%s - %s" % (self.game_name, self.game_type)

class Assign(models.Model):
        customer_phone = models.ForeignKey( Customer, on_delete=models.CASCADE )
        game_name = models.OneToOneField( Game, on_delete=models.CASCADE , primary_key=True)
        current_date = models.DateField(auto_now=True)

        def __str__(self):
            return self.customer_phone.email
