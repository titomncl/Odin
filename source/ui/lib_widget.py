from qtpy import QtWidgets as Qw

from Odin.source.ui.create_dialog import CreateDialog

class Lib(Qw.QWidget):
    def __init__(self, controller, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.create_chara_dialog = CreateDialog(self.controller,
                                                "Create character...", "Character name:", "CHARA",
                                                self)
        self.create_props_dialog = CreateDialog(self.controller,
                                                "Create props...", "Props name:", "PROPS",
                                                self)
        self.create_set_dialog = CreateDialog(self.controller,
                                              "Create set...", "Set name:", "SET",
                                              self)
        self.create_fx_dialog = CreateDialog(self.controller,
                                             "Create FX...", "FX name:", "FX",
                                             self)

        self.setLayout(self.btn_layout())

        self.init_connexions()

    def btn_layout(self):
        main_layout = Qw.QVBoxLayout()

        self.create_chara_btn = Qw.QPushButton("Create character...")
        self.create_props_btn = Qw.QPushButton("Create props...")
        self.create_set_btn = Qw.QPushButton("Create set...")
        self.create_fx_btn = Qw.QPushButton("Create FX...")

        main_layout.addWidget(self.create_chara_btn)
        main_layout.addWidget(self.create_props_btn)
        main_layout.addWidget(self.create_set_btn)
        main_layout.addWidget(self.create_fx_btn)

        return main_layout

    def init_connexions(self):
        self.create_chara_btn.clicked.connect(self.chara_action_dialog)
        self.create_props_btn.clicked.connect(self.props_action_dialog)
        self.create_set_btn.clicked.connect(self.set_action_dialog)
        self.create_fx_btn.clicked.connect(self.fx_action_dialog)

    def chara_action_dialog(self):
        self.create_chara_dialog.show()

    def props_action_dialog(self):
        self.create_props_dialog.show()

    def set_action_dialog(self):
        self.create_set_dialog.show()

    def fx_action_dialog(self):
        self.create_fx_dialog.show()

