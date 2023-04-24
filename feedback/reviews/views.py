from django.http import HttpResponseRedirect 
from django.shortcuts import render

# views will go here 

def review(request):
    if request.method == "POST":
        entered_name = request.Post['name']
        
        if entered_name == "":
            return render(request, "reviews/reviews.html", {
                "has_error": True
            })

        print(entered_name)
        return HttpResponseRedirect("/thank-you.html")
     
    return render(request, "reviews/reviews.html", {
        "has_error": False
    })

