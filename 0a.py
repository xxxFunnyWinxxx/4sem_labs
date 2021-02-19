import gmsh
import sys

gmsh.initialize()
gmsh.model.add("t1")

lc = 1e-1
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, 1, 0, lc, 3)
gmsh.model.geo.addPoint(1, 1, 0, lc, 4)
gmsh.model.geo.addPoint(0, 0, 1, lc, 5)
gmsh.model.geo.addPoint(1, 0, 1, lc, 6)
gmsh.model.geo.addPoint(0, 1, 1, lc, 7)
gmsh.model.geo.addPoint(1, 1, 1, lc, 8)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(3, 1, 2)
gmsh.model.geo.addLine(4, 3, 3)
gmsh.model.geo.addLine(2, 4, 4)
gmsh.model.geo.addLine(1, 5, 5)
gmsh.model.geo.addLine(2, 6, 6)
gmsh.model.geo.addLine(3, 7, 7)
gmsh.model.geo.addLine(4, 8, 8)
gmsh.model.geo.addLine(5, 6, 9)
gmsh.model.geo.addLine(7, 5, 10)
gmsh.model.geo.addLine(6, 8, 11)
gmsh.model.geo.addLine(8, 7, 12)

gmsh.model.geo.addCurveLoop([1, 4, 3, 2], 1)
gmsh.model.geo.addPlaneSurface([1],1)
gmsh.model.geo.addCurveLoop([3, 7, -12, -8], 2)
gmsh.model.geo.addPlaneSurface([2],2)
gmsh.model.geo.addCurveLoop([9, 11, 12, 10], 3)
gmsh.model.geo.addPlaneSurface([3],3)
gmsh.model.geo.addCurveLoop([1, 6, -9, -5], 4)
gmsh.model.geo.addPlaneSurface([4],4)
gmsh.model.geo.addCurveLoop([2, 5, -10, -7], 5)
gmsh.model.geo.addPlaneSurface([5],5)
gmsh.model.geo.addCurveLoop([4, 8, -11, -6], 6)
gmsh.model.geo.addPlaneSurface([6],6)

gmsh.model.geo.addSurfaceLoop([1,2,3,4,5,6],1)
gmsh.model.geo.addVolume([1])


gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("t1.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()