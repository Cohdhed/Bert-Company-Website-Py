from django.shortcuts import render, redirect
from . models import Contact
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home(request):
    context = {}
    return render (request, "index.html", context)


def about(request):
    context = {}
    return render (request, "about.html", context)


def services(request):
    context = {}
    return render (request, "services.html", context)


def supp_trad(request):
    context = {}
    return render (request, "supp_trad.html", context)


def refining(request):
    context = {}
    return render (request, "refining.html", context)




def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            # Process the form data
            contact_form.save()
            send_contact_email(contact_form.cleaned_data)
            # Add success message
            messages.success(request, "Thank you for contacting us, we'll get back to you shortly!")
            return redirect('contact')  # Redirect to the same page to clear the form
    
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form  # Pass the form to the template context
    }

    return render(request, 'contact.html', context)



def send_contact_email(form_data):
    subject = 'New Contact Form'
    message = f'A new contact from a user:\n\nName: {form_data["name"]}\nPhone: {form_data["phone"]}\nEmail: {form_data["email"]}\nMessage: {form_data["message"]}'
    sender_email = settings.EMAIL_HOST_USER
    recipient_email = 'abrahamhosu9@gmail.com'  # Replace with your email address
    send_mail(subject, message, sender_email, [recipient_email])




