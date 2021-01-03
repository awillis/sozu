import QtQuick 2.12
import QtQuick.Layouts 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.0

ApplicationWindow {
    id: root
    title: "sozu threat modeler"
    visible: true

    minimumWidth: 640
    minimumHeight: 480

    Material.theme: Material.Dark
    Material.primary: Material.BlueGrey
    Material.accent: Material.Green

    menuBar: MenuBar {
        id: mainMenu
        hoverEnabled: true

        Menu {
            title: qsTr("&File")

            Action {
                text: qsTr("&New Template")
                icon.name: "document-open"
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
                onTriggered: Qt.quit()
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
            title: qsTr("&View")
        }

        Menu {
            title: qsTr("&Help")
            Action {
                text: qsTr("&About")
            }
        }
    }
    MainView {
        id: mainView
    }
}
