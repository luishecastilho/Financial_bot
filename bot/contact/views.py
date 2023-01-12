from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact_Form

# Create your views here.

def index(request):
    #dados de um possível LOGIN
    user = []

    statusForm = request.GET.get('s')
    return render(request, 'contact/index.html', {'user': user, 'status': statusForm})

def send(request):
    try:
        form = Contact_Form(
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            body = request.POST.get('body')
        )
        form.save()

        #
        #
        # MANDAR EMAIL TAMBÉM
        #
        #

        return HttpResponseRedirect('/contact/?s=s')
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/contact/?s=n')