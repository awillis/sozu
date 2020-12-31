import QtQuick 2.12
import QtQuick.Layouts 2.12
import QtQuick.Controls.Material 2.12

Item {
    id: selector
    width: 200
    height: 200
    focus: true
    activeFocusOnTab: true

    property string blurb: description.text

    Rectangle {
        id: selectRect

        Text {
            id: description
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 20
            anchors.rightMargin: 20

            text: selector.blurb
            font.pixelSize: 12
        }
    }
}
