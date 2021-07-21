from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc
from qtpy import QtGui as Qg

import qtawesome as Qa


class CreateSet(Qw.QWidget):
    def __init__(self, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.set_ui()

    def set_ui(self):

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        ipm_label = Qw.QLabel("Project Manager")
        ipm_label.setFixedHeight(30)
        ipm_label.setFont(Qg.QFont("Calibri", 20))

        main_layout.addWidget(ipm_label, alignment=Qc.Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(self.root_and_project_layout())
        main_layout.addLayout(self.buttons_layout())
        main_layout.addLayout(self.close_layout())

        self.setLayout(main_layout)

    def root_and_project_layout(self):

        label = Qw.QLabel("Root path:")
        self.root_tip = Qw.QLabel("Not set")

        h_layout = Qw.QHBoxLayout()

        self.prod_cbox = Qw.QComboBox()
        self.prod_cbox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)
        self.prod_cbox.setFixedHeight(30)
        self.prod_cbox.setFixedWidth(100)

        h_layout.addWidget(label)
        h_layout.addWidget(self.root_tip, Qc.Qt.AlignmentFlag.AlignLeft)
        h_layout.addSpacerItem(Qw.QSpacerItem(20, 20))
        h_layout.addWidget(self.prod_cbox, alignment=Qc.Qt.AlignmentFlag.AlignRight)

        return h_layout

    def buttons_layout(self):
        h_layout = Qw.QHBoxLayout()

        new_project_icon = Qa.icon('fa5s.plus-square',
                                   options=[{"color": "#EF8229"}])
        self.create_btn = Qw.QPushButton(new_project_icon, "CREATE\nPROJECT")
        self.create_btn.setIconSize(Qc.QSize(64, 64))
        self.create_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        set_project_icon = Qa.icon('fa.folder-open',
                                   options=[{"color": "#EF8229"}])
        self.set_btn = Qw.QPushButton(set_project_icon, "SET PROJECT")
        self.set_btn.setIconSize(Qc.QSize(64, 64))
        self.set_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        h_layout.addWidget(self.create_btn)
        h_layout.addWidget(self.set_btn)

        return h_layout

    def close_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.close_btn = Qw.QPushButton("Close")
        self.close_btn.setFixedHeight(30)
        self.close_btn.setFixedWidth(100)

        h_layout.addWidget(self.close_btn, alignment=Qc.Qt.AlignmentFlag.AlignRight)

        return h_layout
