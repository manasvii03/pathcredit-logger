from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Activity
import json

@api_view(['GET', 'POST'])
def activities(request):
    if request.method == 'GET':
        data = Activity.objects.all().order_by('-id')
        result = [
            {'id': a.id, 'name': a.name, 'category': a.category, 'date': str(a.date)}
            for a in data
        ]
        return Response(result)

    if request.method == 'POST':
        name = request.data.get('name')
        category = request.data.get('category')
        date = request.data.get('date')

        if not name or not category or not date:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        activity = Activity.objects.create(name=name, category=category, date=date)
        return Response({'id': activity.id, 'name': activity.name, 'category': activity.category, 'date': str(activity.date)}, status=status.HTTP_201_CREATED)