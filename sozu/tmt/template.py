from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from sozu.tmt.abstract import Stencil as AbstractStencil

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/template"


class BoundaryType(Enum):
    LINE = "line"
    RECTANGLE = "rectangle"
    ELLIPSE = "ellipse"


@dataclass
class Rule:
    """
    :ivar name:
    :ivar description:
    :ivar filter: Filter to be applied to stencil attributes. If a match
        is                             found, the threat should be
        regarded as valid for a given                             model.
    :ivar stencil:
    :ivar threat:
    """
    class Meta:
        name = "rule"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
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
    stencil: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "length": 36,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    threat: Optional[str] = field(
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
class Stencil:
    class Meta:
        name = "stencil"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Threat:
    class Meta:
        name = "threat"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 3,
            "max_length": 50,
            "white_space": "collapse",
        }
    )
    id: Optional[str] = field(
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
class Boundary:
    class Meta:
        name = "boundary"

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
    type: Optional[BoundaryType] = field(
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
            "type": "Attribute",
            "required": True,
            "length": 36,
            "white_space": "collapse",
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )


@dataclass
class Dataflow(Stencil):
    class Meta:
        name = "dataflow"


@dataclass
class Datastore(Stencil):
    class Meta:
        name = "datastore"


@dataclass
class Function(Stencil):
    class Meta:
        name = "function"


@dataclass
class Process(Stencil):
    class Meta:
        name = "process"


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
    stencils: Optional["Template.Stencils"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ruleset: Optional["Template.Ruleset"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    threats: Optional["Template.Threats"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Stencils:
        stencil: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Ruleset:
        rule: List[Rule] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Threats:
        threat: List[Threat] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )
