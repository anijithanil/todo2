from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    #path('',views.fun,name="fun"),
    #path('cbvview/',views.TaskListView.as_view(),'cbvview'),
    #path('cbvupdate/<int:pk>',views.TaskUpdateView.as_view(),'cbvupdate'),
    #path('cbvdelete/<int:pk>',views.TaskDeleteView.as_view(),'cbvdelete'),
    path('',views.taskview,name="taskview"),

    path('update/<int:pk>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),

]

