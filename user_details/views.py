from _ast import Return

from rest_framework import generics, permissions, status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .Serializers import *

# UserDetailsCollage Views
class UserDetailsCollageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user=request.user
        rollno=request.data.get('rollno')
        program=request.data.get('program')
        course=request.data.get('course')
        collage=request.data.get('collage')
        if UserDetailsCollage.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'User details already exists'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_details_collage=UserDetailsCollage.objects.create(user=user, rollno=rollno, program=program, course=course,collage=collage)
            data={
                'success': True,
                'message': 'User details created successfully',
                'user_details_collage': UserDetailsCollageSerializer(user_details_collage).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,request,*args,**kwargs):
        user=request.user
        if not UserDetailsCollage.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'User details does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            user_details_collage=UserDetailsCollage.objects.get(user=user)
            data={
                'success': True,
                'message': 'User details retreived successfully',
                'user_details_collage': UserDetailsCollageSerializer(user_details_collage).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user=request.user
        if not UserDetailsCollage.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'User details does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            user_details_collage=UserDetailsCollage.objects.get(user=user)
            rollno = request.data.get('rollno',user_details_collage.rollno)
            program = request.data.get('program',user_details_collage.program)
            course = request.data.get('course',user_details_collage.course)
            collage = request.data.get('collage',user_details_collage.collage)
            user_details_collage.rollno=rollno
            user_details_collage.program=program
            user_details_collage.course=course
            user_details_collage.collage=collage
            user_details_collage.save()
            data={
                'success': True,
                'message': 'User details updated successfully',
                'user_details_collage': UserDetailsCollageSerializer(user_details_collage).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        if not UserDetailsCollage.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'User details does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            user_details_collage=UserDetailsCollage.objects.get(user=user)
            user_details_collage.delete()
            data={
                'success': True,
                'message': 'User details deleted successfully',
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactInformationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        if ContactInformation.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Contact info already exists'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        phone=request.data.get('phone')
        email=request.data.get('email')
        student_email=request.data.get('student_email')
        github=request.data.get('github')
        linkedin=request.data.get('linkedin')
        try:
            contact_information=ContactInformation.objects.create(user=user,phone=phone,email=email,student_email=student_email,github=github,linkedin=linkedin)
            data={
                'success': True,
                'message': 'Contact info created successfully',
                'contact_information': ContactInformationSerializer(contact_information).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request,*args,**kwargs):
        user=request.user
        if not ContactInformation.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Contact info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            contact_information=ContactInformation.objects.get(user=user)
            data={
                'success': True,
                'message': 'Contact info created successfully',
                'contact_information': ContactInformationSerializer(contact_information).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request,*args,**kwargs):
        user=request.user
        if not ContactInformation.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Contact info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            contact_information=ContactInformation.objects.get(user=user)
            phone = request.data.get('phone',contact_information.phone)
            email = request.data.get('email',contact_information.email)
            student_email = request.data.get('student_email',contact_information.student_email)
            github = request.data.get('github',contact_information.github)
            linkedin = request.data.get('linkedin',contact_information.linkedin)
            contact_information.phone=phone
            contact_information.email=email
            contact_information.student_email=student_email
            contact_information.github=github
            contact_information.linkedin=linkedin
            contact_information.save()
            data={
                'success': True,
                'message': 'Contact info updated successfully',
                'contact_information': ContactInformationSerializer(contact_information).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        if not ContactInformation.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Contact info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            contact_information=ContactInformation.objects.get(user=user)
            contact_information.delete()
            data={
                'success': True,
                'message': 'Contact info deleted successfully',
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class EducationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        try:
            institution=request.data.get('institution')
            degree=request.data.get('degree')
            board=request.data.get('board')
            cgpa=request.data.get('cgpa')
            year=request.data.get('year')
            education=Education.objects.create(user=user,institution=institution,degree=degree,board=board,cgpa=cgpa,year=year)
            data={
                'success': True,
                'message': 'Education info created successfully',
                'education': EducationSerializer(education).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request,*args,**kwargs):
        user=request.user
        if not Education.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Education info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            education=Education.objects.all().filter(user=user)
            data={
                'success': True,
                'message': 'Education info retrieved successfully',
                'eductaion': EducationSerializer(education,many=True).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Education.objects.filter(user=user,id=id).exists():
            data={
                'success': False,
                'message': 'Education info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            education=Education.objects.get(user=user,id=id)
            institution = request.data.get('institution',education.institution)
            degree = request.data.get('degree',education.degree)
            board = request.data.get('board',education.board)
            cgpa = request.data.get('cgpa',education.cgpa)
            year = request.data.get('year',education.year)
            education.institution=institution
            education.degree=degree
            education.board=board
            education.cgpa=cgpa
            education.year=year
            education.save()
            data={
                'success': True,
                'message': 'Education info updated successfully',
                'education': EducationSerializer(education).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Education.objects.filter(user=user,id=id).exists():
            data={
                'success': False,
                'message': 'Education info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            education=Education.objects.get(user=user,id=id)
            education.delete()
            data={
                'success': True,
                'message': 'Education info deleted successfully',
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ExperienceView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        company=request.data.get('company')
        city=request.data.get('city')
        role=request.data.get('role')
        dates=request.data.get('dates')
        description=request.data.get('descriptions',[])
        try:
            experience=Experience.objects.create(user=user,company=company,city=city,role=role,dates=dates)
            for des in description:
                ExperienceDescription.objects.create(experience=experience,description=des)
            data={
                'success': True,
                'message': 'Experience created successfully',
                'experience': ExperienceSerializer(experience).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,request,*args,**kwargs):
        user=request.user
        try:
            experiences=Experience.objects.all().filter(user=user).order_by('-id')
            data={
                'success': True,
                'message': 'Experience info retrieved successfully',
                'experiences': ExperienceSerializer(experiences,many=True).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Experience.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Experience info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            experience=Experience.objects.get(id=id,user=user)
            company=request.data.get('company',experience.company)
            city=request.data.get('city',experience.city)
            role=request.data.get('role',experience.role)
            dates=request.data.get('dates',experience.dates)
            dess=ExperienceDescription.objects.all().filter(experience=experience)
            dess.all().delete()
            description=request.data.get('descriptions',ExperienceDescriptionSerializer(dess,many=True).data)
            experience.company=company
            experience.city=city
            experience.role=role
            experience.dates=dates
            for des in description:
                ExperienceDescription.objects.create(experience=experience,description=des)
            data={
                'success': True,
                'message': 'Experience updated successfully',
                'experience': ExperienceSerializer(experience).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Experience.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Experience info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            experience=Experience.objects.get(id=id,user=user)
            experience.delete()
            data={
                'success': True,
                'message': 'Experience deleted successfully',
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProjectView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        name=request.data.get('name')
        description=request.data.get('description')
        dates=request.data.get('dates')
        tools=request.data.get('tools')
        descriptions=request.data.get('descriptions')
        try:
            project=Project.objects.create(user=user,name=name,description=description,dates=dates,tools=tools)
            for des in descriptions:
                ProjectDescription.objects.create(project=project,description=des)
            data={
                'success': True,
                'message': 'Project created successfully',
                'project': ProjectSerializer(project).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request,*args,**kwargs):
        user=request.user
        try:
            projects=Project.objects.all().filter(user=user).order_by('-id')
            data={
                'success': True,
                'message': 'Project info retrieved successfully',
                'projects':ProjectSerializer(projects,many=True).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user = request.user
        id = request.data.get('id')
        if not Project.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Project info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            project=Project.objects.get(id=id,user=user)
            name = request.data.get('name',project.name)
            description = request.data.get('description',project.description)
            dates = request.data.get('dates',project.dates)
            tools = request.data.get('tools',project.tools)
            project.name = name
            project.description = description
            project.dates = dates
            project.tools = tools
            project.save()
            prodes=ProjectDescription.objects.filter(project=project)
            descriptions = request.data.get('descriptions',ProjectDescriptionSerializer(prodes,many=True).data)
            prodes.all().delete()
            for des in descriptions:
                ProjectDescription.objects.create(project=project,description=des)
            data={
                'success': True,
                'message': 'Project updated successfully',
                'project': ProjectSerializer(project).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Project.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Project info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            project=Project.objects.get(id=id,user=user)
            project.delete()
            data={
                'success': True,
                'message': 'Project deleted successfully',
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SkillView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        if Skill.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Skill info exist'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            language=request.data.get('language')
            developer_tools=request.data.get('developer_tools')
            framework=request.data.get('framework')
            cloud_database=request.data.get('cloud_database')
            soft_skills=request.data.get('softSkills')
            coursework=request.data.get('coursework')
            area_of_interest=request.data.get('area_of_interest')

            skill=Skill.objects.create(user=user,language=language,developer_tools=developer_tools,framework=framework,cloud_database=cloud_database,soft_skills=soft_skills,coursework=coursework,area_of_interest=area_of_interest)

            data={
                'success': True,
                'message': 'Skill created successfully',
                'skill': SkillSerializer(skill).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,request,*args,**kwargs):
        user=request.user
        if not Skill.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Skill info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            skill=Skill.objects.get(user=user)
            data={
                'success': True,
                'message': 'Skill info retrieved successfully',
                'skill': SkillSerializer(skill).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user=request.user
        if not Skill.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Skill info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            skill=Skill.objects.get(user=user)
            language = request.data.get('language',skill.language)
            developer_tools = request.data.get('developer_tools',skill.developer_tools)
            framework = request.data.get('framework',skill.framework)
            cloud_database = request.data.get('cloud_database',skill.cloud_database)
            soft_skills = request.data.get('soft_skills',skill.soft_skills)
            coursework = request.data.get('coursework',skill.coursework)
            area_of_interest = request.data.get('area_of_interest',skill.area_of_interest)
            skill.language = language
            skill.developer_tools = developer_tools
            skill.framework = framework
            skill.cloud_database = cloud_database
            skill.soft_skills = soft_skills
            skill.coursework = coursework
            skill.area_of_interest = area_of_interest
            skill.save()
            data={
                'success': True,
                'message': 'Skill updated successfully',
                'skill': SkillSerializer(skill).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        if not Skill.objects.filter(user=user).exists():
            data={
                'success': False,
                'message': 'Skill info does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            skill=Skill.objects.get(user=user)
            skill.delete()
            data={
                'success': True,
                'message': 'Skill deleted successfully'
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class PositionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        position=request.data.get('position')
        club_event=request.data.get('club_event')
        tenure=request.data.get('tenure')
        try:
            positi=PositionOfResponsibility.objects.create(user=user,position=position,club_event=club_event,tenure=tenure)
            data={
                'success': True,
                'message': 'Position created successfully',
                'position': PositionOfResponsibilitySerializer(positi).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request,*args,**kwargs):
        user=request.user
        try:
            position=PositionOfResponsibility.objects.all().filter(user=user)
            data={
                'success': True,
                'message': 'Position retrieved successfully',
                'position': PositionOfResponsibilitySerializer(position,many=True).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not PositionOfResponsibility.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Position does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            posi=PositionOfResponsibility.objects.get(id=id,user=user)
            position = request.data.get('position',posi.position)
            club_event = request.data.get('club_event',posi.club_event)
            tenure = request.data.get('tenure',posi.tenure)
            posi.position=position
            posi.club_event=club_event
            posi.tenure=tenure
            posi.save()
            data={
                'success': True,
                'message': 'Position updated successfully',
                'position': PositionOfResponsibilitySerializer(posi).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not PositionOfResponsibility.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Position does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            posi=PositionOfResponsibility.objects.get(id=id,user=user)
            posi.delete()
            data={
                'success': True,
                'message': 'Position deleted successfully'
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class AchievementView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        user=request.user
        try:
            achievement=request.data.get('achievement')
            description=request.data.get('description')
            dates=request.data.get('dates')
            achi=Achievement.objects.create(user=user,achievement=achievement,description=description,dates=dates)
            data={
                'success': True,
                'message': 'Achievement updated successfully',
                'achievement': AchievementSerializer(achi).data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request,*args,**kwargs):
        user=request.user
        try:
            achievement=Achievement.objects.all().filter(user=user)
            data={
                'success': True,
                'message': 'Achievement retrieved successfully',
                'achievement': AchievementSerializer(achievement,many=True).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Achievement.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Achievement does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            achievemen=Achievement.objects.get(id=id,user=user)
            achievemen.achievement=request.data.get('achievement',achievemen.achievement)
            achievemen.description=request.data.get('description',achievemen.description)
            achievemen.dates=request.data.get('dates',achievemen.dates)
            achievemen.save()
            data={
                'success': True,
                'message': 'Achievement updated successfully',
                'achievement': AchievementSerializer(achievemen).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,*args,**kwargs):
        user=request.user
        id=request.data.get('id')
        if not Achievement.objects.filter(id=id,user=user).exists():
            data={
                'success': False,
                'message': 'Achievement does not exist'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        try:
            achievement=Achievement.objects.get(id=id,user=user)
            achievement.delete()
            data={
                'success': True,
                'message': 'Achievement deleted successfully'
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data={
                'success': False,
                'message': str(e)
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


