from django.urls import path,include
from  . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('abute/',views.abute, name= 'abute') ,
    path('edit/<list_id>',views.edit, name= 'edit'),
         path('delete/<list_id>',views.delete, name= 'delete')
    ,    path('cross/<list_id>',views.cross, name= 'cross')
    ,    path('uncross/<list_id>',views.uncross, name= 'uncross')
    

]