import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Universal 2.12

ApplicationWindow {
    id: root
    title: "sozu threat modeler"
    visible: true

    minimumWidth: 640
    minimumHeight: 480

    Universal.theme: Universal.System
    Universal.accent: Universal.White
    Universal.foreground: Universal.Olive
    Universal.background: Universal.Steel

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

            //            Action {
            //                id: darkMode
            //                text: qsTr("Dark Mode")
            //                checkable: true
            //                enabled: false
            //                onCheckedChanged:
            //            }
        }

        Menu {
            title: qsTr("&Help")
            Action {
                text: qsTr("&About")
            }
        }
    }
    SozuMain {
        id: main
    }
}
