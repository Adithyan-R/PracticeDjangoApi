from .views import tutorial_list , tutorial_detail

from django.urls import path

urlpatterns =[
    path('tutorial/', tutorial_list),
    path('tutorial/<int:pk>/', tutorial_detail)
]

