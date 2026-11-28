"""
QMqttServerConnectionProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttconnectionproperties.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteFlags
from ..occult import Rituals
from . import QMqtt, QMqttConnectionProperties


class QMqttServerConnectionProperties(QMqttConnectionProperties):
  """
  The cute side of Qt's QMqttServerConnectionProperties: a plain Python
  object standing in front of one C++ QMqttServerConnectionProperties.

  It is built on the cute 'QMqttConnectionProperties', as Qt's
  QMqttServerConnectionProperties is built on Qt's QMqttConnectionProperties,
  and has everything that class has.

  C++ hands a QMqttServerConnectionProperties around as a copy, so every C++
  QMqttServerConnectionProperties behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QMqttServerConnectionProperties that has a ritual
  and that Python can call so far, 13 names in all: 'availableProperties',
  'isValid', 'maximumQoS', 'retainAvailable', 'clientIdAssigned', 'reason',
  'reasonCode', 'wildcardSupported', 'subscriptionIdentifierSupported',
  'sharedSubscriptionSupported', 'serverKeepAlive', 'responseInformation',
  'serverReference'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttServerConnectionProperties
    &QMqttServerConnectionProperties::operator=(const
    QMqttServerConnectionProperties &a0)': assignment: Python binds a name
    and has no operator for it.
  - Qt's
    'QMqttServerConnectionProperties::~QMqttServerConnectionProperties()':
    the destructor: Python removes its C++ QMqttServerConnectionProperties by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMqttServerConnectionProperties is created at the first use, not
    by 'QMqttServerConnectionProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttServerConnectionProperties back gives a copy the
    ritual made for Python, in a new cute QMqttServerConnectionProperties.
  """

  #  The enums Qt writes inside QMqttServerConnectionProperties, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class ServerPropertyDetail(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QMqttServerConnectionProperties::ServerPropertyDetail' of
    Qt, with the 18 names Qt gives in it. Qt names the type of its
    combinations 'QMqttServerConnectionProperties::ServerPropertyDetails'.
    """

    NULL = 0x0
    SessionExpiryInterval = 0x1
    MaximumReceive = 0x2
    MaximumQoS = 0x4
    RetainAvailable = 0x10
    MaximumPacketSize = 0x20
    AssignedClientId = 0x40
    MaximumTopicAlias = 0x80
    ReasonString = 0x100
    UserProperty = 0x200
    WildCardSupported = 0x400
    SubscriptionIdentifierSupport = 0x800
    SharedSubscriptionSupport = 0x1000
    ServerKeepAlive = 0x2000
    ResponseInformation = 0x4000
    ServerReference = 0x8000
    AuthenticationMethod = 0x10000
    AuthenticationData = 0x20000

  ServerPropertyDetails = ServerPropertyDetail

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttServerConnectionProperties'

  #  Qt's '~QMqttServerConnectionProperties()'. Naming it makes this a value
  #  class: Python owns every C++ QMqttServerConnectionProperties behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QMqttServerConnectionPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def availableProperties(self) -> ServerPropertyDetails:
    """
    Calls Qt's 'ServerPropertyDetails
    QMqttServerConnectionProperties::availableProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html

    Returns
    -------

    ServerPropertyDetails
      The value standing for the combination Qt gave back.
    """
    #  ServerPropertyDetails
    #      QMqttServerConnectionProperties::availableProperties() const
    return QMqttServerConnectionProperties.ServerPropertyDetails(
        self.uglySide.call(
            'ritual_ZNK31QMqttServerConnectionProperties19availableProperti'
            'esEv',
        ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMqttServerConnectionProperties::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html#isValid
    """
    #  bool QMqttServerConnectionProperties::isValid() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties7isValidEv',
    )

  def maximumQoS(self) -> int:
    """
    Calls Qt's 'quint8 QMqttServerConnectionProperties::maximumQoS() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html#maximumQoS
    """
    #  quint8 QMqttServerConnectionProperties::maximumQoS() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties10maximumQoSEv',
    )

  def retainAvailable(self) -> bool:
    """
    Calls Qt's 'bool QMqttServerConnectionProperties::retainAvailable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  bool QMqttServerConnectionProperties::retainAvailable() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties15retainAvailableEv',
    )

  def clientIdAssigned(self) -> bool:
    """
    Calls Qt's 'bool QMqttServerConnectionProperties::clientIdAssigned()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  bool QMqttServerConnectionProperties::clientIdAssigned() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties16clientIdAssignedEv',
    )

  def reason(self) -> str:
    """
    Calls Qt's 'QString QMqttServerConnectionProperties::reason() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html#reason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttServerConnectionProperties::reason() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties6reasonEv',
    )

  def reasonCode(self) -> QMqtt.ReasonCode:
    """
    Calls Qt's 'QMqtt::ReasonCode
    QMqttServerConnectionProperties::reasonCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html#reasonCode

    Returns
    -------

    QMqtt.ReasonCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QMqtt.ReasonCode(number)'
      gives.
    """
    #  QMqtt::ReasonCode QMqttServerConnectionProperties::reasonCode() const
    return QMqtt.ReasonCode(self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties10reasonCodeEv',
    ))

  def wildcardSupported(self) -> bool:
    """
    Calls Qt's 'bool QMqttServerConnectionProperties::wildcardSupported()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  bool QMqttServerConnectionProperties::wildcardSupported() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties17wildcardSupportedEv',
    )

  def subscriptionIdentifierSupported(self) -> bool:
    """
    Calls Qt's 'bool
    QMqttServerConnectionProperties::subscriptionIdentifierSupported()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  bool
    #      QMqttServerConnectionProperties::subscriptionIdentifierSupported()
    #      const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties31subscriptionIdentifie'
        'rSupportedEv',
    )

  def sharedSubscriptionSupported(self) -> bool:
    """
    Calls Qt's 'bool
    QMqttServerConnectionProperties::sharedSubscriptionSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  bool QMqttServerConnectionProperties::sharedSubscriptionSupported()
    #      const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties27sharedSubscriptionSup'
        'portedEv',
    )

  def serverKeepAlive(self) -> int:
    """
    Calls Qt's 'quint16 QMqttServerConnectionProperties::serverKeepAlive()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  quint16 QMqttServerConnectionProperties::serverKeepAlive() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties15serverKeepAliveEv',
    )

  def responseInformation(self) -> str:
    """
    Calls Qt's 'QString
    QMqttServerConnectionProperties::responseInformation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttServerConnectionProperties::responseInformation() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties19responseInformationEv',
    )

  def serverReference(self) -> str:
    """
    Calls Qt's 'QString QMqttServerConnectionProperties::serverReference()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttServerConnectionProperties::serverReference() const
    return self.uglySide.call(
        'ritual_ZNK31QMqttServerConnectionProperties15serverReferenceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QMqttServerConnectionProperties::QMqttServerConnectionProperties()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html
    """
    #  QMqttServerConnectionProperties::QMqttServerConnectionProperties()
    self._noteCreation(QMqttServerConnectionProperties, lambda: Rituals.call(
        'ritual_ZN31QMqttServerConnectionPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttServerConnectionProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttServerConnectionProperties::QMqttServerConnectionProperties(const
    QMqttServerConnectionProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttserverconnectionproperties.html

    Parameters
    ----------

    a0 : QMqttServerConnectionProperties
      Passed on as a value: Qt reads the C++ QMqttServerConnectionProperties,
      which stays Python's own.
    """
    #  QMqttServerConnectionProperties::QMqttServerConnectionProperties(const
    #      QMqttServerConnectionProperties &a0)
    self._noteCreation(QMqttServerConnectionProperties, lambda: Rituals.call(
        'ritual_ZN31QMqttServerConnectionPropertiesC1ERKS_',
        self._valueOf(a0),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
