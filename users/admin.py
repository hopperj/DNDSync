from django.contrib import admin

class NavBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    name = ('title')
