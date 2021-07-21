from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc

from .create_dialog import CreateDialog


class Lib(Qw.QWidget):
    def __init__(self, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.create_chara_dialog = None
        self.create_props_dialog = None
        self.create_set_dialog = None
        self.create_fx_dialog = None

        self.text_field = None
        self.create_btn = None

        self.init_dialog()

        self.setLayout(self.dialog_layout())

    def dialog_layout(self):
        v_layout = Qw.QVBoxLayout()

        v_layout.setContentsMargins(5, 5, 5, 5)

        v_layout.addWidget(self.create_chara_dialog, alignment=Qc.Qt.AlignmentFlag.AlignVCenter)
        v_layout.addWidget(self.create_props_dialog, alignment=Qc.Qt.AlignmentFlag.AlignVCenter)
        v_layout.addWidget(self.create_set_dialog, alignment=Qc.Qt.AlignmentFlag.AlignVCenter)
        v_layout.addWidget(self.create_fx_dialog, alignment=Qc.Qt.AlignmentFlag.AlignVCenter)

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.create_btn = Qw.QPushButton("Create")
        self.create_btn.setFixedHeight(30)

        frame = Qw.QFrame()
        frame.setFrameStyle(Qw.QFrame.StyledPanel | Qw.QFrame.Sunken)
        frame.setLayout(v_layout)

        main_layout.addWidget(frame)
        main_layout.addWidget(self.create_btn)
        return main_layout

    def init_dialog(self):
        self.create_chara_dialog = CreateDialog("", "Character name:", "CHARA", self)
        self.create_props_dialog = CreateDialog("", "Props name:", "PROPS", self)
        self.create_set_dialog = CreateDialog("", "Set name:", "SET", self)
        self.create_fx_dialog = CreateDialog("", "FX name:", "FX", self)
