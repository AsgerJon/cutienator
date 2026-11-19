"""
ButtonLayout stands for the enum 'QDialogButtonBox::ButtonLayout' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qdialogbuttonbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ButtonLayout(CuteNum):
  """
  The enum 'QDialogButtonBox::ButtonLayout' of Qt, with the 5 names Qt gives
  in it.
  """

  WinLayout = Kee[int](0)
  MacLayout = Kee[int](1)
  KdeLayout = Kee[int](2)
  GnomeLayout = Kee[int](3)
  AndroidLayout = Kee[int](4)
