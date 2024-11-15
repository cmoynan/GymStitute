from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order, OrderLineItem
from .forms import UserProfileForm
from bag.contexts import bag_contents


# Create your views here.
@login_required
def profile(request):
    """
    Display the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile')
        else:
            # form errors to debug
            print(form.errors)
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'form': form,
    }

    return render(request, template, context)


def order_detail(request, order_number):
    """ Display a single order's details """
    order = get_object_or_404(Order, order_number=order_number,
                              user=request.user)

    template = 'profiles/order_detail.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
