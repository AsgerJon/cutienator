"""
ProcessState stands for the enum 'QProcess::ProcessState' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ProcessState(CuteNum):
  """
  The enum 'QProcess::ProcessState' of Qt, with the 3 names Qt gives in it.
  """

  NotRunning = Kee[int](0)
  Starting = Kee[int](1)
  Running = Kee[int](2)
