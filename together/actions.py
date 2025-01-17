from django.shortcuts import redirect
from django.urls import reverse
from .models import Calculation


def create_calculation(modeladmin, request, queryset):
    """
    Create calculation object and display the balance.
    """
    # TODO: Handle expenses that were already calculated.
    expenses = list(queryset.all())
    calculation = Calculation()
    calculation.save()
    calculation.expenses.add(*expenses)
    url = reverse(f'admin:{calculation._meta.app_label}_{calculation._meta.model_name}_change', args=(calculation.pk,))
    return redirect(url)
