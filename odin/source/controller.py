import os
import re
from typing import List, NoReturn, Optional

from qtpy.QtWidgets import QApplication, QMainWindow

from .common import concat, camelize
from .core import launch_software
from .core.filming_days import add_days
from .core.project import Project
from .core.sequence import Sequence
from .core.yaml_parser import Parser
from .globals import Logger as log
from .ui.updater import Updater


class Controller(object):
    """UI Controller."""

    def __init__(self, ui, parent=None):
        # type: (callable(QMainWindow), Optional[QApplication]) -> NoReturn

        self._project = None

        self._config_parser = Parser.open("./config/config_file.yaml")
        if not self._config_parser:
            self._config_parser = Parser.new("./config/config_file.yaml")

        self.ui = ui(self, parent)

        self.word_pattern = re.compile(r"^([A-Z0-9_]+)$")

        self.load_root()
        self.load_recent_project()

        self._init_connection()

        self.check_update()

    def show(self):
        self.ui.show()

    def init_root(self):
        try:
            self.root = self.ui.get_new_path("")
            self.load_root()
        except RuntimeError as e:
            log.error(concat("Exit: ", str(e)))
            raise SystemExit

    def load_root(self):
        try:
            self.ui.create_or_set.root_tip.setText(self.root_tip)
            self.update_combobox()

            log.info("Root path set: " + self.root)
        except KeyError:
            from .ui.message_box import MessageBox

            msg_box = MessageBox("Set root path", self.ui)
            msg_box.add_text("No root path found.")
            msg_box.add_informative_text("Specify the root path that will contain your project")
            action_btn = msg_box.action_button("Browse...", msg_box.ButtonRole.ActionRole)
            cancel_btn = msg_box.abort_button("Cancel", msg_box.ButtonRole.RejectRole)
            msg_box.exec_()

            if msg_box.clickedButton() == action_btn:
                self.init_root()
            elif msg_box.clickedButton() == cancel_btn:
                if msg_box.abort_action():
                    self.load_root()

    def load_recent_project(self):
        try:
            prj_index = self.ui.create_or_set.prod_cbox.findText(self.recent_project)
            if prj_index != -1:
                self.ui.create_or_set.prod_cbox.setCurrentIndex(prj_index)

            log.info("Recent project set: " + self.recent_project)
        except KeyError:
            pass

    def check_update(self):
        if "BETA" in self._config_parser.data:
            self.ui.include_beta.setChecked(self._config_parser.data["BETA"])
        else:
            self._config_parser.data["BETA"] = self.ui.include_beta.isChecked()

        self._config_parser.write()

        if "UPDATE" in self._config_parser.data:
            if self._config_parser.data["UPDATE"]:
                Updater(self.ui.include_beta.isChecked(), self.ui)
        else:
            Updater(self.ui.include_beta.isChecked(), self.ui)

            self._config_parser.data["UPDATE"] = True
            self._config_parser.write()

    def update_beta_box(self):
        self._config_parser.data["BETA"] = self.ui.include_beta.isChecked()
        self._config_parser.write()

    def update_combobox(self):
        self.ui.create_or_set.prod_cbox.clear()
        self.ui.create_or_set.prod_cbox.addItems(self.projects)

    def _init_connection(self):
        self.ui.change_root_action.triggered.connect(self.change_root_path)
        self.ui.set_tools_path.triggered.connect(self.change_tools_path)
        self.ui.include_beta.triggered.connect(self.update_beta_box)

        self.ui.create_project_btn.clicked.connect(self.create_project)
        self.ui.create_or_set.set_btn.clicked.connect(self.set_project)

        self.ui.manage_prj.lib_widget.create_btn.clicked.connect(self.create_asset_action)

        self.ui.manage_prj.film_widget.create_filming_days_btn.clicked.connect(self.filming_days_action)
        self.ui.manage_prj.film_widget.create_seq_btn.clicked.connect(self.seq_action)
        self.ui.manage_prj.film_widget.create_shot_btn.clicked.connect(self.shot_action)

        self.ui.manage_prj.software_widget.maya.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.zbrush.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.houdini.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.designer.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.painter.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.mari.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.photoshop.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.guerilla.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.nuke.clicked.connect(self.soft_action)
        self.ui.manage_prj.software_widget.resolve.clicked.connect(self.soft_action)

    def change_root_path(self):
        try:
            value = self.ui.get_new_path(self.root)
            self.root = value
            self.load_root()
        except RuntimeError as e:
            log.warning(e)

    def change_tools_path(self):
        # type: () -> bool
        try:
            self.tool_path = self.ui.get_new_path(self.root)
            os.environ["DEV_ENV"] = self.tool_path
            log.info("Tools path set: " + self.tool_path)
            return True
        except RuntimeError as e:
            log.warning(e)
            return False

    def create_project(self):
        project_name = self.ui.create_project_dialog.text_field

        project_name_match = re.match(r"^([A-Za-z0-9]+)$", project_name)

        if project_name_match:
            project_name = project_name_match.groups()[-1]
        else:
            project_name = camelize(project_name)

        if project_name not in self.projects and project_name != "":

            self.ui.create_project_dialog.green_palette()
            Project.new(self.root, project_name)
        else:
            self.ui.create_project_dialog.red_palette()

        self.update_combobox()

    def set_project(self):
        try:
            if self.tool_path:
                log.info("Tools path set: " + self.tool_path)
            else:
                log.info("No tools path set")
        except KeyError:
            self.tool_path = ""
            log.info("No tools path set")

        if not self.ui.create_or_set.prod_cbox.count() == 0:
            self.project = Project.load(self.root, self.project_name)
            self.set_var_env()
            self.ui.stacked_widget.setCurrentWidget(self.ui.manage_prj)

            self.ui.manage_prj.film_widget.create_shot_dialog.cbox.clear()
            self.ui.manage_prj.film_widget.create_shot_dialog.cbox.addItems(self.sequences)

            self.ui.setMinimumSize(400, 350)
            self.ui.resize(400, 350)

    def set_var_env(self):
        # type: () -> NoReturn
        self.recent_project = self.project_name

        os.environ["ROOT_PATH"] = self.root
        os.environ["PROJECT_ENV"] = os.path.join(self.root, self.project_name).replace("\\", "/")

        venv = os.path.abspath("venv").replace("\\", "/")

        if not os.path.exists(venv):
            venv = os.path.abspath("../venv").replace("\\", "/")

        log.info("Project set: " + os.environ["PROJECT_ENV"])

        os.environ["DEV_ENV"] = self.tool_path
        os.environ["venv"] = venv

        log.info("DEV_ENV: " + self.tool_path)
        log.info("venv: " + venv)

    @property
    def project(self):
        # type: () -> Project
        return self._project

    @project.setter
    def project(self, value):
        # type: (Project) -> None
        self._project = value

    @property
    def projects(self):
        # type: () -> List[str]
        return Project.list(self.root)

    @property
    def sequences(self):
        # type: () -> List[str]
        return Sequence.list(self.project)

    @property
    def root(self):
        # type: () -> str
        p = self._config_parser
        if p:
            return p.data["ROOT_PATH"]
        else:
            return "Not set"

    @root.setter
    def root(self, value):
        # type: (str) -> NoReturn
        self._config_parser.data["ROOT_PATH"] = value
        self._config_parser.write()

    @property
    def recent_project(self):
        # type: () -> str
        p = self._config_parser
        if p:
            return p.data["LAST_PROJECT"]
        else:
            return ""

    @recent_project.setter
    def recent_project(self, value):
        # type: (str) -> None
        self._config_parser.data["LAST_PROJECT"] = value
        self._config_parser.write()

    @property
    def tool_path(self):
        # type: () -> str
        return self._config_parser.data["TOOLS_PATH"]

    @tool_path.setter
    def tool_path(self, value):
        # type: (str) -> None
        self._config_parser.data["TOOLS_PATH"] = value
        self._config_parser.write()

    @property
    def project_name(self):
        # type: () -> str
        return self.ui.create_or_set.prod_cbox.currentText()

    @property
    def root_tip(self):
        # type: () -> str
        if len(self.root) > 30:
            return ".../" + self.root[30:] + "/"
        else:
            if self.root[-1] != "/":
                return self.root + "/"
            else:
                return self.root

    def create_asset_action(self):
        chara_name = self.ui.manage_prj.lib_widget.create_chara_dialog.text_field
        props_name = self.ui.manage_prj.lib_widget.create_props_dialog.text_field
        set_name = self.ui.manage_prj.lib_widget.create_set_dialog.text_field
        fx_name = self.ui.manage_prj.lib_widget.create_fx_dialog.text_field

        if chara_name:
            self.chara_action(chara_name)
        if props_name:
            self.props_action(props_name)
        if set_name:
            self.set_action(set_name)
        if fx_name:
            self.fx_action(fx_name)

    def chara_action(self, chara_name):
        # type: (str) -> None
        chara_is_correct = self.word_pattern.match(chara_name)

        if chara_is_correct:
            self.ui.manage_prj.lib_widget.create_chara_dialog.green_palette()
            self.project.new_asset(chara_name, "CHARA")
        else:
            self.ui.manage_prj.lib_widget.create_chara_dialog.red_palette()

    def props_action(self, props_name):
        # type: (str) -> None
        props_is_correct = self.word_pattern.match(props_name)

        if props_is_correct:
            self.ui.manage_prj.lib_widget.create_props_dialog.green_palette()
            self.project.new_asset(props_name, "PROPS")
        else:
            self.ui.manage_prj.lib_widget.create_props_dialog.red_palette()

    def set_action(self, set_name):
        # type: (str) -> None
        set_is_correct = self.word_pattern.match(set_name)

        if set_is_correct:
            self.ui.manage_prj.lib_widget.create_set_dialog.green_palette()
            self.project.new_asset(set_name, "SET")
        else:
            self.ui.manage_prj.lib_widget.create_set_dialog.red_palette()

    def fx_action(self, fx_name):
        # type: (str) -> None
        fx_is_correct = self.word_pattern.match(fx_name)

        if fx_is_correct:
            self.ui.manage_prj.lib_widget.create_fx_dialog.green_palette()
            self.project.new_asset(fx_name, "FX")
        else:
            self.ui.manage_prj.lib_widget.create_fx_dialog.red_palette()

    def filming_days_action(self):
        days = self.ui.manage_prj.film_widget.create_filming_days_dialog.text_field

        try:
            days = int(days)
            self.ui.manage_prj.film_widget.create_filming_days_dialog.green_palette()

            add_days(self.root, self.project_name, days)

            log.info("Filming days created")

        except ValueError:
            self.ui.manage_prj.film_widget.create_filming_days_dialog.red_palette()
            e = "Only integer are allowed here."
            log.error(e)

    def seq_action(self):
        seq_name = self.ui.manage_prj.film_widget.create_seq_dialog.text_field
        seq_pattern = re.compile(r"S(\d{3})")

        seq_is_correct = seq_pattern.match(seq_name)

        if seq_is_correct:
            self.ui.manage_prj.film_widget.create_seq_dialog.green_palette()
            self.project.new_sequence(seq_name)

            self.ui.manage_prj.film_widget.create_shot_dialog.cbox.clear()
            self.ui.manage_prj.film_widget.create_shot_dialog.cbox.addItems(self.sequences)
        else:
            self.ui.manage_prj.film_widget.create_seq_dialog.red_palette()

    def shot_action(self):
        shot_name = self.ui.manage_prj.film_widget.create_shot_dialog.text_field

        shot_pattern = re.compile(r"P(\d{3})")

        shot_is_correct = shot_pattern.match(shot_name)

        if shot_is_correct:
            self.ui.manage_prj.film_widget.create_shot_dialog.green_palette()

            seq_name = self.ui.manage_prj.film_widget.create_shot_dialog.cbox.currentText()

            Sequence.load(self.project, seq_name).new_shot(shot_name)
        else:
            self.ui.manage_prj.film_widget.create_shot_dialog.red_palette()

    def soft_action(self):
        soft_name = self.ui.sender().text().lower()
        py_version = self.ui.sender().property("python")

        launch_software.launch_software(soft_name, py_version)
