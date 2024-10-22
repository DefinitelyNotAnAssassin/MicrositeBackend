from django.contrib import admin
from Models.models import Student, Curriculum, Account, ProgramHighlight, Article
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):  
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Student) 
admin.site.register(Curriculum)
admin.site.register(Account, AccountAdmin)
admin.site.register(ProgramHighlight)
admin.site.register(Article)