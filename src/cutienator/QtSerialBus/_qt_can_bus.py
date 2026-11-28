"""
QtCanBus stands for the namespace 'QtCanBus' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtCanBus:
  """
  The namespace 'QtCanBus' of Qt, which holds no objects. It holds the 3
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class DataFormat(CuteNum, scoped=True):
    """
    The enum 'QtCanBus::DataFormat' of Qt, with the 5 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    SignedInteger = Kee[int](0)
    UnsignedInteger = Kee[int](1)
    Float = Kee[int](2)
    Double = Kee[int](3)
    AsciiString = Kee[int](4)

  class DataSource(CuteNum, scoped=True):
    """
    The enum 'QtCanBus::DataSource' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Payload = Kee[int](0)
    FrameId = Kee[int](1)

  class MultiplexState(CuteNum, scoped=True):
    """
    The enum 'QtCanBus::MultiplexState' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    MultiplexorSwitch = Kee[int](1)
    MultiplexedSignal = Kee[int](2)
    SwitchAndSignal = Kee[int](3)
