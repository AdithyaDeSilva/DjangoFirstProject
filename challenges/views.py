from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.template.loader import render_to_string    #We can get rid of this line with djang.shortcuts

monthlyChallenges = {
    "january": "Chicken dinners only!",
    "february": "https://www.youtube.com/watch?v=8kooIgKESYE",
    "march": "GG bois!",
    "april":"GGWP!",
    "may": "Better luck next time!",
    "june":"Ez for ence!",
    "july": "This is dua lipa!",
    "august":"New rules!",
    "september": "Friends",
    'october':"IDGAF",
    "november":"Levitating",
    "december": None
}

# Create your views here.
def index(request):
    # just using list fuynction for approve
    months = list(monthlyChallenges.keys())

    return render(request , "challenges/index.html", {
        "months" : months 
    })

    # listItem = ''
    # for month in  months:
    #     capitalizedMonth = month.capitalize()
    #     monthPath = reverse('month-challenge',args=[month])
    #     listItem += f"<li><a href=\"{monthPath}\">{capitalizedMonth}</a></li>"

    # responseData = f"<ul>{listItem}</ul>"
    # return HttpResponse(responseData)

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
        return render(requset,"challenges\challenge.html",{
            "monthName" :  month ,  #we don't capitalize here but in the html with django template filters (because it is formatting thing)
            "text": challengeText   # this is called context
        }) # must pass the request as the first argument render function replace the render_to_string line and sending httpresponse line 

    except:
        raise Http404() #replaces the hard coded 404 error
        # responseData = render_to_string("404.html")
        # return HttpResponseNotFound(responseData)  # We could not use render function here it always returns a http response not a "not found" one
