from rest_framework.serializers import ModelSerializer
from training.models import Exercise

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'min_age', 'activo']