import sys

from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtGui import Qt, QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def main():

    qml = str(Path(__file__).parent.joinpath('main.qml'))
    app = QGuiApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)

    # QApplication must be parent of QQmlApplicationEngine to prevent segfault on app exit
    engine = QQmlApplicationEngine(parent=app)
    context = engine.rootContext()
    # context.setContextProperty()

    engine.load(QUrl.fromLocalFile(qml))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
