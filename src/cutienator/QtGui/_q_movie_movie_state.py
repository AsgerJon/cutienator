"""
MovieState stands for the enum 'QMovie::MovieState' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qmovie.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MovieState(CuteNum):
  """
  The enum 'QMovie::MovieState' of Qt, with the 3 names Qt gives in it.
  """

  NotRunning = Kee[int](0)
  Paused = Kee[int](1)
  Running = Kee[int](2)
