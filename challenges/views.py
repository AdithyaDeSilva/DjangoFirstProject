from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render

import challenges

monthlyChallenges = {
    "january": "Chicken dinners only!",
    "february" : "Noobs only!",
    "march": "GG bois!",
    "april":"GGWP!",
    "may": "Better luck next time!",
    "june":"Ez for ence!",
    "july": "This is dua lipa!",
    "august":"New rules!",
    "september": "Friends",
    'october':"IDGAF",
    "november":"Levitating",
    "december":"No lie!"
}

# Create your views here.

# def index(request):
#     return HttpResponse('This works!')
# def january(request):
#     return HttpResponse('Chicken dinners only!')
# def february(request):
#     return HttpResponse('Noobs only!')
# def march(request):
#     return HttpResponse('GG bois!')


def monthlyChallengeByNumber(request, month):
    months = list(monthlyChallenges.keys()) #just using list fuynction for approve

    if month > len(months):
        return HttpResponseNotFound('This month is not eligible!      (int) ')
    
    redirectMonth = months[month - 1]
    return HttpResponseRedirect("/challenges/"+redirectMonth) # redirects into mentioned url  sends this url into the browser and browser send it back to the server

def monthlyChallenge(requset, month):
    # challengeText =None
    # if(month =='january'):
    #     challengeText = "Chicken dinners only!"
    # elif (month == 'february'):
    #     challengeText = 'Noobs only!'
    # elif (month == 'march'):
    #     challengeText = "GG bois!"
    # else:
    #     return HttpResponseNotFound("This month is not supported!")
    # return HttpResponse(challengeText)

    try:
        challengeText = monthlyChallenges[month]
        return HttpResponse(challengeText)
    except:
        return HttpResponseNotFound('This month is not eligible!')