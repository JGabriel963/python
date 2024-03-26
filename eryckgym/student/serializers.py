from rest_framework.serializers import ModelSerializer
from student.models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student # Tabela Studante
        fields = ['id', 'name', 'age', 'active']

# - Isso é serializar 