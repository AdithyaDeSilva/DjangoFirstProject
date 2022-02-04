from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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
def index(request):
    listItem = ''
    # just using list fuynction for approve
    months = list(monthlyChallenges.keys())

    for month in  months:
        capitalizedMonth = month.capitalize()
        monthPath = reverse('month-challenge',args=[month])
        listItem += f"<li><a href=\"{monthPath}\">{capitalizedMonth}</a></li>"

    responseData = f"<ul>{listItem}</ul>"
    return HttpResponse(responseData)

def monthlyChallengeByNumber(request, month):
    months = list(monthlyChallenges.keys()) #just using list fuynction for approve

    if month > len(months):
        return HttpResponseNotFound('This month is not eligible!      (int) ')
    
    redirectMonth = months[month - 1]
    redirectPath = reverse("month-challenge",args=[redirectMonth]) # /challenge/january       ***** we have to mention the url config(by the name of it)  and give the other parameters django will find the url and return with reverse fumction ****
    return HttpResponseRedirect(redirectPath) # redirects into mentioned url  sends this url into the browser and browser send it back to the server

def monthlyChallenge(requset, month):
    try:
        challengeText = monthlyChallenges[month]
        responseData = render_to_string("challenges\challenge.html")
        return HttpResponse(responseData)
    except:
        return HttpResponseNotFound('<h1>This month is not eligible!</h1>')
