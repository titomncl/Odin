import sys

from Odin.source.controller.controller import Controller
from Odin.source.ui.main_window import MainWindow as UI
from Odin.source.ui.palette import Palette

from qtpy import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    UI_INSTANCE = Controller(UI, None)
    Palette().set_app(app)

    UI_INSTANCE.show()
    sys.exit(app.exec_())
