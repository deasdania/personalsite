# from django.shortcuts import render

# Create your views here.
from .models import SocialMedia, Variable, Experience, Course, Education, Jobdesc, AboutDesc, Project
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.views.generic import TemplateView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect

def index(APIView):
    return HttpResponseRedirect("/admin/")

class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['message'] = 'Hello, World!'
        content['sosial_media'] = GetSocialMedia()
        content['educations'] = GetEducation()
        content['experiences'] = GetExperience()
        content['courses'] = GetCourse()
        content['variable'] = GetVariables()
        return Response(content)

class PersonalDataView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello, World!'
        context['educations'] = GetEducation()
        context['experiences'] = GetExperience()
        context['courses'] = GetCourse()
        for v in GetSocialMedia():
            context[v["media_name"]] = v["url"]
        for v in GetVariables():
            context[v["name"]] = v["value"]
        return context
    
class DataView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['message'] = 'Hello, World!'
        content['educations'] = GetEducation()
        content['experiences'] = GetExperience()
        content['courses'] = GetCourse()
        for v in GetSocialMedia():
            content[v["media_name"]] = v["url"]
        for v in GetVariables():
            content[v["name"]] = v["value"]
        return Response(content)

class GetContentAboutView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['content_about'] = GetAbout()
        return Response(content)

class GetSocialMediaView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['sosial_media'] = GetSocialMedia()
        return Response(content)

class GetEducationView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['educations'] = GetEducation()
        return Response(content)

class GetExperienceView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['experiences'] = GetExperience()
        return Response(content)

class GetCourseView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['courses'] = GetCourse()
        return Response(content)

class GetVariableView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['variables'] = GetVariables()
        return Response(content)

class GetProjectsView(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {}
        content['projects'] = GetProjects()
        return Response(content)

def GetSocialMedia():
    sosmeds = SocialMedia.objects.filter(is_publish=True)
    sosmelist = []
    for sosmed in sosmeds:
        sosmedict = {}
        sosmedict["id"] = sosmed.id
        sosmedict["media_name"] = sosmed.media_name
        sosmedict["url"] = sosmed.url
        sosmelist.append(sosmedict)
    return sosmelist

def GetEducation():
    educations = Education.objects.filter(is_publish=True)
    educationlist = []
    for education in educations:
        edict = {}
        edict["id"] = education.id
        edict["university_location"] = education.university_location
        edict["university_name"] = education.university_name
        edict["major"] = education.major
        edict["education_level"] = education.education_level
        edict["department"] = education.department
        edict["start_date"] = education.start_date
        edict["end_date"] = education.end_date
        edict["gpa"] = education.gpa
        educationlist.append(edict)
    return educationlist

def GetExperience():
    experiences = Experience.objects.filter(is_publish=True).order_by('-start_date')
    experiencelist = []
    for experience in experiences:
        exdict = {}
        exdict["id"] = experience.id
        exdict["position_name"] = experience.position_name
        exdict["company_name"] = experience.company_name
        exdict["start_date"] = experience.start_date
        exdict["end_date"] = experience.end_date
        exdict["status"] = experience.status
        jobdesc = Jobdesc.objects.filter(experience=experience).order_by('-id')[:1]
        content = ""
        try:
            if jobdesc[0].content:
                content = jobdesc[0].content
        except:
            pass
        exdict["jobdesc"] = content
        experiencelist.append(exdict)
    return experiencelist

def GetCourse():
    courses = Course.objects.filter(is_publish=True).order_by('-end_date')
    courselist = []
    sort_number = 1
    for course in courses:
        coursedict = {}
        coursedict["id"] = course.id
        coursedict["number"] = sort_number
        coursedict["course_name"] = course.course_name
        coursedict["start_date"] = course.start_date
        coursedict["end_date"] = course.end_date
        coursedict["promotor"] = course.promotor
        coursedict["certificate_id"] = course.certificate_id
        courselist.append(coursedict)
        sort_number+=1
    return courselist

def GetVariables():
    variables = Variable.objects.all()
    variablelist = []
    for variable in variables:
        variabledict = {}
        variabledict["id"] = variable.id
        variabledict["name"] = variable.name
        variabledict["value"] = variable.value
        variablelist.append(variabledict)
    return variablelist

def GetProjects():
    projects = Project.objects.filter(is_publish=True)
    projectlist = []
    for project in projects:
        projectdict = {}
        projectdict["id"] = project.id
        projectdict["name"] = project.name
        projectdict["short_line"] = project.short_line
        projectdict["description"] = project.description
        projectdict["image_path"] = project.image_path
        projectdict["repo_url"] = project.repo_url
        projectdict["journal_url"] = project.journal_url
        projectdict["stacks"] = [a.name for a in project.stacks.all()]
        projectlist.append(projectdict)
    return projectlist

def GetAbout():
    about = AboutDesc.objects.get(is_publish=True)
    return about.content