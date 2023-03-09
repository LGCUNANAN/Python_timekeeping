from import_export import resources
from .models import TimeRecord

class TimeRecordResource(resources.ModelResource):
    class Meta:
        model = TimeRecord
        fields = ('id', 'user', 'time_in', 'time_out', 'total_time')
        export_order = ('id', 'user', 'time_in', 'time_out', 'total_time')
    def dehydrate_user(self, time_record):
        return time_record.user.get_full_name()