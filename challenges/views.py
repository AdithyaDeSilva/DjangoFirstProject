from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return HttpResponse('This works!')
    
# def january(request):
#     return HttpResponse('Chicken dinners only!')

# def february(request):
#     return HttpResponse('Noobs only!')

# def march(request):
#     return HttpResponse('GG bois!')
def monthlyChallenge(requset, month):
    challengeText =None
    if(month =='january'):
        challengeText = "Chicken dinners only!"
    elif (month == 'february'):
        challengeText = 'Noobs only!'
    elif (month == 'march'):
        challengeText = "GG bois!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challengeText)