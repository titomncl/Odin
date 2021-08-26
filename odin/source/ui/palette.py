from qtpy.QtGui import QColor, QPalette
from qtpy.QtWidgets import QApplication

WHITE = QColor(255, 255, 255)
BLACK = QColor(0, 0, 0)
GREY = QColor(127, 127, 127)
RED = QColor(230, 60, 30)
PRIMARY = QColor(38, 49, 70)
SECONDARY = QColor(70, 86, 113)
ORANGE = QColor(239, 130, 41)


class Palette(QPalette):
    def __init__(self, *args):
        QPalette.__init__(self, *args)

        self.setColor(QPalette.Window, PRIMARY)
        self.setColor(QPalette.WindowText, WHITE)
        self.setColor(QPalette.Base, SECONDARY)
        self.setColor(QPalette.Background, PRIMARY)
        self.setColor(QPalette.AlternateBase, PRIMARY)
        self.setColor(QPalette.ToolTipBase, WHITE)
        self.setColor(QPalette.ToolTipText, WHITE)
        self.setColor(QPalette.Text, WHITE)
        self.setColor(QPalette.Button, PRIMARY)
        self.setColor(QPalette.ButtonText, WHITE)
        self.setColor(QPalette.BrightText, RED)
        self.setColor(QPalette.Link, ORANGE)
        self.setColor(QPalette.Highlight, ORANGE)
        self.setColor(QPalette.HighlightedText, BLACK)

        self.setColor(QPalette.Light, PRIMARY)
        self.setColor(QPalette.Dark, SECONDARY)

    def set_app(self, app):

        if isinstance(app, QApplication):
            app.setStyle("Fusion")
            app.setPalette(self)
