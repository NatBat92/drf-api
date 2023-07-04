from django.urls import path, include
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]