from typing import NoReturn, Optional

from qtpy import QtCore as Qc
from qtpy import QtGui as Qg
from qtpy import QtWidgets as Qw

from ..globals import Logger as log
from .create_dialog import CreateDialog
from .create_or_set_prj import CreateSet
from .manage_prj import ManageProject
from .updater import Updater


class MainWindow(Qw.QMainWindow):
    def __init__(self, controller, parent=None):
        # type: (object, Optional[Qw.QApplication]) -> NoReturn

        super(MainWindow, self).__init__(parent=parent)

        self.controller = controller

        self.setWindowTitle("Odin")

        self.setWindowIcon(Qg.QIcon("./resources/icons/odin.png"))

        self.setMinimumSize(400, 250)
        self.resize(400, 250)

        self.create_or_set = CreateSet(self)
        self.create_project_dialog = CreateDialog("Create project...", "Project name:", "PRJ", self.create_or_set)
        self.add_widget_project_dialog()

        self.manage_prj = ManageProject(self)

        self.stacked_widget = Qw.QStackedWidget()

        self.stacked_widget.addWidget(self.create_or_set)
        self.stacked_widget.addWidget(self.manage_prj)

        self.setCentralWidget(self.stacked_widget)

        self.menu_bar = Qw.QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.menu_actions()
        self.create_menu()

        self._init_connexions()

    def _init_connexions(self):
        self.create_or_set.create_btn.clicked.connect(self.create_btn_action)
        self.create_or_set.close_btn.clicked.connect(self.close)

    def add_widget_project_dialog(self):
        self.create_project_dialog.setWindowFlag(Qc.Qt.WindowType.Tool)
        layout = self.create_project_dialog.layout()

        self.create_project_btn = Qw.QPushButton("Create")
        self.create_project_btn.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)

        close_btn = Qw.QPushButton("Close")
        close_btn.setSizePolicy(Qw.QSizePolicy.Policy.Expanding, Qw.QSizePolicy.Policy.Fixed)
        close_btn.clicked.connect(self.create_project_dialog.close)

        h_layout = Qw.QHBoxLayout()
        h_layout.addWidget(self.create_project_btn)
        h_layout.addWidget(close_btn)

        layout.addLayout(h_layout)

    def create_menu(self):
        config = Qw.QMenu("&Config", self)
        self.menu_bar.addMenu(config)
        config.addAction(self.change_root_action)
        config.addSeparator()
        config.addAction(self.create_project_action)
        config.addAction(self.set_project_action)
        config.addSeparator()
        config.addAction(self.set_tools_path)

        update = Qw.QMenu("Update", self)
        self.menu_bar.addMenu(update)
        update.addAction(self.check_new_update)
        update.addAction(self.include_beta)

        help = Qw.QAction("Help", self)
        help.triggered.connect(self.open_doc)
        self.menu_bar.addAction(help)

    def menu_actions(self):
        self.change_root_action = Qw.QAction("Change root..", self)

        self.create_project_action = Qw.QAction("Create project...", self)
        self.create_project_action.triggered.connect(self.create_btn_action)

        self.set_project_action = Qw.QAction("Change project", self)
        self.set_project_action.triggered.connect(self.change_project_action)

        self.set_tools_path = Qw.QAction("Set tools path...", self)

        self.check_new_update = Qw.QAction("Check new update...", self)
        self.check_new_update.triggered.connect(self.check_new_update_action)

        self.include_beta = Qw.QAction("Include beta", self, checkable=True)

    def open_doc(self):
        import webbrowser

        from ... import __version__

        webbrowser.open("https://odin-project-manager.readthedocs.io/en/{}/".format(__version__))

    def get_new_path(self, root):
        # type: (str) -> str
        path = Qw.QFileDialog.getExistingDirectory(self, directory=root, options=Qw.QFileDialog.ShowDirsOnly)

        if path:
            return path
        else:
            raise RuntimeError("Path can't be empty")

    def create_btn_action(self):
        self.create_project_dialog.show()

    def change_project_action(self):
        self.stacked_widget.setCurrentWidget(self.create_or_set)
        self.setMinimumSize(400, 250)
        self.resize(400, 250)

    def check_new_update_action(self):

        u = Updater(self.include_beta.isChecked(), self)

        if not u.updated:
            msg_box = Qw.QMessageBox(self)
            msg_box.setIcon(msg_box.Information)
            msg_box.setWindowTitle("Updated")
            msg_box.setText("Odin is up to date.")

            msg_box.exec_()

    def closeEvent(self, close_event):
        # type: (Qg.QCloseEvent) -> NoReturn
        log.info("Close Odin")
