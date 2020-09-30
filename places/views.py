from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def serialize_place(place):
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
    places = Place.objects.all()
    points_places = []
    for place in places:
        points_places.append(serialize_place(place))
    places_features = {"type": "FeatureCollection",
                       "features": points_places}
    return render(request, 'places/index.html', {'places': places_features})


def places_json(request, pk):
    place = get_object_or_404(Place, pk=pk)
    response_data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(response_data, safe=False,
                        json_dumps_params={'indent': 2, 'ensure_ascii': False})
