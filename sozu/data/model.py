from dataclasses import dataclass, field
from typing import Optional
from sozu.data.template import (
    RuleList,
    StencilList,
    ThreatList,
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
class DiagramList:
    class Meta:
        name = "diagramList"

    diagram: Optional[Diagram] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/model",
            "required": True,
        }
    )


@dataclass
class Model:
    class Meta:
        name = "model"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/model"

    diagrams: Optional[DiagramList] = field(
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
        stencils: Optional[StencilList] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        ruleset: Optional[RuleList] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        threats: Optional[ThreatList] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
