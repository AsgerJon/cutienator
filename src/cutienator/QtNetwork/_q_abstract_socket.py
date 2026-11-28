"""
QAbstractSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qabstractsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QIODevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QAbstractSocketPrivate, QAuthenticator, QHostAddress
  from . import QNetworkProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QHostAddress = WAIT['QHostAddress']
  QNetworkProxy = WAIT['QNetworkProxy']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSocket(QIODevice):
  """
  The cute side of Qt's QAbstractSocket: a plain Python object standing in
  front of one C++ QAbstractSocket.

  It is built on the cute 'QIODevice', as Qt's QAbstractSocket is built on
  Qt's QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSocket that has a ritual and that Python
  can call so far, 53 names in all: 'metaObject', 'tr', 'resume',
  'pauseMode', 'setPauseMode', 'bind', 'connectToHost', 'disconnectFromHost',
  'isValid', 'bytesAvailable', 'bytesToWrite', 'localPort', 'localAddress',
  'peerPort', 'peerAddress', 'peerName', 'readBufferSize',
  'setReadBufferSize', 'abort', 'socketDescriptor', 'setSocketDescriptor',
  'setSocketOption', 'socketOption', 'socketType', 'state', 'error', 'close',
  'isSequential', 'flush', 'waitForConnected', 'waitForReadyRead',
  'waitForBytesWritten', 'waitForDisconnected', 'setProxy', 'proxy',
  'protocolTag', 'setProtocolTag', 'hostFound', 'connected', 'disconnected',
  'stateChanged', 'errorOccurred', 'proxyAuthenticationRequired', 'skipData',
  'writeData', 'setSocketState', 'setSocketError', 'setLocalPort',
  'setLocalAddress', 'setPeerPort', 'setPeerAddress', 'setPeerName',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractSocket::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractSocket::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractSocket::~QAbstractSocket()': the destructor: Python never
    removes a C++ QAbstractSocket.
  - Qt's 'qint64 QAbstractSocket::readData(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QAbstractSocket::readLineData(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'QAbstractSocket::QAbstractSocket(SocketType socketType,
    QAbstractSocketPrivate &dd, QObject *parent)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QAbstractSocketPrivate *QAbstractSocket::d_func() const':
    takes in Python what 'QAbstractSocketPrivate *QAbstractSocket::d_func()'
    takes.

  What has no ritual
  ------------------

  6 of the 69 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractSocket is created at the first use, not by
    'QAbstractSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSocket.
  - Qt tells when it has removed the C++ QAbstractSocket. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractSocket, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BindFlag(CuteFlags):
    """
    The flags enum 'QAbstractSocket::BindFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QAbstractSocket::BindMode'.
    """

    DefaultForPlatform = 0x0
    ShareAddress = 0x1
    DontShareAddress = 0x2
    ReuseAddressHint = 0x4

  BindMode = BindFlag

  class NetworkLayerProtocol(CuteNum):
    """
    The enum 'QAbstractSocket::NetworkLayerProtocol' of Qt, with the 4 names
    Qt gives in it.
    """

    IPv4Protocol = Kee[int](0)
    IPv6Protocol = Kee[int](1)
    AnyIPProtocol = Kee[int](2)
    UnknownNetworkLayerProtocol = Kee[int](-1)

  class PauseMode(CuteFlags):
    """
    The flags enum 'QAbstractSocket::PauseMode' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QAbstractSocket::PauseModes'.
    """

    PauseNever = 0x0
    PauseOnSslErrors = 0x1

  PauseModes = PauseMode

  class SocketError(CuteNum):
    """
    The enum 'QAbstractSocket::SocketError' of Qt, with the 24 names Qt gives
    in it.
    """

    ConnectionRefusedError = Kee[int](0)
    RemoteHostClosedError = Kee[int](1)
    HostNotFoundError = Kee[int](2)
    SocketAccessError = Kee[int](3)
    SocketResourceError = Kee[int](4)
    SocketTimeoutError = Kee[int](5)
    DatagramTooLargeError = Kee[int](6)
    NetworkError = Kee[int](7)
    AddressInUseError = Kee[int](8)
    SocketAddressNotAvailableError = Kee[int](9)
    UnsupportedSocketOperationError = Kee[int](10)
    UnfinishedSocketOperationError = Kee[int](11)
    ProxyAuthenticationRequiredError = Kee[int](12)
    SslHandshakeFailedError = Kee[int](13)
    ProxyConnectionRefusedError = Kee[int](14)
    ProxyConnectionClosedError = Kee[int](15)
    ProxyConnectionTimeoutError = Kee[int](16)
    ProxyNotFoundError = Kee[int](17)
    ProxyProtocolError = Kee[int](18)
    OperationError = Kee[int](19)
    SslInternalError = Kee[int](20)
    SslInvalidUserDataError = Kee[int](21)
    TemporaryError = Kee[int](22)
    UnknownSocketError = Kee[int](-1)

  class SocketOption(CuteNum):
    """
    The enum 'QAbstractSocket::SocketOption' of Qt, with the 11 names Qt
    gives in it.
    """

    LowDelayOption = Kee[int](0)
    KeepAliveOption = Kee[int](1)
    MulticastTtlOption = Kee[int](2)
    MulticastLoopbackOption = Kee[int](3)
    TypeOfServiceOption = Kee[int](4)
    SendBufferSizeSocketOption = Kee[int](5)
    ReceiveBufferSizeSocketOption = Kee[int](6)
    PathMtuSocketOption = Kee[int](7)
    KeepAliveIdleOption = Kee[int](8)
    KeepAliveIntervalOption = Kee[int](9)
    KeepAliveCountOption = Kee[int](10)

  class SocketState(CuteNum):
    """
    The enum 'QAbstractSocket::SocketState' of Qt, with the 7 names Qt gives
    in it.
    """

    UnconnectedState = Kee[int](0)
    HostLookupState = Kee[int](1)
    ConnectingState = Kee[int](2)
    ConnectedState = Kee[int](3)
    BoundState = Kee[int](4)
    ListeningState = Kee[int](5)
    ClosingState = Kee[int](6)

  class SocketType(CuteNum):
    """
    The enum 'QAbstractSocket::SocketType' of Qt, with the 4 names Qt gives
    in it.
    """

    TcpSocket = Kee[int](0)
    UdpSocket = Kee[int](1)
    SctpSocket = Kee[int](2)
    UnknownSocketType = Kee[int](-1)

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
    Calls Qt's 'QString QAbstractSocket::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#tr

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
    #  QString QAbstractSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstractSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSocket'

  #  A C++ QAbstractSocket Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSocket'

  #  The functions Qt calls itself that QAbstractSocket is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'resume': (
          ('_ZN15QAbstractSocket6resumeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bind': (
          ('_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindFlag'
           'EE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('unsigned short', 'number', ''),
               ('int', 'flags', 'QtNetwork:QAbstractSocket.BindFlag'),
           )),
      ),
      'connectToHost': (
          ('_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QIODe'
           'viceBase12OpenModeFlagEENS_20NetworkLayerProtocolE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('unsigned short', 'number', ''),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
               ('int', 'enum',
                'QtNetwork:QAbstractSocket.NetworkLayerProtocol'),
           )),
      ),
      'disconnectFromHost': (
          ('_ZN15QAbstractSocket18disconnectFromHostEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setReadBufferSize': (
          ('_ZN15QAbstractSocket17setReadBufferSizeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'socketDescriptor': (
          ('_ZNK15QAbstractSocket16socketDescriptorEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setSocketDescriptor': (
          ('_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE6QF'
           'lagsIN13QIODeviceBase12OpenModeFlagEE',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
               ('int', 'enum', 'QtNetwork:QAbstractSocket.SocketState'),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
           )),
      ),
      'setSocketOption': (
          ('_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8QVar'
           'iant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtNetwork:QAbstractSocket.SocketOption'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'socketOption': (
          ('_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtNetwork:QAbstractSocket.SocketOption'),
           )),
      ),
      'waitForConnected': (
          ('_ZN15QAbstractSocket16waitForConnectedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'waitForDisconnected': (
          ('_ZN15QAbstractSocket19waitForDisconnectedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSocket::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSocket10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pauseMode(self) -> PauseModes:
    """
    Calls Qt's 'PauseModes QAbstractSocket::pauseMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#pauseMode

    Returns
    -------

    PauseModes
      The value standing for the combination Qt gave back.
    """
    #  PauseModes QAbstractSocket::pauseMode() const
    return QAbstractSocket.PauseModes(self.uglySide.call(
        'ritual_ZNK15QAbstractSocket9pauseModeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#isValid
    """
    #  bool QAbstractSocket::isValid() const
    return self.uglySide.call('ritual_ZNK15QAbstractSocket7isValidEv')

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocket::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#bytesAvailable
    """
    #  qint64 QAbstractSocket::bytesAvailable() const
    ritual = 'ritual_ZNK15QAbstractSocket14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAbstractSocket14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocket::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#bytesToWrite
    """
    #  qint64 QAbstractSocket::bytesToWrite() const
    ritual = 'ritual_ZNK15QAbstractSocket12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAbstractSocket12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QAbstractSocket::localPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#localPort
    """
    #  quint16 QAbstractSocket::localPort() const
    return self.uglySide.call('ritual_ZNK15QAbstractSocket9localPortEv')

  def localAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QAbstractSocket::localAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#localAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QAbstractSocket::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK15QAbstractSocket12localAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QAbstractSocket::peerPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#peerPort
    """
    #  quint16 QAbstractSocket::peerPort() const
    return self.uglySide.call('ritual_ZNK15QAbstractSocket8peerPortEv')

  def peerAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QAbstractSocket::peerAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#peerAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QAbstractSocket::peerAddress() const
    address = self.uglySide.call(
        'ritual_ZNK15QAbstractSocket11peerAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def peerName(self) -> str:
    """
    Calls Qt's 'QString QAbstractSocket::peerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#peerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSocket::peerName() const
    return self.uglySide.call('ritual_ZNK15QAbstractSocket8peerNameEv')

  def readBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocket::readBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#readBufferSize
    """
    #  qint64 QAbstractSocket::readBufferSize() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractSocket14readBufferSizeEv',
    )

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QAbstractSocket::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#socketDescriptor
    """
    #  qintptr QAbstractSocket::socketDescriptor() const
    ritual = 'ritual_ZNK15QAbstractSocket16socketDescriptorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAbstractSocket16socketDescriptorEv'
    return self.uglySide.call(ritual)

  def socketType(self) -> SocketType:
    """
    Calls Qt's 'SocketType QAbstractSocket::socketType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#socketType

    Returns
    -------

    SocketType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SocketType(number)'
      gives.
    """
    #  SocketType QAbstractSocket::socketType() const
    return QAbstractSocket.SocketType(self.uglySide.call(
        'ritual_ZNK15QAbstractSocket10socketTypeEv',
    ))

  def state(self) -> SocketState:
    """
    Calls Qt's 'SocketState QAbstractSocket::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#state

    Returns
    -------

    SocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SocketState(number)'
      gives.
    """
    #  SocketState QAbstractSocket::state() const
    return QAbstractSocket.SocketState(self.uglySide.call(
        'ritual_ZNK15QAbstractSocket5stateEv',
    ))

  def error(self) -> SocketError:
    """
    Calls Qt's 'SocketError QAbstractSocket::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#error

    Returns
    -------

    SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SocketError(number)'
      gives.
    """
    #  SocketError QAbstractSocket::error() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK15QAbstractSocket5errorEv',
    ))

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#isSequential
    """
    #  bool QAbstractSocket::isSequential() const
    ritual = 'ritual_ZNK15QAbstractSocket12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAbstractSocket12isSequentialEv'
    return self.uglySide.call(ritual)

  def proxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QAbstractSocket::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#proxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QAbstractSocket::proxy() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSocket5proxyEv')
    from . import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def protocolTag(self) -> str:
    """
    Calls Qt's 'QString QAbstractSocket::protocolTag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#protocolTag

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSocket::protocolTag() const
    return self.uglySide.call('ritual_ZNK15QAbstractSocket11protocolTagEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PauseModes)
  def setPauseMode(self, pauseMode: PauseModes) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setPauseMode(PauseModes pauseMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#setPauseMode

    Parameters
    ----------

    pauseMode : PauseModes
      Passed on as its number.
    """
    #  void QAbstractSocket::setPauseMode(PauseModes pauseMode)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket12setPauseModeE6QFlagsINS_9PauseModeEE',
        pauseMode.value,
    )

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setReadBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QAbstractSocket::setReadBufferSize(qint64 size)
    ritual = 'ritual_ZN15QAbstractSocket17setReadBufferSizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket17setReadBufferSizeEx'
    self.uglySide.call(ritual, size)

  @overload(int)
  @overload(int, SocketState)
  @overload(int, SocketState, QIODeviceBase.OpenMode)
  def setSocketDescriptor(
      self,
      socketDescriptor: int,
      state: SocketState = SocketState.ConnectedState,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::setSocketDescriptor(qintptr
    socketDescriptor, SocketState state, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    state : SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      SocketState.ConnectedState.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QAbstractSocket::setSocketDescriptor(qintptr socketDescriptor,
    #      SocketState state, OpenMode openMode)
    ritual = (
        'ritual_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE'
        '6QFlagsIN13QIODeviceBase12OpenModeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractSocket19setSocketDescriptorExNS_11Socket'
          'StateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE')
    return self.uglySide.call(
        ritual, socketDescriptor, state.value, openMode.value,
    )

  @overload(SocketOption, QVariant)
  def setSocketOption(self, option: SocketOption, value: QVariant) -> None:
    """
    Calls Qt's 'void
    QAbstractSocket::setSocketOption(QAbstractSocket::SocketOption option,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setSocketOption

    Parameters
    ----------

    option : SocketOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractSocket::setSocketOption(QAbstractSocket::SocketOption
    #      option, const QVariant &value)
    ritual = (
        'ritual_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8Q'
        'Variant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptio'
          'nERK8QVariant')
    self.uglySide.call(ritual, option.value, self._valueOf(value))

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QAbstractSocket::setProxy(const QNetworkProxy &networkProxy)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(str)
  def setProtocolTag(self, tag: str) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setProtocolTag(const QString &tag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setProtocolTag

    Parameters
    ----------

    tag : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSocket::setProtocolTag(const QString &tag)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket14setProtocolTagERK7QString', tag,
    )

  @overload(SocketState)
  def setSocketState(self, state: SocketState) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setSocketState(SocketState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setSocketState

    Parameters
    ----------

    state : SocketState
      Passed on as its number.
    """
    #  void QAbstractSocket::setSocketState(SocketState state)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket14setSocketStateENS_11SocketStateE',
        state.value,
    )

  @overload(SocketError)
  def setSocketError(self, socketError: SocketError) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setSocketError(SocketError
    socketError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setSocketError

    Parameters
    ----------

    socketError : SocketError
      Passed on as its number.
    """
    #  void QAbstractSocket::setSocketError(SocketError socketError)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket14setSocketErrorENS_11SocketErrorE',
        socketError.value,
    )

  @overload(int)
  def setLocalPort(self, port: int) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setLocalPort(quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#setLocalPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QAbstractSocket::setLocalPort(quint16 port)
    self.uglySide.call('ritual_ZN15QAbstractSocket12setLocalPortEt', port)

  @overload(QHostAddress)
  def setLocalAddress(self, address: QHostAddress) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setLocalAddress(const QHostAddress
    &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setLocalAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QAbstractSocket::setLocalAddress(const QHostAddress &address)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket15setLocalAddressERK12QHostAddress',
        self._valueOf(address),
    )

  @overload(int)
  def setPeerPort(self, port: int) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setPeerPort(quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#setPeerPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QAbstractSocket::setPeerPort(quint16 port)
    self.uglySide.call('ritual_ZN15QAbstractSocket11setPeerPortEt', port)

  @overload(QHostAddress)
  def setPeerAddress(self, address: QHostAddress) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setPeerAddress(const QHostAddress
    &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#setPeerAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QAbstractSocket::setPeerAddress(const QHostAddress &address)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket14setPeerAddressERK12QHostAddress',
        self._valueOf(address),
    )

  @overload(str)
  def setPeerName(self, name: str) -> None:
    """
    Calls Qt's 'void QAbstractSocket::setPeerName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#setPeerName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSocket::setPeerName(const QString &name)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket11setPeerNameERK7QString', name,
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

  @overload(SocketType, QObject)
  @overload(SocketType, NoneType)
  def __init__(
      self,
      socketType: SocketType,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractSocket::QAbstractSocket(SocketType socketType, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#QAbstractSocket

    Parameters
    ----------

    socketType : SocketType
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractSocket::QAbstractSocket(SocketType socketType, QObject
    #      *parent)
    self._noteCreation(QAbstractSocket, lambda: Rituals.call(
        'ritual_ZN15QAbstractSocketC1ENS_10SocketTypeEP7QObject',
        socketType.value, self._addressOf(parent, 'QObject'),
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

  def resume(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#resume
    """
    #  void QAbstractSocket::resume()
    ritual = 'ritual_ZN15QAbstractSocket6resumeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket6resumeEv'
    self.uglySide.call(ritual)

  @overload(QHostAddress)
  @overload(QHostAddress, int)
  @overload(QHostAddress, int, BindMode)
  def bind(
      self,
      address: QHostAddress,
      port: int = 0,
      mode: BindMode = BindMode.DefaultForPlatform,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::bind(const QHostAddress &address,
    quint16 port, BindMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#bind

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    mode : BindMode
      Passed on as its number. May be left out, as in Qt: it is then
      BindMode.DefaultForPlatform.
    """
    #  bool QAbstractSocket::bind(const QHostAddress &address, quint16 port,
    #      BindMode mode)
    ritual = (
        'ritual_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindF'
        'lagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_'
          '8BindFlagEE')
    return self.uglySide.call(
        ritual, self._valueOf(address), port, mode.value,
    )

  @overload()
  @overload(int)
  @overload(int, BindMode)
  def bind(
      self,
      port: int = 0,
      mode: BindMode = BindMode.DefaultForPlatform,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::bind(quint16 port, BindMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#bind

    Parameters
    ----------

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    mode : BindMode
      Passed on as its number. May be left out, as in Qt: it is then
      BindMode.DefaultForPlatform.
    """
    #  bool QAbstractSocket::bind(quint16 port, BindMode mode)
    return self.uglySide.call(
        'ritual_ZN15QAbstractSocket4bindEt6QFlagsINS_8BindFlagEE',
        port, mode.value,
    )

  @overload(str, int)
  @overload(str, int, QIODeviceBase.OpenMode)
  @overload(str, int, QIODeviceBase.OpenMode, NetworkLayerProtocol)
  def connectToHost(
      self,
      hostName: str,
      port: int,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
      protocol: NetworkLayerProtocol = NetworkLayerProtocol.AnyIPProtocol,
  ) -> None:
    """
    Calls Qt's 'void QAbstractSocket::connectToHost(const QString &hostName,
    quint16 port, OpenMode mode, NetworkLayerProtocol protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#connectToHost

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.

    protocol : NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      NetworkLayerProtocol.AnyIPProtocol.
    """
    #  void QAbstractSocket::connectToHost(const QString &hostName, quint16
    #      port, OpenMode mode, NetworkLayerProtocol protocol)
    ritual = (
        'ritual_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QI'
        'ODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlags'
          'IN13QIODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE')
    self.uglySide.call(ritual, hostName, port, mode.value, protocol.value)

  @overload(QHostAddress, int)
  @overload(QHostAddress, int, QIODeviceBase.OpenMode)
  def connectToHost(
      self,
      address: QHostAddress,
      port: int,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QAbstractSocket::connectToHost(const QHostAddress
    &address, quint16 port, OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#connectToHost

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QAbstractSocket::connectToHost(const QHostAddress &address,
    #      quint16 port, OpenMode mode)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket13connectToHostERK12QHostAddresst6QFlags'
        'IN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, mode.value,
    )

  def disconnectFromHost(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::disconnectFromHost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#disconnectFromHost
    """
    #  void QAbstractSocket::disconnectFromHost()
    ritual = 'ritual_ZN15QAbstractSocket18disconnectFromHostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket18disconnectFromHostEv'
    self.uglySide.call(ritual)

  def abort(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#abort
    """
    #  void QAbstractSocket::abort()
    self.uglySide.call('ritual_ZN15QAbstractSocket5abortEv')

  @overload(SocketOption)
  def socketOption(self, option: SocketOption) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAbstractSocket::socketOption(QAbstractSocket::SocketOption option)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#socketOption

    Parameters
    ----------

    option : SocketOption
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractSocket::socketOption(QAbstractSocket::SocketOption
    #      option)
    ritual = 'ritual_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE')
    address = self.uglySide.call(ritual, option.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def close(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#close
    """
    #  void QAbstractSocket::close()
    ritual = 'ritual_ZN15QAbstractSocket5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket5closeEv'
    self.uglySide.call(ritual)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#flush
    """
    #  bool QAbstractSocket::flush()
    return self.uglySide.call('ritual_ZN15QAbstractSocket5flushEv')

  @overload()
  @overload(int)
  def waitForConnected(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::waitForConnected(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#waitForConnected

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QAbstractSocket::waitForConnected(int msecs)
    ritual = 'ritual_ZN15QAbstractSocket16waitForConnectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket16waitForConnectedEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::waitForReadyRead(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QAbstractSocket::waitForReadyRead(int msecs)
    ritual = 'ritual_ZN15QAbstractSocket16waitForReadyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket16waitForReadyReadEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::waitForBytesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QAbstractSocket::waitForBytesWritten(int msecs)
    ritual = 'ritual_ZN15QAbstractSocket19waitForBytesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket19waitForBytesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForDisconnected(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QAbstractSocket::waitForDisconnected(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#waitForDisconnected

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QAbstractSocket::waitForDisconnected(int msecs)
    ritual = 'ritual_ZN15QAbstractSocket19waitForDisconnectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket19waitForDisconnectedEi'
    return self.uglySide.call(ritual, msecs)

  def hostFound(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::hostFound()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#hostFound
    """
    #  void QAbstractSocket::hostFound()
    self.uglySide.call('ritual_ZN15QAbstractSocket9hostFoundEv')

  def connected(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#connected
    """
    #  void QAbstractSocket::connected()
    self.uglySide.call('ritual_ZN15QAbstractSocket9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QAbstractSocket::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#disconnected
    """
    #  void QAbstractSocket::disconnected()
    self.uglySide.call('ritual_ZN15QAbstractSocket12disconnectedEv')

  @overload(SocketState)
  def stateChanged(self, a0: SocketState) -> None:
    """
    Calls Qt's 'void
    QAbstractSocket::stateChanged(QAbstractSocket::SocketState a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#stateChanged

    Parameters
    ----------

    a0 : SocketState
      Passed on as its number.
    """
    #  void QAbstractSocket::stateChanged(QAbstractSocket::SocketState a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket12stateChangedENS_11SocketStateE',
        a0.value,
    )

  @overload(SocketError)
  def errorOccurred(self, a0: SocketError) -> None:
    """
    Calls Qt's 'void
    QAbstractSocket::errorOccurred(QAbstractSocket::SocketError a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#errorOccurred

    Parameters
    ----------

    a0 : SocketError
      Passed on as its number.
    """
    #  void QAbstractSocket::errorOccurred(QAbstractSocket::SocketError a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket13errorOccurredENS_11SocketErrorE',
        a0.value,
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QAbstractSocket::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocket.html#proxyAuthenticationRequired

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSocket::proxyAuthenticationRequired(const QNetworkProxy
    #      &proxy, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN15QAbstractSocket27proxyAuthenticationRequiredERK13QNetwo'
        'rkProxyP14QAuthenticator',
        self._valueOf(proxy), self._addressOf(authenticator),
    )

  @overload(int)
  def skipData(self, maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocket::skipData(qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#skipData

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QAbstractSocket::skipData(qint64 maxSize)
    ritual = 'ritual_ZN15QAbstractSocket8skipDataEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSocket8skipDataEx'
    return self.uglySide.call(ritual, maxSize)

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocket::writeData(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QAbstractSocket::writeData(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN15QAbstractSocket9writeDataEPKcx',
        self._bytesOf(data), len,
    )

  def d_func(self) -> Optional[QAbstractSocketPrivate]:
    """
    Calls Qt's 'QAbstractSocketPrivate *QAbstractSocket::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocket.html#d_func

    Returns
    -------

    Optional[QAbstractSocketPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSocketPrivate *QAbstractSocket::d_func()
    address = self.uglySide.call('ritual_ZN15QAbstractSocket6d_funcEv')
    from . import QAbstractSocketPrivate
    return QAbstractSocketPrivate._cuteAt(address)
