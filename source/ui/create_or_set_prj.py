from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc
from qtpy import QtGui as Qg

# from Odin.source.ui.create_prj import CreateProject

class CreateSet(Qw.QWidget):
    def __init__(self, controller, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.set_ui()

    def set_ui(self):

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        ipm_label = Qw.QLabel("Project Manager")
        ipm_label.setFixedHeight(30)
        ipm_label.setFont(Qg.QFont("Calibri", 20))

        main_layout.addWidget(ipm_label, alignment=Qc.Qt.AlignCenter)
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        main_layout.addLayout(self.buttons_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 10))
        main_layout.addLayout(self.close_layout())

        self.setLayout(main_layout)

    def buttons_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.create_btn = Qw.QPushButton("CREATE\nPROJECT")
        self.create_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        h_layout.addWidget(self.create_btn)
        h_layout.addLayout(self.set_prj_layout())

        return h_layout

    def set_prj_layout(self):
        v_layout = Qw.QVBoxLayout()

        self.prod_cbox = Qw.QComboBox()
        self.prod_cbox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)
        self.prod_cbox.setFixedHeight(30)
        self.prod_cbox.addItems(self.controller.projects)

        self.set_btn = Qw.QPushButton("SET PROJECT")
        self.set_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        v_layout.addWidget(self.prod_cbox)
        v_layout.addSpacerItem(Qw.QSpacerItem(100, 4))
        v_layout.addWidget(self.set_btn)

        return v_layout

    def close_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.close_btn = Qw.QPushButton("Close")
        self.close_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)

        h_layout.addSpacerItem(Qw.QSpacerItem(300, 1))
        h_layout.addWidget(self.close_btn)

        return h_layout
