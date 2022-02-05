Just started to learn django.
[Learnt with the academnd tutorial course]

First section
=============
* URLs
* Put in local urls into the project urls with include function 
* Create view functions to be triggered when requested by the client
* Created views for each month seperately
* Replaced those function with a one function using if ladder
* Replaced if ladder using a dictionary of months and challenges
* Responded the request which made as number of the month
* Redirect that request into the their urls   ex:- /challenges/1   =>  /challenges/january
* Replace the hard coded redirecting path with dynamic reverse function
* Send a HTML code as the response
* Created the index view and responded the challenge/ url by returning a list of months which generates the links to the months with HTML


Second Section
==============
* Sending html file as a string as the response
* We have to configure a settings in the main project DIRS and tell django to find templates in the template folder in the app "DIRS"
* And also register our app in the settings file and tell django to templates can be found at relevant app folders (for this the APP_DIRS variable should set to be True)
* Replaced the render_to_string_ function and returning the httpresponse object with render function in the django.shortcut module
* Dynamically changed the values in the html with django DTL (Django Template Language) changed html page will return with the response   (Note :- *We have to use ajax requests to do this without reloading the page) 
* Use the Django template filters (https://docs.djangoproject.com/en/4.0/ref/templates/builtins/) to format the injected value just because formating the code is not a part of logics.
