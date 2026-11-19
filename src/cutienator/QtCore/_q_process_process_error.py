"""
ProcessError stands for the enum 'QProcess::ProcessError' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ProcessError(CuteNum):
  """
  The enum 'QProcess::ProcessError' of Qt, with the 6 names Qt gives in it.
  """

  FailedToStart = Kee[int](0)
  Crashed = Kee[int](1)
  Timedout = Kee[int](2)
  ReadError = Kee[int](3)
  WriteError = Kee[int](4)
  UnknownError = Kee[int](5)
