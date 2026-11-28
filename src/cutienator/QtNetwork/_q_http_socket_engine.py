"""
QHttpSocketEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpSocketEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QAbstractSocket, QAbstractSocketEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDeadlineTimer, QMetaObject
  from . import QHostAddress, QHttpSocketEnginePrivate, QIpPacketHeader
  from . import QNetworkInterface, QNetworkProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QHostAddress = WAIT['QHostAddress']
  QIpPacketHeader = WAIT['QIpPacketHeader']
  QNetworkInterface = WAIT['QNetworkInterface']
  QNetworkProxy = WAIT['QNetworkProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpSocketEngine(QAbstractSocketEngine):
  """
  The cute side of Qt's QHttpSocketEngine: a plain Python object standing in
  front of one C++ QHttpSocketEngine.

  It is built on the cute 'QAbstractSocketEngine', as Qt's QHttpSocketEngine
  is built on Qt's QAbstractSocketEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpSocketEngine that has a ritual and that Python
  can call so far, 44 names in all: 'metaObject', 'initialize', 'setProxy',
  'socketDescriptor', 'isValid', 'connectToHost', 'connectToHostByName',
  'bind', 'listen', 'accept', 'close', 'bytesAvailable', 'write',
  'joinMulticastGroup', 'leaveMulticastGroup', 'multicastInterface',
  'setMulticastInterface', 'hasPendingDatagrams', 'pendingDatagramSize',
  'writeDatagram', 'bytesToWrite', 'option', 'setOption',
  'waitForProtocolHandshake', 'isReadNotificationEnabled',
  'setReadNotificationEnabled', 'isWriteNotificationEnabled',
  'setWriteNotificationEnabled', 'isExceptionNotificationEnabled',
  'setExceptionNotificationEnabled', 'slotSocketConnected',
  'slotSocketDisconnected', 'slotSocketReadNotification',
  'slotSocketBytesWritten', 'slotSocketError', 'slotSocketStateChanged',
  'emitPendingReadNotification', 'emitPendingWriteNotification',
  'emitPendingConnectionNotification', 'emitReadNotification',
  'emitWriteNotification', 'emitConnectionNotification', 'readHttpHeader',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpSocketEngine::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHttpSocketEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHttpSocketEngine::~QHttpSocketEngine()': the destructor: Python
    never removes a C++ QHttpSocketEngine.
  - Qt's 'qint64 QHttpSocketEngine::read(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QHttpSocketEngine::readDatagram(char *data, qint64 maxlen,
    QIpPacketHeader *a2, PacketHeaderOptions a3)': names 'char', which has no
    cute class yet.
  - Qt's 'bool QHttpSocketEngine::waitForRead(QDeadlineTimer deadline, bool
    *timedOut)': takes a number to change where it is.
  - Qt's 'bool QHttpSocketEngine::waitForWrite(QDeadlineTimer deadline, bool
    *timedOut)': takes a number to change where it is.
  - Qt's 'bool QHttpSocketEngine::waitForReadOrWrite(bool *readyToRead, bool
    *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer deadline,
    bool *timedOut)': takes a number to change where it is.
  - Qt's 'const QHttpSocketEnginePrivate *QHttpSocketEngine::d_func() const':
    takes in Python what 'QHttpSocketEnginePrivate
    *QHttpSocketEngine::d_func()' takes.

  What has no ritual
  ------------------

  9 of the 63 functions Qt declares: 4 forbidden; 3 leans on
  'QHttpSocketEngine; 2 not a gap.

  What to expect
  --------------

  - The C++ QHttpSocketEngine is created at the first use, not by
    'QHttpSocketEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpSocketEngine.
  - Qt tells when it has removed the C++ QHttpSocketEngine. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpSocketEngine that has no cute function yet,
    '__init__', 'connectInternal', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttpSocketEngine, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HttpState(CuteNum):
    """
    The enum 'QHttpSocketEngine::HttpState' of Qt, with the 6 names Qt gives
    in it.
    """

    NULL = Kee[int](0)
    ConnectSent = Kee[int](1)
    Connected = Kee[int](2)
    SendAuthentication = Kee[int](3)
    ReadResponseContent = Kee[int](4)
    ReadResponseHeader = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpSocketEngine'

  #  A C++ QHttpSocketEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpSocketEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttpSocketEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpSocketEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpSocketEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QHttpSocketEngine::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#socketDescriptor
    """
    #  qintptr QHttpSocketEngine::socketDescriptor() const
    ritual = 'ritual_ZNK17QHttpSocketEngine16socketDescriptorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine16socketDescriptorEv'
    return self.uglySide.call(ritual)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#isValid
    """
    #  bool QHttpSocketEngine::isValid() const
    ritual = 'ritual_ZNK17QHttpSocketEngine7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine7isValidEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QHttpSocketEngine::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#bytesAvailable
    """
    #  qint64 QHttpSocketEngine::bytesAvailable() const
    ritual = 'ritual_ZNK17QHttpSocketEngine14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def multicastInterface(self) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QHttpSocketEngine::multicastInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#multicastInterface

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QHttpSocketEngine::multicastInterface() const
    ritual = 'ritual_ZNK17QHttpSocketEngine18multicastInterfaceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine18multicastInterfaceEv'
    address = self.uglySide.call(ritual)
    from . import QNetworkInterface
    return QNetworkInterface._cuteOwning(address)

  def hasPendingDatagrams(self) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::hasPendingDatagrams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#hasPendingDatagrams
    """
    #  bool QHttpSocketEngine::hasPendingDatagrams() const
    ritual = 'ritual_ZNK17QHttpSocketEngine19hasPendingDatagramsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine19hasPendingDatagramsEv'
    return self.uglySide.call(ritual)

  def pendingDatagramSize(self) -> int:
    """
    Calls Qt's 'qint64 QHttpSocketEngine::pendingDatagramSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#pendingDatagramSize
    """
    #  qint64 QHttpSocketEngine::pendingDatagramSize() const
    ritual = 'ritual_ZNK17QHttpSocketEngine19pendingDatagramSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine19pendingDatagramSizeEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QHttpSocketEngine::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#bytesToWrite
    """
    #  qint64 QHttpSocketEngine::bytesToWrite() const
    ritual = 'ritual_ZNK17QHttpSocketEngine12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpSocketEngine12bytesToWriteEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractSocketEngine.SocketOption)
  def option(self, option: QAbstractSocketEngine.SocketOption) -> int:
    """
    Calls Qt's 'int QHttpSocketEngine::option(SocketOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#option

    Parameters
    ----------

    option : QAbstractSocketEngine.SocketOption
      Passed on as its number.
    """
    #  int QHttpSocketEngine::option(SocketOption option) const
    ritual = (
        'ritual_ZNK17QHttpSocketEngine6optionEN21QAbstractSocketEngine12Soc'
        'ketOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QHttpSocketEngine6optionEN21QAbstractSocketEngin'
          'e12SocketOptionE')
    return self.uglySide.call(ritual, option.value)

  def isReadNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::isReadNotificationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#isReadNotificationEnabled
    """
    #  bool QHttpSocketEngine::isReadNotificationEnabled() const
    ritual = 'ritual_ZNK17QHttpSocketEngine25isReadNotificationEnabledEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QHttpSocketEngine25isReadNotificationEnabledEv')
    return self.uglySide.call(ritual)

  def isWriteNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::isWriteNotificationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#isWriteNotificationEnabled
    """
    #  bool QHttpSocketEngine::isWriteNotificationEnabled() const
    ritual = 'ritual_ZNK17QHttpSocketEngine26isWriteNotificationEnabledEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QHttpSocketEngine26isWriteNotificationEnabledEv')
    return self.uglySide.call(ritual)

  def isExceptionNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::isExceptionNotificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html
    """
    #  bool QHttpSocketEngine::isExceptionNotificationEnabled() const
    ritual = (
        'ritual_ZNK17QHttpSocketEngine30isExceptionNotificationEnabledEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QHttpSocketEngine30isExceptionNotificationEnable'
          'dEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QHttpSocketEngine::setProxy(const QNetworkProxy &networkProxy)
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(QNetworkInterface)
  def setMulticastInterface(self, iface: QNetworkInterface) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::setMulticastInterface(const
    QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#setMulticastInterface

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QHttpSocketEngine::setMulticastInterface(const QNetworkInterface
    #      &iface)
    ritual = (
        'ritual_ZN17QHttpSocketEngine21setMulticastInterfaceERK17QNetworkIn'
        'terface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpSocketEngine21setMulticastInterfaceERK17QNet'
          'workInterface')
    return self.uglySide.call(ritual, self._valueOf(iface))

  @overload(QAbstractSocketEngine.SocketOption, int)
  def setOption(
      self,
      option: QAbstractSocketEngine.SocketOption,
      value: int,
  ) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::setOption(SocketOption option, int
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#setOption

    Parameters
    ----------

    option : QAbstractSocketEngine.SocketOption
      Passed on as its number.

    value : int
      Passed on as it is.
    """
    #  bool QHttpSocketEngine::setOption(SocketOption option, int value)
    ritual = (
        'ritual_ZN17QHttpSocketEngine9setOptionEN21QAbstractSocketEngine12S'
        'ocketOptionEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpSocketEngine9setOptionEN21QAbstractSocketEng'
          'ine12SocketOptionEi')
    return self.uglySide.call(ritual, option.value, value)

  @overload(bool)
  def setReadNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::setReadNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#setReadNotificationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHttpSocketEngine::setReadNotificationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine26setReadNotificationEnabledEb', enable,
    )

  @overload(bool)
  def setWriteNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::setWriteNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#setWriteNotificationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHttpSocketEngine::setWriteNotificationEnabled(bool enable)
    ritual = 'ritual_ZN17QHttpSocketEngine27setWriteNotificationEnabledEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpSocketEngine27setWriteNotificationEnabledEb')
    self.uglySide.call(ritual, enable)

  @overload(bool)
  def setExceptionNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::setExceptionNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHttpSocketEngine::setExceptionNotificationEnabled(bool enable)
    ritual = (
        'ritual_ZN17QHttpSocketEngine31setExceptionNotificationEnabledEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpSocketEngine31setExceptionNotificationEnable'
          'dEb')
    self.uglySide.call(ritual, enable)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QHttpSocketEngine::QHttpSocketEngine(QObject *parent)': leans on
    'QHttpSocketEngine::initialize(QAbstractSocket::SocketType,
    QAbstractSocket::NetworkLayerProtocol)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpSocketEngine.__init__' has no cute function yet. Qt's "
        "'QHttpSocketEngine::QHttpSocketEngine(QObject *parent)': leans on "
        "'QHttpSocketEngine::initialize(QAbstractSocket::SocketType, "
        "QAbstractSocket::NetworkLayerProtocol)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QAbstractSocket.SocketType)
  @overload(QAbstractSocket.SocketType, QAbstractSocket.NetworkLayerProtocol)
  def initialize(
      self,
      type: QAbstractSocket.SocketType,
      protocol: QAbstractSocket.NetworkLayerProtocol = (
          QAbstractSocket.NetworkLayerProtocol.IPv4Protocol),
  ) -> bool:
    """
    Calls Qt's 'bool
    QHttpSocketEngine::initialize(QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#initialize

    Parameters
    ----------

    type : QAbstractSocket.SocketType
      Passed on as its number.

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.NetworkLayerProtocol.IPv4Protocol.
    """
    #  bool QHttpSocketEngine::initialize(QAbstractSocket::SocketType type,
    #      QAbstractSocket::NetworkLayerProtocol protocol)
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine10initializeEN15QAbstractSocket10Socke'
        'tTypeENS0_20NetworkLayerProtocolE',
        type.value, protocol.value,
    )

  @overload(int)
  @overload(int, QAbstractSocket.SocketState)
  def initialize(
      self,
      socketDescriptor: int,
      socketState: QAbstractSocket.SocketState = (
          QAbstractSocket.SocketState.ConnectedState),
  ) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::initialize(qintptr socketDescriptor,
    QAbstractSocket::SocketState socketState)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#initialize

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    socketState : QAbstractSocket.SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.SocketState.ConnectedState.
    """
    #  bool QHttpSocketEngine::initialize(qintptr socketDescriptor,
    #      QAbstractSocket::SocketState socketState)
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine10initializeExN15QAbstractSocket11Sock'
        'etStateE',
        socketDescriptor, socketState.value,
    )

  @overload(QHostAddress, int)
  def connectToHost(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::connectToHost(const QHostAddress
    &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#connectToHost

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QHttpSocketEngine::connectToHost(const QHostAddress &address,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine13connectToHostERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(str, int)
  def connectToHostByName(self, name: str, port: int) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::connectToHostByName(const QString
    &name, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#connectToHostByName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  bool QHttpSocketEngine::connectToHostByName(const QString &name,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine19connectToHostByNameERK7QStringt',
        name, port,
    )

  @overload(QHostAddress, int)
  def bind(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::bind(const QHostAddress &address,
    quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#bind

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QHttpSocketEngine::bind(const QHostAddress &address, quint16
    #      port)
    ritual = 'ritual_ZN17QHttpSocketEngine4bindERK12QHostAddresst'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QHttpSocketEngine4bindERK12QHostAddresst'
    return self.uglySide.call(ritual, self._valueOf(address), port)

  @overload(int)
  def listen(self, backlog: int) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::listen(int backlog)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#listen

    Parameters
    ----------

    backlog : int
      Passed on as it is.
    """
    #  bool QHttpSocketEngine::listen(int backlog)
    ritual = 'ritual_ZN17QHttpSocketEngine6listenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QHttpSocketEngine6listenEi'
    return self.uglySide.call(ritual, backlog)

  def accept(self) -> int:
    """
    Calls Qt's 'qintptr QHttpSocketEngine::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#accept
    """
    #  qintptr QHttpSocketEngine::accept()
    ritual = 'ritual_ZN17QHttpSocketEngine6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QHttpSocketEngine6acceptEv'
    return self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#close
    """
    #  void QHttpSocketEngine::close()
    ritual = 'ritual_ZN17QHttpSocketEngine5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QHttpSocketEngine5closeEv'
    self.uglySide.call(ritual)

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QHttpSocketEngine::write(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QHttpSocketEngine::write(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine5writeEPKcx', self._bytesOf(data), len,
    )

  @overload(QHostAddress, QNetworkInterface)
  def joinMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::joinMulticastGroup(const QHostAddress
    &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#joinMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QHttpSocketEngine::joinMulticastGroup(const QHostAddress
    #      &groupAddress, const QNetworkInterface &iface)
    ritual = (
        'ritual_ZN17QHttpSocketEngine18joinMulticastGroupERK12QHostAddressR'
        'K17QNetworkInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpSocketEngine18joinMulticastGroupERK12QHostAd'
          'dressRK17QNetworkInterface')
    return self.uglySide.call(
        ritual, self._valueOf(groupAddress), self._valueOf(iface),
    )

  @overload(QHostAddress, QNetworkInterface)
  def leaveMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::leaveMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#leaveMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QHttpSocketEngine::leaveMulticastGroup(const QHostAddress
    #      &groupAddress, const QNetworkInterface &iface)
    ritual = (
        'ritual_ZN17QHttpSocketEngine19leaveMulticastGroupERK12QHostAddress'
        'RK17QNetworkInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpSocketEngine19leaveMulticastGroupERK12QHostA'
          'ddressRK17QNetworkInterface')
    return self.uglySide.call(
        ritual, self._valueOf(groupAddress), self._valueOf(iface),
    )

  @overload(str, int, QIpPacketHeader)
  @overload(NoneType, int, QIpPacketHeader)
  def writeDatagram(
      self,
      data: Optional[str],
      len: int,
      a2: QIpPacketHeader,
  ) -> int:
    """
    Calls Qt's 'qint64 QHttpSocketEngine::writeDatagram(const char *data,
    qint64 len, const QIpPacketHeader &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#writeDatagram

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    a2 : QIpPacketHeader
      Passed on as a value: Qt reads the C++ QIpPacketHeader, which stays
      Python's own.
    """
    #  qint64 QHttpSocketEngine::writeDatagram(const char *data, qint64 len,
    #      const QIpPacketHeader &a2)
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine13writeDatagramEPKcxRK15QIpPacketHeade'
        'r',
        self._bytesOf(data), len, self._valueOf(a2),
    )

  @overload(QDeadlineTimer)
  def waitForProtocolHandshake(self, deadline: QDeadlineTimer) -> None:
    """
    Calls Qt's 'void
    QHttpSocketEngine::waitForProtocolHandshake(QDeadlineTimer deadline)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#waitForProtocolHandshake

    Parameters
    ----------

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  void QHttpSocketEngine::waitForProtocolHandshake(QDeadlineTimer
    #      deadline) const
    self.uglySide.call(
        'ritual_ZNK17QHttpSocketEngine24waitForProtocolHandshakeE14QDeadlin'
        'eTimer',
        self._valueOf(deadline),
    )

  def slotSocketConnected(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::slotSocketConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#slotSocketConnected
    """
    #  void QHttpSocketEngine::slotSocketConnected()
    self.uglySide.call('ritual_ZN17QHttpSocketEngine19slotSocketConnectedEv')

  def slotSocketDisconnected(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::slotSocketDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#slotSocketDisconnected
    """
    #  void QHttpSocketEngine::slotSocketDisconnected()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine22slotSocketDisconnectedEv',
    )

  def slotSocketReadNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::slotSocketReadNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#slotSocketReadNotification
    """
    #  void QHttpSocketEngine::slotSocketReadNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine26slotSocketReadNotificationEv',
    )

  def slotSocketBytesWritten(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::slotSocketBytesWritten()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#slotSocketBytesWritten
    """
    #  void QHttpSocketEngine::slotSocketBytesWritten()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine22slotSocketBytesWrittenEv',
    )

  @overload(QAbstractSocket.SocketError)
  def slotSocketError(self, error: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void
    QHttpSocketEngine::slotSocketError(QAbstractSocket::SocketError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#slotSocketError

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QHttpSocketEngine::slotSocketError(QAbstractSocket::SocketError
    #      error)
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine15slotSocketErrorEN15QAbstractSocket11'
        'SocketErrorE',
        error.value,
    )

  @overload(QAbstractSocket.SocketState)
  def slotSocketStateChanged(
      self,
      state: QAbstractSocket.SocketState,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpSocketEngine::slotSocketStateChanged(QAbstractSocket::SocketState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#slotSocketStateChanged

    Parameters
    ----------

    state : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QHttpSocketEngine::slotSocketStateChanged(QAbstractSocket::
    #      SocketState state)
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine22slotSocketStateChangedEN15QAbstractS'
        'ocket11SocketStateE',
        state.value,
    )

  def emitPendingReadNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::emitPendingReadNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#emitPendingReadNotification
    """
    #  void QHttpSocketEngine::emitPendingReadNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine27emitPendingReadNotificationEv',
    )

  def emitPendingWriteNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::emitPendingWriteNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html
    """
    #  void QHttpSocketEngine::emitPendingWriteNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine28emitPendingWriteNotificationEv',
    )

  def emitPendingConnectionNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::emitPendingConnectionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html
    """
    #  void QHttpSocketEngine::emitPendingConnectionNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine33emitPendingConnectionNotificationEv',
    )

  def emitReadNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::emitReadNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#emitReadNotification
    """
    #  void QHttpSocketEngine::emitReadNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine20emitReadNotificationEv',
    )

  def emitWriteNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::emitWriteNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#emitWriteNotification
    """
    #  void QHttpSocketEngine::emitWriteNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine21emitWriteNotificationEv',
    )

  def emitConnectionNotification(self) -> None:
    """
    Calls Qt's 'void QHttpSocketEngine::emitConnectionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#emitConnectionNotification
    """
    #  void QHttpSocketEngine::emitConnectionNotification()
    self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine26emitConnectionNotificationEv',
    )

  def readHttpHeader(self) -> bool:
    """
    Calls Qt's 'bool QHttpSocketEngine::readHttpHeader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketengine.html#readHttpHeader
    """
    #  bool QHttpSocketEngine::readHttpHeader()
    return self.uglySide.call(
        'ritual_ZN17QHttpSocketEngine14readHttpHeaderEv',
    )

  def d_func(self) -> Optional[QHttpSocketEnginePrivate]:
    """
    Calls Qt's 'QHttpSocketEnginePrivate *QHttpSocketEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpsocketengine.html#d_func

    Returns
    -------

    Optional[QHttpSocketEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpSocketEnginePrivate *QHttpSocketEngine::d_func()
    address = self.uglySide.call('ritual_ZN17QHttpSocketEngine6d_funcEv')
    from . import QHttpSocketEnginePrivate
    return QHttpSocketEnginePrivate._cuteAt(address)

  @staticmethod
  def connectInternal(*__, **_) -> Never:
    """
    Qt's 'bool QHttpSocketEngine::connectInternal()': leans on
    'QHttpSocketEngine::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpSocketEngine.connectInternal' has no cute function yet. Qt's "
        "'bool QHttpSocketEngine::connectInternal()': leans on "
        "'QHttpSocketEngine::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
