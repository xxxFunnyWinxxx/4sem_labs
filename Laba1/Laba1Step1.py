import gmsh
import sys
from numpy import cos, sin, pi
##########################################
def TorusPlanes(R, r, N = 100, lc = 1e-1,):
    CenterPoints = []
    FirstPoints = []
    SecondPoints = []

    for i in range(N):
        z = r * sin(i * 2 * pi / N)
        y = r * cos(i * 2 * pi / N)
        CenterPoints.append(gmsh.model.geo.addPoint(0, 0, z, lc))
        FirstPoints.append(gmsh.model.geo.addPoint(0, R + y, z, lc))
        SecondPoints.append(gmsh.model.geo.addPoint(0, - R - y, z, lc))

    Circles1 = []
    Circles2 = []
    Arc1 = []
    Arc2 = []
    CenterPoint1 = gmsh.model.geo.addPoint(0, R, 0)
    CenterPoint2 = gmsh.model.geo.addPoint(0, - R, 0)

    for i in range(N):
        Circles1.append(gmsh.model.geo.addCircleArc(FirstPoints[i], CenterPoints[i], SecondPoints[i]))
        Circles2.append(gmsh.model.geo.addCircleArc(SecondPoints[i], CenterPoints[i], FirstPoints[i]))
        Arc1.append(gmsh.model.geo.addCircleArc(FirstPoints[i % N], CenterPoint1, FirstPoints[(i + 1) % N]))
        Arc2.append(gmsh.model.geo.addCircleArc(SecondPoints[i % N], CenterPoint2, SecondPoints[(i + 1) % N]))

    Loops1 = []
    Loops2 = []
    for i in range(N):
        Loops1.append(
            gmsh.model.geo.addCurveLoop([Circles1[i % N], Arc2[i % N], - Circles1[(i + 1) % N], - Arc1[i % N]]))
        Loops2.append(
            gmsh.model.geo.addCurveLoop([Circles2[i % N], Arc1[i % N], - Circles2[(i + 1) % N], - Arc2[i % N]]))

    Planes = []
    for i in Loops1:
        Planes.append(gmsh.model.geo.addPlaneSurface([i]))
    for i in Loops2:
        Planes.append(gmsh.model.geo.addPlaneSurface([i]))
    return Planes

gmsh.initialize()

gmsh.model.add("tor.stl")

PlanesIn = TorusPlanes(5, 0.9)
PlanesOut = TorusPlanes(5, 1)

gmsh.model.geo.addSurfaceLoop(PlanesIn, 1)
gmsh.model.geo.addSurfaceLoop(PlanesOut, 2)
gmsh.model.geo.addVolume([1, -2])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("t1.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()