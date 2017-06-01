import os
from django.contrib.gis.utils import LayerMapping
from .models import procareas

procareas_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}





procareas_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../portal/data/PROCAREAS.shp'))

def run(verbose=True):
    lm = LayerMapping(procareas, procareas_shp  , procareas_mapping, transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)