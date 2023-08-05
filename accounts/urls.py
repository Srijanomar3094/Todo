from django.urls import path
from accounts import views

urlpatterns = [
      path('register/', views.register),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('todo/', views.todo, name='todo'),
  #  path('login_again/', views.login_again, name='login_again'),
   # path('savetodos/', views.savetodos, name='savetodos')

]







#from django.urls import path
#from .views import register_view

#urlpatterns = [
#    path('register/', register_view, name='register'),
#]