from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://schema.amekoshi.com/2020/12/tmt/abstract"


class StencilType(Enum):
    PROCESS = "process"
    FUNCTION = "function"
    DATASTORE = "datastore"
    DATAFLOW = "dataflow"
    BOUNDARY = "boundary"


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
    type: Optional[StencilType] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
