"""
DropAction stands for the flags enum 'Qt::DropAction' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DropAction(CuteFlags):
  """
  The flags enum 'Qt::DropAction' of Qt, with the 6 names Qt gives in it. Qt
  names the type of its combinations 'Qt::DropActions'.
  """

  CopyAction = 0x1
  MoveAction = 0x2
  LinkAction = 0x4
  ActionMask = 0xff
  TargetMoveAction = 0x8002
  IgnoreAction = 0x0
