import re
import os

from Odin.source.core import project, software
from Odin.source.core import config_parser
from Odin.source.core import assets, sets, fx, sequence, shot

from Odin.source.common import concat


class Controller(object):

    def __init__(self, ui, parent=None):

        self.ui = ui(self, parent)

        self.word_pattern = re.compile(r"^([A-Z0-9_]+)$")

        self.env = "main"

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
    def recent_project(self):
        return config_parser.get_value("RECENT_PROJECT")

    @property
    def project_name(self):
        return self.ui.create_or_set.prod_cbox.currentText()

    @property
    def sequences(self):
        return sequence.find_sequences(self.root, self.project_name)

    @staticmethod
    def set_root(value):
        new_value = value
        if value[-1] == "/":
            new_value = value.split("/")[0]
        config_parser.change_content("ROOT_PATH", new_value)

    @staticmethod
    def set_recent_project(value):
        config_parser.change_content("RECENT_PROJECT", value)

    def set_var_env(self):

        self.set_recent_project(self.project_name)

        os.environ["ROOT_PATH"] = self.root
        os.environ["PFE_ENV"] = concat(self.root, self.project_name, separator="/")

        venv = "/venv"

        env_path = concat(self.root, self.project_name, "DEV", self.env, separator="/")

        if os.path.isdir(env_path):
            os.environ["DEV_ENV"] = env_path
            os.environ["venv"] = env_path + venv

    def chara_action(self):
        chara_name = self.ui.manage_prj.lib_widget.create_chara_dialog.text_field.text().upper()

        chara_is_correct = self.word_pattern.match(chara_name)

        if chara_is_correct:
            self.ui.manage_prj.lib_widget.create_chara_dialog.green_palette()
            assets.create_asset(self.root, self.project_name, chara_name, "CHARA")
        else:
            self.ui.manage_prj.lib_widget.create_chara_dialog.red_palette()

    def props_action(self):
        props_name = self.ui.manage_prj.lib_widget.create_props_dialog.text_field.text().upper()

        props_is_correct = self.word_pattern.match(props_name)

        if props_is_correct:
            self.ui.manage_prj.lib_widget.create_props_dialog.green_palette()
            assets.create_asset(self.root, self.project_name, props_name, "PROPS")
        else:
            self.ui.manage_prj.lib_widget.create_props_dialog.red_palette()

    def set_action(self):
        set_name = self.ui.manage_prj.lib_widget.create_set_dialog.text_field.text().upper()

        set_is_correct = self.word_pattern.match(set_name)

        if set_is_correct:
            self.ui.manage_prj.lib_widget.create_set_dialog.green_palette()
            sets.create_set(self.root, self.project_name, set_name)
        else:
            self.ui.manage_prj.lib_widget.create_set_dialog.red_palette()

    def fx_action(self):
        fx_name = self.ui.manage_prj.lib_widget.create_fx_dialog.text_field.text().upper()

        fx_is_correct = self.word_pattern.match(fx_name)

        if fx_is_correct:
            self.ui.manage_prj.lib_widget.create_fx_dialog.green_palette()
            fx.create_fx(self.root, self.project_name, fx_name)
        else:
            self.ui.manage_prj.lib_widget.create_fx_dialog.red_palette()

    def seq_action(self):
        seq_name = self.ui.manage_prj.film_widget.create_seq_dialog.text_field.text().upper()
        seq_pattern = re.compile(r"S(\d{3})")

        seq_is_correct = seq_pattern.match(seq_name)

        if seq_is_correct:
            self.ui.manage_prj.film_widget.create_seq_dialog.green_palette()
            sequence.create_sequences(self.root, self.project_name, seq_name)

            self.ui.manage_prj.film_widget.create_shot_dialog.cbox.clear()
            self.ui.manage_prj.film_widget.create_shot_dialog.cbox.addItems(self.sequences)
        else:
            self.ui.manage_prj.film_widget.create_seq_dialog.red_palette()

    def shot_action(self):
        shot_name = self.ui.manage_prj.film_widget.create_shot_dialog.text_field.text().upper()

        shot_pattern = re.compile(r"P(\d{3})")

        shot_is_correct = shot_pattern.match(shot_name)

        if shot_is_correct:
            self.ui.manage_prj.film_widget.create_shot_dialog.green_palette()

            seq_name = self.ui.manage_prj.film_widget.create_shot_dialog.cbox.currentText()

            shot.create_shot(self.root, self.project_name, seq_name, shot_name)
        else:
            self.ui.manage_prj.film_widget.create_shot_dialog.red_palette()

    def soft_action(self):
        soft_name = self.ui.sender().text().lower()
        py_version = self.ui.sender().property("python")
        cwd = self.ui.sender().property("cwd")

        software.launch_software(soft_name, py_version, cwd)
