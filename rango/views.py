from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    # Construct a dictionary to pass to thetemplateengineasitscontext. 
    # Note the key boldmessage matches to{{boldmessage}}in the template!
    context_dict ={'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
    
    # Returna rendered response to send totheclient. 
    # We make use of the shortcut function to make our lives easier. 
    # Note that the firstparameter isthe templatewewishtouse.
    return render(request, 'rango/index.html',context=context_dict)
    
def about(request):
    context_dict ={'boldmessage':'Xinrui Liu'}
    return render(request, 'rango/about.html',context=context_dict)
    

