from django.shortcuts import render, redirect
from django.contrib import messages

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # Check if size is provided, and update the session bag accordingly
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                # Add a success message
                messages.success(request, f'{quantity} x {size}  added to your bag!')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                # Add a success message
                messages.success(request, f'{quantity} x {size}  added to your bag!')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            # Add a success message
            messages.success(request, f'{quantity} {size} of the product added to your bag!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            # Add a success message
            messages.success(request, f'{quantity} more of the product added to your bag!')
        else:
            bag[item_id] = quantity
            # Add a success message
            messages.success(request, f'{quantity} of the product added to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove the specified item from the shopping bag"""
    bag = request.session.get('bag', {})

    # Remove the item if it exists in the bag
    if item_id in bag:
        del bag[item_id]
        request.session['bag'] = bag
        # Add a success message
        messages.success(request, 'Item successfully removed from your bag!')
    else:
        # If the item does not exist in the bag, show an error message
        messages.error(request, 'Item not found in your bag.')

    return redirect('view_bag')

