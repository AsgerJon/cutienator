"""
QMqttConnectionProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttconnectionproperties.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QMqttUserProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMqttUserProperties = WAIT['QMqttUserProperties']


class QMqttConnectionProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttConnectionProperties: a plain Python object
  standing in front of one C++ QMqttConnectionProperties.

  C++ hands a QMqttConnectionProperties around as a copy, so every C++
  QMqttConnectionProperties behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttConnectionProperties that has a ritual and that
  Python can call so far, 18 names in all: 'sessionExpiryInterval',
  'maximumReceive', 'maximumPacketSize', 'maximumTopicAlias',
  'requestResponseInformation', 'requestProblemInformation',
  'userProperties', 'authenticationMethod', 'authenticationData',
  'setSessionExpiryInterval', 'setMaximumReceive', 'setMaximumPacketSize',
  'setMaximumTopicAlias', 'setRequestResponseInformation',
  'setRequestProblemInformation', 'setUserProperties',
  'setAuthenticationMethod', 'setAuthenticationData'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttConnectionProperties
    &QMqttConnectionProperties::operator=(const QMqttConnectionProperties
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QMqttConnectionProperties::~QMqttConnectionProperties()': the
    destructor: Python removes its C++ QMqttConnectionProperties by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QMqttConnectionProperties is created at the first use, not by
    'QMqttConnectionProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttConnectionProperties back gives a copy the
    ritual made for Python, in a new cute QMqttConnectionProperties.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttConnectionProperties'

  #  Qt's '~QMqttConnectionProperties()'. Naming it makes this a value class:
  #  Python owns every C++ QMqttConnectionProperties behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QMqttConnectionPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sessionExpiryInterval(self) -> int:
    """
    Calls Qt's 'quint32 QMqttConnectionProperties::sessionExpiryInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html
    """
    #  quint32 QMqttConnectionProperties::sessionExpiryInterval() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties21sessionExpiryIntervalEv',
    )

  def maximumReceive(self) -> int:
    """
    Calls Qt's 'quint16 QMqttConnectionProperties::maximumReceive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#maximumReceive
    """
    #  quint16 QMqttConnectionProperties::maximumReceive() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties14maximumReceiveEv',
    )

  def maximumPacketSize(self) -> int:
    """
    Calls Qt's 'quint32 QMqttConnectionProperties::maximumPacketSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#maximumPacketSize
    """
    #  quint32 QMqttConnectionProperties::maximumPacketSize() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties17maximumPacketSizeEv',
    )

  def maximumTopicAlias(self) -> int:
    """
    Calls Qt's 'quint16 QMqttConnectionProperties::maximumTopicAlias()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#maximumTopicAlias
    """
    #  quint16 QMqttConnectionProperties::maximumTopicAlias() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties17maximumTopicAliasEv',
    )

  def requestResponseInformation(self) -> bool:
    """
    Calls Qt's 'bool QMqttConnectionProperties::requestResponseInformation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html
    """
    #  bool QMqttConnectionProperties::requestResponseInformation() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties26requestResponseInformationE'
        'v',
    )

  def requestProblemInformation(self) -> bool:
    """
    Calls Qt's 'bool QMqttConnectionProperties::requestProblemInformation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html
    """
    #  bool QMqttConnectionProperties::requestProblemInformation() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties25requestProblemInformationEv',
    )

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties
    QMqttConnectionProperties::userProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttConnectionProperties::userProperties() const
    address = self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  def authenticationMethod(self) -> str:
    """
    Calls Qt's 'QString QMqttConnectionProperties::authenticationMethod()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttConnectionProperties::authenticationMethod() const
    return self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties20authenticationMethodEv',
    )

  def authenticationData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttConnectionProperties::authenticationData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#authenticationData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttConnectionProperties::authenticationData() const
    address = self.uglySide.call(
        'ritual_ZNK25QMqttConnectionProperties18authenticationDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSessionExpiryInterval(self, expiry: int) -> None:
    """
    Calls Qt's 'void
    QMqttConnectionProperties::setSessionExpiryInterval(quint32 expiry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    expiry : int
      Passed on as it is.
    """
    #  void QMqttConnectionProperties::setSessionExpiryInterval(quint32
    #      expiry)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties24setSessionExpiryIntervalEj',
        expiry,
    )

  @overload(int)
  def setMaximumReceive(self, maximumReceive: int) -> None:
    """
    Calls Qt's 'void QMqttConnectionProperties::setMaximumReceive(quint16
    maximumReceive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#setMaximumReceive

    Parameters
    ----------

    maximumReceive : int
      Passed on as it is.
    """
    #  void QMqttConnectionProperties::setMaximumReceive(quint16
    #      maximumReceive)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties17setMaximumReceiveEt',
        maximumReceive,
    )

  @overload(int)
  def setMaximumPacketSize(self, packetSize: int) -> None:
    """
    Calls Qt's 'void QMqttConnectionProperties::setMaximumPacketSize(quint32
    packetSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    packetSize : int
      Passed on as it is.
    """
    #  void QMqttConnectionProperties::setMaximumPacketSize(quint32
    #      packetSize)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties20setMaximumPacketSizeEj',
        packetSize,
    )

  @overload(int)
  def setMaximumTopicAlias(self, alias: int) -> None:
    """
    Calls Qt's 'void QMqttConnectionProperties::setMaximumTopicAlias(quint16
    alias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    alias : int
      Passed on as it is.
    """
    #  void QMqttConnectionProperties::setMaximumTopicAlias(quint16 alias)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties20setMaximumTopicAliasEt',
        alias,
    )

  @overload(bool)
  def setRequestResponseInformation(self, response: bool) -> None:
    """
    Calls Qt's 'void
    QMqttConnectionProperties::setRequestResponseInformation(bool response)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    response : bool
      Passed on as it is.
    """
    #  void QMqttConnectionProperties::setRequestResponseInformation(bool
    #      response)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties29setRequestResponseInformatio'
        'nEb',
        response,
    )

  @overload(bool)
  def setRequestProblemInformation(self, problem: bool) -> None:
    """
    Calls Qt's 'void
    QMqttConnectionProperties::setRequestProblemInformation(bool problem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    problem : bool
      Passed on as it is.
    """
    #  void QMqttConnectionProperties::setRequestProblemInformation(bool
    #      problem)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties28setRequestProblemInformation'
        'Eb',
        problem,
    )

  @overload(QMqttUserProperties)
  def setUserProperties(self, properties: QMqttUserProperties) -> None:
    """
    Calls Qt's 'void QMqttConnectionProperties::setUserProperties(const
    QMqttUserProperties &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html#setUserProperties

    Parameters
    ----------

    properties : QMqttUserProperties
      Passed on as a value: Qt reads the C++ QMqttUserProperties, which stays
      Python's own.
    """
    #  void QMqttConnectionProperties::setUserProperties(const
    #      QMqttUserProperties &properties)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties17setUserPropertiesERK19QMqttU'
        'serProperties',
        self._valueOf(properties),
    )

  @overload(str)
  def setAuthenticationMethod(self, authMethod: str) -> None:
    """
    Calls Qt's 'void QMqttConnectionProperties::setAuthenticationMethod(const
    QString &authMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    authMethod : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttConnectionProperties::setAuthenticationMethod(const QString
    #      &authMethod)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties23setAuthenticationMethodERK7Q'
        'String',
        authMethod,
    )

  @overload(QByteArray)
  def setAuthenticationData(self, authData: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttConnectionProperties::setAuthenticationData(const
    QByteArray &authData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    authData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttConnectionProperties::setAuthenticationData(const QByteArray
    #      &authData)
    self.uglySide.call(
        'ritual_ZN25QMqttConnectionProperties21setAuthenticationDataERK10QB'
        'yteArray',
        self._valueOf(authData),
    )

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
    'QMqttConnectionProperties::QMqttConnectionProperties()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html
    """
    #  QMqttConnectionProperties::QMqttConnectionProperties()
    self._noteCreation(QMqttConnectionProperties, lambda: Rituals.call(
        'ritual_ZN25QMqttConnectionPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttConnectionProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttConnectionProperties::QMqttConnectionProperties(const
    QMqttConnectionProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnectionproperties.html

    Parameters
    ----------

    a0 : QMqttConnectionProperties
      Passed on as a value: Qt reads the C++ QMqttConnectionProperties, which
      stays Python's own.
    """
    #  QMqttConnectionProperties::QMqttConnectionProperties(const
    #      QMqttConnectionProperties &a0)
    self._noteCreation(QMqttConnectionProperties, lambda: Rituals.call(
        'ritual_ZN25QMqttConnectionPropertiesC1ERKS_', self._valueOf(a0),
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
