import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Universal 2.12
import "qml/dev/sozu/editor" as Editor

Item {

    id: mainItem
    focus: true
    activeFocusOnTab: true

    GridLayout {

        id: mainGrid
        anchors.fill: parent
        rows: 2
        columns: 2

        Editor.Create {
            id: templateCreateSelector
            Layout.preferredWidth: 200
            Layout.preferredHeight: 150
            Layout.margins: 20
            Layout.column: 0
            Layout.row: 0
            blurb: qsTr("Create a new template")
        }

        Editor.Open {
            id: templateOpenSelector
            Layout.preferredWidth: 200
            Layout.preferredHeight: 150
            Layout.margins: 20
            Layout.column: 1
            Layout.row: 0
            blurb: qsTr("Open an existing template")
        }

        Editor.Create {
            id: modelCreateSelector
            Layout.preferredWidth: 200
            Layout.preferredHeight: 150
            Layout.margins: 20
            Layout.column: 0
            Layout.row: 1
            blurb: qsTr("Create a new model from a template")
        }

        Editor.Open {
            id: modelOpenSelector
            Layout.preferredWidth: 200
            Layout.preferredHeight: 150
            Layout.margins: 20
            Layout.column: 1
            Layout.row: 1
            blurb: qsTr("Open an existing model")
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.33;height:480;width:640}
}
##^##*/

