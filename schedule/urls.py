from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_schedule, name='add'),
    path('complete/<schedule_id>', views.complete_schedule, name='complete'),
    path('deletecomplete', views.delete_completed, name='deletecomplete'),
    path('deleteall', views.delete_all, name='deleteall')
]
