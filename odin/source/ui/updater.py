import urllib.request
import os

from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc

from odin import __version__
from ..core.update_version import new_update
from ..core.yaml_parser import Parser


class Updater(Qw.QDialog):
    def __init__(self, is_beta, parent=None):
        Qw.QDialog.__init__(self, parent)

        self.setWindowTitle("Update Odin")

        self.p_bar = None
        self.tag = new_update(__version__, is_beta)

        self.updated = False

        if self.tag:
            if self.do_update():
                self.update_soft(self.tag)
                self.confirm_msg_box()
                self.updated = True

    def do_update(self):
        do_update_msg_box = Qw.QMessageBox(self)

        do_update_msg_box.setIcon(do_update_msg_box.Icon.Question)
        do_update_msg_box.setWindowTitle("New update")
        do_update_msg_box.setText("A new version of Odin is available.")
        do_update_msg_box.setInformativeText("Do you want to download it?")

        action_btn = do_update_msg_box.addButton("Yes", do_update_msg_box.ButtonRole.AcceptRole)
        cancel_btn = do_update_msg_box.addButton("No", do_update_msg_box.ButtonRole.RejectRole)
        later_btn = do_update_msg_box.addButton("Later", do_update_msg_box.ButtonRole.ActionRole)

        do_update_msg_box.exec()

        if do_update_msg_box.clickedButton() == action_btn:
            return True
        elif do_update_msg_box.clickedButton() == cancel_btn:
            self.update_reminder()
            return False
        elif do_update_msg_box.clickedButton() == later_btn:
            return False

    def confirm_msg_box(self):
        msg_box = Qw.QMessageBox(self)

        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.setWindowTitle("Updated")
        msg_box.setText("The new version of Odin has been downloaded here:")
        msg_box.setInformativeText(os.path.join(os.path.expanduser("~"), "Downloads"))

        action_btn = msg_box.addButton("Open", msg_box.ButtonRole.ActionRole)
        cancel_btn = msg_box.addButton("Cancel", msg_box.ButtonRole.RejectRole)

        msg_box.exec()

        if msg_box.clickedButton() == action_btn:
            os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
            self.close()
        elif msg_box.clickedButton() == cancel_btn:
            self.close()

    def update_reminder(self):
        reminder = Qw.QMessageBox(self)

        reminder.setWindowTitle("Reminder")

        reminder.setText("Do you want to me reminded?")

        action_btn = reminder.addButton("Yes", reminder.ButtonRole.ActionRole)
        cancel_btn = reminder.addButton("No", reminder.ButtonRole.RejectRole)

        reminder.exec()

        config = Parser.open("./config/config_file.yaml")

        if reminder.clickedButton() == cancel_btn:
            config.data["UPDATE"] = False
        elif reminder.clickedButton() == action_btn:
            config.data["UPDATE"] = True

        config.write()

    def progress_bar(self):
        self.p_bar = Qw.QProgressBar()
        self.p_bar.setFixedSize(200, 50)
        self.p_bar.setWindowFlag(Qc.Qt.WindowType.Tool)

        label = Qw.QLabel("Download Odin v{}...".format(self.tag))

        layout = Qw.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.p_bar)
        self.setLayout(layout)
        self.setWindowTitle("Downloading...")

        self.show()

    def handle_progress(self, block_num, block_size, total_size):
        # type: (int, int, int) -> None
        data = block_num * block_size

        if total_size > 0:
            download_percentage = data * 100 / total_size
            self.p_bar.setValue(int(download_percentage))
            Qw.QApplication.processEvents()

    def update_soft(self, last_version):
        # type: (str) -> None
        self.progress_bar()

        new_release_url = (
            "https://github.com/titomncl/Odin/releases/download/" + last_version + "/Odin_" + last_version + ".zip"
        )

        download_path = os.path.join(os.path.expanduser("~"), "Downloads", "Odin_" + last_version + ".zip")

        urllib.request.urlretrieve(new_release_url, download_path, self.handle_progress)
