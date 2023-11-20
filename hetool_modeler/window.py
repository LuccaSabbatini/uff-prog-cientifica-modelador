from PyQt5.QtWidgets import *
from OpenGL.GL import *
from PyQt5.QtGui import *
from hetool.include.hetool import Hetool
from canvas import AppCanvas


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
