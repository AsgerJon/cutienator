"""
CurrencySymbolFormat stands for the enum 'QLocale::CurrencySymbolFormat' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CurrencySymbolFormat(CuteNum):
  """
  The enum 'QLocale::CurrencySymbolFormat' of Qt, with the 3 names Qt gives
  in it.
  """

  CurrencyIsoCode = Kee[int](0)
  CurrencySymbol = Kee[int](1)
  CurrencyDisplayName = Kee[int](2)
