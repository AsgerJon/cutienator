"""
QAudio stands for the namespace 'QAudio' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QAudio:
  """
  The namespace 'QAudio' of Qt, which holds no objects. It holds the 3 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class Error(CuteNum):
    """The enum 'QAudio::Error' of Qt, with the 5 names Qt gives in it."""

    NoError = Kee[int](0)
    OpenError = Kee[int](1)
    IOError = Kee[int](2)
    UnderrunError = Kee[int](3)
    FatalError = Kee[int](4)

  class State(CuteNum):
    """The enum 'QAudio::State' of Qt, with the 4 names Qt gives in it."""

    ActiveState = Kee[int](0)
    SuspendedState = Kee[int](1)
    StoppedState = Kee[int](2)
    IdleState = Kee[int](3)

  class VolumeScale(CuteNum):
    """
    The enum 'QAudio::VolumeScale' of Qt, with the 4 names Qt gives in it.
    """

    LinearVolumeScale = Kee[int](0)
    CubicVolumeScale = Kee[int](1)
    LogarithmicVolumeScale = Kee[int](2)
    DecibelVolumeScale = Kee[int](3)
