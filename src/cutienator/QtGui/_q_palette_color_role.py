"""
ColorRole stands for the enum 'QPalette::ColorRole' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpalette.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorRole(CuteNum):
  """
  The enum 'QPalette::ColorRole' of Qt, with the 23 names Qt gives in it.
  """

  WindowText = Kee[int](0)
  Button = Kee[int](1)
  Light = Kee[int](2)
  Midlight = Kee[int](3)
  Dark = Kee[int](4)
  Mid = Kee[int](5)
  Text = Kee[int](6)
  BrightText = Kee[int](7)
  ButtonText = Kee[int](8)
  Base = Kee[int](9)
  Window = Kee[int](10)
  Shadow = Kee[int](11)
  Highlight = Kee[int](12)
  HighlightedText = Kee[int](13)
  Link = Kee[int](14)
  LinkVisited = Kee[int](15)
  AlternateBase = Kee[int](16)
  NoRole = Kee[int](17)
  ToolTipBase = Kee[int](18)
  ToolTipText = Kee[int](19)
  PlaceholderText = Kee[int](20)
  Accent = Kee[int](21)
  NColorRoles = Kee[int](22)
