from django.contrib.auth import get_user_model
from rest_framework import serializers

from user_details.Serializers import *

User=get_user_model()
class ResumeSerializer(serializers.ModelSerializer):
    userdetailscollage=serializers.SerializerMethodField()
    usercontactinformation=serializers.SerializerMethodField()
    usereducation=serializers.SerializerMethodField()
    userexperience=serializers.SerializerMethodField()
    userprojects= serializers.SerializerMethodField()
    userskills=serializers.SerializerMethodField()
    userpositionofresponsibility=serializers.SerializerMethodField()
    userachivements=serializers.SerializerMethodField()

    class Meta:
        model=User
        fields=['userdetailscollage','usercontactinformation','usereducation','userexperience','userprojects','userskills','userpositionofresponsibility','userachivements']


    def get_userdetailscollage(self,obj):
        user_details=UserDetailsCollageSerializer(obj.user_details).data
        return user_details
    def get_usercontactinformation(self,obj):
        user_contact=ContactInformationSerializer(obj.contact_info).data
        return user_contact
    def get_usereducation(self,obj):
        user_edu=EducationSerializer(obj.educations,many=True).data
        return user_edu
    def get_userexperience(self,obj):
        user_edu=ExperienceSerializer(obj.experiences,many=True).data
        return user_edu
    def get_userprojects(self,obj):
        user_projects=ProjectSerializer(obj.projects,many=True).data
        return user_projects
    def get_userskills(self,obj):
        user_skills=SkillSerializer(obj.skills).data
        return user_skills
    def get_userpositionofresponsibility(self,obj):
        user_position=PositionOfResponsibilitySerializer(obj.positions,many=True).data
        return user_position
    def get_userachivements(self,obj):
        user_ach=AchievementSerializer(obj.achievements,many=True).data
        return user_ach

