import sys

from pathlib import Path
from PySide2.QtCore import QUrl, QResource
from PySide2.QtGui import Qt, QGuiApplication, QIconEngine
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtQuickControls2 import QQuickStyle

from sozu.app.selector import Selector

def main():

    appdir = Path(__file__).parent
    qml = str(appdir.joinpath('main.qml'))

    # setup app with style
    app = QGuiApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    QQuickStyle.setFallbackStyle("Basic")
    QQuickStyle.setStyle("Universal")

    # setup engine
    engine = QQmlApplicationEngine(parent=app)
    engine.addImportPath(str(appdir.joinpath('qml')))
    qmlRegisterType(Selector, 'selector', 1, 0, 'Selector')

    # load qml
    url = QUrl.fromLocalFile(qml)
    engine.load(url)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
