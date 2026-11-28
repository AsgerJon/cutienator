"""
QtConcurrent stands for the namespace 'QtConcurrent' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtConcurrent:
  """
  The namespace 'QtConcurrent' of Qt, which holds no objects. It holds the 3
  enums Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class FutureResult(CuteNum, scoped=True):
    """
    The enum 'QtConcurrent::FutureResult' of Qt, with the 1 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Ignore = Kee[int](0)

  class ReduceOption(CuteFlags):
    """
    The flags enum 'QtConcurrent::ReduceOption' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QtConcurrent::ReduceOptions'.
    """

    UnorderedReduce = 0x1
    OrderedReduce = 0x2
    SequentialReduce = 0x4

  ReduceOptions = ReduceOption

  class ThreadFunctionResult(CuteNum):
    """
    The enum 'QtConcurrent::ThreadFunctionResult' of Qt, with the 2 names Qt
    gives in it.
    """

    ThrottleThread = Kee[int](0)
    ThreadFinished = Kee[int](1)
