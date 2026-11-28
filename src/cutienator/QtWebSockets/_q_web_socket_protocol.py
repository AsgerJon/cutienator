"""
QWebSocketProtocol stands for the namespace 'QWebSocketProtocol' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QWebSocketProtocol:
  """
  The namespace 'QWebSocketProtocol' of Qt, which holds no objects. It holds
  the 3 enums Qt writes in it, each under its name, and the 0 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class CloseCode(CuteNum):
    """
    The enum 'QWebSocketProtocol::CloseCode' of Qt, with the 13 names Qt
    gives in it.
    """

    CloseCodeNormal = Kee[int](1000)
    CloseCodeGoingAway = Kee[int](1001)
    CloseCodeProtocolError = Kee[int](1002)
    CloseCodeDatatypeNotSupported = Kee[int](1003)
    CloseCodeReserved1004 = Kee[int](1004)
    CloseCodeMissingStatusCode = Kee[int](1005)
    CloseCodeAbnormalDisconnection = Kee[int](1006)
    CloseCodeWrongDatatype = Kee[int](1007)
    CloseCodePolicyViolated = Kee[int](1008)
    CloseCodeTooMuchData = Kee[int](1009)
    CloseCodeMissingExtension = Kee[int](1010)
    CloseCodeBadOperation = Kee[int](1011)
    CloseCodeTlsHandshakeFailed = Kee[int](1015)

  class OpCode(CuteNum):
    """
    The enum 'QWebSocketProtocol::OpCode' of Qt, with the 16 names Qt gives
    in it.
    """

    OpCodeContinue = Kee[int](0)
    OpCodeText = Kee[int](1)
    OpCodeBinary = Kee[int](2)
    OpCodeReserved3 = Kee[int](3)
    OpCodeReserved4 = Kee[int](4)
    OpCodeReserved5 = Kee[int](5)
    OpCodeReserved6 = Kee[int](6)
    OpCodeReserved7 = Kee[int](7)
    OpCodeClose = Kee[int](8)
    OpCodePing = Kee[int](9)
    OpCodePong = Kee[int](10)
    OpCodeReservedB = Kee[int](11)
    OpCodeReservedC = Kee[int](12)
    OpCodeReservedD = Kee[int](13)
    OpCodeReservedE = Kee[int](14)
    OpCodeReservedF = Kee[int](15)

  class Version(CuteNum):
    """
    The enum 'QWebSocketProtocol::Version' of Qt, with the 9 names Qt gives
    in it.
    """

    VersionUnknown = Kee[int](-1)
    Version0 = Kee[int](0)
    Version4 = Kee[int](4)
    Version5 = Kee[int](5)
    Version6 = Kee[int](6)
    Version7 = Kee[int](7)
    Version8 = Kee[int](8)
    Version13 = Kee[int](13)
    VersionLatest = Kee[int](13)
