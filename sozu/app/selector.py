from pathlib import Path
from sozu.tmt.template import Template
from sozu.tmt.model import Model

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from PySide2.QtCore import QObject, Signal, Slot, Property


class Selector(QObject):

    def __init__(self):
        QObject.__init__(self)
    
    @Signal
    def templateOpened(self):
        pass
    
    @Signal
    def modelOpened(self):
        pass
    
    @Slot(str)
    def createTemplate(self, name: str):
        self.create_template(name)
    
    def create_template(self, name: str):

        stt = Template()
        stt.name = name
        self.templateOpened.emit(stt)
        
    new_template = Property(str, create_template, notify=templateOpened)

    @Slot(str)
    def openTemplate(self, filename: str):
        self.open_template(Path(filename))
    
    def open_template(self, filename: Path):

        parser = XmlParser(context=XmlContext())
        stt = parser.from_path(filename, Template)
        self.templateOpened.emit(stt)

    template = Property(str, open_template, notify=templateOpened)

    @Slot(str)
    def createModel(self, template: str):
        self.create_model(Path(template))
    
    def create_model(self, template: Path):

        stm = Model()
        stm.template = self.openTemplate(template)
        self.modelOpened.emit(stm)

    new_model = Property(str, create_model, notify=modelOpened)

    @Slot(str)
    def openModel(self, filename: str):
        self.open_model(Path(filename))
    
    def open_model(self, filename: Path):

        parser = XmlParser(context=XmlContext())
        stm = parser.from_path(filename, Model)
        self.modelOpened.emit(stm)

    model = Property(str, open_model, notify=modelOpened)
