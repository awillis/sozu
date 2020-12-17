from dataclasses import dataclass, field
from typing import Optional
from sozu.data.template import (
    Ruleset,
    Stencils,
    Threats,
)

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/model"


@dataclass
class Diagram:
    class Meta:
        name = "diagram"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/model"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Diagrams:
    class Meta:
        name = "diagrams"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/model"

    diagram: Optional[Diagram] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Model:
    class Meta:
        name = "model"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/model"

    diagrams: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    template: Optional["Model.Template"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Template:
        stencils: Optional[Stencils] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        ruleset: Optional[Ruleset] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        threats: Optional[Threats] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
