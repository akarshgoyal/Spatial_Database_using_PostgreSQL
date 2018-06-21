import math
import simplekml

R=5
r=1
a=4
n=10
b=34.0212823
c=-118.2892845
kml=simplekml.Kml()

t=0.0
while (t<n*math.pi): 
    x= (R+r)*math.cos((r/R)*t)-a*math.cos((1+r/R)*t)
    y= (R+r)*math.sin((r/R)*t)-a*math.sin((1+r/R)*t)
    d=b+x
    e=c+y
    kml.newpoint(name="hefje", coords=[(e,d)])
    t+=0.01
    
kml.save("bbg.kml")



    
