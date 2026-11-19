"""
FileMode stands for the enum 'QFileDialog::FileMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FileMode(CuteNum):
  """
  The enum 'QFileDialog::FileMode' of Qt, with the 4 names Qt gives in it.
  """

  AnyFile = Kee[int](0)
  ExistingFile = Kee[int](1)
  Directory = Kee[int](2)
  ExistingFiles = Kee[int](3)
