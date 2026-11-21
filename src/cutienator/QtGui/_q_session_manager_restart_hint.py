"""
RestartHint stands for the enum 'QSessionManager::RestartHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsessionmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RestartHint(CuteNum):
  """
  The enum 'QSessionManager::RestartHint' of Qt, with the 4 names Qt gives in
  it.
  """

  RestartIfRunning = Kee[int](0)
  RestartAnyway = Kee[int](1)
  RestartImmediately = Kee[int](2)
  RestartNever = Kee[int](3)
