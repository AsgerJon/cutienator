"""
QBluetoothServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QBluetooth, QBluetoothServiceInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QBluetoothAddress, QBluetoothServerPrivate, QBluetoothSocket
  from . import QBluetoothUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothUuid = WAIT['QBluetoothUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothServer(QObject):
  """
  The cute side of Qt's QBluetoothServer: a plain Python object standing in
  front of one C++ QBluetoothServer.

  It is built on the cute 'QObject', as Qt's QBluetoothServer is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothServer that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'close', 'listen',
  'isListening', 'setMaxPendingConnections', 'maxPendingConnections',
  'hasPendingConnections', 'nextPendingConnection', 'serverAddress',
  'serverPort', 'setSecurityFlags', 'securityFlags', 'serverType', 'error',
  'newConnection', 'errorOccurred', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBluetoothServer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QBluetoothServer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBluetoothServer::~QBluetoothServer()': the destructor: Python
    never removes a C++ QBluetoothServer.
  - Qt's 'const QBluetoothServerPrivate *QBluetoothServer::d_func() const':
    takes in Python what 'QBluetoothServerPrivate
    *QBluetoothServer::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothServer is created at the first use, not by
    'QBluetoothServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothServer.
  - Qt tells when it has removed the C++ QBluetoothServer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBluetoothServer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QBluetoothServer::Error' of Qt, with the 7 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    UnknownError = Kee[int](1)
    PoweredOffError = Kee[int](2)
    InputOutputError = Kee[int](3)
    ServiceAlreadyRegisteredError = Kee[int](4)
    UnsupportedProtocolError = Kee[int](5)
    MissingPermissionsError = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QBluetoothServer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QBluetoothServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothServer'

  #  A C++ QBluetoothServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBluetoothServer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBluetoothServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBluetoothServer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QBluetoothServer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServer::isListening() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#isListening
    """
    #  bool QBluetoothServer::isListening() const
    return self.uglySide.call('ritual_ZNK16QBluetoothServer11isListeningEv')

  def maxPendingConnections(self) -> int:
    """
    Calls Qt's 'int QBluetoothServer::maxPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#maxPendingConnections
    """
    #  int QBluetoothServer::maxPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK16QBluetoothServer21maxPendingConnectionsEv',
    )

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServer::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#hasPendingConnections
    """
    #  bool QBluetoothServer::hasPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK16QBluetoothServer21hasPendingConnectionsEv',
    )

  def serverAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothServer::serverAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#serverAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothServer::serverAddress() const
    address = self.uglySide.call(
        'ritual_ZNK16QBluetoothServer13serverAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def serverPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothServer::serverPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#serverPort
    """
    #  quint16 QBluetoothServer::serverPort() const
    return self.uglySide.call('ritual_ZNK16QBluetoothServer10serverPortEv')

  def securityFlags(self) -> QBluetooth.SecurityFlags:
    """
    Calls Qt's 'QBluetooth::SecurityFlags QBluetoothServer::securityFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#securityFlags

    Returns
    -------

    QBluetooth.SecurityFlags
      The value standing for the combination Qt gave back.
    """
    #  QBluetooth::SecurityFlags QBluetoothServer::securityFlags() const
    return QBluetooth.SecurityFlags(self.uglySide.call(
        'ritual_ZNK16QBluetoothServer13securityFlagsEv',
    ))

  def serverType(self) -> QBluetoothServiceInfo.Protocol:
    """
    Calls Qt's 'QBluetoothServiceInfo::Protocol
    QBluetoothServer::serverType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#serverType

    Returns
    -------

    QBluetoothServiceInfo.Protocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QBluetoothServiceInfo.Protocol(number)' gives.
    """
    #  QBluetoothServiceInfo::Protocol QBluetoothServer::serverType() const
    return QBluetoothServiceInfo.Protocol(self.uglySide.call(
        'ritual_ZNK16QBluetoothServer10serverTypeEv',
    ))

  def error(self) -> Error:
    """
    Calls Qt's 'Error QBluetoothServer::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QBluetoothServer::error() const
    return QBluetoothServer.Error(self.uglySide.call(
        'ritual_ZNK16QBluetoothServer5errorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxPendingConnections(self, numConnections: int) -> None:
    """
    Calls Qt's 'void QBluetoothServer::setMaxPendingConnections(int
    numConnections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#setMaxPendingConnections

    Parameters
    ----------

    numConnections : int
      Passed on as it is.
    """
    #  void QBluetoothServer::setMaxPendingConnections(int numConnections)
    self.uglySide.call(
        'ritual_ZN16QBluetoothServer24setMaxPendingConnectionsEi',
        numConnections,
    )

  @overload(QBluetooth.SecurityFlags)
  def setSecurityFlags(self, security: QBluetooth.SecurityFlags) -> None:
    """
    Calls Qt's 'void
    QBluetoothServer::setSecurityFlags(QBluetooth::SecurityFlags security)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#setSecurityFlags

    Parameters
    ----------

    security : QBluetooth.SecurityFlags
      Passed on as its number.
    """
    #  void QBluetoothServer::setSecurityFlags(QBluetooth::SecurityFlags
    #      security)
    self.uglySide.call(
        'ritual_ZN16QBluetoothServer16setSecurityFlagsE6QFlagsIN10QBluetoot'
        'h8SecurityEE',
        security.value,
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

  @overload(QBluetoothServiceInfo.Protocol)
  @overload(QBluetoothServiceInfo.Protocol, QObject)
  @overload(QBluetoothServiceInfo.Protocol, NoneType)
  def __init__(
      self,
      serverType: QBluetoothServiceInfo.Protocol,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothServer::QBluetoothServer(QBluetoothServiceInfo::Protocol
    serverType, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#QBluetoothServer

    Parameters
    ----------

    serverType : QBluetoothServiceInfo.Protocol
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothServer::QBluetoothServer(QBluetoothServiceInfo::Protocol
    #      serverType, QObject *parent)
    self._noteCreation(QBluetoothServer, lambda: Rituals.call(
        'ritual_ZN16QBluetoothServerC1EN21QBluetoothServiceInfo8ProtocolEP7'
        'QObject',
        serverType.value, self._addressOf(parent, 'QObject'),
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

  def close(self) -> None:
    """
    Calls Qt's 'void QBluetoothServer::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#close
    """
    #  void QBluetoothServer::close()
    self.uglySide.call('ritual_ZN16QBluetoothServer5closeEv')

  @overload()
  @overload(QBluetoothAddress)
  @overload(QBluetoothAddress, int)
  def listen(
      self,
      address: Optional[QBluetoothAddress] = None,
      port: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QBluetoothServer::listen(const QBluetoothAddress
    &address, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#listen

    Parameters
    ----------

    address : Optional[QBluetoothAddress]
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own. May be left out, as in Qt: a new 'QBluetoothAddress()' is
      then passed on.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QBluetoothServer::listen(const QBluetoothAddress &address,
    #      quint16 port)
    if address is None:
      from . import QBluetoothAddress
      address = QBluetoothAddress()
    return self.uglySide.call(
        'ritual_ZN16QBluetoothServer6listenERK17QBluetoothAddresst',
        self._valueOf(address), port,
    )

  @overload(QBluetoothUuid)
  @overload(QBluetoothUuid, str)
  def listen(
      self,
      uuid: QBluetoothUuid,
      serviceName: str = '',
  ) -> QBluetoothServiceInfo:
    """
    Calls Qt's 'QBluetoothServiceInfo QBluetoothServer::listen(const
    QBluetoothUuid &uuid, const QString &serviceName)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#listen

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    serviceName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QBluetoothServiceInfo
      A new cute QBluetoothServiceInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QBluetoothServiceInfo QBluetoothServer::listen(const QBluetoothUuid
    #      &uuid, const QString &serviceName)
    address = self.uglySide.call(
        'ritual_ZN16QBluetoothServer6listenERK14QBluetoothUuidRK7QString',
        self._valueOf(uuid), serviceName,
    )
    return QBluetoothServiceInfo._cuteOwning(address)

  def nextPendingConnection(self) -> Optional[QBluetoothSocket]:
    """
    Calls Qt's 'QBluetoothSocket *QBluetoothServer::nextPendingConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#nextPendingConnection

    Returns
    -------

    Optional[QBluetoothSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothSocket *QBluetoothServer::nextPendingConnection()
    address = self.uglySide.call(
        'ritual_ZN16QBluetoothServer21nextPendingConnectionEv',
    )
    from . import QBluetoothSocket
    return QBluetoothSocket._cuteAt(address)

  def newConnection(self) -> None:
    """
    Calls Qt's 'void QBluetoothServer::newConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#newConnection
    """
    #  void QBluetoothServer::newConnection()
    self.uglySide.call('ritual_ZN16QBluetoothServer13newConnectionEv')

  @overload(Error)
  def errorOccurred(self, error: Error) -> None:
    """
    Calls Qt's 'void QBluetoothServer::errorOccurred(QBluetoothServer::Error
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserver.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QBluetoothServer::errorOccurred(QBluetoothServer::Error error)
    self.uglySide.call(
        'ritual_ZN16QBluetoothServer13errorOccurredENS_5ErrorE', error.value,
    )

  def d_func(self) -> Optional[QBluetoothServerPrivate]:
    """
    Calls Qt's 'QBluetoothServerPrivate *QBluetoothServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserver.html#d_func

    Returns
    -------

    Optional[QBluetoothServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothServerPrivate *QBluetoothServer::d_func()
    address = self.uglySide.call('ritual_ZN16QBluetoothServer6d_funcEv')
    from . import QBluetoothServerPrivate
    return QBluetoothServerPrivate._cuteAt(address)
