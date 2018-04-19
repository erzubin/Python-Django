from django.urls import path, re_path
from inventory import views

app_name = 'inventory'
urlpatterns  = [
    re_path(r'(?P<customer_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<game_type>[A-Za-z0-9]{2,10})/$', views.gamereturn , name="gamereturn"),
    path('addgame/' , views.addgame , name = "addgame"),
    path('addgame/' , views.addgame , name = "addgame"),
    path('game/' , views.game , name = "game"),
    path('assign/' , views.assign , name = "assign"),
    path('signup/' , views.signup , name = "signup"),
    path('customerinfo/' , views.customerinfo , name = "customerinfo"),
    path('gamereturn/' , views.gamereturn , name = "gamereturn"),
    path('user_login/' , views.user_login , name = "user_login"),
]
