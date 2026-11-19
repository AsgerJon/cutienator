"""
ModelSorting stands for the enum 'QCompleter::ModelSorting' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qcompleter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ModelSorting(CuteNum):
  """
  The enum 'QCompleter::ModelSorting' of Qt, with the 3 names Qt gives in it.
  """

  UnsortedModel = Kee[int](0)
  CaseSensitivelySortedModel = Kee[int](1)
  CaseInsensitivelySortedModel = Kee[int](2)
