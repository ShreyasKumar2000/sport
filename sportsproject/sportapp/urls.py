from django.urls import path

from . import views
from  django.urls import path
app_name='sportapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('football/<int:football_id>/',views.detail,name='detail'),
    path('add/',views.add_football,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
