from django.contrib import admin

from .models import SocialMedia, Variable, Experience, Course, Education, Jobdesc, AboutDesc

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'certificate_id', 'is_publish', 'update_date')
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'company_name', 'status', 'is_publish', 'update_date')
@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'update_date')
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('media_name', 'url', 'is_publish', 'update_date')
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'major', 'education_level','gpa', 'is_publish')
@admin.register(Jobdesc)
class JobdescAdmin(admin.ModelAdmin):
    list_display = ('experience', 'update_date', 'content')
@admin.register(AboutDesc)
class AboutDescAdmin(admin.ModelAdmin):
    list_display = ('purpose', 'is_publish', 'update_date')

