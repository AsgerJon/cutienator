"""
QtTaskTree stands for the namespace 'QtTaskTree' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtTaskTree:
  """
  The namespace 'QtTaskTree' of Qt, which holds no objects. It holds the 5
  enums Qt writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class CallDoneFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QtTaskTree::CallDoneFlag' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QtTaskTree::CallDone'. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Never = 0x0
    OnSuccess = 0x1
    OnError = 0x2
    OnCancel = 0x4
    Always = 0x7

  CallDone = CallDoneFlag

  class DoneResult(CuteNum, scoped=True):
    """
    The enum 'QtTaskTree::DoneResult' of Qt, with the 2 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Success = Kee[int](0)
    Error = Kee[int](1)

  class DoneWith(CuteNum, scoped=True):
    """
    The enum 'QtTaskTree::DoneWith' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Success = Kee[int](0)
    Error = Kee[int](1)
    Cancel = Kee[int](2)

  class SetupResult(CuteNum, scoped=True):
    """
    The enum 'QtTaskTree::SetupResult' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Continue = Kee[int](0)
    StopWithSuccess = Kee[int](1)
    StopWithError = Kee[int](2)

  class WorkflowPolicy(CuteNum, scoped=True):
    """
    The enum 'QtTaskTree::WorkflowPolicy' of Qt, with the 7 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    StopOnError = Kee[int](0)
    ContinueOnError = Kee[int](1)
    StopOnSuccess = Kee[int](2)
    ContinueOnSuccess = Kee[int](3)
    StopOnSuccessOrError = Kee[int](4)
    FinishAllAndSuccess = Kee[int](5)
    FinishAllAndError = Kee[int](6)
