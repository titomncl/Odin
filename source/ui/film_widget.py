from qtpy import QtWidgets as Qw

from Odin.source.ui.create_dialog import CreateDialog


class Film(Qw.QWidget):
    def __init__(self, controller, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.init_dialog()

        self.setLayout(self.dialog_layout())

    def dialog_layout(self):
        v_layout = Qw.QVBoxLayout()

        v_layout.setContentsMargins(5, 5, 5, 5)

        v_layout.addWidget(self.create_seq_dialog)
        v_layout.addWidget(self.create_shot_dialog)

        return v_layout

    def btn_layout(self):
        main_layout = Qw.QVBoxLayout()

        self.new_seq = Qw.QPushButton("Add new sequence...")
        self.new_shot = Qw.QPushButton("Add new shot...")

        main_layout.addWidget(self.new_seq)
        main_layout.addWidget(self.new_shot)

        return main_layout

    def init_dialog(self):
        self.create_seq_dialog = CreateDialog(self.controller,
                                                "Create sequence...", "New sequence:", "S###",
                                                self)

        self.create_seq_dialog.text_field.setText("S")

        self.create_shot_dialog = CreateDialog(self.controller,
                                               "Create shot...", "New shot:", "P###",
                                               self, "Sequence:")

        self.create_shot_dialog.text_field.setText("P")
