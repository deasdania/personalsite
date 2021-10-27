from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class CreateUpdate(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()

        self.update_date = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

STATUS_TYPE = (
    ('ONGOING', 'Ongoing'),
    ('PASSED', 'Passed'),
)

class Education(CreateUpdate):
    university_location = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    education_level = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=3,decimal_places=2)
    is_publish = models.BooleanField(default=False)

class Experience(CreateUpdate):
    position_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_TYPE, default='ONGOING', db_index=True)
    is_publish = models.BooleanField(default=False)
    def __str__(self):
        return self.position_name
    # class Meta:
    #     ordering = [-1]

class Course(CreateUpdate):
    course_name = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    promotor = models.CharField(max_length=255)
    certificate_id = models.CharField(max_length=255, null=True, blank=True)
    course_file = models.FileField(upload_to='course_files')
    is_publish = models.BooleanField(default=False)

class SocialMedia(CreateUpdate):
    media_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    is_publish = models.BooleanField(default=False)

class Variable(CreateUpdate):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

# class Task(models.Model):
#     TODO = 'todo'
#     DONE = 'done'
#
#     STATUS_CHOICES = (
#         (TODO, 'Todo'),
#         (DONE, 'Done')
#     )
#
#     description = models.CharField(max_length=255)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)

class Jobdesc(CreateUpdate):
    content = RichTextField(blank=True,null=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='jobdesc_experience')

class AboutDesc(CreateUpdate):
    content = RichTextField(blank=True,null=True)
    purpose = models.CharField(max_length=255, null=True, blank=True)
    is_publish = models.BooleanField(default=False)

class Stacks(CreateUpdate):
    TYPE_CHOICES = [
        ('LANGUAGE', 'Programming Language'),
        ('FRAMEWORK', 'Framework'),
        ('PLATFORM', 'Platform'),
    ]
    name = models.CharField(max_length=20)
    stack_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='LANGUAGE'
        )
    icon_class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(CreateUpdate):
    name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255)
    short_line = models.CharField(max_length=255)
    description = RichTextField(blank=True,null=True)
    repo_url = models.CharField(max_length=255)
    journal_url = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True)
    is_publish = models.BooleanField(default=False)
    stacks = models.ManyToManyField(Stacks)
    def __str__(self):
        return self.name

