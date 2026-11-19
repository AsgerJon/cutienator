"""
LocateOption stands for the flags enum 'QStandardPaths::LocateOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qstandardpaths.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class LocateOption(CuteFlags):
  """
  The flags enum 'QStandardPaths::LocateOption' of Qt, with the 2 names Qt
  gives in it. Qt names the type of its combinations
  'QStandardPaths::LocateOptions'.
  """

  LocateFile = 0x0
  LocateDirectory = 0x1
