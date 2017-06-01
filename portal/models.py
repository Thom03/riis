from __future__ import unicode_literals

from django.db import models

from django.contrib.gis.db import models

class boundary(models.Model):
    objectid = models.IntegerField()
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4210)

# Auto-generated `LayerMapping` dictionary for boundary model
boundary_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'geom' : 'MULTILINESTRING',
}

class Highway(models.Model):
    objectid = models.IntegerField()
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4210)

# Auto-generated `LayerMapping` dictionary for Highway model
highway_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'geom' : 'MULTILINESTRING',
}

class Houses(models.Model):
    objectid = models.IntegerField()
    name = models.CharField(max_length=50,  default='House Name')
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4210)

    
    
        

# Auto-generated `LayerMapping` dictionary for Houses model
houses_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}


class Road(models.Model):
    objectid = models.IntegerField()
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4210)

# Auto-generated `LayerMapping` dictionary for Road model
road_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'geom' : 'MULTILINESTRING',
}

class procareas(models.Model):
    objectid = models.IntegerField()
    name = models.CharField(max_length=50,  default='protected')
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4210)

    def __unicode__(self):
        return self.name

# Auto-generated `LayerMapping` dictionary for procareas model
procareas_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}




