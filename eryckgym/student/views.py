from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.decorators import api_view

# Importa o serializer

@api_view(['GET', 'POST'])
def get_or_create_student(request, format=None):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        student = StudentSerializer(data=request.data)
        # If - SE
        if student.is_valid():
            student.save()
            return Response(student.data, status=201)
        else:
            return Response(student.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'GET':
        selializer = StudentSerializer(student, many=False)
        return Response(selializer.data, status=200)
    
    if request.method == 'PUT':
        selializer = StudentSerializer(student, data=request.data)
        if selializer.is_valid():
            selializer.save()
            return Response(selializer.data)
        else:
            return Response(selializer.errors, status=400)
        
    if request.method == 'DELETE':
        student.delete()
        return Response(status=204)