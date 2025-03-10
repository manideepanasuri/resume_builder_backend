from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserDetailsCollage)
class UserDetailsCollageAdmin(admin.ModelAdmin):
    list_display = ('user', 'program','rollno','course','collage')
    search_fields = ('user__name', 'user__email', 'program','rollno','course','collage')
    list_filter = ('user',)

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'student_email', 'github', 'linkedin', )
    search_fields = ('user__name','user__email', 'phone', 'email', 'student_email')
    list_filter = ('user',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'institution', 'degree', 'year')
    search_fields = ('user__name', 'institution', 'degree')
    list_filter = ('user', 'year')

class ExperienceDescriptionInline(admin.TabularInline):
    model = ExperienceDescription
    extra = 1
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'role', 'dates')
    search_fields = ('user__name', 'company', 'role')
    list_filter = ('user', 'dates')
    inlines = [ExperienceDescriptionInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dates')
    search_fields = ('user__name', 'name')
    list_filter = ('user', 'dates')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__name',)
    list_filter = ('user',)

@admin.register(PositionOfResponsibility)
class PositionOfResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'club_event', 'tenure')
    search_fields = ('user__name', 'position', 'club_event')
    list_filter = ('user', 'tenure')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'dates')
    search_fields = ('user__name', 'achievement')
    list_filter = ('user', 'dates')
