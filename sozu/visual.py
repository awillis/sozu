import sys
import qml_rc

from pathlib import Path
from PySide6.QtCore import QUrl, QResource
from PySide6.QtGui import Qt, QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from pprint import pprint as pp


def main():

    qml = str(Path(__file__).parent.joinpath('main.qml'))
    app = QGuiApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)

    # per matplotlib, setting QApplication as parent prevents segfault on app exit
    engine = QQmlApplicationEngine(parent=app)
    url = QUrl.fromLocalFile(qml)
    engine.load(url)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
