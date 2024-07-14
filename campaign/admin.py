from django.contrib import admin
from .models import Event, Participation

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Event model.

    Attributes:
    list_display (tuple): Fields to be displayed in the list view of the admin interface.
    search_fields (tuple): Fields to be used for searching in the admin interface.
    """    
    list_display = ('name', 'date', 'location')
    search_fields = ('name', 'location')

class ParticipationAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Participation model.

    Attributes:
    list_display (tuple): Fields to be displayed in the list view of the admin interface.
    list_filter (tuple): Fields to be used for filtering in the admin interface.
    search_fields (tuple): Fields to be used for searching in the admin interface.
    """    
    list_display = ('user', 'event')
    list_filter = ('event',)
    search_fields = ('user__username', 'event__name')

admin.site.register(Event, EventAdmin)
admin.site.register(Participation, ParticipationAdmin)

