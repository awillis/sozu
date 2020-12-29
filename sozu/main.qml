import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import dev.sozu 1.0

ApplicationWindow {
    id: root
    title: qsTr("sozu modeler")

    width: 800
    height: 600
    visible: true

    Material.theme: Material.Dark
    Material.primary: Material.BlueGrey
    Material.accent: Material.Green

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")

            Action { text: qsTr("&New Template") }
            Action { text: qsTr("&New Model from Template") }
            Action { text: qsTr("&Open Template") }
            Action { text: qsTr("&Open Model") }
            Action { text: qsTr("&Save") }
            Action { text: qsTr("Save &As...") }
            MenuSeparator { }
            Action { text: qsTr("&Quit") }
        }
        Menu {
            title: qsTr("&Edit")
            Action { text: qsTr("Cu&t") }
            Action { text: qsTr("&Copy") }
            Action { text: qsTr("&Paste") }
        }
        Menu {
            title: qsTr("&Help")
            Action { text: qsTr("&About") }
        }
    }

    header: ToolBar {
        id: toolBar
        width: implicitBackgroundWidth
        height: implicitBackgroundHeight
    }

    footer: TabBar {
        id: tabBar
        width: implicitBackgroundWidth
        height: implicitBackgroundHeight
    }

    StackView {
        id: stackView
        anchors.fill: parent
    }
}
