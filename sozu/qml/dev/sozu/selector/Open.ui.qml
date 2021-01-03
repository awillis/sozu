import QtQuick 2.12
import QtQuick.Layouts 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Universal 2.12

Item {
    id: selector
    focus: true
    activeFocusOnTab: true

    property string blurb: selectDesc.text

    Rectangle {
        id: selectRect
        border.width: 5
        radius: 10

        Text {
            id: selectTitle
            text: selector.blurb
            font.pixelSize: 12
            wrapMode: Text.Wrap
        }

        Text {
            id: selectDesc
            text: selector.blurb
            font.pixelSize: 12
            wrapMode: Text.Wrap
        }
    }

    ComboBox {
        id: comboBox
        x: 31
        y: 102
    }

    ScrollView {
        id: scrollView
        x: 28
        y: 24
        width: 126
        height: 64
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.66;height:480;width:640}
}
##^##*/

