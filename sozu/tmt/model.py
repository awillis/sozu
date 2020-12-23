from dataclasses import dataclass, field
from typing import List, Optional
from sozu.tmt.template import (
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
class ValidThreats:
    class Meta:
        name = "validThreats"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/model"

    threat: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
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

    id: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    owner: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    reviewer: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    short_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "required": True,
        }
    )
    long_description: Optional[object] = field(
        default=None,
        metadata={
            "name": "longDescription",
            "type": "Element",
            "required": True,
        }
    )
    diagrams: Optional[DiagramList] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    valid_threats: Optional[ValidThreats] = field(
        default=None,
        metadata={
            "name": "validThreats",
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
        author: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
        version: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
                "required": True,
            }
        )
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
