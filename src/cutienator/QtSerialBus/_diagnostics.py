"""
Diagnostics stands for the namespace 'Diagnostics' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Diagnostics:
  """
  The namespace 'Diagnostics' of Qt, which holds no objects. It holds the 1
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class SubFunctionCode(CuteNum):
    """
    The enum 'Diagnostics::SubFunctionCode' of Qt, with the 15 names Qt gives
    in it.
    """

    ReturnQueryData = Kee[int](0)
    RestartCommunicationsOption = Kee[int](1)
    ReturnDiagnosticRegister = Kee[int](2)
    ChangeAsciiInputDelimiter = Kee[int](3)
    ForceListenOnlyMode = Kee[int](4)
    ClearCountersAndDiagnosticRegister = Kee[int](10)
    ReturnBusMessageCount = Kee[int](11)
    ReturnBusCommunicationErrorCount = Kee[int](12)
    ReturnBusExceptionErrorCount = Kee[int](13)
    ReturnServerMessageCount = Kee[int](14)
    ReturnServerNoResponseCount = Kee[int](15)
    ReturnServerNAKCount = Kee[int](16)
    ReturnServerBusyCount = Kee[int](17)
    ReturnBusCharacterOverrunCount = Kee[int](18)
    ClearOverrunCounterAndFlag = Kee[int](20)
