"""
AcceptMode stands for the enum 'QFileDialog::AcceptMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AcceptMode(CuteNum):
  """
  The enum 'QFileDialog::AcceptMode' of Qt, with the 2 names Qt gives in it.
  """

  AcceptOpen = Kee[int](0)
  AcceptSave = Kee[int](1)
