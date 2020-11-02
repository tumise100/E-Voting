import nested_admin
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Polls, Choice, User, VOTED

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        ('None',{
            'fields': ('Matric', 'first_name', 'Other_Name','last_name','Faculty', 'Dept', 'Tel','email', 'username', 'is_voter', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        ('Profile', {
            'fields': ('Matric', 'first_name', 'Other_Name','last_name','Faculty', 'Dept', 'Tel','email', 'username', 'is_voter', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )

    list_display = ['Matric', 'first_name', 'Other_Name','email', 'is_voter', 'is_staff']
    search_fields = ('Matric','username','Dept',)
    ordering = ('Matric',)
    readonly_fields = ('username',)

class VotedAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'Voted', 'get_user_voted')

    def get_student(self, obj):
        return obj.student.first_name

    def get_user_voted(self, obj):
        return obj.user_voted.Category

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra = 0
    readonly_fields = ('votes',)

class PollsAdmin(admin.ModelAdmin):
    list_display = ('Award','Type', 'Category','deadline')
    model = Choice
    inlines = [ChoiceInline]

    def get_dept(self, obj):
        return obj.Dept.deptName

    def get_SUG(self,obj):
        return obj.sug.SUG

    def get_faculty(self,obj):
        return obj.Dept.group.faculty

    get_faculty.short_description = 'Faculty'
    get_SUG.short_description = 'SUG'
    get_dept.short_description = 'Department'

admin.site.register(Polls, PollsAdmin)
admin.site.register(VOTED, VotedAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

