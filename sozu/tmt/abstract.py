from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/abstract"


@dataclass
class Name:
    class Meta:
        name = "name"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/abstract"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 3,
            "max_length": 50,
            "white_space": "collapse",
        }
    )


@dataclass
class Stencil:
    class Meta:
        name = "stencil"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/abstract",
            "required": True,
            "min_length": 3,
            "max_length": 50,
            "white_space": "collapse",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/abstract",
            "required": True,
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/abstract",
            "required": True,
        }
    )
    stencil_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "length": 36,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )


@dataclass
class ModelStencilType(Stencil):
    class Meta:
        name = "modelStencilType"


@dataclass
class TemplateStencilType(Stencil):
    class Meta:
        name = "templateStencilType"


@dataclass
class ModelStencil(ModelStencilType):
    class Meta:
        namespace = "http://schema.amekoshi.com/2020/12/tmt/abstract"


@dataclass
class TemplateStencil(TemplateStencilType):
    class Meta:
        namespace = "http://schema.amekoshi.com/2020/12/tmt/abstract"
