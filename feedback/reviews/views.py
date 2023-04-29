from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .forms import ReviewForm
# views will go here 

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else: 
        form = ReviewForm()

    return render(request, "reviews/reviews.html", {
        "form": form
    })

# prints thank you to screen 

def thank_you(request):
    return render(request, "reviews/thank_you.html")