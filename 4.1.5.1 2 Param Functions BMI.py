def ftintom(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lbstokg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))