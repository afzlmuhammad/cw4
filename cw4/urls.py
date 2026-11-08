from django.urls import path
from form import views
urlpatterns = [
  path('', views.form), 
  path('th/', views.ty)
]