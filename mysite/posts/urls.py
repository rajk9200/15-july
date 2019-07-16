from django.urls import path
from . import views


urlpatterns = [

    path('add-post/', views.add_post),
    path('showpost/',views.show_posts)
]
