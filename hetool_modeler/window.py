from PyQt5.QtWidgets import *
from OpenGL.GL import *
from PyQt5.QtGui import *
from hetool.include.hetool import Hetool
from canvas import AppCanvas
from dialogs import *
from constants import MIN_MESH_DISTANCE


class AppWindow(QMainWindow):
    def __init__(self, scale_factor=1.0):
        # Window initialization
        super(AppWindow, self).__init__()
        self.setGeometry(150, 100, 600, 400)
        self.setWindowTitle("MyGLDrawer")
        self.m_canvas = AppCanvas(scale_factor=scale_factor)
        self.setCentralWidget(self.m_canvas)

        # ToolBar Actions
        tb = self.addToolBar("ToolBar")
        fit = QAction("Fit View", self)
        tb.addAction(fit)
        addLine = QAction("Add Line", self)
        tb.addAction(addLine)
        addBezier2 = QAction("Add Bezier", self)
        tb.addAction(addBezier2)
        addRectangular = QAction("Add Rectangular", self)
        tb.addAction(addRectangular)
        addQuadrilateral = QAction("Add Quadrilateral", self)
        tb.addAction(addQuadrilateral)
        createMesh = QAction("Create Mesh", self)
        tb.addAction(createMesh)
        select = QAction("Select", self)
        tb.addAction(select)
        selectMultiple = QAction("Select Multiple", self)
        tb.addAction(selectMultiple)
        delete = QAction("Delete", self)
        tb.addAction(delete)
        undo = QAction("Undo", self)
        tb.addAction(undo)
        redo = QAction("Redo", self)
        tb.addAction(redo)
        tb.actionTriggered[QAction].connect(self.tbpressed)

    # ToolBar Pressed Function
    def tbpressed(self, _action):
        if _action.text() == "Fit View":
            self.m_canvas.fitWorldToViewport()
            self.m_canvas.update()
        elif _action.text() == "Add Line":
            self.m_canvas.setState("Collect", "Line")
        elif _action.text() == "Add Bezier":
            self.m_canvas.setState("Collect", "Bezier2")
        elif _action.text() == "Add Rectangular":
            self.m_canvas.setState("Collect", "Rectangular")
        elif _action.text() == "Add Quadrilateral":
            self.m_canvas.setState("Collect", "Quadrilateral")
        elif _action.text() == "Create Mesh":
            if len(Hetool.getSelectedPatches()) == 0:
                NoPatchSelectedDialog().exec_()
            else:
                dialog = CreateMeshDialog()
                dialog.exec_()
                distance = dialog.getDistance()

                if distance >= MIN_MESH_DISTANCE:
                    self.m_canvas.setState("CreateMesh", distance)
        elif _action.text() == "Select":
            self.m_canvas.setState("Select")
        elif _action.text() == "Select Multiple":
            self.m_canvas.setState("SelectMultiple")
        elif _action.text() == "Delete":
            Hetool.delSelectedEntities()
            self.m_canvas.update()
        elif _action.text() == "Undo":
            Hetool.undo()
            self.m_canvas.update()
        elif _action.text() == "Redo":
            Hetool.redo()
            self.m_canvas.update()
