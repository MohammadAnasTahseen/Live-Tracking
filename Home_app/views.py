from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Home_app.models import *
# Create your views here.

def index(request):
    return render(request,'index.html')


def get_location_data(request):

    # locations=DiverLocationUpdate.objects.filter('-timestamp')
    locations = DiverLocationUpdate.objects.order_by('-timestamp').first()  # Get the latest entry

    print("savced data in db",locations.latitude)



    return JsonResponse({'latitude':locations.latitude, 'longitude':locations.longitude,'time':locations.timestamp},safe=False)



# def get_location_data(request):
#     locations = DiverLocationUpdate.objects.order_by('-timestamp')[:10]
#     location_list = list(locations.values('latitude', 'longitude', 'timestamp'))  # Convert QuerySet to list of dicts

#     return JsonResponse({'locations': location_list}, safe=False)