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
* Used Django tags and using 'for' tag iterate the list of keys inside HTML template file.
* Used 'if' tag to create a conditional statement inside a template.
* Create a base html (layout.html) template and usign inheritance created other sub templates insides the apps(extends them by layout.html).
* Using DIR in the settings.py file tell django to find the base template file.
* Extended challenge.html by layout.html
* Use include tag for get rid of boiler plate code in the templates and move that code into a folder created as "shared" inside the template folder. And also there was a another feature which we can access variable inside which we includes in templates.  (Created a navigation header.)
* Create a standard 404 error project wide and tell django to find that 404 template (HttpResponseNotFound replaced with Http404() its not returning anything its raise)
* Added styling css files into the template by loading static module into the template files with "load" tag. Created a block inside the layout template called cssFiles and link the specific css files inside the sub templates with <link> tag. Lol
* Add general stylesheet css file and configured django settings to track that file also. As what we did with the layout(base) html file.
* Styled the view


Conclusion
==========
* Templates - allow us to create dynamic html contents 
* Interpolation - Adding dynamic values into a html file   {{ varName}}
* Filters - format the dynamic variables
* Tags - Programming inside a html template
* Template inheritance (extends tag)
* Use block tags to inject new values into parent template and render that file.
* Loading static files with load tag
* Avoiding code duplication with shared codes.
* Views in the django handles the request send by the client.

* Creating directory structure and configure django to track the files correctly.
