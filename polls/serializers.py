from rest_framework import serializers
from .models import Poll, Choice, Vote

class VoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vote
    fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
  votes = VoteSerializer(required=False, many=True)
  class Meta:
    model = Choice
    fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
  choices = ChoiceSerializer(required=False, many=True, read_only=True)
  class Meta:
    model = Poll
    fields = '__all__'