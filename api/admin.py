from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Doctor, Patient, Note, Audit


@admin.register(Doctor)
class CustomDoctorAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active',)
    list_filter = ('username', 'first_name', 'last_name', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_active')}
         ),
    )


@admin.register(Patient)
class CustomPatientAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'age',)
    list_filter = ('username', 'first_name', 'last_name', 'is_active', 'age',)
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'age',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'age', 'password1', 'password2', 'is_active')}
         ),
    )


admin.site.register(Note)
admin.site.register(Audit)
