from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Rule:
    class Meta:
        name = "rule"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Stencil:
    class Meta:
        name = "stencil"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Threat:
    class Meta:
        name = "threat"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class RuleList:
    class Meta:
        name = "ruleList"

    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
        }
    )


@dataclass
class StencilList:
    class Meta:
        name = "stencilList"

    stencil: List[Stencil] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
        }
    )


@dataclass
class ThreatList:
    class Meta:
        name = "threatList"

    threat: List[Threat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
        }
    )
