import sys

from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtGui import Qt, QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def main():

    appdir = Path(__file__).parent
    qml = str(appdir.joinpath('main.qml'))
    app = QGuiApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)

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
