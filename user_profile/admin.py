import imp
from re import A
from django.contrib import admin
from .models import Account, Address, Person

# Register your models here.
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(Person)