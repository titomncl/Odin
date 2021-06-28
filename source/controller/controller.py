

class Controller(object):

    def __init__(self, ui, parent=None):

        self.ui = ui(self, parent)

    def show(self):
        self.ui.show()
