from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,TimeRecord

class EmployeeAdmin(UserAdmin):
    pass

admin.site.register(User, EmployeeAdmin)

class TimeRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_in', 'time_out','total_time_display')
    def check_in_time(self, obj):
        return obj.time_in.strftime("%H:%M")

    def check_out_time(self, obj):
        return obj.time_out.strftime("%H:%M") if obj.time_out else ""
    def total_time(self, obj):
        return obj.total_time.strftime("%H:%M") 
    ordering = ('-time_in',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(TimeRecord, TimeRecordAdmin)

admin.site.site_header="GoCloud Time Keeping Administrator"


