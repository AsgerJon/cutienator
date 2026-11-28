"""
QtCoap stands for the namespace 'QtCoap' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtCoap:
  """
  The namespace 'QtCoap' of Qt, which holds no objects. It holds the 6 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class Error(CuteNum, scoped=True):
    """
    The enum 'QtCoap::Error' of Qt, with the 22 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Ok = Kee[int](0)
    HostNotFound = Kee[int](1)
    AddressInUse = Kee[int](2)
    TimeOut = Kee[int](3)
    BadRequest = Kee[int](4)
    Unauthorized = Kee[int](5)
    BadOption = Kee[int](6)
    Forbidden = Kee[int](7)
    NotFound = Kee[int](8)
    MethodNotAllowed = Kee[int](9)
    NotAcceptable = Kee[int](10)
    RequestEntityIncomplete = Kee[int](11)
    PreconditionFailed = Kee[int](12)
    RequestEntityTooLarge = Kee[int](13)
    UnsupportedContentFormat = Kee[int](14)
    InternalServerFault = Kee[int](15)
    NotImplemented = Kee[int](16)
    BadGateway = Kee[int](17)
    ServiceUnavailable = Kee[int](18)
    GatewayTimeout = Kee[int](19)
    ProxyingNotSupported = Kee[int](20)
    Unknown = Kee[int](21)

  class Method(CuteNum, scoped=True):
    """
    The enum 'QtCoap::Method' of Qt, with the 6 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Invalid = Kee[int](0)
    Get = Kee[int](1)
    Post = Kee[int](2)
    Put = Kee[int](3)
    Delete = Kee[int](4)
    Other = Kee[int](5)

  class MulticastGroup(CuteNum, scoped=True):
    """
    The enum 'QtCoap::MulticastGroup' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    AllCoapNodesIPv4 = Kee[int](0)
    AllCoapNodesIPv6LinkLocal = Kee[int](1)
    AllCoapNodesIPv6SiteLocal = Kee[int](2)

  class Port(CuteNum):
    """The enum 'QtCoap::Port' of Qt, with the 2 names Qt gives in it."""

    DefaultPort = Kee[int](5683)
    DefaultSecurePort = Kee[int](5684)

  class ResponseCode(CuteNum, scoped=True):
    """
    The enum 'QtCoap::ResponseCode' of Qt, with the 25 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    EmptyMessage = Kee[int](0)
    Created = Kee[int](65)
    Deleted = Kee[int](66)
    Valid = Kee[int](67)
    Changed = Kee[int](68)
    Content = Kee[int](69)
    Continue = Kee[int](95)
    BadRequest = Kee[int](128)
    Unauthorized = Kee[int](129)
    BadOption = Kee[int](130)
    Forbidden = Kee[int](131)
    NotFound = Kee[int](132)
    MethodNotAllowed = Kee[int](133)
    NotAcceptable = Kee[int](134)
    RequestEntityIncomplete = Kee[int](136)
    PreconditionFailed = Kee[int](140)
    RequestEntityTooLarge = Kee[int](141)
    UnsupportedContentFormat = Kee[int](142)
    InternalServerFault = Kee[int](160)
    NotImplemented = Kee[int](161)
    BadGateway = Kee[int](162)
    ServiceUnavailable = Kee[int](163)
    GatewayTimeout = Kee[int](164)
    ProxyingNotSupported = Kee[int](165)
    InvalidCode = Kee[int](255)

  class SecurityMode(CuteNum, scoped=True):
    """
    The enum 'QtCoap::SecurityMode' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoSecurity = Kee[int](0)
    PreSharedKey = Kee[int](1)
    RawPublicKey = Kee[int](2)
    Certificate = Kee[int](3)
