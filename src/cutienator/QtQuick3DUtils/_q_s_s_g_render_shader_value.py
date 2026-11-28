"""
QSSGRenderShaderValue stands for the namespace 'QSSGRenderShaderValue' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QSSGRenderShaderValue:
  """
  The namespace 'QSSGRenderShaderValue' of Qt, which holds no objects. It
  holds the 1 enums Qt writes in it, each under its name, and the 0 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class Type(CuteNum):
    """
    The enum 'QSSGRenderShaderValue::Type' of Qt, with the 28 names Qt gives
    in it.
    """

    Unknown = Kee[int](0)
    Integer = Kee[int](1)
    IntegerVec2 = Kee[int](2)
    IntegerVec3 = Kee[int](3)
    IntegerVec4 = Kee[int](4)
    Boolean = Kee[int](5)
    BooleanVec2 = Kee[int](6)
    BooleanVec3 = Kee[int](7)
    BooleanVec4 = Kee[int](8)
    Float = Kee[int](9)
    Vec2 = Kee[int](10)
    Vec3 = Kee[int](11)
    Vec4 = Kee[int](12)
    UnsignedInteger = Kee[int](13)
    UnsignedIntegerVec2 = Kee[int](14)
    UnsignedIntegerVec3 = Kee[int](15)
    UnsignedIntegerVec4 = Kee[int](16)
    Matrix3x3 = Kee[int](17)
    Matrix4x4 = Kee[int](18)
    Rgba = Kee[int](19)
    Size = Kee[int](20)
    SizeF = Kee[int](21)
    Point = Kee[int](22)
    PointF = Kee[int](23)
    Rect = Kee[int](24)
    RectF = Kee[int](25)
    Quaternion = Kee[int](26)
    Texture = Kee[int](27)
