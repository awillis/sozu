import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: root
    title: "sozu modeler"
    visible: true

    minimumWidth: 800
    minimumHeight: 600

    Material.theme: Material.System
    Material.primary: Material.BlueGrey
    Material.accent: Material.Green

    menuBar: MenuBar {
        id: mainMenu
        anchors.left: parent.left
        anchors.right: parent.right
        activeFocusOnTab: false

        Menu {
            title: qsTr("&File")

            Action {
                text: qsTr("&New Template")
            }
            Action {
                text: qsTr("&New Model from Template")
            }
            Action {
                text: qsTr("&Open Template")
            }
            Action {
                text: qsTr("&Open Model")
            }
            Action {
                text: qsTr("&Save")
            }
            Action {
                text: qsTr("Save &As...")
            }
            MenuSeparator {}
            Action {
                id: quit
                text: qsTr("&Quit")
            }
        }
        Menu {
            title: qsTr("&Edit")
            Action {
                text: qsTr("&Cut")
            }
            Action {
                text: qsTr("&Copy")
            }
            Action {
                text: qsTr("&Paste")
            }
        }
        Menu {
            title: qsTr("&Help")
            Action {
                text: qsTr("&About")
            }
        }
    }

    header: ToolBar {
        id: mainTop
        width: implicitBackgroundWidth
        height: 50
    }

    GridView {
        id: mainGrid
        anchors.fill: parent
        anchors.margins: 30

        Selector {
            id: templateNewSelector
            anchors.fill: parent
            blurb: qsTr("Create a new template")
        }

        Selector {
            id: templateOpenSelector
            anchors.fill: parent
            blurb: qsTr("Open an existing template")
        }

        Selector {
            id: modelNewSelector
            anchors.fill: parent
            blurb: qsTr("Create a new model from a template")
        }

        Selector {
            id: modelOpenSelector
            anchors.fill: parent
            blurb: qsTr("Open an existing model")
        }
    }

    footer: TabBar {
        id: mainBottom
        width: implicitBackgroundWidth
        height: 50
    }
}
