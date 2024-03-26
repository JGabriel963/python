from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from training.models import Exercise
from training.selializers import ExerciseSerializer

@api_view(['GET', 'POST'])
def get_or_create(request):
    if request.method == "GET":
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data, status=200)
    if request.method == "POST":
        exercise = ExerciseSerializer(data=request.data)
        if exercise.is_valid():
            exercise.save()
            return Response(exercise.data, status=201)
        else:
            return Response(exercise.errors, status=400)
        
@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete(request, pk):
    exercise = Exercise.objects.get(id=pk)

    if request.method == "GET":
        serializer = ExerciseSerializer(exercise, many=False)
        return Response(serializer.data, status=200)
    
    if request.method == 'PUT':
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        exercise.delete()
        return Response(status=204)