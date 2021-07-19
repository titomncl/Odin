from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc
from qtpy import QtGui as Qg

from Odin.source.ui.create_or_set_prj import CreateSet
from Odin.source.ui.create_dialog import CreateDialog
from Odin.source.ui.manage_prj import ManageProject
from Odin.source.globals import Logger as log


class MainWindow(Qw.QMainWindow):
    def __init__(self, controller, parent):

        super(MainWindow, self).__init__(parent=parent)

        self.controller = controller

        self.setWindowTitle("Odin")

        self.setWindowIcon(Qg.QIcon("./icon/odin.png"))

        self.setMinimumSize(400, 250)
        self.resize(400, 250)

        self.create_or_set = CreateSet(self)
        self.create_project_dialog = CreateDialog("Create project...", "Project name:", "PRJ", self.create_or_set)
        self.add_widget_project_dialog()

        self.manage_prj = ManageProject(self.controller, self)

        self.stacked_widget = Qw.QStackedWidget()

        self.stacked_widget.addWidget(self.create_or_set)
        self.stacked_widget.addWidget(self.manage_prj)

        self.setCentralWidget(self.stacked_widget)

        self.menu_bar = Qw.QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.menu_actions()
        self.create_menu()

        self.update_combobox()

        self.init_connexions()

    def init_connexions(self):
        self.create_or_set.create_btn.clicked.connect(self.create_btn_action)
        self.create_or_set.set_btn.clicked.connect(self.set_btn_action)
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
        config.addAction(self.set_change_root_action)
        config.addAction(self.create_project_action)
        config.addAction(self.set_project_action)

    def menu_actions(self):
        self.set_change_root_action = Qw.QAction("&Set/Change root..", self)
        self.set_change_root_action.triggered.connect(self.set_change_root)

        self.create_project_action = Qw.QAction("&Create project...", self)
        self.create_project_action.triggered.connect(self.create_btn_action)

        self.set_project_action = Qw.QAction("&Change project", self)
        self.set_project_action.triggered.connect(self.change_project_action)

    def set_change_root(self):
        if self.stacked_widget.currentWidget() is not self.create_or_set:
            self.change_project_action()
        root = Qw.QFileDialog.getExistingDirectory(self, directory=self.controller.root,
                                                   options=Qw.QFileDialog.ShowDirsOnly)
        if root:
            self.controller.set_root(root)
            self.update_combobox()

    def create_prj_btn(self):
        self.controller.create_project()

        self.update_combobox()

    def update_combobox(self):
        if self.controller.root:
            self.create_or_set.root_tip.setText(self.controller.root_tip)
            self.create_or_set.prod_cbox.clear()
            self.create_or_set.prod_cbox.addItems(self.controller.projects)

            if self.controller.recent_project:
                prj_index = self.create_or_set.prod_cbox.findText(self.controller.recent_project)
                if prj_index != -1:
                    self.create_or_set.prod_cbox.setCurrentIndex(prj_index)

    def create_btn_action(self):
        self.create_project_dialog.show()

    def change_project_action(self):
        self.stacked_widget.setCurrentWidget(self.create_or_set)
        self.setMinimumSize(400, 250)
        self.resize(400, 250)

    def set_btn_action(self):
        if not self.create_or_set.prod_cbox.count() == 0:

            self.controller.set_var_env()

            self.manage_prj.film_widget.create_shot_dialog.cbox.clear()
            self.manage_prj.film_widget.create_shot_dialog.cbox.addItems(self.controller.sequences)

            self.stacked_widget.setCurrentWidget(self.manage_prj)
            self.setMinimumSize(400, 350)
            self.resize(400, 350)

    def closeEvent(self, a0: Qg.QCloseEvent) -> None:
        log.info("Close Odin")
