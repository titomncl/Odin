from qtpy import QtWidgets as Qw
from qtpy import QtGui as Qg
from qtpy import QtCore as Qc


class CreateDialog(Qw.QWidget):
    def __init__(self, title, label, place_holder, parent=None, cbox_label=None):
        Qw.QWidget.__init__(self, parent)

        self.setWindowTitle(title)

        self._text = label
        self._place_holder = place_holder

        self._cbox_label = cbox_label

        self._text_field = Qw.QLineEdit("")

        self.setWindowModality(Qc.Qt.WindowModality.WindowModal)

        self.setLayout(self.dialog_layout())

    def dialog_layout(self):
        label = Qw.QLabel(self._text)
        label.setSizePolicy(Qw.QSizePolicy.Policy.Fixed, Qw.QSizePolicy.Policy.Fixed)

        self._text_field.setPlaceholderText(self._place_holder)
        self._text_field.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)
        self._text_field.textChanged.connect(self.base_palette)

        v_layout = Qw.QVBoxLayout()

        if self._cbox_label:
            v_layout.addLayout(self.cbox_layout())

        v_layout.addWidget(label)
        v_layout.addWidget(self._text_field)

        main_layout = Qw.QVBoxLayout()
        main_layout.addLayout(v_layout)

        return main_layout

    def cbox_layout(self):
        label = Qw.QLabel(self._cbox_label)
        label.setSizePolicy(Qw.QSizePolicy.Policy.Fixed, Qw.QSizePolicy.Policy.Expanding)

        self._cbox = Qw.QComboBox()
        self._cbox.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)
        self._cbox.setFixedHeight(20)

        cbox_layout = Qw.QVBoxLayout()
        cbox_layout.addWidget(label)
        cbox_layout.addWidget(self._cbox)

        return cbox_layout

    def red_palette(self):
        red_color = Qg.QBrush(Qg.QColor(234, 102, 102))
        palette = Qg.QPalette()
        palette.setBrush(Qg.QPalette.All, Qg.QPalette.Base, red_color)

        self._text_field.setPalette(palette)

    def base_palette(self):
        base_color = Qg.QBrush(Qg.QColor(70, 86, 113))
        palette = Qg.QPalette()
        palette.setBrush(Qg.QPalette.All, Qg.QPalette.Base, base_color)

        self._text_field.setPalette(palette)

    def green_palette(self):
        base_color = Qg.QBrush(Qg.QColor(102, 234, 102))
        palette = Qg.QPalette()
        palette.setBrush(Qg.QPalette.All, Qg.QPalette.Base, base_color)

        self._text_field.setPalette(palette)

    @property
    def text_field(self):
        return self._text_field.text().upper()

    @text_field.setter
    def text_field(self, value):
        self._text_field.setText(value)

    @property
    def cbox(self):
        return self._cbox
