from django.shortcuts import render, HttpResponse

# Create your views here.
def message_sender(request):
    return render(request,"message_sender.html")