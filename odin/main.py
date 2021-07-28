#!/usr/bin/env python3

# Odin is a project manager and software launcher

import sys
import requests
import os
import urllib.request

from odin.source.globals import Logger as log
from odin.source.controller import Controller
from odin.source.ui.main_window import MainWindow
from odin.source.ui.palette import Palette

from qtpy import QtWidgets, QtCore


class Updater(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.p_bar = None

    def check_update(self):
        import re
        from odin import __version__

        url = "https://github.com/titomncl/Odin/releases/latest"
        r = requests.get(url, allow_redirects=True)

        regex = re.compile(r"(?P<major>\d).(?P<minor>\d).(?P<micro>\d)")

        last_version = r.url.split("/")[-1]

        last_version_dict = regex.match(last_version).groupdict()
        actual_version_dict = regex.match(__version__).groupdict()

        if int(last_version_dict["major"]) > int(actual_version_dict["major"]):
            self.update_soft(last_version)
            return True
        elif int(last_version_dict["major"]) < int(actual_version_dict["major"]):
            return False
        else:
            if int(last_version_dict["minor"]) > int(actual_version_dict["minor"]):
                self.update_soft(last_version)
                return True
            elif int(last_version_dict["minor"]) < int(actual_version_dict["minor"]):
                return False
            else:
                if int(last_version_dict["micro"]) > int(actual_version_dict["micro"]):
                    self.update_soft(last_version)
                    return True
                else:
                    return False

    def progress_bar(self):
        self.p_bar = QtWidgets.QProgressBar()
        self.p_bar.setFixedSize(200, 50)
        self.p_bar.setWindowFlag(QtCore.Qt.WindowType.Tool)

        label = QtWidgets.QLabel("Download new Odin update...")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.p_bar)
        self.setLayout(layout)
        self.setWindowTitle("Downloading...")
        self.setWindowIcon(QIcon("./odin/resources/icons/odin.png"))

        self.show()

    def handle_progress(self, blocknum, blocksize, totalsize):
        data = blocknum * blocksize

        if totalsize > 0:
            download_percentage = data * 100 / totalsize
            self.p_bar.setValue(int(download_percentage))
            QtWidgets.QApplication.processEvents()

    def update_soft(self, last_version):
        self.progress_bar()

        new_release_url = "https://github.com/titomncl/Odin/releases/download/" \
                          + last_version + "/Odin_" + last_version + ".zip"

        download_path = os.path.join(os.path.expanduser("~"), "Downloads", 'Odin_' + last_version + '.zip')

        urllib.request.urlretrieve(new_release_url, download_path, self.handle_progress)


def main():
    log.info("Init Odin")

    ui_instance = Controller(MainWindow, None)

    log.info("Ready to use")

    ui_instance.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Palette().set_app(app)

    updated = Updater().check_update()

    if updated:
        from qtpy.QtGui import QIcon

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowIcon(QIcon("./odin/resources/icons/odin.png"))

        msg_box.setIcon(msg_box.Information)
        msg_box.setWindowTitle("Updated")
        msg_box.setText("A new version of Odin has been downloaded here:")
        msg_box.setInformativeText(os.path.join(os.path.expanduser("~"), "Downloads"))

        action_btn = msg_box.addButton("Open", msg_box.ButtonRole.ActionRole)
        cancel_btn = msg_box.addButton("Cancel", msg_box.ButtonRole.RejectRole)

        msg_box.exec_()

        if msg_box.clickedButton() == action_btn:
            os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
            raise SystemExit
        elif msg_box.clickedButton() == cancel_btn:
            raise SystemExit

    else:
        main()

    sys.exit(app.exec_())
