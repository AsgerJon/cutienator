"""
TypeFlag stands for the flags enum 'QMetaType::TypeFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qmetatype.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class TypeFlag(CuteFlags):
  """
  The flags enum 'QMetaType::TypeFlag' of Qt, with the 17 names Qt gives in
  it. Qt names the type of its combinations 'QMetaType::TypeFlags'.
  """

  NeedsConstruction = 0x1
  NeedsDestruction = 0x2
  RelocatableType = 0x4
  MovableType = 0x4
  PointerToQObject = 0x8
  IsEnumeration = 0x10
  SharedPointerToQObject = 0x20
  WeakPointerToQObject = 0x40
  TrackingPointerToQObject = 0x80
  IsUnsignedEnumeration = 0x100
  IsGadget = 0x200
  PointerToGadget = 0x400
  IsPointer = 0x800
  IsQmlList = 0x1000
  IsConst = 0x2000
  NeedsCopyConstruction = 0x4000
  NeedsMoveConstruction = 0x8000
