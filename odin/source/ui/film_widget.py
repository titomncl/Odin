from qtpy import QtWidgets as Qw

from .create_dialog import CreateDialog


class Film(Qw.QWidget):
    def __init__(self, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.init_dialog()

        self.setLayout(self.dialog_layout())

    def dialog_layout(self):
        v_layout = Qw.QVBoxLayout()

        v_layout.setContentsMargins(5, 5, 5, 5)

        v_layout.addWidget(self.create_filming_days_dialog)
        v_layout.addWidget(self.create_seq_dialog)
        v_layout.addWidget(self.create_shot_dialog)

        _frame = Qw.QFrame()
        _frame.setFrameStyle(Qw.QFrame.StyledPanel | Qw.QFrame.Sunken)
        _frame.setSizePolicy(Qw.QSizePolicy.Policy.Minimum, Qw.QSizePolicy.Policy.Fixed)
        _frame.setLayout(v_layout)

        main_layout = Qw.QVBoxLayout()
        main_layout.addWidget(_frame)

        return main_layout

    def init_dialog(self):

        # Init days of filming
        self.create_filming_days_dialog = CreateDialog("Create filming days", "Add filming days:", "##", self)
        film_layout = self.create_filming_days_dialog.layout()

        self.create_filming_days_btn = Qw.QPushButton("Create")
        self.create_filming_days_btn.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)

        film_layout.addWidget(self.create_filming_days_btn)

        self.create_filming_days_dialog.setLayout(film_layout)
        self.create_filming_days_dialog.text_field = "1"

        # Init sequence dialog
        self.create_seq_dialog = CreateDialog("Create sequence...", "New sequence:", "S###", self)
        seq_layout = self.create_seq_dialog.layout()

        self.create_seq_btn = Qw.QPushButton("Create")
        self.create_seq_btn.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)

        seq_layout.addWidget(self.create_seq_btn)

        self.create_seq_dialog.setLayout(seq_layout)
        self.create_seq_dialog.text_field = "S"

        # Init shot dialog
        self.create_shot_dialog = CreateDialog("Create shot...", "New shot:", "P###", self, "Sequence:")
        shot_layout = self.create_shot_dialog.layout()

        self.create_shot_btn = Qw.QPushButton("Create")
        self.create_shot_btn.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)

        shot_layout.addWidget(self.create_shot_btn)

        self.create_shot_dialog.setLayout(shot_layout)
        self.create_shot_dialog.text_field = "P"
