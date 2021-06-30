from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc
from qtpy import QtGui as Qg


class CreateDialog(Qw.QDialog):
    def __init__(self, controller, title, label, place_holder, parent=None):
        Qw.QDialog.__init__(self, parent)

        self.setWindowTitle(title)

        self.controller = controller
        self.label = label
        self.place_holder = place_holder

        self.setParent(parent)

        self.setModal(True)

        self.set_ui()

    def set_ui(self):

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel(self.label)
        label.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Expanding)

        self.text_field = Qw.QLineEdit()
        self.text_field.setPlaceholderText(self.place_holder)

        self.text_field.textChanged.connect(self.base_palette)

        v_layout.addWidget(label)
        v_layout.addWidget(self.text_field)

        h_layout = Qw.QHBoxLayout()
        self.setContentsMargins(0, 0, 0, 0)

        self.create_btn = Qw.QPushButton("Create")
        self.close_btn = Qw.QPushButton("Close")

        self.close_btn.clicked.connect(self.close)

        h_layout.addWidget(self.create_btn)
        h_layout.addWidget(self.close_btn)
        v_layout.addLayout(h_layout)

        # ------------ SET LAYOUT ------------

        frame = Qw.QFrame()
        frame.setFrameStyle(Qw.QFrame.StyledPanel | Qw.QFrame.Sunken)
        frame.setLayout(v_layout)

        main_layout.addWidget(frame)
        self.setLayout(main_layout)

    def red_palette(self):
        red_color = Qg.QBrush(Qg.QColor(234, 102, 102, 255))
        palette = Qg.QPalette()
        palette.setBrush(Qg.QPalette.All, Qg.QPalette.Base, red_color)

        self.text_field.setPalette(palette)

    def base_palette(self):
        base_color = Qg.QBrush(Qg.QColor(255, 255, 255, 255))
        palette = Qg.QPalette()
        palette.setBrush(Qg.QPalette.All, Qg.QPalette.Base, base_color)

        self.text_field.setPalette(palette)

    def green_palette(self):
        base_color = Qg.QBrush(Qg.QColor(102, 234, 102, 255))
        palette = Qg.QPalette()
        palette.setBrush(Qg.QPalette.All, Qg.QPalette.Base, base_color)

        self.text_field.setPalette(palette)
