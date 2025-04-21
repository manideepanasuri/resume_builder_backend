from rest_framework import serializers
from .models import (
    UserDetailsCollage,
    ContactInformation,
    Education,
    Experience,
    ExperienceDescription,
    Project,
    ProjectDescription,
    Skill,
    PositionOfResponsibility,
    Achievement,
)

class UserDetailsCollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailsCollage
        fields = '__all__'


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'



class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'

class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = ('id', 'description')

class ExperienceSerializer(serializers.ModelSerializer):
    descriptions = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ('id', 'company', 'city', 'role', 'dates', 'descriptions')


class ProjectDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDescription
        fields = ('id', 'description')

class ProjectSerializer(serializers.ModelSerializer):
    descriptions = ProjectDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'dates', 'tools', 'descriptions')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class PositionOfResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionOfResponsibility
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
