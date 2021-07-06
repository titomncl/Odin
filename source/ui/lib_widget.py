from qtpy import QtWidgets as Qw

from Odin.source.ui.create_dialog import CreateDialog


class Lib(Qw.QWidget):
    def __init__(self, controller, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.init_dialog()

        self.setLayout(self.dialog_layout())

    def dialog_layout(self):
        v_layout = Qw.QVBoxLayout()

        v_layout.setContentsMargins(5, 5, 5, 5)

        v_layout.addWidget(self.create_chara_dialog)
        v_layout.addWidget(self.create_props_dialog)
        v_layout.addWidget(self.create_set_dialog)
        v_layout.addWidget(self.create_fx_dialog)

        return v_layout

    def init_dialog(self):
        self.create_chara_dialog = CreateDialog(self.controller,
                                                "Create character...", "Character name:", "CHARA",
                                                self, close_btn=False)
        self.create_props_dialog = CreateDialog(self.controller,
                                                "Create props...", "Props name:", "PROPS",
                                                self, close_btn=False)
        self.create_set_dialog = CreateDialog(self.controller,
                                              "Create set...", "Set name:", "SET",
                                              self, close_btn=False)
        self.create_fx_dialog = CreateDialog(self.controller,
                                             "Create FX...", "FX name:", "FX",
                                             self, close_btn=False)
