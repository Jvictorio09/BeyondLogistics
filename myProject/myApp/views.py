from django.shortcuts import render

def base(request):
    context={}
    return render(request, "myApp/base.html", context)

def about(request):
    return render(request, 'myApp/about.html')

def coming_soon(request):
    return render(request, 'myApp/comming-soon.html')

def contact(request):
    return render(request, 'myApp/contact.html')

def contact_form(request):
    return render(request, 'myApp/contact-form.html')

def gallery(request):
    return render(request, 'myApp/gallery.html')


def index(request):
    return render(request, 'myApp/index.html')

def organizer(request):
    return render(request, 'myApp/organizer.html')

def pricing(request):
    return render(request, 'myApp/pricing.html')

def services(request):
    return render(request, 'myApp/services.html')

def single_gallery(request):
    return render(request, 'myApp/single_gallery.html')

from django.shortcuts import render, redirect

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReservationForm

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Get form data
            event_date = form.cleaned_data['event_date']
            event_type = form.cleaned_data['event_type']
            celebrant_name = form.cleaned_data['celebrant_name']
            event_address = form.cleaned_data['event_address']
            invite_time = form.cleaned_data['invite_time']
            client_name = form.cleaned_data['client_name']
            relationship = form.cleaned_data['relationship']
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']
            guests = form.cleaned_data['guests']
            venue = form.cleaned_data['venue']

            # 1. Send Email to Admin
            admin_subject = 'New Event Reservation'
            admin_context = {
                'event_date': event_date,
                'event_type': event_type,
                'celebrant_name': celebrant_name,
                'event_address': event_address,
                'invite_time': invite_time,
                'client_name': client_name,
                'relationship': relationship,
                'email': email,
                'contact_number': contact_number,
                'guests': guests,
                'venue': venue
            }


            # Render HTML email for admin
            admin_html_content = render_to_string('admin_email_template.html', admin_context)
            admin_text_content = strip_tags(admin_html_content)

            # Create and send admin email
            admin_email = EmailMultiAlternatives(admin_subject, admin_text_content, 'hello@beyondlogisticsevent.com', ['hello@beyondlogisticsevent.com'])
            admin_email.attach_alternative(admin_html_content, "text/html")
            admin_email.send()

            # 2. Send Confirmation Email to Customer
            send_confirmation_email(client_name, email)

            # Optionally, redirect to a success page or render a success message
            return redirect('index')  # Change this to your success page
    else:
        form = ReservationForm()

    return render(request, 'myApp/index.html', {'form': form})


def send_confirmation_email(client_name, client_email):
    subject = 'Thank You for Your Reservation with Beyond Logistics!'
    from_email = 'hello@beyondlogisticsevent.com'
    to_email = [client_email]

    # Prepare the context for the email template
    context = {
        'client_name': client_name,
    }

    # Render the HTML template with context
    html_content = render_to_string('customer_email_template.html', context)
    text_content = strip_tags(html_content)  # Fallback for email clients that don't support HTML

    # Create email
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")

    # Send email
    email.send()
