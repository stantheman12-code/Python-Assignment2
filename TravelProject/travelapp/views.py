from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

# When user inputs "/bookings" as the URL, the view will redirect the user to the external booking chatbot URL
def app(request):
    return HttpResponseRedirect('https://d3lugqqos7gipo.cloudfront.net/')