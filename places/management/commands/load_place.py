import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Add Place from json file in DB'

    def add_arguments(self, parser):
        parser.add_argument('path_json', type=str)

    def print_stdout_success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def add_images(self, images, place):
        for position, url in enumerate(images):
            with requests.get(url, stream=True) as response_file:
                response_file.raise_for_status()
                response_content_file = response_file.content

            file_name = url.split('/')[-1]
            image_obj, image_created = Image.objects.get_or_create(
                place=place, position=position)
            if not image_created:
                continue
            content_file = ContentFile(response_content_file)
            image_obj.image.save(file_name, content_file, save=True)
            self.print_stdout_success(f'Add image in place `{place.title}`')

    def handle(self, *args, **options):
        response = requests.get(options['path_json'])
        response.raise_for_status()
        raw_place = response.json()
        place, created = Place.objects.update_or_create(
            title=raw_place['title'],
            defaults={
                "description_short": raw_place['description_short'],
                "description_long": raw_place['description_long'],
                "lng": raw_place['coordinates']['lng'],
                "lat": raw_place['coordinates']['lat'],
            }
        )

        if created:
            message = ('Successfully added a description for the place '
                       f'`{place.title}`')
            self.print_stdout_success(message)
            self.add_images(raw_place['imgs'], place)
        else:
            message = f'updated description place `{place.title}`'
            self.print_stdout_success(message)
