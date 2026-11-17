from django.contrib import admin

from .models import About, Skill, Experience,Project

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    filter_horizontal = ('skill',)

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('project_title',)
    filter_horizontal = ('skill',)
    search_help_text = 'Type the project name you are looking for'

class SkillAdmin(admin.ModelAdmin):
    list_filter = ('skill_name',)

admin.site.register(About)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)

# Register your models here.
