from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place
from where_to_go import settings


def generate_point_place(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse('places', args=[place.id])
        }
    }


def index(request):
    places_db = Place.objects.all()
    points_places = []
    for place in places_db:
        points_places.append(generate_point_place(place))
    places = {"type": "FeatureCollection",
              "features": points_places}
    return render(request, 'places/index.html', {'places': places})


def get_absolute_image_url(img):
    return f'{settings.MEDIA_URL}{img.file_name}'


def places_json(request, pk):
    place = get_object_or_404(Place, pk=pk)
    response_data = {
        "title": place.title,
        "imgs": [get_absolute_image_url(img) for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(response_data, safe=False)
