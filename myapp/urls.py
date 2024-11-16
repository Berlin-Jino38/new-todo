from django.urls import path
from .views import home,login,signup,addtask,updatetask

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup',signup,name='signup'),
    path('addtask',addtask,name='addtask'),
    path('updatetask',updatetask,name='updatetask'),
    
]
