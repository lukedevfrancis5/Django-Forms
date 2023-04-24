from django.http import HttpResponseRedirect 
from django.shortcuts import render

# views will go here 

def review(request):
    if request.method == 'POST':
        entered_name = request.POST['name']
        
        if entered_name == "":
            return render(request, "reviews/reviews.html", {
                "has_error": True
            })

        print(entered_name)
        return HttpResponseRedirect("/thank-you")
     
    return render(request, "reviews/reviews.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")