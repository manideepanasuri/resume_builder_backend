from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User=get_user_model()
class UserDetailsCollage(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_details')
    rollno=models.CharField(max_length=20)
    program=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    collage=models.CharField(max_length=200)
    def __str__(self):
        return f'{self.user.name} - {self.rollno} - {self.program} - {self.course} - {self.collage}'

class ContactInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact_info')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    student_email = models.EmailField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.user.name}'s Contact Info"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True, null=True)
    board = models.CharField(max_length=255, blank=True, null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255)
    dates = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.role} at {self.company}"

class ExperienceDescription(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='descriptions')
    description = models.TextField()

    def __str__(self):
        return self.description

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField()
    dates = models.CharField(max_length=255)
    tools = models.TextField()

    def __str__(self):
        return self.name
class ProjectDescription(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='descriptions')
    description = models.TextField()
    def __str__(self):
        return self.description

class Skill(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='skills')
    language = models.TextField(blank=True, null=True)
    developer_tools = models.TextField(blank=True, null=True)
    framework = models.TextField(blank=True, null=True)
    cloud_database = models.TextField(blank=True, null=True)
    soft_skills = models.TextField(blank=True, null=True)
    coursework = models.TextField(blank=True, null=True)
    area_of_interest = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name}'s Skills"

class PositionOfResponsibility(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='positions')
    position = models.CharField(max_length=255)
    club_event = models.CharField(max_length=255)
    tenure = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.position} at {self.club_event}"

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.CharField(max_length=500)
    description = models.TextField()
    dates = models.CharField(max_length=255)

    def __str__(self):
        return self.achievement
