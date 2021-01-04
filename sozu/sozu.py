import sys

from pathlib import Path
from PySide6.QtCore import QUrl, QResource
from PySide6.QtGui import Qt, QGuiApplication, QIconEngine
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle


def main():

    appdir = Path(__file__).parent
    qml = str(appdir.joinpath('sozu.qml'))

    # setup app with style
    app = QGuiApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    QQuickStyle.setFallbackStyle("Basic")
    QQuickStyle.setStyle("Universal")

    # per matplotlib, setting QApplication as parent prevents segfault on app exit
    engine = QQmlApplicationEngine(parent=app)
    engine.addImportPath(str(appdir.joinpath('qml')))
    url = QUrl.fromLocalFile(qml)
    engine.load(url)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
