# This Python file uses the following encoding: utf-8
import sys

from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from pprint import pprint as pp

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(str(Path(__file__).parent.joinpath("main.qml")))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
