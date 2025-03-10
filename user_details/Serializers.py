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

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = ('id', 'description')

class ExperienceSerializer(serializers.ModelSerializer):
    descriptions = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ('id', 'company', 'city', 'role', 'dates', 'descriptions')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        descriptions_data = validated_data.pop('descriptions', [])
        experience = Experience.objects.create(**validated_data)
        for description_data in descriptions_data:
            ExperienceDescription.objects.create(experience=experience, **description_data)
        return experience

    def update(self, instance, validated_data):
        descriptions_data = validated_data.pop('descriptions', [])
        instance.company = validated_data.get('company', instance.company)
        instance.city = validated_data.get('city', instance.city)
        instance.role = validated_data.get('role', instance.role)
        instance.dates = validated_data.get('dates', instance.dates)
        instance.save()

        # Update descriptions
        instance.descriptions.all().delete() #replace all existing descriptions.
        for description_data in descriptions_data:
            ExperienceDescription.objects.create(experience=instance, **description_data)
        return instance

class ProjectDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDescription
        fields = ('id', 'description')

class ProjectSerializer(serializers.ModelSerializer):
    descriptions = ProjectDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'dates', 'tools', 'descriptions')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        descriptions_data = validated_data.pop('descriptions', [])
        project = Project.objects.create(**validated_data)
        for description_data in descriptions_data:
            ProjectDescription.objects.create(project=project, **description_data)
        return project

    def update(self, instance, validated_data):
        descriptions_data = validated_data.pop('descriptions', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.dates = validated_data.get('dates', instance.dates)
        instance.tools = validated_data.get('tools', instance.tools)
        instance.save()

        # Update descriptions
        instance.descriptions.all().delete() #replace all existing descriptions.
        for description_data in descriptions_data:
            ProjectDescription.objects.create(project=instance, **description_data)
        return instance

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class PositionOfResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionOfResponsibility
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)