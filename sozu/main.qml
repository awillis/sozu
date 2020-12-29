import QtQuick 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    id: root
    width: 800
    height: 600
    visible: true

    menuBar: MenuBar {}

    header: ToolBar {}

    footer: TabBar {}

    StackView {
        anchors.fill: parent
    }
}
