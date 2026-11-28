"""
QMqtt stands for the namespace 'QMqtt' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QMqtt:
  """
  The namespace 'QMqtt' of Qt, which holds no objects. It holds the 3 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class MessageStatus(CuteNum, scoped=True):
    """
    The enum 'QMqtt::MessageStatus' of Qt, with the 6 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Unknown = Kee[int](0)
    Published = Kee[int](1)
    Acknowledged = Kee[int](2)
    Received = Kee[int](3)
    Released = Kee[int](4)
    Completed = Kee[int](5)

  class PayloadFormatIndicator(CuteNum, scoped=True):
    """
    The enum 'QMqtt::PayloadFormatIndicator' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unspecified = Kee[int](0)
    UTF8Encoded = Kee[int](1)

  class ReasonCode(CuteNum, scoped=True):
    """
    The enum 'QMqtt::ReasonCode' of Qt, with the 35 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Success = Kee[int](0)
    SubscriptionQoSLevel0 = Kee[int](0)
    SubscriptionQoSLevel1 = Kee[int](1)
    SubscriptionQoSLevel2 = Kee[int](2)
    NoMatchingSubscriber = Kee[int](16)
    NoSubscriptionExisted = Kee[int](17)
    ContinueAuthentication = Kee[int](24)
    ReAuthenticate = Kee[int](25)
    UnspecifiedError = Kee[int](128)
    MalformedPacket = Kee[int](129)
    ProtocolError = Kee[int](130)
    ImplementationSpecificError = Kee[int](131)
    UnsupportedProtocolVersion = Kee[int](132)
    InvalidClientId = Kee[int](133)
    InvalidUserNameOrPassword = Kee[int](134)
    NotAuthorized = Kee[int](135)
    ServerNotAvailable = Kee[int](136)
    ServerBusy = Kee[int](137)
    ClientBanned = Kee[int](138)
    InvalidAuthenticationMethod = Kee[int](140)
    InvalidTopicFilter = Kee[int](143)
    InvalidTopicName = Kee[int](144)
    MessageIdInUse = Kee[int](145)
    MessageIdNotFound = Kee[int](146)
    PacketTooLarge = Kee[int](149)
    QuotaExceeded = Kee[int](151)
    InvalidPayloadFormat = Kee[int](153)
    RetainNotSupported = Kee[int](154)
    QoSNotSupported = Kee[int](155)
    UseAnotherServer = Kee[int](156)
    ServerMoved = Kee[int](157)
    SharedSubscriptionsNotSupported = Kee[int](158)
    ExceededConnectionRate = Kee[int](159)
    SubscriptionIdsNotSupported = Kee[int](161)
    WildCardSubscriptionsNotSupported = Kee[int](162)
