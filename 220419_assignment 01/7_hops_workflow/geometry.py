import rhino3dm as rg
def brepEdges(brep):

    curves = []
    for i in range(len (brep.Edges)):
        nc = brep.Edges[i].ToNurbsCurve()
        curves.append(nc)
    
    return curves