# we import all the libraries that our functions need here too
# import random as r
import rhino3dm as rg

def createcountourCrvs(shape,pt, dr, di):

    countourCrvs = []
    for obj_ref in obj_refs:
        geometry = obj_ref.Geometry()
        if geometry == None:
            return Result.Failure

        if type(geometry) == Brep:
            countourCrvs = shape.CreateContourCurves(shape, pt, dr, di)

    return countourCrvs