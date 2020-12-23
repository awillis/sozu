from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from sozu.tmt.abstract import (
    TemplateStencil,
    TemplateStencilType,
)

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Rule:
    """
    :ivar name:
    :ivar description:
    :ivar filter: Filter to be applied to stencil attributes. If a match
        is                             found, the threat should be
        regarded as valid for a given                             model.
    :ivar stencil_id:
    :ivar threat_id:
    """
    class Meta:
        name = "rule"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

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
            "required": True,
        }
    )
    filter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
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
    threat_id: Optional[str] = field(
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
class Threat:
    class Meta:
        name = "threat"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

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
    threat_id: Optional[str] = field(
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
class Boundary(TemplateStencilType):
    class Meta:
        name = "boundary"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    type: Optional["Boundary.Type"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    class Type(Enum):
        LINE = "line"
        RECTANGLE = "rectangle"
        ELLIPSE = "ellipse"


@dataclass
class Dataflow(TemplateStencilType):
    class Meta:
        name = "dataflow"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Datastore(TemplateStencilType):
    class Meta:
        name = "datastore"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Function(TemplateStencilType):
    class Meta:
        name = "function"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Process(TemplateStencilType):
    class Meta:
        name = "process"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"


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


@dataclass
class StencilList:
    class Meta:
        name = "stencilList"

    boundary: List[Boundary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    dataflow: List[Dataflow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    datastore: List[Datastore] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    process: List[Process] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/template",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    template_stencil: List[TemplateStencil] = field(
        default_factory=list,
        metadata={
            "name": "TemplateStencil",
            "type": "Element",
            "namespace": "http://schema.amekoshi.com/2020/12/tmt/abstract",
            "min_occurs": 1,
            "sequential": True,
        }
    )


@dataclass
class Template:
    class Meta:
        name = "template"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    stencils: Optional[StencilList] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ruleset: Optional[RuleList] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    threats: Optional[ThreatList] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
