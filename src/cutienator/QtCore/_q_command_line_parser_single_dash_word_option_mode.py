"""
SingleDashWordOptionMode stands for the enum
'QCommandLineParser::SingleDashWordOptionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qcommandlineparser.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SingleDashWordOptionMode(CuteNum):
  """
  The enum 'QCommandLineParser::SingleDashWordOptionMode' of Qt, with the 2
  names Qt gives in it.
  """

  ParseAsCompactedShortOptions = Kee[int](0)
  ParseAsLongOptions = Kee[int](1)
