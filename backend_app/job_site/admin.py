from django.contrib import admin

from .models import Vacancy, Resume, Employee, Employer, Category


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'employer', 'created')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'employee', 'created')


class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_first_name', 'get_last_name')

    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username

    @admin.display(ordering='user__first_name', description='First Name')
    def get_first_name(self, obj):
        return obj.user.username

    @admin.display(ordering='user__last_name', description='Second Name')
    def get_last_name(self, obj):
        return obj.user.first_name

    class Meta:
        abstract = True


@admin.register(Employee)
class EmployeeAdmin(BaseUserAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(BaseUserAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
