from django.contrib import admin
from seva.models import Newreg

# Register your models here.
class adminreg(admin.ModelAdmin):
    list_display=[
        'name','Gmail','address','city','fathername','date'
    ]
admin.site.register(Newreg,adminreg)
