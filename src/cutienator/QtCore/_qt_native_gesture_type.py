"""
NativeGestureType stands for the enum 'Qt::NativeGestureType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class NativeGestureType(CuteNum):
  """
  The enum 'Qt::NativeGestureType' of Qt, with the 7 names Qt gives in it.
  """

  BeginNativeGesture = Kee[int](0)
  EndNativeGesture = Kee[int](1)
  PanNativeGesture = Kee[int](2)
  ZoomNativeGesture = Kee[int](3)
  SmartZoomNativeGesture = Kee[int](4)
  RotateNativeGesture = Kee[int](5)
  SwipeNativeGesture = Kee[int](6)
