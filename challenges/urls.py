from django.urls import path
from . import views


urlpatterns = [
    # path('january', views.january )  ,    #url config / url
    # path('february', views.february ),      #url config / url
    # path('march', views.march),
    path("<month>", views.monthlyChallenge)
]