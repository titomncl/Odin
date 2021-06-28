from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc

class CreateProject(Qw.QWidget):
    def __init__(self, parent=None):
        Qw.QWidget.__init__(self, parent)

        # self.setParent(parent)
        self.setWindowFlags(Qc.Qt.Tool)

        self.set_ui()

        self.show()

    def set_ui(self):

        self.setMinimumSize(200, 50)

        # ------------ VERTICAL LAYOUT ------------

        self.v_layout = Qw.QVBoxLayout()
        self.setContentsMargins(0, 0, 0, 0)

        label = Qw.QLabel("Project name:")

        self.text_field = Qw.QLineEdit()
        self.text_field.setPlaceholderText("PRJ")

        self.v_layout.addWidget(label)
        self.v_layout.addWidget(self.text_field)

        # ------------ HORIZONTAL LAYOUT ------------

        self.h_layout = Qw.QHBoxLayout()
        self.setContentsMargins(0, 0, 0, 0)

        self.create_btn = Qw.QPushButton("CREATE")
        self.close_btn = Qw.QPushButton("CLOSE")

        # self.create_btn.clicked.connect(self.ct_create_project)
        # self.close_btn.clicked.connect(self.close)

        self.h_layout.addWidget(self.create_btn)
        self.h_layout.addWidget(self.close_btn)
        self.v_layout.addLayout(self.h_layout)

        # ------------ SET LAYOUT ------------

        self.setLayout(self.v_layout)
