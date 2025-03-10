from django.urls import path
from .views import *

urlpatterns = [
    # UserDetailsCollage URLs
    path('user-details/', UserDetailsCollageView.as_view(), name='user-details'),

    # ContactInformation URLs
    path('contact-info/', ContactInformationView.as_view(), name='contact'),
    # Education URLs
    path('educations/', EducationView.as_view(), name='education'),
    # Experience URLs
    path('experiences/', ExperienceView.as_view(), name='experience'),
    # Project URLs
    path('projects/', ProjectView.as_view(), name='project'),

    # Skill URLs
    path('skills/', SkillView.as_view(), name='skill'),

    # PositionOfResponsibility URLs
    path('positions/', PositionView.as_view(), name='position'),

    # Achievement URLs
    path('achievements/', AchievementView.as_view(), name='achievement'),
]