from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer
from rest_framework.response import Response
from rest_framework import generics

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
  queryset = Choice.objects.all()
  serializer_class = ChoiceSerializer

class CreateVote(generics.ListCreateAPIView):
  queryset = Vote.objects.all()
  serializer_class = VoteSerializer

class VoteDetail(generics.RetrieveDestroyAPIView):
  queryset = Vote.objects.all()
  serializer_class = VoteSerializer