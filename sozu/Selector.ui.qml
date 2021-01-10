import QtQuick 2.12
import QtScxml 5.8

Item {

    property StateMachine stateMachine: scxmlLoader.stateMachine
    property alias gridViewWidth: gridView.width
    property alias gridViewHeight: gridView.height


    StateMachineLoader {
        id: scxmlLoader
        source: "statemachine.scxml"
    }

    GridView {
        id: gridView
        opacity: 1
        anchors.fill: parent

        cellWidth: 140
        cellHeight: 140

        children: [
            Rectangle {
                color: "#1d1d1d"
                anchors.fill: parent
                z: -1
            }
        ]

        model: SelectorModel {}

        highlight: Rectangle {
            width: 120
            height: 120
            color: "#343434"
            radius: 4
            border.color: "#0d52a4"
            border.width: 8
        }

        delegate: SelectorDelegate {}
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.5;height:480;width:640}D{i:2}
}
##^##*/

