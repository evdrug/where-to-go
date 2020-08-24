import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Add Place from json file in DB'

    def add_arguments(self, parser):
        parser.add_argument('path_json', type=str)

    def created_place(self, data):
        return Place.objects.get_or_create(
            title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            lng=data['coordinates']['lng'],
            lat=data['coordinates']['lat'],
        )

    def add_images(self, images, place):
        for position, url in enumerate(images):
            with requests.get(url, stream=True) as respone_file:
                respone_file.raise_for_status()
                file_name = url.split('/')[-1]
                obj_image, created_image = Image.objects.get_or_create(
                    place=place, position=position)
                if created_image:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Add image in place `{place.title}`'))
                    obj_image.file_name.save(file_name,
                                       ContentFile(respone_file.content),
                                       save=True)

    def handle(self, *args, **options):
        response = requests.get(options['path_json'])
        response.raise_for_status()
        place_json = response.json()
        place, created = self.created_place(place_json)

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully add Place'))
            self.add_images(place_json['imgs'], place)

        else:
            self.stdout.write(self.style.WARNING(
                f'Place `{place.title}` already exists!'))
