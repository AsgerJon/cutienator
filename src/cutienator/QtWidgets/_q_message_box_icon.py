"""
Icon stands for the enum 'QMessageBox::Icon' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmessagebox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Icon(CuteNum):
  """
  The enum 'QMessageBox::Icon' of Qt, with the 5 names Qt gives in it.
  """

  NoIcon = Kee[int](0)
  Information = Kee[int](1)
  Warning = Kee[int](2)
  Critical = Kee[int](3)
  Question = Kee[int](4)
