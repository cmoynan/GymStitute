from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin for OrderLineItem to be displayed within the OrderAdmin.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date', 'delivery_cost', 'order_total',
        'grand_total', 'original_bag', 'stripe_pid'
    )

    fields = (
        'order_number', 'date', 'full_name', 'email', 'phone_number',
        'country', 'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county', 'delivery_cost', 'order_total',
        'grand_total', 'original_bag', 'stripe_pid'
    )

    list_display = (
        'order_number', 'full_name', 'date', 'order_total',
        'delivery_cost', 'grand_total'
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
