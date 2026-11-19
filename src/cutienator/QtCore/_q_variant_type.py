"""
Type stands for the enum 'QVariant::Type' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Type(CuteNum):
  """
  The enum 'QVariant::Type' of Qt, with the 60 names Qt gives in it.
  """

  Invalid = Kee[int](0)
  Bool = Kee[int](1)
  Int = Kee[int](2)
  UInt = Kee[int](3)
  LongLong = Kee[int](4)
  ULongLong = Kee[int](5)
  Double = Kee[int](6)
  Char = Kee[int](7)
  Map = Kee[int](8)
  List = Kee[int](9)
  String = Kee[int](10)
  StringList = Kee[int](11)
  ByteArray = Kee[int](12)
  BitArray = Kee[int](13)
  Date = Kee[int](14)
  Time = Kee[int](15)
  DateTime = Kee[int](16)
  Url = Kee[int](17)
  Locale = Kee[int](18)
  Rect = Kee[int](19)
  RectF = Kee[int](20)
  Size = Kee[int](21)
  SizeF = Kee[int](22)
  Line = Kee[int](23)
  LineF = Kee[int](24)
  Point = Kee[int](25)
  PointF = Kee[int](26)
  RegularExpression = Kee[int](44)
  Hash = Kee[int](28)
  EasingCurve = Kee[int](29)
  Uuid = Kee[int](30)
  ModelIndex = Kee[int](42)
  PersistentModelIndex = Kee[int](50)
  LastCoreType = Kee[int](63)
  Font = Kee[int](4096)
  Pixmap = Kee[int](4097)
  Brush = Kee[int](4098)
  Color = Kee[int](4099)
  Palette = Kee[int](4100)
  Image = Kee[int](4102)
  Polygon = Kee[int](4103)
  Region = Kee[int](4104)
  Bitmap = Kee[int](4105)
  Cursor = Kee[int](4106)
  KeySequence = Kee[int](4107)
  Pen = Kee[int](4108)
  TextLength = Kee[int](4109)
  TextFormat = Kee[int](4110)
  Transform = Kee[int](4112)
  Matrix4x4 = Kee[int](4113)
  Vector2D = Kee[int](4114)
  Vector3D = Kee[int](4115)
  Vector4D = Kee[int](4116)
  Quaternion = Kee[int](4117)
  PolygonF = Kee[int](4118)
  Icon = Kee[int](4101)
  LastGuiType = Kee[int](4119)
  SizePolicy = Kee[int](8192)
  UserType = Kee[int](65536)
  LastType = Kee[int](4294967295)
