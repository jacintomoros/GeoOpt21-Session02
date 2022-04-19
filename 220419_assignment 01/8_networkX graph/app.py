#importing libraries and 'geometry' file
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import scipy as sp

app = Flask(__name__)
hops = hs.Hops(app)

#creating the workflow
@hops.component(
    "/createNetWork",
    name = "Create NetWork",
    inputs=[
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createStarGraph():

    G = geo.createGridGraph()
    GW = geo.addRandomWeigths(G)

    nodes = geo.getNodes(GW)
    edges = geo.getEdges(GW) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)