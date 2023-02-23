from django.contrib import admin
from .models import Employee,Position
#from django.contrib.auth.admin import UserAdmin
#from .models import User

admin.site.register(Employee)
admin.site.register(Position)
#admin.site.register(User, UserAdmin)

admin.site.site_header="GoCloud Time Keeping Administrator"


