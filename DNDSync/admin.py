from django.contrib import admin
from DNDSync.models import *


class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)
admin.site.register(JournalEntries)
admin.site.register(Notes)
