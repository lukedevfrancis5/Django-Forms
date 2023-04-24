from django.shortcuts import render

# views will go here 

def review(request):
    return render(request, "reviews/reviews.html")

