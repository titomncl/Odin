from qtpy import QtWidgets as Qw
from qtpy import QtGui as Qg
from qtpy import QtCore as Qc


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

        maya_ico = Qg.QIcon("./icon/maya.ico")
        zbrush_ico = Qg.QIcon("./icon/zbrush.ico")
        houdini_ico = Qg.QIcon("./icon/houdini.ico")

        self.maya_btn = Qw.QToolButton()
        self.maya_btn.setIcon(maya_ico)
        self.maya_btn.setIconSize(Qc.QSize(48, 48))
        self.maya_btn.setText("Maya")
        self.maya_btn.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.maya_btn.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.zbrush = Qw.QToolButton()
        self.zbrush.setIcon(zbrush_ico)
        self.zbrush.setIconSize(Qc.QSize(48, 48))
        self.zbrush.setText("ZBrush")
        self.zbrush.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.zbrush.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.houdini_btn = Qw.QToolButton()
        self.houdini_btn.setIcon(houdini_ico)
        self.houdini_btn.setIconSize(Qc.QSize(48, 48))
        self.houdini_btn.setText("Houdini")
        self.houdini_btn.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.houdini_btn.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        btn_layout.addWidget(self.maya_btn)
        btn_layout.addWidget(self.zbrush)
        btn_layout.addWidget(self.houdini_btn)

        widget.setLayout(btn_layout)

        return widget

    def texturing_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        designer_ico = Qg.QIcon("./icon/designer.ico")
        painter_ico = Qg.QIcon("./icon/painter.ico")
        mari_ico = Qg.QIcon("./icon/mari.ico")
        photoshop_ico = Qg.QIcon("./icon/photoshop.ico")

        self.designer_btn = Qw.QToolButton()
        self.designer_btn.setIcon(designer_ico)
        self.designer_btn.setIconSize(Qc.QSize(48, 48))
        self.designer_btn.setText("Designer")
        self.designer_btn.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.designer_btn.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.painter_btn = Qw.QToolButton()
        self.painter_btn.setIcon(painter_ico)
        self.painter_btn.setIconSize(Qc.QSize(48, 48))
        self.painter_btn.setText("Painter")
        self.painter_btn.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.painter_btn.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.mari_btn = Qw.QToolButton()
        self.mari_btn.setIcon(mari_ico)
        self.mari_btn.setIconSize(Qc.QSize(48, 48))
        self.mari_btn.setText("Mari")
        self.mari_btn.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.mari_btn.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.photoshop = Qw.QToolButton()
        self.photoshop.setIcon(photoshop_ico)
        self.photoshop.setIconSize(Qc.QSize(48, 48))
        self.photoshop.setText("Photoshop")
        self.photoshop.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.photoshop.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        btn_layout.addWidget(self.designer_btn)
        btn_layout.addWidget(self.painter_btn)
        btn_layout.addWidget(self.mari_btn)
        btn_layout.addWidget(self.photoshop)

        widget.setLayout(btn_layout)

        return widget

    def render_comp_widget(self):
        widget = Qw.QWidget()

        btn_layout = Qw.QHBoxLayout()

        guerilla_ico = Qg.QIcon("./icon/guerilla.ico")
        nuke_ico = Qg.QIcon("./icon/nuke.ico")
        resolve_ico = Qg.QIcon("./icon/resolve.ico")

        self.guerilla = Qw.QToolButton()
        self.guerilla.setIcon(guerilla_ico)
        self.guerilla.setIconSize(Qc.QSize(48, 48))
        self.guerilla.setText("Guerilla")
        self.guerilla.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.guerilla.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.nuke = Qw.QToolButton()
        self.nuke.setIcon(nuke_ico)
        self.nuke.setIconSize(Qc.QSize(48, 48))
        self.nuke.setText("Nuke")
        self.nuke.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.nuke.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        self.resolve = Qw.QToolButton()
        self.resolve.setIcon(resolve_ico)
        self.resolve.setIconSize(Qc.QSize(48, 48))
        self.resolve.setText("Resolve")
        self.resolve.setToolButtonStyle(Qc.Qt.ToolButtonTextUnderIcon)
        self.resolve.setSizePolicy(Qw.QSizePolicy.Minimum, Qw.QSizePolicy.Fixed)

        btn_layout.addWidget(self.guerilla)
        btn_layout.addWidget(self.nuke)
        btn_layout.addWidget(self.resolve)

        widget.setLayout(btn_layout)

        return widget
