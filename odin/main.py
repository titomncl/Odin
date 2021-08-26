#!/usr/bin/env python3

# Odin is a project manager and software launcher

import sys

from qtpy import QtWidgets

from odin.source.controller import Controller
from odin.source.globals import Logger as log
from odin.source.ui.main_window import MainWindow
from odin.source.ui.palette import Palette

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Palette().set_app(app)

    log.info("Init Odin")

    ui_instance = Controller(MainWindow, None)

    log.info("Ready to use")

    ui_instance.show()

    sys.exit(app.exec_())
