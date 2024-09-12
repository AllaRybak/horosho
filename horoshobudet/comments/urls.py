
from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('', CommentsList.as_view(), name='all_comments'),
    path('contact_us/', ContactUsCreateView.as_view(), name='contact_us'),
    path('addcomment/', AddComment.as_view(), name='add_comment'),
]
