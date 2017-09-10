from pyproj import Proj

p=Proj(init='epsg:3857')

p.srs
x,y=p(-97.75,30.25)
print(x,y)
x,y=p(x,y,inverse=True)
print(x,y)