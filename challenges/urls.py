from django.urls import path
from . import views


urlpatterns = [
    # path('january', views.january )  ,    #url config / url
    # path('february', views.february ),      #url config / url
    # path('march', views.march),
    path("",views.index, name="index"),  #  /challenges/
    path("<int:month>",views.monthlyChallengeByNumber),
    path("<str:month>", views.monthlyChallenge, name="month-challenge")
]