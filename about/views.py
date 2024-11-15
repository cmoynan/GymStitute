from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm
from django.contrib import messages


# Create your views here.
def about(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Add a success message to be displayed after form submission
        messages.success(
         request,
         'Thank you for subscribing to our newsletter!'
         )

        return redirect('about')

        # Redirect to the same page to show the message

    return render(request, 'about/about.html')
