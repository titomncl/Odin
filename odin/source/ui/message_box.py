from typing import NoReturn

from qtpy import QtWidgets as Qw

from .palette import PRIMARY, SECONDARY, WHITE


class MessageBox(Qw.QMessageBox):
    def __init__(self, title,  parent=None):
        # type: (str, Qw.QMainWindow) -> NoReturn
        Qw.QMessageBox.__init__(self, parent=parent)

        self.setStyle(Qw.QStyleFactory.create("Fusion"))

        self.setStyleSheet(
            "QMessageBox {"
                "background-color: rgb" + str(PRIMARY.getRgb()) + ";"
                "}"
            "QLabel {"
                "color: rgb" + str(WHITE.getRgb()) + ";"
                "}"
            "QPushButton {"
                "background-color: rgb" + str(SECONDARY.getRgb()) + ";"
                "color: rgb" + str(WHITE.getRgb()) + ";"
                "}"
        )

        self.setWindowTitle(title)

    def add_text(self, text):
      #  type: (str) -> NoReturn
        self.setText(text)

    def add_informative_text(self, text):
      #  type: (str) -> NoReturn
        self.setInformativeText(text)

    def action_button(self, text, button_role):
      #  type: (str, Qw.QMessageBox.ButtonRole) -> Qw.QAbstractButton
        return self.addButton(text, button_role)

    def abort_button(self, text, button_role=None):
        #  type: (str, Qw.QMessageBox.ButtonRole) -> NoReturn
        return self.addButton(text, button_role)

    def abort_action(self):
        # type: () -> NoReturn
        abort_msg = Qw.QMessageBox(self)

        abort_msg.setStyleSheet(
            "QMessageBox {"
                "background-color: rgb" + str(PRIMARY.getRgb()) + ";"
                "}"
            "QLabel {"
                "color: rgb" + str(WHITE.getRgb()) + ";"
                "}"
            "QPushButton {"
                "background-color: rgb" + str(SECONDARY.getRgb()) + ";"
                "color: rgb" + str(WHITE.getRgb()) + ";"
                "}"
        )

        abort_msg.setStyle(Qw.QStyleFactory.create("Fusion"))

        abort_msg.setWindowTitle("Continue?")
        abort_msg.setText("You are going to exit the program.")
        abort_msg.setInformativeText("Continue?")

        abort_msg.setStandardButtons(abort_msg.Yes | abort_msg.No)
        abort_msg.setDefaultButton(abort_msg.Yes)

        action = abort_msg.exec_()

        if action == abort_msg.Yes:
            raise SystemExit
        else:
            return True
