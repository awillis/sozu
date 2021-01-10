import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Universal 2.12
import QtQuick.Window 2.14

Window {
    id: root
    width: 203
    height: 87
    title: "sozu threat modeler"
    visible: true

    minimumWidth: 350
    minimumHeight: 375
    Universal.theme: Universal.System
    Universal.accent: Universal.White
    Universal.foreground: Universal.Olive
    Universal.background: Universal.Steel

    Selector {
        id: main
        anchors.fill: parent
        gridViewHeight: implicitHeight
        gridViewWidth: implicitWidth
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/

