from NodeGraphQt import BaseNode, NodeBaseWidget
from Qt import QtWidgets


class DropdownMenuNode(BaseNode):
    """
    An example node with a embedded added QCombobox menu.
    """

    # unique node identifier.
    __identifier__ = 'nodes.widget'

    # initial default node name.
    NODE_NAME = 'menu'

    def __init__(self):
        super(DropdownMenuNode, self).__init__()

        # create input & output ports
        self.add_input('in 1')
        self.add_output('out 1')
        self.add_output('out 2')

        # create the QComboBox menu.
        items = ['item 1', 'item 2', 'item 3']
        self.add_combo_menu('my_menu', 'Menu Test', items=items)


class TextInputNode(BaseNode):
    """
    An example of a node with a embedded QLineEdit.
    """

    # unique node identifier.
    __identifier__ = 'nodes.widget'

    # initial default node name.
    NODE_NAME = 'text'

    def __init__(self):
        super(TextInputNode, self).__init__()

        # create input & output ports
        self.add_input('in')
        self.add_output('out')

        # create QLineEdit text input widget.
        self.add_text_input('my_input', 'Text Input', tab='widgets')


class CheckboxNode(BaseNode):
    """
    An example of a node with 2 embedded QCheckBox widgets.
    """

    # set a unique node identifier.
    __identifier__ = 'nodes.widget'

    # set the initial default node name.
    NODE_NAME = 'checkbox'

    def __init__(self):
        super(CheckboxNode, self).__init__()

        # create the checkboxes.
        self.add_checkbox('cb_1', '', 'Checkbox 1', True)
        self.add_checkbox('cb_2', '', 'Checkbox 2', False)

        # create input and output port.
        self.add_input('in', color=(200, 100, 0))
        self.add_output('out', color=(0, 100, 200))


class NodeWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(NodeWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QPushButton('Test'))
        layout.addWidget(QtWidgets.QComboBox())
        layout.addWidget(QtWidgets.QLabel('Node Label'))
        layout.setContentsMargins(0, 0, 0, 0)


class NodeWidgetWrapper(NodeBaseWidget):

    def __init__(self, parent=None):
        super(NodeWidgetWrapper, self).__init__(parent)
        self.set_custom_widget(NodeWidget())

    def get_value(self):
        return

    def set_value(self, text):
        return


class CustomWidgetNode(BaseNode):

    # unique node identifier.
    __identifier__ = 'nodes.widget'

    # initial default node name.
    NODE_NAME = 'custom widget'

    def __init__(self):
        super(CustomWidgetNode, self).__init__()
        self.add_custom_widget(NodeWidgetWrapper(self.view), tab="Custom")
        # create input and output port.
        self.add_input('in')
        # self.add_output('out')
