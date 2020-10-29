def l100kmtompg(liters):
    gallons=liters/3.785411784
    miles=100/1.609344
    mpg=miles/gallons
    return mpg

def mpgtol100km(miles):
    kmg=miles*1.609344
    #print(miles,"mpg are",kmg,"kmpg")
    kml=kmg/3.785411784
    #print(kml,"kilometers lasts per liter")
    l100km=100/kml
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))