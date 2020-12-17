from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/template"


@dataclass
class Ruleset:
    class Meta:
        name = "ruleset"
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
class Stencils:
    class Meta:
        name = "stencils"
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
class Threats:
    class Meta:
        name = "threats"
        namespace = "http://schema.amekoshi.com/2020/12/tmt/template"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
