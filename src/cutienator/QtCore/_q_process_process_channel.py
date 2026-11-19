"""
ProcessChannel stands for the enum 'QProcess::ProcessChannel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ProcessChannel(CuteNum):
  """
  The enum 'QProcess::ProcessChannel' of Qt, with the 2 names Qt gives in it.
  """

  StandardOutput = Kee[int](0)
  StandardError = Kee[int](1)
