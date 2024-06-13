from rest_framework import serializers
from .models import RestapiTutorial

class Tutorial1Serializer(serializers.ModelSerializer):

    class Meta:
        model = RestapiTutorial
        fields = ['id','tutorialNo','title','content','StartDate','EndDate']