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

def make_reservation(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        guests = request.POST.get('guests')
        date = request.POST.get('date')
        event = request.POST.get('event')
        
        # You can save to the database or perform other actions here
        
        return redirect('success')  # Redirect to a success page

    return render(request, 'index.html')