from django.urls import path
<<<<<<< HEAD

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
=======
from django.views.generic import TemplateView

urlpatterns= [
    path('', TemplateView.as_view(template_name="base.html"), name='home'),
] 
>>>>>>> 93a9b19... Long Time no C
