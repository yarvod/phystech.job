from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Employer, Vacancy,
    Employee, Resume,
    Freelancer, Service,
    Client, Task,
    Tag, Category,
)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'employer', 'created')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'employee', 'created')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'freelancer', 'created')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'created')


class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_first_name', 'get_last_name')

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username

    @admin.display(ordering='user__first_name', description='First Name')
    def get_first_name(self, obj):
        return obj.user.first_name

    @admin.display(ordering='user__last_name', description='Second Name')
    def get_last_name(self, obj):
        return obj.user.last_name

    class Meta:
        abstract = True


@admin.register(Employee)
class EmployeeAdmin(BaseUserAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(BaseUserAdmin):
    pass


@admin.register(Client)
class ClientAdmin(BaseUserAdmin):
    pass


@admin.register(Freelancer)
class FreelancerAdmin(BaseUserAdmin):
    pass


admin.site.register(Category, MPTTModelAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

