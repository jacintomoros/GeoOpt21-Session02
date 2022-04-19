from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

# #we also import random library to generate some randomness 
# import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/contour",
    name = "Slicing object",
    inputs=[
        hs.HopsBrep("Shape", "Brep", "Brep or mesh to analyze", hs.HopsParamAccess.ITEM),
        # hs.HopsPoint("Point", "PT", "Contour start point", hs.HopsParamAccess.ITEM, default= (0,0,0)),
        # hs.HopsNumber("Direction", "DR", "Contour normal direction", hs.HopsParamAccess.ITEM, default= (0,0,1)),
        # hs.HopsInteger("Distance", "DI", "Distance between countours", hs.HopsParamAccess.ITEM, default= 1)

    ],
    outputs=[
       hs.HopsCurve("Resulting Edges","Edges","List of generated edges ", hs.HopsParamAccess.LIST),
       hs.HopsPoint("Resulting Nodes","Nodes","List of generated nodes ", hs.HopsParamAccess.LIST)
    ]
)


def createcountourCrvs(brep):

    edges = geo.brepEdges(brep)
    nodes = geo.brepNodes()
    
    return edges, nodes
    
#be careful with cache!
if __name__== "__main__":
    app.run(debug=True)