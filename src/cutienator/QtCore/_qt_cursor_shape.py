"""
CursorShape stands for the enum 'Qt::CursorShape' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CursorShape(CuteNum):
  """
  The enum 'Qt::CursorShape' of Qt, with the 25 names Qt gives in it.
  """

  ArrowCursor = Kee[int](0)
  UpArrowCursor = Kee[int](1)
  CrossCursor = Kee[int](2)
  WaitCursor = Kee[int](3)
  IBeamCursor = Kee[int](4)
  SizeVerCursor = Kee[int](5)
  SizeHorCursor = Kee[int](6)
  SizeBDiagCursor = Kee[int](7)
  SizeFDiagCursor = Kee[int](8)
  SizeAllCursor = Kee[int](9)
  BlankCursor = Kee[int](10)
  SplitVCursor = Kee[int](11)
  SplitHCursor = Kee[int](12)
  PointingHandCursor = Kee[int](13)
  ForbiddenCursor = Kee[int](14)
  WhatsThisCursor = Kee[int](15)
  BusyCursor = Kee[int](16)
  OpenHandCursor = Kee[int](17)
  ClosedHandCursor = Kee[int](18)
  DragCopyCursor = Kee[int](19)
  DragMoveCursor = Kee[int](20)
  DragLinkCursor = Kee[int](21)
  LastCursor = Kee[int](21)
  BitmapCursor = Kee[int](24)
  CustomCursor = Kee[int](25)
