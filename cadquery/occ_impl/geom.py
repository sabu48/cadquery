"""Geometry utilities for CadQuery.

This module provides core geometric primitives and transformations used
throughout the CadQuery modeling pipeline, wrapping OCC (Open CASCADE)
geometry objects with a more Pythonic interface.
"""

import math
from typing import Tuple, Union, Optional, Sequence

from OCC.Core.gp import (
    gp_Vec,
    gp_Pnt,
    gp_Dir,
    gp_Ax1,
    gp_Ax2,
    gp_Ax3,
    gp_Trsf,
    gp_GTrsf,
    gp_XYZ,
)
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform

# Type alias for a 3-tuple of floats
VectorLike = Union["Vector", Tuple[float, float, float], Sequence[float]]


class Vector:
    """A 3D vector with common geometric operations.

    Wraps OCC's gp_Vec and gp_Pnt, providing a unified interface for
    both direction vectors and point coordinates.

    Examples::

        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        v3 = v1 + v2
        print(v3)  # Vector(1.0, 1.0, 0.0)
    """

    def __init__(self, *args):
        if len(args) == 3:
            x, y, z = float(args[0]), float(args[1]), float(args[2])
        elif len(args) == 1:
            if isinstance(args[0], Vector):
                x, y, z = args[0].x, args[0].y, args[0].z
            elif isinstance(args[0], gp_Vec):
                x, y, z = args[0].X(), args[0].Y(), args[0].Z()
            elif isinstance(args[0], gp_Pnt):
                x, y, z = args[0].X(), args[0].Y(), args[0].Z()
            elif isinstance(args[0], gp_Dir):
                x, y, z = args[0].X(), args[0].Y(), args[0].Z()
            elif hasattr(args[0], '__iter__'):
                coords = list(args[0])
                if len(coords) == 2:
                    x, y, z = float(coords[0]), float(coords[1]), 0.0
                elif len(coords) == 3:
                    x, y, z = float(coords[0]), float(coords[1]), float(coords[2])
                else:
                    raise ValueError(f"Expected 2 or 3 coordinates, got {len(coords)}")
            else:
                raise TypeError(f"Cannot construct Vector from {type(args[0])}")
        elif len(args) == 2:
            x, y, z = float(args[0]), float(args[1]), 0.0
        else:
            raise TypeError(f"Vector() takes 1, 2, or 3 arguments ({len(args)} given)")

        self._vec = gp_Vec(x, y, z)

    @property
    def x(self) -> float:
        return self._vec.X()

    @property
    def y(self) -> float:
        return self._vec.Y()

    @property
    def z(self) -> float:
        return self._vec.Z()

    def to_pnt(self) -> gp_Pnt:
        """Convert to an OCC gp_Pnt."""
        return gp_Pnt(self.x, self.y, self.z)

    def to_dir(self) -> gp_Dir:
        """Convert to an OCC gp_Dir (unit direction)."""
        return gp_Dir(self._vec)

    def to_vec(self) -> gp_Vec:
        """Return the underlying OCC gp_Vec."""
        return self._vec

    def length(self) -> float:
        """Return the Euclidean length of this vector."""
        return self._vec.Magnitude()

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        mag = self.length()
        if mag < 1e-10:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    def dot(self, other: "Vector") -> float:
        """Compute the dot product with another vector."""
        return self._vec.Dot(other._vec)

    def cross(self, other: "Vector") -> "Vector":
        """Compute the cross product with another vector."""
        return Vector(self._vec.Crossed(other._vec))

    def angle_between(self, other: "Vector") -> float:
        """Return the angle in degrees between this and another vector."""
        return math.degrees(self._vec.Angle(other._vec))

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self._vec.Added(other._vec))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self._vec.Subtracted(other._vec))

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self._vec.Multiplied(scalar))

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self._vec.IsEqual(other._vec, 1e-10, 1e-10)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
