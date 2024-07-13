from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import Point
from .models import UserLocation

def index(request):
    return render(request, 'geo_app/index.html')

@csrf_exempt
def submit_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except (TypeError, ValueError) as e:
            return JsonResponse({'error': 'Invalid latitude or longitude'}, status = 400)
        

        if latitude is None or longitude is None:
            return JsonResponse({'error': 'Missing latitude or longitude'}, status = 400)
        
        user_location = UserLocation.objects.create(location=Point(longitude, latitude))

        return JsonResponse({'message': 'Location submitted successfully'})
    
    return JsonResponse({'error': 'Invalid location'}, status = 405)
