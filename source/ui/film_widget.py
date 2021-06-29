from qtpy import QtWidgets as Qw


class Film(Qw.QWidget):
    def __init__(self, controller, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.setLayout(self.btn_layout())

    def btn_layout(self):
        main_layout = Qw.QVBoxLayout()

        self.new_seq = Qw.QPushButton("Add new sequence...")
        self.new_shot = Qw.QPushButton("Add new shot...")

        main_layout.addWidget(self.new_seq)
        main_layout.addWidget(self.new_shot)

        return main_layout
