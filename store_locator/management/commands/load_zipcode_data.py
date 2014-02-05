""" Load data for the zip code location table. The file has the following format.
    zip,city,state,lat,long
"""
import csv
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import os


from ...models import ZipCodeLocation

class Command(BaseCommand):
    args = "<csv_file_name>"
    help = "Load a CSV zip code data file Format: zip,city,state,lat,long"


    def load_data(self, reader):
        with transaction.commit_on_success():
            cnt = 0
            insert_list = []
            for row in reader:
                location = "POINT({0} {1})".format(row['longitude'], row['latitude'])
                insert_list.append(ZipCodeLocation(zip_code=row['zip'], location=location))
                cnt = cnt + 1

            ZipCodeLocation.objects.bulk_create(insert_list)

        return cnt


    def handle(self, *args, **kwargs):
        if( len(args) != 1):
            raise CommandError("CSV data file required.")

        filename = args[0]
        if not os.path.exists(filename):
            raise CommandError("Data file {0} does not exist.".format(filename))


        result = raw_input("Existing Zip Code Locations will be deleted. Do you wish to continuse yes/no?")
        if result.upper() != "YES":
            raise CommandError("Loading Zip Code Data Cancelled")

        # Delete existing ZipCode Locations
        ZipCodeLocation.objects.all().delete()

        csvfile = file(filename, "rU")
        reader = csv.DictReader(csvfile)

        load_count = 0
        load_count = self.load_data(reader)

        csvfile.close()
        self.stdout.write("Loaded {0} zip code locations".format(load_count))
