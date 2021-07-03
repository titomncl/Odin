import re
import os

from Odin.source.core import project
from Odin.source.core import config_parser
from Odin.source.core import assets, sets, fx

from Odin.source.common import concat


class Controller(object):

    def __init__(self, ui, parent=None):

        self.ui = ui(self, parent)

        self.word_pattern = re.compile(r"^([A-Z0-9]+)$")


    def show(self):
        self.ui.show()

    def create_project(self):
        project_name = self.ui.create_project_dialog.text_field.text().upper()

        if project_name not in self.projects and project_name != "" and len(project_name) < 5:
            self.ui.create_project_dialog.green_palette()
            project.create_project(self.root, project_name)
        else:
            self.ui.create_project_dialog.red_palette()

    @property
    def projects(self):
        return project.find_project(self.root)

    @property
    def root(self):
        return config_parser.get_value("ROOT_PATH")

    @property
    def project_name(self):
        return self.ui.create_or_set.prod_cbox.currentText()

    def set_root(self, value):
        new_value = value
        if value[-1] == "/":
            new_value = value.split("/")[0]
        config_parser.change_content("ROOT_PATH", new_value)

    def set_var_env(self):
        os.environ["ROOT_PATH"] = self.root
        os.environ["PFE_ENV"] = concat(self.root, self.project_name, separator="/")

        dev_env = "E:/DEV"
        venv = "/venv/Lib/site-packages"

        if os.path.isdir("E:/DEV/Odin"):
            os.environ["DEV_ENV"] = dev_env
            os.environ["venv"] = dev_env + venv
        elif os.path.isdir(concat(self.root, self.project_name, "DEV/main", separator="/'")):
            dev_env = concat(self.root, self.project_name, "DEV/main", separator="/'")
            os.environ["DEV_ENV"] = dev_env
            os.environ["venv"] = dev_env + venv



    def chara_action(self):
        chara_name = self.ui.manage_prj.lib_widget.create_chara_dialog.text_field.text().upper()

        chara_is_correct = self.word_pattern.match(chara_name)

        if chara_is_correct:
            self.ui.manage_prj.lib_widget.create_chara_dialog.green_palette()
            assets.create_asset(concat(self.root, self.project_name, separator="/"), chara_name, "CHARA")
        else:
            self.ui.manage_prj.lib_widget.create_chara_dialog.red_palette()

    def props_action(self):
        props_name = self.ui.manage_prj.lib_widget.create_props_dialog.text_field.text().upper()

        props_is_correct = self.word_pattern.match(props_name)

        if props_is_correct:
            self.ui.manage_prj.lib_widget.create_props_dialog.green_palette()
            assets.create_asset(concat(self.root, self.project_name, separator="/"), props_name, "PROPS")
        else:
            self.ui.manage_prj.lib_widget.create_props_dialog.red_palette()

    def set_action(self):
        set_name = self.ui.manage_prj.lib_widget.create_set_dialog.text_field.text().upper()

        set_is_correct = self.word_pattern.match(set_name)

        if set_is_correct:
            self.ui.manage_prj.lib_widget.create_set_dialog.green_palette()
            sets.create_set(concat(self.root, self.project_name, separator="/"), set_name)
        else:
            self.ui.manage_prj.lib_widget.create_set_dialog.red_palette()

    def fx_action(self):
        fx_name = self.ui.manage_prj.lib_widget.create_fx_dialog.text_field.text().upper()

        fx_is_correct = self.word_pattern.match(fx_name)

        if fx_is_correct:
            self.ui.manage_prj.lib_widget.create_fx_dialog.green_palette()
            fx.create_fx(concat(self.root, self.project_name, separator="/"), fx_name)
        else:
            self.ui.manage_prj.lib_widget.create_fx_dialog.red_palette()
