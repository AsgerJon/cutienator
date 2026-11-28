"""
QSocks5SocketEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSocks5SocketEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractSocket, QAbstractSocketEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHostAddress, QIpPacketHeader, QNetworkInterface
  from . import QNetworkProxy, QSocks5SocketEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QIpPacketHeader = WAIT['QIpPacketHeader']
  QNetworkInterface = WAIT['QNetworkInterface']
  QNetworkProxy = WAIT['QNetworkProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSocks5SocketEngine(QAbstractSocketEngine):
  """
  The cute side of Qt's QSocks5SocketEngine: a plain Python object standing
  in front of one C++ QSocks5SocketEngine.

  It is built on the cute 'QAbstractSocketEngine', as Qt's
  QSocks5SocketEngine is built on Qt's QAbstractSocketEngine, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSocks5SocketEngine that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'initialize',
  'setProxy', 'socketDescriptor', 'isValid', 'connectToHost',
  'connectToHostByName', 'bind', 'listen', 'accept', 'close',
  'bytesAvailable', 'write', 'joinMulticastGroup', 'leaveMulticastGroup',
  'multicastInterface', 'setMulticastInterface', 'hasPendingDatagrams',
  'pendingDatagramSize', 'writeDatagram', 'bytesToWrite', 'option',
  'setOption', 'isReadNotificationEnabled', 'setReadNotificationEnabled',
  'isWriteNotificationEnabled', 'setWriteNotificationEnabled',
  'isExceptionNotificationEnabled', 'setExceptionNotificationEnabled',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSocks5SocketEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSocks5SocketEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'qint64 QSocks5SocketEngine::read(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QSocks5SocketEngine::readDatagram(char *data, qint64 maxlen,
    QIpPacketHeader *a2, PacketHeaderOptions a3)': names 'char', which has no
    cute class yet.
  - Qt's 'bool QSocks5SocketEngine::waitForRead(QDeadlineTimer deadline, bool
    *timedOut)': takes a number to change where it is.
  - Qt's 'bool QSocks5SocketEngine::waitForWrite(QDeadlineTimer deadline,
    bool *timedOut)': takes a number to change where it is.
  - Qt's 'bool QSocks5SocketEngine::waitForReadOrWrite(bool *readyToRead,
    bool *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer
    deadline, bool *timedOut)': takes a number to change where it is.
  - Qt's 'const QSocks5SocketEnginePrivate *QSocks5SocketEngine::d_func()
    const': takes in Python what 'QSocks5SocketEnginePrivate
    *QSocks5SocketEngine::d_func()' takes.

  What has no ritual
  ------------------

  10 of the 49 functions Qt declares: 4 forbidden; 2 not a gap; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 2 leans on 'QSocks5SocketEngine.

  What to expect
  --------------

  - The C++ QSocks5SocketEngine is created at the first use, not by
    'QSocks5SocketEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSocks5SocketEngine.
  - Qt tells when it has removed the C++ QSocks5SocketEngine. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSocks5SocketEngine that has no cute function yet,
    '__init__', 'connectInternal', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSocks5SocketEngine'

  #  A C++ QSocks5SocketEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSocks5SocketEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSocks5SocketEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSocks5SocketEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QSocks5SocketEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QSocks5SocketEngine::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#socketDescriptor
    """
    #  qintptr QSocks5SocketEngine::socketDescriptor() const
    ritual = 'ritual_ZNK19QSocks5SocketEngine16socketDescriptorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSocks5SocketEngine16socketDescriptorEv'
    return self.uglySide.call(ritual)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#isValid
    """
    #  bool QSocks5SocketEngine::isValid() const
    ritual = 'ritual_ZNK19QSocks5SocketEngine7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSocks5SocketEngine7isValidEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QSocks5SocketEngine::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#bytesAvailable
    """
    #  qint64 QSocks5SocketEngine::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK19QSocks5SocketEngine14bytesAvailableEv',
    )

  def multicastInterface(self) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QSocks5SocketEngine::multicastInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#multicastInterface

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QSocks5SocketEngine::multicastInterface() const
    ritual = 'ritual_ZNK19QSocks5SocketEngine18multicastInterfaceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSocks5SocketEngine18multicastInterfaceEv'
    address = self.uglySide.call(ritual)
    from . import QNetworkInterface
    return QNetworkInterface._cuteOwning(address)

  def hasPendingDatagrams(self) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::hasPendingDatagrams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#hasPendingDatagrams
    """
    #  bool QSocks5SocketEngine::hasPendingDatagrams() const
    return self.uglySide.call(
        'ritual_ZNK19QSocks5SocketEngine19hasPendingDatagramsEv',
    )

  def pendingDatagramSize(self) -> int:
    """
    Calls Qt's 'qint64 QSocks5SocketEngine::pendingDatagramSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#pendingDatagramSize
    """
    #  qint64 QSocks5SocketEngine::pendingDatagramSize() const
    return self.uglySide.call(
        'ritual_ZNK19QSocks5SocketEngine19pendingDatagramSizeEv',
    )

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QSocks5SocketEngine::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#bytesToWrite
    """
    #  qint64 QSocks5SocketEngine::bytesToWrite() const
    ritual = 'ritual_ZNK19QSocks5SocketEngine12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSocks5SocketEngine12bytesToWriteEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractSocketEngine.SocketOption)
  def option(self, option: QAbstractSocketEngine.SocketOption) -> int:
    """
    Calls Qt's 'int QSocks5SocketEngine::option(SocketOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#option

    Parameters
    ----------

    option : QAbstractSocketEngine.SocketOption
      Passed on as its number.
    """
    #  int QSocks5SocketEngine::option(SocketOption option) const
    ritual = (
        'ritual_ZNK19QSocks5SocketEngine6optionEN21QAbstractSocketEngine12S'
        'ocketOptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QSocks5SocketEngine6optionEN21QAbstractSocketEng'
          'ine12SocketOptionE')
    return self.uglySide.call(ritual, option.value)

  def isReadNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::isReadNotificationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#isReadNotificationEnabled
    """
    #  bool QSocks5SocketEngine::isReadNotificationEnabled() const
    ritual = 'ritual_ZNK19QSocks5SocketEngine25isReadNotificationEnabledEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QSocks5SocketEngine25isReadNotificationEnabledEv')
    return self.uglySide.call(ritual)

  def isWriteNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::isWriteNotificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html
    """
    #  bool QSocks5SocketEngine::isWriteNotificationEnabled() const
    ritual = 'ritual_ZNK19QSocks5SocketEngine26isWriteNotificationEnabledEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QSocks5SocketEngine26isWriteNotificationEnabledE'
          'v')
    return self.uglySide.call(ritual)

  def isExceptionNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::isExceptionNotificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html
    """
    #  bool QSocks5SocketEngine::isExceptionNotificationEnabled() const
    ritual = (
        'ritual_ZNK19QSocks5SocketEngine30isExceptionNotificationEnabledEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QSocks5SocketEngine30isExceptionNotificationEnab'
          'ledEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QSocks5SocketEngine::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QSocks5SocketEngine::setProxy(const QNetworkProxy &networkProxy)
    self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(QNetworkInterface)
  def setMulticastInterface(self, iface: QNetworkInterface) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::setMulticastInterface(const
    QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#setMulticastInterface

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QSocks5SocketEngine::setMulticastInterface(const
    #      QNetworkInterface &iface)
    ritual = (
        'ritual_ZN19QSocks5SocketEngine21setMulticastInterfaceERK17QNetwork'
        'Interface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSocks5SocketEngine21setMulticastInterfaceERK17QN'
          'etworkInterface')
    return self.uglySide.call(ritual, self._valueOf(iface))

  @overload(QAbstractSocketEngine.SocketOption, int)
  def setOption(
      self,
      option: QAbstractSocketEngine.SocketOption,
      value: int,
  ) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::setOption(SocketOption option, int
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#setOption

    Parameters
    ----------

    option : QAbstractSocketEngine.SocketOption
      Passed on as its number.

    value : int
      Passed on as it is.
    """
    #  bool QSocks5SocketEngine::setOption(SocketOption option, int value)
    ritual = (
        'ritual_ZN19QSocks5SocketEngine9setOptionEN21QAbstractSocketEngine1'
        '2SocketOptionEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSocks5SocketEngine9setOptionEN21QAbstractSocketE'
          'ngine12SocketOptionEi')
    return self.uglySide.call(ritual, option.value, value)

  @overload(bool)
  def setReadNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSocks5SocketEngine::setReadNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSocks5SocketEngine::setReadNotificationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine26setReadNotificationEnabledEb',
        enable,
    )

  @overload(bool)
  def setWriteNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSocks5SocketEngine::setWriteNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSocks5SocketEngine::setWriteNotificationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine27setWriteNotificationEnabledEb',
        enable,
    )

  @overload(bool)
  def setExceptionNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QSocks5SocketEngine::setExceptionNotificationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSocks5SocketEngine::setExceptionNotificationEnabled(bool enable)
    ritual = (
        'ritual_ZN19QSocks5SocketEngine31setExceptionNotificationEnabledEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSocks5SocketEngine31setExceptionNotificationEnab'
          'ledEb')
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
    Qt's 'QSocks5SocketEngine::QSocks5SocketEngine(QObject *parent)': leans
    on 'QSocks5SocketEngine::initialize(QAbstractSocket::SocketType,
    QAbstractSocket::NetworkLayerProtocol)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSocks5SocketEngine.__init__' has no cute function yet. Qt's "
        "'QSocks5SocketEngine::QSocks5SocketEngine(QObject *parent)': leans "
        "on 'QSocks5SocketEngine::initialize(QAbstractSocket::SocketType, "
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
    QSocks5SocketEngine::initialize(QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#initialize

    Parameters
    ----------

    type : QAbstractSocket.SocketType
      Passed on as its number.

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.NetworkLayerProtocol.IPv4Protocol.
    """
    #  bool QSocks5SocketEngine::initialize(QAbstractSocket::SocketType type,
    #      QAbstractSocket::NetworkLayerProtocol protocol)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine10initializeEN15QAbstractSocket10Soc'
        'ketTypeENS0_20NetworkLayerProtocolE',
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
    Calls Qt's 'bool QSocks5SocketEngine::initialize(qintptr
    socketDescriptor, QAbstractSocket::SocketState socketState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#initialize

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    socketState : QAbstractSocket.SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.SocketState.ConnectedState.
    """
    #  bool QSocks5SocketEngine::initialize(qintptr socketDescriptor,
    #      QAbstractSocket::SocketState socketState)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine10initializeExN15QAbstractSocket11So'
        'cketStateE',
        socketDescriptor, socketState.value,
    )

  @overload(QHostAddress, int)
  def connectToHost(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::connectToHost(const QHostAddress
    &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#connectToHost

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QSocks5SocketEngine::connectToHost(const QHostAddress &address,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine13connectToHostERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(str, int)
  def connectToHostByName(self, name: str, port: int) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::connectToHostByName(const QString
    &name, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#connectToHostByName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  bool QSocks5SocketEngine::connectToHostByName(const QString &name,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine19connectToHostByNameERK7QStringt',
        name, port,
    )

  @overload(QHostAddress, int)
  def bind(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::bind(const QHostAddress &address,
    quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#bind

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QSocks5SocketEngine::bind(const QHostAddress &address, quint16
    #      port)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine4bindERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(int)
  def listen(self, backlog: int) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::listen(int backlog)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#listen

    Parameters
    ----------

    backlog : int
      Passed on as it is.
    """
    #  bool QSocks5SocketEngine::listen(int backlog)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine6listenEi', backlog,
    )

  def accept(self) -> int:
    """
    Calls Qt's 'qintptr QSocks5SocketEngine::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#accept
    """
    #  qintptr QSocks5SocketEngine::accept()
    return self.uglySide.call('ritual_ZN19QSocks5SocketEngine6acceptEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QSocks5SocketEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#close
    """
    #  void QSocks5SocketEngine::close()
    self.uglySide.call('ritual_ZN19QSocks5SocketEngine5closeEv')

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QSocks5SocketEngine::write(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QSocks5SocketEngine::write(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine5writeEPKcx',
        self._bytesOf(data), len,
    )

  @overload(QHostAddress, QNetworkInterface)
  def joinMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QSocks5SocketEngine::joinMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#joinMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QSocks5SocketEngine::joinMulticastGroup(const QHostAddress
    #      &groupAddress, const QNetworkInterface &iface)
    ritual = (
        'ritual_ZN19QSocks5SocketEngine18joinMulticastGroupERK12QHostAddres'
        'sRK17QNetworkInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSocks5SocketEngine18joinMulticastGroupERK12QHost'
          'AddressRK17QNetworkInterface')
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
    Calls Qt's 'bool QSocks5SocketEngine::leaveMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#leaveMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QSocks5SocketEngine::leaveMulticastGroup(const QHostAddress
    #      &groupAddress, const QNetworkInterface &iface)
    ritual = (
        'ritual_ZN19QSocks5SocketEngine19leaveMulticastGroupERK12QHostAddre'
        'ssRK17QNetworkInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSocks5SocketEngine19leaveMulticastGroupERK12QHos'
          'tAddressRK17QNetworkInterface')
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
    Calls Qt's 'qint64 QSocks5SocketEngine::writeDatagram(const char *data,
    qint64 len, const QIpPacketHeader &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengine.html#writeDatagram

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
    #  qint64 QSocks5SocketEngine::writeDatagram(const char *data, qint64
    #      len, const QIpPacketHeader &a2)
    return self.uglySide.call(
        'ritual_ZN19QSocks5SocketEngine13writeDatagramEPKcxRK15QIpPacketHea'
        'der',
        self._bytesOf(data), len, self._valueOf(a2),
    )

  def d_func(self) -> Optional[QSocks5SocketEnginePrivate]:
    """
    Calls Qt's 'QSocks5SocketEnginePrivate *QSocks5SocketEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5socketengine.html#d_func

    Returns
    -------

    Optional[QSocks5SocketEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSocks5SocketEnginePrivate *QSocks5SocketEngine::d_func()
    address = self.uglySide.call('ritual_ZN19QSocks5SocketEngine6d_funcEv')
    from . import QSocks5SocketEnginePrivate
    return QSocks5SocketEnginePrivate._cuteAt(address)

  @staticmethod
  def connectInternal(*__, **_) -> Never:
    """
    Qt's 'bool QSocks5SocketEngine::connectInternal()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QSocks5Data'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEngine.connectInternal' has no cute function yet. "
        "Qt's 'bool QSocks5SocketEngine::connectInternal()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QSocks5Data'.")
