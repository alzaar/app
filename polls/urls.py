from django.urls import path
from .views import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

# PollViewSet takes care of the routes below 
# path('polls/', PollList.as_view(), name='poll_list'),
# path('polls/<int:pk>/', PollDetail.as_view(), name='poll_detail'),


urlpatterns = [
  path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
  path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
  path('user/', UserCreate.as_view(),  name='create_user'),
  path('login/', views.obtain_auth_token, name='login_view')
]

urlpatterns += router.urls