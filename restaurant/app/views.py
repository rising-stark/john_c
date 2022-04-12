from django.shortcuts import render, redirect
from app.models import *

def index(request):
  if request.method == "POST":
    recipient_firstname = request.POST.get('recipient_firstname', "")
    recipient_lastname = request.POST.get('recipient_lastname', "")
    company_name = request.POST.get('company_name', "")
    country = request.POST.get('country', "")

    print("HERE printing the data submitted from the form")
    print(recipient_firstname)
    print(recipient_lastname)
    print(company_name)

    # saving in the database
    r = Recipient.objects.create(recipient_firstname=recipient_firstname, recipient_lastname=recipient_lastname)

    return render(request, 'offer.html', {recepient: r})

  recepients = Recipient.objects.all()
  return render(request, "index.html", {"recepients":recepients, "recepient":recepients[0]})
