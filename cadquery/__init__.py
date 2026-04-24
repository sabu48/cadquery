""" 
CadQuery - A parametric 3D CAD scripting framework built on top of OCCT.

CadQuery is a Python module for building 3D CAD models. It is similar to
OpenSCAD, but uses Python as the scripting language. It is built on top of
the Open CASCADE Technology (OCCT) geometric kernel via the pythonOCC bindings.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("front").box(2, 2, 0.5)

Note: This is a personal fork. See https://github.com/CadQuery/cadquery for
the upstream project.

Personal notes:
    - Studying the assembly and constraint solver internals
    - Experimenting with custom selectors for project-specific workflows
    - Added cq_version() helper for quick version checks in scripts
"""

from .occ_impl.geom import Vector, Matrix, Plane, BoundBox
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
    CompSolid,
)
from .occ_impl.exporters import exporters
from .occ_impl.assembly import (
    Assembly,
    Constraint,
    ConstraintKind,
)

from .cq import CQ, Workplane
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    CenterNthSelector,
    RadiusNthSelector,
    LengthNthSelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .sketch import Sketch
from . import cq_types as types

# Expose the Location type for assembly positioning
from .occ_impl.geom import Location

__version__ = "2.4.0"
__author__ = "CadQuery Authors"
__license__ = "Apache Public License 2.0"

# Personal fork metadata
__fork_author__ = "personal"
__fork_notes__ = "Personal learning fork; upstream at CadQuery/cadquery"


def cq_version():
    """Return a short version string. Handy for quick sanity checks in scripts.

    Example::

        import cadquery as cq
        print(cq.cq_version())  # 'CadQuery 2.4.0 (personal fork)'
    """
    return f"CadQuery {__version__} (personal fork)"


__all__ = [
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "BoundBox",
    "Location",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "CompSolid",
    # Core workplane
    "CQ",
    "Workplane",
    # Sketch
    "Sketch",
    # Assembly
    "Assembly",
    "Constraint",
    "ConstraintKind",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "CenterNthSelector",
    "RadiusNthSelector",
    "LengthNthSelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Exporters
    "exporters",
    # Types
    "types",
    # Utilities
    "cq_version",
]
