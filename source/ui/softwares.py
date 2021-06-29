from qtpy import QtWidgets as Qw

class Softwares(Qw.QWidget):
    def __init__(self, controller, parent=None):
        Qw.QWidget.__init__(self, parent)

        self.controller = controller

        self.set_ui()

    def set_ui(self):
        main_layout = Qw.QVBoxLayout()

        mod_set_w = self.modeling_set_widget()
        tx_w = self.texturing_widget()
        render_comp_w = self.render_comp_widget()

        soft_tab = Qw.QTabWidget()
        soft_tab.addTab(mod_set_w, "Modeling/Set")
        soft_tab.addTab(tx_w, "Texturing")
        soft_tab.addTab(render_comp_w, "Render/Comp")

        main_layout.addWidget(soft_tab)

        self.setLayout(main_layout)

    def modeling_set_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        self.maya_btn = Qw.QPushButton("Maya")
        self.zbrush = Qw.QPushButton("ZBrush")
        self.houdini_btn = Qw.QPushButton("Houdini")

        btn_layout.addWidget(self.maya_btn)
        btn_layout.addWidget(self.zbrush)
        btn_layout.addWidget(self.houdini_btn)

        widget.setLayout(btn_layout)

        return widget

    def texturing_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        self.designer_btn = Qw.QPushButton("Designer")
        self.painter_btn = Qw.QPushButton("Painter")
        self.mari_btn = Qw.QPushButton("Mari")
        self.photoshop = Qw.QPushButton("Photoshop")

        btn_layout.addWidget(self.designer_btn)
        btn_layout.addWidget(self.painter_btn)
        btn_layout.addWidget(self.mari_btn)
        btn_layout.addWidget(self.photoshop)

        widget.setLayout(btn_layout)

        return widget

    def render_comp_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        self.guerilla = Qw.QPushButton("Guerilla")
        self.nuke = Qw.QPushButton("Nuke")
        self.resolve = Qw.QPushButton("Resolve")

        btn_layout.addWidget(self.guerilla)
        btn_layout.addWidget(self.nuke)
        btn_layout.addWidget(self.resolve)

        widget.setLayout(btn_layout)

        return widget
