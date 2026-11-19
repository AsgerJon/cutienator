"""
InputChannelMode stands for the enum 'QProcess::InputChannelMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class InputChannelMode(CuteNum):
  """
  The enum 'QProcess::InputChannelMode' of Qt, with the 2 names Qt gives in
  it.
  """

  ManagedInputChannel = Kee[int](0)
  ForwardedInputChannel = Kee[int](1)
