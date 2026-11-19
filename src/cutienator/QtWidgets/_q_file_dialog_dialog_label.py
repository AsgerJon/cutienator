"""
DialogLabel stands for the enum 'QFileDialog::DialogLabel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class DialogLabel(CuteNum):
  """
  The enum 'QFileDialog::DialogLabel' of Qt, with the 5 names Qt gives in it.
  """

  LookIn = Kee[int](0)
  FileName = Kee[int](1)
  FileType = Kee[int](2)
  Accept = Kee[int](3)
  Reject = Kee[int](4)
