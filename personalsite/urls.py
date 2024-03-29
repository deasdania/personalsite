"""personalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from personaldata import views

# patterns
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PersonalDataView.as_view(), name='personaldata'),
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('personaldata/', views.DataView.as_view(), name='data'),

    path('social/', views.GetSocialMediaView.as_view(), name='social'),
    path('education/', views.GetEducationView.as_view(), name='education'),
    path('projects/', views.GetProjectsView.as_view(), name='projects'),
    path('experience/', views.GetExperienceView.as_view(), name='experience'),
    path('course/', views.GetCourseView.as_view(), name='course'),
    path('variable/', views.GetVariableView.as_view(), name='variable'),
    path('about/', views.GetContentAboutView.as_view(), name='about'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
