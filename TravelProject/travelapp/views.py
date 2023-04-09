from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponse("<h1>Travel Agent</h1>")
    return render(request, home.html)

def travel(request):
    return HttpResponse("<h1>Travel Bookings</h1>")

# When user inputs "/travel/bookings" as the URL, the view will redirect the user to the external booking chatbot URL
def app(request):
    return HttpResponseRedirect('https://d3lugqqos7gipo.cloudfront.net/')