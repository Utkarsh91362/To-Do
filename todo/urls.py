from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='todo/login.html'), name='login'),  
    path('', views.index, name='index'),  
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteall, name='deleteall'),

  
    path('logout/', views.logout_view, name='logout'),
]
