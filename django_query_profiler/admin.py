from django.contrib import admin
from .models import QueryProfile

@admin.register(QueryProfile)
class QueryProfileAdmin(admin.ModelAdmin):
    list_display = ('query', 'execution_time', 'created_at')
    search_fields = ('query',)
