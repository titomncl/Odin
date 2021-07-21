from qtpy import QtWidgets as Qw
from qtpy import QtGui as Qg
from qtpy import QtCore as Qc


class Software(Qw.QWidget):
    def __init__(self, parent=None):
        Qw.QWidget.__init__(self, parent)

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

    def soft_button(self, text, icon, py_version):
        btn = Qw.QToolButton()
        btn.setIcon(icon)
        btn.setIconSize(Qc.QSize(48, 48))
        btn.setText(text)
        btn.setToolButtonStyle(Qc.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        btn.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)
        btn.setProperty("python", py_version)

        return btn

    def modeling_set_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        maya_ico = Qg.QIcon("./odin/resources/maya.ico")
        zbrush_ico = Qg.QIcon("./odin/resources/zbrush.ico")
        houdini_ico = Qg.QIcon("./odin/resources/houdini.ico")

        self.maya = self.soft_button("Maya", maya_ico, "27")
        self.zbrush = self.soft_button("ZBrush", zbrush_ico, "27")
        self.houdini = self.soft_button("Houdini", houdini_ico, "27")

        btn_layout.addWidget(self.maya)
        btn_layout.addWidget(self.zbrush)
        btn_layout.addWidget(self.houdini)

        widget.setLayout(btn_layout)

        return widget

    def texturing_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        designer_ico = Qg.QIcon("./odin/resources/designer.ico")
        painter_ico = Qg.QIcon("./odin/resources/painter.ico")
        mari_ico = Qg.QIcon("./odin/resources/mari.ico")
        photoshop_ico = Qg.QIcon("./odin/resources/photoshop.ico")

        self.designer = self.soft_button("Designer", designer_ico, "38")
        self.painter = self.soft_button("Painter", painter_ico, "38")
        self.mari = self.soft_button("Mari", mari_ico, "27")
        self.photoshop = self.soft_button("Photoshop", photoshop_ico, "27")

        btn_layout.addWidget(self.designer)
        btn_layout.addWidget(self.painter)
        btn_layout.addWidget(self.mari)
        btn_layout.addWidget(self.photoshop)

        widget.setLayout(btn_layout)

        return widget

    def render_comp_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        guerilla_ico = Qg.QIcon("./odin/resources/guerilla.ico")
        nuke_ico = Qg.QIcon("./odin/resources/nuke.ico")
        resolve_ico = Qg.QIcon("./odin/resources/resolve.ico")

        self.guerilla = self.soft_button("Guerilla", guerilla_ico, "27")
        self.nuke = self.soft_button("Nuke", nuke_ico, "27")
        self.resolve = self.soft_button("Resolve", resolve_ico, "27")

        btn_layout.addWidget(self.guerilla)
        btn_layout.addWidget(self.nuke)
        btn_layout.addWidget(self.resolve)

        widget.setLayout(btn_layout)

        return widget
