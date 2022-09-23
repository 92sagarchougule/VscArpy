import arcpy

from arcpy import env

ecs = env.workspace = r'D:\General\Professional\1. Ph.D\Agrani\GIS data\Vector Data\Shapefiles'

row = arcpy.da.UpdateCursor(r'D:\DataforArcObject\Properties_with_HH.shp',['FID','Shape','Ow_Name','Cast','TypeHouse'])

# with row as upcurso:
#     for raw in upcurso:
#         if(raw[2]=='Take Me'):
#             raw[2]="Take"
#         #if(row[2] == 'Veerappa bagewadi'):
#             #row[2]="New_Tag"

#         upcurso.updateRow(raw)
#         print(row[0],':',raw[1],' : ',raw[2],' : ',raw[3] ,' : ',raw[4])

    
for raw in row:
    if(raw[2]=='Take Le'):
        raw[2]="Veerappa bagewadi"

        print(row[0],':',raw[1],' : ',raw[2],' : ',raw[3] ,' : ',raw[4])
    
    row.updateRow(raw)
    #print(row[0],':',raw[1],' : ',raw[2],' : ',raw[3] ,' : ',raw[4])

    
del(row)
