from django.shortcuts import render

# Create your views here.
def home_page(request):
        
    return render(request, 'index.html')

def event_details(request):
    return render(request, 'event-details.html')

def book(request):
    return render(request, 'book.html')