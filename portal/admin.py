from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis import admin
from .models import *



admin.site.register(boundary, LeafletGeoAdmin)
admin.site.register(Highway, LeafletGeoAdmin)
admin.site.register(Houses, LeafletGeoAdmin)
admin.site.register(Road, LeafletGeoAdmin)
admin.site.register(procareas, LeafletGeoAdmin)




# <!-- admin.site.register(Buildings, LeafletGeoAdmin) -->s