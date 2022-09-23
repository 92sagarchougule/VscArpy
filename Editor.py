import arcpy

from arcpy import env

ecs = env.workspace = r'D:\General\Professional\1. Ph.D\Agrani\GIS data\Vector Data\Shapefiles'



editor = arcpy.da.Editor(r'D:\DataforArcObject')

row = arcpy.da.UpdateCursor(r'D:\DataforArcObject\Properties_with_HH.shp',['FID','Shape','Ow_Name','Cast','TypeHouse'])