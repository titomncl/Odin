#!/usr/bin/env python3

# Odin is a project manager and software launcher

import sys

from Odin.source.globals import Logger as log
from Odin.source.controller.controller import Controller
from Odin.source.ui.main_window import MainWindow
from Odin.source.ui.palette import Palette

from qtpy import QtWidgets

__version__ = '0.1.4'
__author__ = 'Thomas Nicole'

if __name__ == '__main__':
    log.info("Init Odin")

    app = QtWidgets.QApplication(sys.argv)

    UI_INSTANCE = Controller(MainWindow, None)
    Palette().set_app(app)

    log.info("Ready to use")

    UI_INSTANCE.show()
    sys.exit(app.exec_())
