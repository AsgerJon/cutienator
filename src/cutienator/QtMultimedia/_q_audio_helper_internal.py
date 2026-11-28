"""
QAudioHelperInternal stands for the namespace 'QAudioHelperInternal' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QAudioHelperInternal:
  """
  The namespace 'QAudioHelperInternal' of Qt, which holds no objects. It
  holds the 3 enums Qt writes in it, each under its name, and the 0 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class DownmixScaling(CuteNum, scoped=True):
    """
    The enum 'QAudioHelperInternal::DownmixScaling' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Average = Kee[int](0)
    KeepPower = Kee[int](1)

  class NativeSampleFormat(CuteNum, scoped=True):
    """
    The enum 'QAudioHelperInternal::NativeSampleFormat' of Qt, with the 6
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    uint8_t = Kee[int](0)
    int16_t = Kee[int](1)
    int32_t = Kee[int](2)
    int24_t_3b = Kee[int](3)
    int24_t_4b_low = Kee[int](4)
    float32_t = Kee[int](5)

  class UpmixScaling(CuteNum, scoped=True):
    """
    The enum 'QAudioHelperInternal::UpmixScaling' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Duplicate = Kee[int](0)
    EqualPower = Kee[int](1)
