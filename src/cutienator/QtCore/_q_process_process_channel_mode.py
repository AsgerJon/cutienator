"""
ProcessChannelMode stands for the enum 'QProcess::ProcessChannelMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ProcessChannelMode(CuteNum):
  """
  The enum 'QProcess::ProcessChannelMode' of Qt, with the 5 names Qt gives in
  it.
  """

  SeparateChannels = Kee[int](0)
  MergedChannels = Kee[int](1)
  ForwardedChannels = Kee[int](2)
  ForwardedOutputChannel = Kee[int](3)
  ForwardedErrorChannel = Kee[int](4)
