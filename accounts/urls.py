from django.urls import path
from .views import login,register,logout_page


urlpatterns = [
    path("login",login,name="login"),
    path('logout/', logout_page, name='logout'),
    path('register/',register,name="register")
]
