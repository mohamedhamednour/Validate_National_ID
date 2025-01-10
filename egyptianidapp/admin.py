from django.contrib import admin

# Register your models here.


from .models import NationalID , NationalIDLog

@admin.register(NationalID)
class NationalIDAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'location', 'birth_date')
    readonly_fields = ('number', 'location', 'birth_date')

@admin.register(NationalIDLog)
class NationalIDLogAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'method', 'status_code', 'response_data', 'request_data', 'timestamp')
    list_filter = ('status_code',)

