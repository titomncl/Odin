import qtawesome as Qa
from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc

from Odin.source.ui.lib_widget import Lib
from Odin.source.ui.softwares import Softwares
from Odin.source.ui.film_widget import Film


class ManageProject(Qw.QWidget):
    def __init__(self, controller, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.software_widget = Softwares(self.controller, self.parent())

        self.set_ui()

        self.init_connections()

    def set_ui(self):

        main_layout = Qw.QVBoxLayout()

        main_layout.addLayout(self.lib_film_layout())
        main_layout.addWidget(self.software_widget)

        self.setLayout(main_layout)

    def lib_film_layout(self):

        main_layout = Qw.QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        btn_layout = Qw.QVBoxLayout()

        lib_icon = Qa.icon('fa5s.archive',
                           options=[{"color": "#EF8229"}])

        self.lib_btn = Qw.QPushButton(lib_icon, "Lib")
        self.lib_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.MinimumExpanding)
        self.lib_btn.setIconSize(Qc.QSize(32, 32))
        self.lib_btn.setCheckable(True)

        film_icon = Qa.icon('fa5s.photo-video',
                            options=[{"color": "#EF8229"}])

        self.film_btn = Qw.QPushButton(film_icon, "Film")
        self.film_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.MinimumExpanding)
        self.film_btn.setIconSize(Qc.QSize(32, 32))
        self.film_btn.setCheckable(True)

        btn_layout.addWidget(self.lib_btn)
        btn_layout.addSpacerItem(Qw.QSpacerItem(10, 4))
        btn_layout.addWidget(self.film_btn)

        self.stacked_widgets = Qw.QStackedWidget()

        self.empty_w = self.empty_widget()
        self.lib_widget = self.lib_btn_widget()
        self.film_widget = self.film_btn_widget()

        self.stacked_widgets.addWidget(self.empty_w)
        self.stacked_widgets.addWidget(self.lib_widget)
        self.stacked_widgets.addWidget(self.film_widget)

        main_layout.addLayout(btn_layout)
        main_layout.addSpacerItem(Qw.QSpacerItem(10, 10))
        main_layout.addWidget(self.stacked_widgets)

        return main_layout

    def empty_widget(self):
        return Qw.QWidget()

    def lib_btn_widget(self):
        widget = Lib(self.controller, self.parent())

        return widget

    def film_btn_widget(self):
        widget = Film(self.controller, self.parent())

        return widget

    def init_connections(self):
        self.lib_btn.clicked.connect(self.lib_btn_action)
        self.film_btn.clicked.connect(self.film_btn_action)

    def lib_btn_action(self):
        if self.lib_btn.isChecked():
            self.stacked_widgets.setCurrentWidget(self.lib_widget)
            self.film_btn.setChecked(False)

            self.parent().parent().setMinimumSize(600, 665)
            self.parent().parent().resize(600, 665)
        else:
            self.stacked_widgets.setCurrentWidget(self.empty_w)
            self.parent().parent().setMinimumSize(400, 350)
            self.parent().parent().resize(400, 350)

    def film_btn_action(self):
        if self.film_btn.isChecked():
            self.stacked_widgets.setCurrentWidget(self.film_widget)
            self.lib_btn.setChecked(False)

            self.parent().parent().setMinimumSize(600, 480)
            self.parent().parent().resize(600, 480)
        else:
            self.stacked_widgets.setCurrentWidget(self.empty_w)
            self.parent().parent().setMinimumSize(400, 350)
            self.parent().parent().resize(400, 350)
