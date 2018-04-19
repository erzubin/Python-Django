from django.contrib import admin
from inventory.models import Customer, Game, Assign
# Register your models here.

admin.site.register(Customer)
admin.site.register(Game)
admin.site.register(Assign)
