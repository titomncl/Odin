from qtpy import QtWidgets as Qw
from qtpy import QtGui as Qg

from Odin.source.ui.create_or_set_prj import CreateSet
from Odin.source.ui.create_dialog import CreateDialog
from Odin.source.ui.manage_prj import ManageProject


class MainWindow(Qw.QMainWindow):
    def __init__(self, controller, parent):

        super(MainWindow, self).__init__(parent=parent)

        self.controller = controller

        self.setWindowTitle("Odin")

        self.setWindowIcon(Qg.QIcon("./icon/odin.png"))

        self.setMinimumSize(400, 250)

        self.create_or_set = CreateSet(self.controller, self.parent())
        self.create_project_dialog = CreateDialog(self.controller,
                                       "Create project...", "Project name:", "PRJ",
                                                  self.create_or_set)
        self.manage_prj = ManageProject(self.controller, self.parent())

        self.stacked_widget = Qw.QStackedWidget()

        self.stacked_widget.addWidget(self.create_or_set)
        self.stacked_widget.addWidget(self.manage_prj)

        self.setCentralWidget(self.stacked_widget)

        self.menu_bar = Qw.QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.menu_actions()
        self.create_menu()

        self.init_connexions()

    def init_connexions(self):
        self.create_or_set.create_btn.clicked.connect(self.create_btn_action)
        self.create_or_set.set_btn.clicked.connect(self.set_btn_action)
        self.create_or_set.close_btn.clicked.connect(self.close)

        self.create_project_dialog.create_btn.clicked.connect(self.create_prj_btn)
        self.manage_prj.lib_widget.create_chara_dialog.create_btn.clicked.connect(self.controller.chara_action)
        self.manage_prj.lib_widget.create_props_dialog.create_btn.clicked.connect(self.controller.props_action)
        self.manage_prj.lib_widget.create_set_dialog.create_btn.clicked.connect(self.controller.set_action)
        self.manage_prj.lib_widget.create_fx_dialog.create_btn.clicked.connect(self.controller.fx_action)

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

        self.set_project_action = Qw.QAction("&Set project", self)
        self.set_project_action.triggered.connect(self.set_btn_action)

    def set_change_root(self):
        self.create_or_set.prod_cbox.clear()
        root = Qw.QFileDialog.getExistingDirectory(self, directory=self.controller.root,
                                                   options=Qw.QFileDialog.ShowDirsOnly)
        if root:
            self.controller.set_root(root)
            self.update_combobox()

    def create_prj_btn(self):
        self.controller.create_project()

        self.update_combobox()

    def update_combobox(self):
        self.create_or_set.prod_cbox.clear()
        self.create_or_set.prod_cbox.addItems(self.controller.projects)

    def create_btn_action(self):
        self.create_project_dialog.show()

    def set_btn_action(self):
        if not self.create_or_set.prod_cbox.count() == 0:
            self.stacked_widget.setCurrentWidget(self.manage_prj)
            self.resize(400, 350)
