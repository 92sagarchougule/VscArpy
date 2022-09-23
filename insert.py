import arcpy

from arcpy import env

ecs = env.workspace = r'D:\General\Professional\1. Ph.D\Agrani\GIS data\Vector Data\Shapefiles'

row = arcpy.da.InsertCursor(r'E:\5. KRSRDPU\Nagavi Mapping\Styles\LuLc.shp',['Name','Area'])

dlist = []


dlist.append('Sagar Chougule')
dlist.append(125436)

tpl = tuple(dlist)

row.insertRow(tpl)

print('done')


# f1 = open(r'D:\DataforArcObject\Shingtaluru_Data.csv','r')

# for lines in f1.readlines():
#     print(lines)

# f1.close()