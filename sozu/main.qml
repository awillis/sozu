import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: root
    title: "sozu threat modeler"
    visible: true

    minimumWidth: 640
    minimumHeight: 480

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

    GridLayout {

        id: mainGrid
        anchors.fill: parent

        Selector {
            id: templateNewSelector
            Layout.margins: 20
            Layout.column: 0
            Layout.row: 0
            blurb: qsTr("Create a new template")
        }

        Selector {
            id: templateOpenSelector
            Layout.margins: 20
            Layout.column: 1
            Layout.row: 0
            blurb: qsTr("Open an existing template")
        }

        Selector {
            id: modelNewSelector
            Layout.margins: 20
            Layout.column: 0
            Layout.row: 1
            blurb: qsTr("Create a new model from a template")
        }

        Selector {
            id: modelOpenSelector
            Layout.margins: 20
            Layout.column: 1
            Layout.row: 1
            blurb: qsTr("Open an existing model")
        }
    }

    footer: TabBar {
        id: mainBottom
        width: implicitBackgroundWidth
        height: 50
    }
}
