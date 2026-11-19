"""
CheckIndexOption stands for the flags enum
'QAbstractItemModel::CheckIndexOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class CheckIndexOption(CuteFlags, scoped=True):
  """
  The flags enum 'QAbstractItemModel::CheckIndexOption' of Qt, with the 4
  names Qt gives in it. Qt names the type of its combinations
  'QAbstractItemModel::CheckIndexOptions'. C++ keeps these names inside the
  enum, so the class that holds the enum does not have them.
  """

  NoOption = 0x0
  IndexIsValid = 0x1
  DoNotUseParent = 0x2
  ParentIsInvalid = 0x4
