from django.urls import path
from .views import ChoiceList, CreateVote
from .views import PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

# PollViewSet takes care of the routes below 
# path('polls/', PollList.as_view(), name='poll_list'),
# path('polls/<int:pk>/', PollDetail.as_view(), name='poll_detail'),


urlpatterns = [
  path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
  path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
]

urlpatterns += router.urls