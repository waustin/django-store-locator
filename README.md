Django Store Locator app that uses geohasing to find locations.
Locations can be looked up by zipcode or lat/long



Requirements:
- GeoDjango
- PostGIS (might work on other geospatial databases, but I haven't tested it)


An example project is included in the demo directory.
The demo project requires:
- django-dotenv
- dj-database-url
- django-nose
- coverage
