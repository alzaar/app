from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import generics, viewsets

# Poll List and Poll Detail classes can be grouped together under PollViewSet class whihc is a subclass of ModelViewSets and thus can be ignored
class PollList(generics.ListCreateAPIView):
  queryset = Poll.objects.all()
  serializer_class = PollSerializer
  # def get(self, request):
  #   polls = Poll.objects.all()
  #   data = PollSerializer(polls, many=True).data
  #   return Response(data)

class PollDetail(generics.RetrieveDestroyAPIView):
  queryset = Poll.objects.all()
  serializer_class = PollSerializer
  # def get(self, request, pk):
  #   poll = get_object_or_404(Poll, pk=pk)
  #   data = PollSerializer(poll).data
  #   return Response(data)

class ChoiceList(generics.ListCreateAPIView):
  def get_queryset(self):
    queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
    return queryset
  serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
  serializer_class = VoteSerializer

  def post(self, request, pk, choice_pk):
    voted_by = request.data.get('voted_by')
    data = {
      'poll_id': pk,
      'choice_id': choice_id,
      'voted_by': voted_by
    }
    serializer = VoteSerializer(data=data)
    if serializer.is_valid():
      vote = serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class VoteDetail(generics.RetrieveDestroyAPIView):
#   queryset = Vote.objects.all()
#   serializer_class = VoteSerializer

class PollViewSet(viewsets.ModelViewSet):
  queryset = Poll.objects.all()
  serializer_class = PollSerializer

class UserCreate(generics.CreateAPIView):
  permission_classes = ()
  authentication_classes = ()
  serializer_class = UserSerializer