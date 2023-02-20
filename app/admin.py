from django.contrib import admin
from app.models import Registration


class StudentRegistration(admin.ModelAdmin):
    list_display = ('enroll', 'password', 'email',
                    'first_name', 'last_name', 'gender',
                    'degree', 'branch')


admin.site.register(Registration, StudentRegistration)
# Register your models here.
