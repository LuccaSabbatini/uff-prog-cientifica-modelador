from PyQt5.QtWidgets import *
from OpenGL.GL import *
from PyQt5.QtGui import *
from hetool.include.hetool import Hetool
from hetool.geometry.point import Point


class AppCurveCollector:
    def __init__(self):
        # Initialization
        self.m_isActive = False
        self.m_curveType = "None"
        self.m_ctrlPts = []
        self.m_tempCurve = []

    def isActive(self):
        return self.m_isActive

    # Activation w/ curve type
    def activateCollector(self, _curve):
        self.m_isActive = True
        self.m_curveType = _curve

    # Deactivation clearing the collector
    def deactivateCollector(self):
        self.m_isActive = False
        self.m_curveType = "None"
        self.m_ctrlPts = []
        self.m_tempCurve = []

    # Point Collection (depends on curve type and points collected)
    def collectPoint(self, _x, _y):
        isComplete = False
        if self.m_isActive:
            if self.m_curveType == "Line":
                if len(self.m_ctrlPts) == 0:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 1:
                    self.m_ctrlPts.append([_x, _y])
                    isComplete = True
            elif self.m_curveType == "Bezier2":
                if len(self.m_ctrlPts) == 0:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 1:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 2:
                    self.m_ctrlPts.append([_x, _y])
                    isComplete = True
            elif self.m_curveType == "Rectangular":
                if len(self.m_ctrlPts) == 0:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 1:
                    self.m_ctrlPts.append([_x, _y])
                    isComplete = True
            elif self.m_curveType == "Quadrilateral":
                if len(self.m_ctrlPts) == 0:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 1:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 2:
                    self.m_ctrlPts.append([_x, _y])
                elif len(self.m_ctrlPts) == 3:
                    self.m_ctrlPts.append([_x, _y])
                    isComplete = True
        return isComplete

    # Curve (temporary and finalized)
    def getCurveToDraw(self):
        return self.m_tempCurve

    def getCurve(self):
        if self.m_curveType == "Line":
            curve = self.m_ctrlPts
        else:
            curve = self.m_tempCurve
        self.m_ctrlPts = []
        self.m_tempCurve = []
        return curve

    # Create Mesh
    def createMesh(self, _patch, _distance):
        # Get the bounding box of the selected patch
        xMin, xMax, yMin, yMax = _patch.getBoundBox()

        # Print the bounding box
        print("Bounding Box: ", xMin, xMax, yMin, yMax)
        print("Distance Between Points: ", _distance)

        # Get all points inside the bounding box
        all_points = []
        for x in range(int(xMin), int(xMax), int(_distance)):
            for y in range(int(yMin), int(yMax), int(_distance)):
                all_points.append([x, y])

        # Get all points inside the patch
        for point in all_points:
            hetool_point = Point(point[0], point[1])
            if _patch.isPointInside(hetool_point):
                Hetool.insertPoint(hetool_point)

    # Update temporary curve (mouse tracking)
    def update(self, _x, _y):
        if self.m_curveType == "Line":
            if len(self.m_ctrlPts) == 0:
                pass
            elif len(self.m_ctrlPts) == 1:
                self.m_tempCurve = [self.m_ctrlPts[0], [_x, _y]]
        elif self.m_curveType == "Bezier2":
            if len(self.m_ctrlPts) == 0:
                pass
            elif len(self.m_ctrlPts) == 1:
                self.m_tempCurve = [self.m_ctrlPts[0], [_x, _y]]
            elif len(self.m_ctrlPts) == 2:
                nSampling = 20
                self.m_tempCurve = []
                for ii in range(nSampling + 1):
                    t = ii / nSampling
                    ptx = (
                        (1 - t) ** 2 * self.m_ctrlPts[0][0]
                        + 2 * (1 - t) * t * _x
                        + t**2 * self.m_ctrlPts[1][0]
                    )
                    pty = (
                        (1 - t) ** 2 * self.m_ctrlPts[0][1]
                        + 2 * (1 - t) * t * _y
                        + t**2 * self.m_ctrlPts[1][1]
                    )
                    self.m_tempCurve.append([ptx, pty])
        elif self.m_curveType == "Rectangular":
            if len(self.m_ctrlPts) == 0:
                pass
            elif len(self.m_ctrlPts) == 1:
                self.m_tempCurve = [
                    self.m_ctrlPts[0],
                    [self.m_ctrlPts[0][0], _y],
                    [_x, _y],
                    [_x, self.m_ctrlPts[0][1]],
                    self.m_ctrlPts[0],
                ]
        elif self.m_curveType == "Quadrilateral":
            # draw a rectangle one vertex at a time
            if len(self.m_ctrlPts) == 0:
                pass
            elif len(self.m_ctrlPts) == 1:
                # draw line
                self.m_tempCurve = [self.m_ctrlPts[0], [_x, _y]]
            elif len(self.m_ctrlPts) == 2:
                # draw triangle
                self.m_tempCurve = [self.m_ctrlPts[0], self.m_ctrlPts[1], [_x, _y]]
            elif len(self.m_ctrlPts) == 3:
                # draw rectangle
                self.m_tempCurve = [
                    self.m_ctrlPts[0],
                    self.m_ctrlPts[1],
                    self.m_ctrlPts[2],
                    [_x, _y],
                    self.m_ctrlPts[0],
                ]
