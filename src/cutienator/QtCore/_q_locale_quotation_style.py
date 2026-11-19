"""
QuotationStyle stands for the enum 'QLocale::QuotationStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QuotationStyle(CuteNum):
  """
  The enum 'QLocale::QuotationStyle' of Qt, with the 2 names Qt gives in it.
  """

  StandardQuotation = Kee[int](0)
  AlternateQuotation = Kee[int](1)
