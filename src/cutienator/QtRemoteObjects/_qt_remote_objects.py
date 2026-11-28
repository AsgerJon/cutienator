"""
QtRemoteObjects stands for the namespace 'QtRemoteObjects' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtRemoteObjects:
  """
  The namespace 'QtRemoteObjects' of Qt, which holds no objects. It holds the
  2 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class InitialAction(CuteNum):
    """
    The enum 'QtRemoteObjects::InitialAction' of Qt, with the 2 names Qt
    gives in it.
    """

    FetchRootSize = Kee[int](0)
    PrefetchData = Kee[int](1)

  class QRemoteObjectPacketTypeEnum(CuteNum):
    """
    The enum 'QtRemoteObjects::QRemoteObjectPacketTypeEnum' of Qt, with the
    12 names Qt gives in it.
    """

    Invalid = Kee[int](0)
    Handshake = Kee[int](1)
    InitPacket = Kee[int](2)
    InitDynamicPacket = Kee[int](3)
    AddObject = Kee[int](4)
    RemoveObject = Kee[int](5)
    InvokePacket = Kee[int](6)
    InvokeReplyPacket = Kee[int](7)
    PropertyChangePacket = Kee[int](8)
    ObjectList = Kee[int](9)
    Ping = Kee[int](10)
    Pong = Kee[int](11)
