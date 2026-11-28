"""
QAbstractSocketEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractSocketEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..QtCore import QObject
from . import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstractSocketEnginePrivate, QAbstractSocketEngineReceiver
  from . import QAuthenticator, QHostAddress, QIpPacketHeader
  from . import QNetworkInterface, QNetworkProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractSocketEngineReceiver = WAIT['QAbstractSocketEngineReceiver']
  QAuthenticator = WAIT['QAuthenticator']
  QHostAddress = WAIT['QHostAddress']
  QIpPacketHeader = WAIT['QIpPacketHeader']
  QNetworkInterface = WAIT['QNetworkInterface']
  QNetworkProxy = WAIT['QNetworkProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSocketEngine(QObject):
  """
  The cute side of Qt's QAbstractSocketEngine: a plain Python object standing
  in front of one C++ QAbstractSocketEngine.

  It is built on the cute 'QObject', as Qt's QAbstractSocketEngine is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSocketEngine that has a ritual and that
  Python can call so far, 55 names in all: 'metaObject', 'initialize',
  'socketDescriptor', 'isValid', 'connectToHost', 'connectToHostByName',
  'bind', 'listen', 'accept', 'close', 'bytesAvailable', 'write',
  'joinMulticastGroup', 'leaveMulticastGroup', 'multicastInterface',
  'setMulticastInterface', 'hasPendingDatagrams', 'pendingDatagramSize',
  'writeDatagram', 'bytesToWrite', 'option', 'setOption', 'error',
  'errorString', 'state', 'socketType', 'protocol', 'localAddress',
  'localPort', 'peerAddress', 'peerPort', 'inboundStreamCount',
  'outboundStreamCount', 'isReadNotificationEnabled',
  'setReadNotificationEnabled', 'isWriteNotificationEnabled',
  'setWriteNotificationEnabled', 'isExceptionNotificationEnabled',
  'setExceptionNotificationEnabled', 'readNotification', 'writeNotification',
  'closeNotification', 'exceptionNotification', 'connectionNotification',
  'proxyAuthenticationRequired', 'setReceiver', 'setError', 'setState',
  'setSocketType', 'setProtocol', 'setLocalAddress', 'setLocalPort',
  'setPeerAddress', 'setPeerPort', 'd_func'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractSocketEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractSocketEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qint64 QAbstractSocketEngine::read(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'qint64 QAbstractSocketEngine::readDatagram(char *data, qint64
    maxlen, QIpPacketHeader *header, PacketHeaderOptions a3)': names 'char',
    which has no cute class yet.
  - Qt's 'bool QAbstractSocketEngine::waitForRead(QDeadlineTimer deadline,
    bool *timedOut)': takes a number to change where it is.
  - Qt's 'bool QAbstractSocketEngine::waitForWrite(QDeadlineTimer deadline,
    bool *timedOut)': takes a number to change where it is.
  - Qt's 'bool QAbstractSocketEngine::waitForReadOrWrite(bool *readyToRead,
    bool *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer
    deadline, bool *timedOut)': takes a number to change where it is.
  - Qt's 'const QAbstractSocketEnginePrivate *QAbstractSocketEngine::d_func()
    const': takes in Python what 'QAbstractSocketEnginePrivate
    *QAbstractSocketEngine::d_func()' takes.

  What has no ritual
  ------------------

  11 of the 75 functions Qt declares: 4 forbidden; 2 not a gap; 2 the class
  is abstract, so C++ cannot make one, and the C++ class of ours does not
  fill in every function it leaves open; 2 Qt's library has no name for it,
  and its code in Qt's source does not compile apart from its file; 1 leans
  on 'QAbstractSocketEngine.

  What to expect
  --------------

  - The C++ QAbstractSocketEngine is created at the first use, not by
    'QAbstractSocketEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSocketEngine.
  - Qt tells when it has removed the C++ QAbstractSocketEngine. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractSocketEngine that has no cute function yet,
    '__init__', 'createSocketEngine', 'read', 'readDatagram', 'waitForRead',
    'waitForReadOrWrite', 'waitForWrite', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractSocketEngine, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class PacketHeaderOption(CuteFlags):
    """
    The flags enum 'QAbstractSocketEngine::PacketHeaderOption' of Qt, with
    the 7 names Qt gives in it. Qt names the type of its combinations
    'QAbstractSocketEngine::PacketHeaderOptions'.
    """

    WantNone = 0x0
    WantDatagramSender = 0x1
    WantDatagramDestination = 0x2
    WantDatagramHopLimit = 0x4
    WantStreamNumber = 0x8
    WantEndOfRecord = 0x10
    WantAll = 0xff

  PacketHeaderOptions = PacketHeaderOption

  class SocketOption(CuteNum):
    """
    The enum 'QAbstractSocketEngine::SocketOption' of Qt, with the 20 names
    Qt gives in it.
    """

    NonBlockingSocketOption = Kee[int](0)
    BroadcastSocketOption = Kee[int](1)
    ReceiveBufferSocketOption = Kee[int](2)
    SendBufferSocketOption = Kee[int](3)
    AddressReusable = Kee[int](4)
    BindExclusively = Kee[int](5)
    ReceiveOutOfBandData = Kee[int](6)
    LowDelayOption = Kee[int](7)
    KeepAliveOption = Kee[int](8)
    MulticastTtlOption = Kee[int](9)
    MulticastLoopbackOption = Kee[int](10)
    TypeOfServiceOption = Kee[int](11)
    ReceivePacketInformation = Kee[int](12)
    ReceiveHopLimit = Kee[int](13)
    MaxStreamsSocketOption = Kee[int](14)
    PathMtuInformation = Kee[int](15)
    BindInterfaceIndex = Kee[int](16)
    KeepAliveIdleOption = Kee[int](17)
    KeepAliveIntervalOption = Kee[int](18)
    KeepAliveCountOption = Kee[int](19)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSocketEngine'

  #  The functions Qt calls itself that QAbstractSocketEngine is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'read': (
          'qint64 QAbstractSocketEngine::read(char *, qint64)',
      ),
      'write': (
          'qint64 QAbstractSocketEngine::write(const char *, qint64)',
      ),
      'readDatagram': (
          'qint64 QAbstractSocketEngine::readDatagram(char *, qint64, '
          'QIpPacketHeader *, PacketHeaderOptions)',
      ),
      'writeDatagram': (
          'qint64 QAbstractSocketEngine::writeDatagram(const char *, '
          'qint64, const QIpPacketHeader &)',
      ),
      'waitForRead': (
          'bool QAbstractSocketEngine::waitForRead(QDeadlineTimer, bool *)',
      ),
      'waitForWrite': (
          'bool QAbstractSocketEngine::waitForWrite(QDeadlineTimer, bool *)',
      ),
      'waitForReadOrWrite': (
          'bool QAbstractSocketEngine::waitForReadOrWrite(bool *, bool *, '
          'bool, bool, QDeadlineTimer, bool *)',
      ),
  }

  #  The functions Qt calls itself that QAbstractSocketEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10Sock'
           'etTypeENS0_20NetworkLayerProtocolE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtNetwork:QAbstractSocket.SocketType'),
               ('int', 'enum',
                'QtNetwork:QAbstractSocket.NetworkLayerProtocol'),
           )),
          ('_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11Soc'
           'ketStateE',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
               ('int', 'enum', 'QtNetwork:QAbstractSocket.SocketState'),
           )),
      ),
      'socketDescriptor': (
          ('_ZNK21QAbstractSocketEngine16socketDescriptorEv',
           ('long long', 'number', ''),
           ()),
      ),
      'isValid': (
          ('_ZNK21QAbstractSocketEngine7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'connectToHost': (
          ('_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('unsigned short', 'number', ''),
           )),
      ),
      'connectToHostByName': (
          ('_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('unsigned short', 'number', ''),
           )),
      ),
      'bind': (
          ('_ZN21QAbstractSocketEngine4bindERK12QHostAddresst',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('unsigned short', 'number', ''),
           )),
      ),
      'listen': (
          ('_ZN21QAbstractSocketEngine6listenEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'accept': (
          ('_ZN21QAbstractSocketEngine6acceptEv',
           ('long long', 'number', ''),
           ()),
      ),
      'close': (
          ('_ZN21QAbstractSocketEngine5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bytesAvailable': (
          ('_ZNK21QAbstractSocketEngine14bytesAvailableEv',
           ('long long', 'number', ''),
           ()),
      ),
      'joinMulticastGroup': (
          ('_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddress'
           'RK17QNetworkInterface',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('address', 'value', 'QtNetwork:QNetworkInterface'),
           )),
      ),
      'leaveMulticastGroup': (
          ('_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddres'
           'sRK17QNetworkInterface',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('address', 'value', 'QtNetwork:QNetworkInterface'),
           )),
      ),
      'multicastInterface': (
          ('_ZNK21QAbstractSocketEngine18multicastInterfaceEv',
           ('address', 'value', 'QtNetwork:QNetworkInterface'),
           ()),
      ),
      'setMulticastInterface': (
          ('_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkI'
           'nterface',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QNetworkInterface'),
           )),
      ),
      'hasPendingDatagrams': (
          ('_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'pendingDatagramSize': (
          ('_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'bytesToWrite': (
          ('_ZNK21QAbstractSocketEngine12bytesToWriteEv',
           ('long long', 'number', ''),
           ()),
      ),
      'option': (
          ('_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE',
           ('int', 'number', ''),
           (
               ('int', 'enum',
                'QtNetwork:QAbstractSocketEngine.SocketOption'),
           )),
      ),
      'setOption': (
          ('_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi',
           ('bool', 'number', ''),
           (
               ('int', 'enum',
                'QtNetwork:QAbstractSocketEngine.SocketOption'),
               ('int', 'number', ''),
           )),
      ),
      'isReadNotificationEnabled': (
          ('_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setReadNotificationEnabled': (
          ('_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isWriteNotificationEnabled': (
          ('_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setWriteNotificationEnabled': (
          ('_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isExceptionNotificationEnabled': (
          ('_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setExceptionNotificationEnabled': (
          ('_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QAbstractSocketEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSocketEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QAbstractSocketEngine::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#socketDescriptor
    """
    #  qintptr QAbstractSocketEngine::socketDescriptor() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine16socketDescriptorEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#isValid
    """
    #  bool QAbstractSocketEngine::isValid() const
    return self.uglySide.call('ritual_ZNK21QAbstractSocketEngine7isValidEv')

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocketEngine::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#bytesAvailable
    """
    #  qint64 QAbstractSocketEngine::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine14bytesAvailableEv',
    )

  def multicastInterface(self) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QAbstractSocketEngine::multicastInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#multicastInterface

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QAbstractSocketEngine::multicastInterface() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine18multicastInterfaceEv',
    )
    from . import QNetworkInterface
    return QNetworkInterface._cuteOwning(address)

  def hasPendingDatagrams(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::hasPendingDatagrams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#hasPendingDatagrams
    """
    #  bool QAbstractSocketEngine::hasPendingDatagrams() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv',
    )

  def pendingDatagramSize(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocketEngine::pendingDatagramSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#pendingDatagramSize
    """
    #  qint64 QAbstractSocketEngine::pendingDatagramSize() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv',
    )

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocketEngine::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#bytesToWrite
    """
    #  qint64 QAbstractSocketEngine::bytesToWrite() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine12bytesToWriteEv',
    )

  @overload(SocketOption)
  def option(self, option: SocketOption) -> int:
    """
    Calls Qt's 'int QAbstractSocketEngine::option(SocketOption option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#option

    Parameters
    ----------

    option : SocketOption
      Passed on as its number.
    """
    #  int QAbstractSocketEngine::option(SocketOption option) const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE',
        option.value,
    )

  def error(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError QAbstractSocketEngine::error()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#error

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError QAbstractSocketEngine::error() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QAbstractSocketEngine::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSocketEngine::errorString() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine11errorStringEv',
    )

  def state(self) -> QAbstractSocket.SocketState:
    """
    Calls Qt's 'QAbstractSocket::SocketState QAbstractSocketEngine::state()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#state

    Returns
    -------

    QAbstractSocket.SocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketState(number)' gives.
    """
    #  QAbstractSocket::SocketState QAbstractSocketEngine::state() const
    return QAbstractSocket.SocketState(self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine5stateEv',
    ))

  def socketType(self) -> QAbstractSocket.SocketType:
    """
    Calls Qt's 'QAbstractSocket::SocketType
    QAbstractSocketEngine::socketType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#socketType

    Returns
    -------

    QAbstractSocket.SocketType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketType(number)' gives.
    """
    #  QAbstractSocket::SocketType QAbstractSocketEngine::socketType() const
    return QAbstractSocket.SocketType(self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine10socketTypeEv',
    ))

  def protocol(self) -> QAbstractSocket.NetworkLayerProtocol:
    """
    Calls Qt's 'QAbstractSocket::NetworkLayerProtocol
    QAbstractSocketEngine::protocol() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#protocol

    Returns
    -------

    QAbstractSocket.NetworkLayerProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.NetworkLayerProtocol(number)' gives.
    """
    #  QAbstractSocket::NetworkLayerProtocol
    #      QAbstractSocketEngine::protocol() const
    return QAbstractSocket.NetworkLayerProtocol(self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine8protocolEv',
    ))

  def localAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QAbstractSocketEngine::localAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#localAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QAbstractSocketEngine::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine12localAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QAbstractSocketEngine::localPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#localPort
    """
    #  quint16 QAbstractSocketEngine::localPort() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine9localPortEv',
    )

  def peerAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QAbstractSocketEngine::peerAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#peerAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QAbstractSocketEngine::peerAddress() const
    address = self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine11peerAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QAbstractSocketEngine::peerPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#peerPort
    """
    #  quint16 QAbstractSocketEngine::peerPort() const
    return self.uglySide.call('ritual_ZNK21QAbstractSocketEngine8peerPortEv')

  def inboundStreamCount(self) -> int:
    """
    Calls Qt's 'int QAbstractSocketEngine::inboundStreamCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#inboundStreamCount
    """
    #  int QAbstractSocketEngine::inboundStreamCount() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine18inboundStreamCountEv',
    )

  def outboundStreamCount(self) -> int:
    """
    Calls Qt's 'int QAbstractSocketEngine::outboundStreamCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#outboundStreamCount
    """
    #  int QAbstractSocketEngine::outboundStreamCount() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine19outboundStreamCountEv',
    )

  def isReadNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::isReadNotificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html
    """
    #  bool QAbstractSocketEngine::isReadNotificationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv',
    )

  def isWriteNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::isWriteNotificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html
    """
    #  bool QAbstractSocketEngine::isWriteNotificationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv',
    )

  def isExceptionNotificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::isExceptionNotificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html
    """
    #  bool QAbstractSocketEngine::isExceptionNotificationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkInterface)
  def setMulticastInterface(self, iface: QNetworkInterface) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::setMulticastInterface(const
    QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setMulticastInterface

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QAbstractSocketEngine::setMulticastInterface(const
    #      QNetworkInterface &iface)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetwo'
        'rkInterface',
        self._valueOf(iface),
    )

  @overload(SocketOption, int)
  def setOption(self, option: SocketOption, value: int) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::setOption(SocketOption option,
    int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setOption

    Parameters
    ----------

    option : SocketOption
      Passed on as its number.

    value : int
      Passed on as it is.
    """
    #  bool QAbstractSocketEngine::setOption(SocketOption option, int value)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi',
        option.value, value,
    )

  @overload(bool)
  def setReadNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::setReadNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractSocketEngine::setReadNotificationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb',
        enable,
    )

  @overload(bool)
  def setWriteNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::setWriteNotificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractSocketEngine::setWriteNotificationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb',
        enable,
    )

  @overload(bool)
  def setExceptionNotificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketEngine::setExceptionNotificationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractSocketEngine::setExceptionNotificationEnabled(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledE'
        'b',
        enable,
    )

  @overload(QAbstractSocketEngineReceiver)
  @overload(NoneType)
  def setReceiver(
      self,
      receiver: Optional[QAbstractSocketEngineReceiver],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketEngine::setReceiver(QAbstractSocketEngineReceiver
    *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setReceiver

    Parameters
    ----------

    receiver : Optional[QAbstractSocketEngineReceiver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSocketEngine::setReceiver(QAbstractSocketEngineReceiver
    #      *receiver)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine11setReceiverEP29QAbstractSocketEn'
        'gineReceiver',
        self._addressOf(receiver, 'QAbstractSocketEngineReceiver'),
    )

  @overload(QAbstractSocket.SocketError, str)
  def setError(
      self,
      error: QAbstractSocket.SocketError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketEngine::setError(QAbstractSocket::SocketError error, const
    QString &errorString) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setError

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSocketEngine::setError(QAbstractSocket::SocketError
    #      error, const QString &errorString) const
    self.uglySide.call(
        'ritual_ZNK21QAbstractSocketEngine8setErrorEN15QAbstractSocket11Soc'
        'ketErrorERK7QString',
        error.value, errorString,
    )

  @overload(QAbstractSocket.SocketState)
  def setState(self, state: QAbstractSocket.SocketState) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketEngine::setState(QAbstractSocket::SocketState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setState

    Parameters
    ----------

    state : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QAbstractSocketEngine::setState(QAbstractSocket::SocketState
    #      state)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine8setStateEN15QAbstractSocket11Sock'
        'etStateE',
        state.value,
    )

  @overload(QAbstractSocket.SocketType)
  def setSocketType(self, socketType: QAbstractSocket.SocketType) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketEngine::setSocketType(QAbstractSocket::SocketType
    socketType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setSocketType

    Parameters
    ----------

    socketType : QAbstractSocket.SocketType
      Passed on as its number.
    """
    #  void QAbstractSocketEngine::setSocketType(QAbstractSocket::SocketType
    #      socketType)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine13setSocketTypeEN15QAbstractSocket'
        '10SocketTypeE',
        socketType.value,
    )

  @overload(QAbstractSocket.NetworkLayerProtocol)
  def setProtocol(
      self,
      protocol: QAbstractSocket.NetworkLayerProtocol,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketEngine::setProtocol(QAbstractSocket::NetworkLayerProtocol
    protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setProtocol

    Parameters
    ----------

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number.
    """
    #  void QAbstractSocketEngine::setProtocol(QAbstractSocket::
    #      NetworkLayerProtocol protocol)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine11setProtocolEN15QAbstractSocket20'
        'NetworkLayerProtocolE',
        protocol.value,
    )

  @overload(QHostAddress)
  def setLocalAddress(self, address: QHostAddress) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::setLocalAddress(const
    QHostAddress &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setLocalAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QAbstractSocketEngine::setLocalAddress(const QHostAddress
    #      &address)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine15setLocalAddressERK12QHostAddress',
        self._valueOf(address),
    )

  @overload(int)
  def setLocalPort(self, port: int) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::setLocalPort(quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setLocalPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QAbstractSocketEngine::setLocalPort(quint16 port)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine12setLocalPortEt', port,
    )

  @overload(QHostAddress)
  def setPeerAddress(self, address: QHostAddress) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::setPeerAddress(const QHostAddress
    &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setPeerAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QAbstractSocketEngine::setPeerAddress(const QHostAddress
    #      &address)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine14setPeerAddressERK12QHostAddress',
        self._valueOf(address),
    )

  @overload(int)
  def setPeerPort(self, port: int) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::setPeerPort(quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#setPeerPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QAbstractSocketEngine::setPeerPort(quint16 port)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine11setPeerPortEt', port,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QAbstractSocketEngine::QAbstractSocketEngine(QObject *parent)':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
    - Qt's 'QAbstractSocketEngine::QAbstractSocketEngine(
      QAbstractSocketEnginePrivate &dd, QObject *parent)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.__init__' has no cute function yet. Qt's "
        "'QAbstractSocketEngine::QAbstractSocketEngine(QObject *parent)': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open. Qt's "
        "'QAbstractSocketEngine::QAbstractSocketEngine(QAbstractSocketEngine"
        "Private &dd, QObject *parent)': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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
    QAbstractSocketEngine::initialize(QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#initialize

    Parameters
    ----------

    type : QAbstractSocket.SocketType
      Passed on as its number.

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.NetworkLayerProtocol.IPv4Protocol.
    """
    #  bool QAbstractSocketEngine::initialize(QAbstractSocket::SocketType
    #      type, QAbstractSocket::NetworkLayerProtocol protocol)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10S'
        'ocketTypeENS0_20NetworkLayerProtocolE',
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
    Calls Qt's 'bool QAbstractSocketEngine::initialize(qintptr
    socketDescriptor, QAbstractSocket::SocketState socketState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#initialize

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    socketState : QAbstractSocket.SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.SocketState.ConnectedState.
    """
    #  bool QAbstractSocketEngine::initialize(qintptr socketDescriptor,
    #      QAbstractSocket::SocketState socketState)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11'
        'SocketStateE',
        socketDescriptor, socketState.value,
    )

  @overload(QHostAddress, int)
  def connectToHost(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::connectToHost(const QHostAddress
    &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#connectToHost

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QAbstractSocketEngine::connectToHost(const QHostAddress &address,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(str, int)
  def connectToHostByName(self, name: str, port: int) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::connectToHostByName(const QString
    &name, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#connectToHostByName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  bool QAbstractSocketEngine::connectToHostByName(const QString &name,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt',
        name, port,
    )

  @overload(QHostAddress, int)
  def bind(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::bind(const QHostAddress &address,
    quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#bind

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QAbstractSocketEngine::bind(const QHostAddress &address, quint16
    #      port)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine4bindERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(int)
  def listen(self, backlog: int) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::listen(int backlog)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#listen

    Parameters
    ----------

    backlog : int
      Passed on as it is.
    """
    #  bool QAbstractSocketEngine::listen(int backlog)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine6listenEi', backlog,
    )

  def accept(self) -> int:
    """
    Calls Qt's 'qintptr QAbstractSocketEngine::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#accept
    """
    #  qintptr QAbstractSocketEngine::accept()
    return self.uglySide.call('ritual_ZN21QAbstractSocketEngine6acceptEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#close
    """
    #  void QAbstractSocketEngine::close()
    self.uglySide.call('ritual_ZN21QAbstractSocketEngine5closeEv')

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocketEngine::write(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QAbstractSocketEngine::write(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine5writeEPKcx',
        self._bytesOf(data), len,
    )

  @overload(QHostAddress, QNetworkInterface)
  def joinMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::joinMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#joinMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QAbstractSocketEngine::joinMulticastGroup(const QHostAddress
    #      &groupAddress, const QNetworkInterface &iface)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddr'
        'essRK17QNetworkInterface',
        self._valueOf(groupAddress), self._valueOf(iface),
    )

  @overload(QHostAddress, QNetworkInterface)
  def leaveMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketEngine::leaveMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#leaveMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QAbstractSocketEngine::leaveMulticastGroup(const QHostAddress
    #      &groupAddress, const QNetworkInterface &iface)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAdd'
        'ressRK17QNetworkInterface',
        self._valueOf(groupAddress), self._valueOf(iface),
    )

  @overload(str, int, QIpPacketHeader)
  @overload(NoneType, int, QIpPacketHeader)
  def writeDatagram(
      self,
      data: Optional[str],
      len: int,
      header: QIpPacketHeader,
  ) -> int:
    """
    Calls Qt's 'qint64 QAbstractSocketEngine::writeDatagram(const char *data,
    qint64 len, const QIpPacketHeader &header)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#writeDatagram

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    header : QIpPacketHeader
      Passed on as a value: Qt reads the C++ QIpPacketHeader, which stays
      Python's own.
    """
    #  qint64 QAbstractSocketEngine::writeDatagram(const char *data, qint64
    #      len, const QIpPacketHeader &header)
    return self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine13writeDatagramEPKcxRK15QIpPacketH'
        'eader',
        self._bytesOf(data), len, self._valueOf(header),
    )

  def readNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::readNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#readNotification
    """
    #  void QAbstractSocketEngine::readNotification()
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine16readNotificationEv',
    )

  def writeNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::writeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#writeNotification
    """
    #  void QAbstractSocketEngine::writeNotification()
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine17writeNotificationEv',
    )

  def closeNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::closeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#closeNotification
    """
    #  void QAbstractSocketEngine::closeNotification()
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine17closeNotificationEv',
    )

  def exceptionNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::exceptionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#exceptionNotification
    """
    #  void QAbstractSocketEngine::exceptionNotification()
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine21exceptionNotificationEv',
    )

  def connectionNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::connectionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html#connectionNotification
    """
    #  void QAbstractSocketEngine::connectionNotification()
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine22connectionNotificationEv',
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QAbstractSocketEngine::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketengine.html

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSocketEngine::proxyAuthenticationRequired(const
    #      QNetworkProxy &proxy, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN21QAbstractSocketEngine27proxyAuthenticationRequiredERK13'
        'QNetworkProxyP14QAuthenticator',
        self._valueOf(proxy), self._addressOf(authenticator),
    )

  def d_func(self) -> Optional[QAbstractSocketEnginePrivate]:
    """
    Calls Qt's 'QAbstractSocketEnginePrivate
    *QAbstractSocketEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketengine.html#d_func

    Returns
    -------

    Optional[QAbstractSocketEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSocketEnginePrivate *QAbstractSocketEngine::d_func()
    address = self.uglySide.call('ritual_ZN21QAbstractSocketEngine6d_funcEv')
    from . import QAbstractSocketEnginePrivate
    return QAbstractSocketEnginePrivate._cuteAt(address)

  @staticmethod
  def createSocketEngine(*__, **_) -> Never:
    """
    - Qt's 'QAbstractSocketEngine
      *QAbstractSocketEngine::createSocketEngine(QAbstractSocket::SocketType
      socketType, const QNetworkProxy &a1, QObject *parent)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: use of undeclared identifier 'socketHandlers'.
    - Qt's 'QAbstractSocketEngine
      *QAbstractSocketEngine::createSocketEngine(qintptr socketDescriptor,
      QObject *parent)': Qt's library has no name for it, and its code in
      Qt's source does not compile apart from its file: use of undeclared
      identifier 'socketHandlers'.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.createSocketEngine' has no cute function "
        "yet. Qt's 'QAbstractSocketEngine "
        "*QAbstractSocketEngine::createSocketEngine(QAbstractSocket::SocketT"
        "ype socketType, const QNetworkProxy &a1, QObject *parent)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'socketHandlers'. Qt's 'QAbstractSocketEngine "
        "*QAbstractSocketEngine::createSocketEngine(qintptr "
        "socketDescriptor, QObject *parent)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'socketHandlers'.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'qint64 QAbstractSocketEngine::read(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.read' has no cute function yet. Qt's "
        "'qint64 QAbstractSocketEngine::read(char *data, qint64 maxlen)': "
        "names 'char', which has no cute class yet.")

  @staticmethod
  def readDatagram(*__, **_) -> Never:
    """
    Qt's 'qint64 QAbstractSocketEngine::readDatagram(char *data, qint64
    maxlen, QIpPacketHeader *header, PacketHeaderOptions a3)': names 'char',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.readDatagram' has no cute function yet. "
        "Qt's 'qint64 QAbstractSocketEngine::readDatagram(char *data, "
        "qint64 maxlen, QIpPacketHeader *header, PacketHeaderOptions a3)': "
        "names 'char', which has no cute class yet.")

  @staticmethod
  def waitForRead(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractSocketEngine::waitForRead(QDeadlineTimer deadline,
    bool *timedOut)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.waitForRead' has no cute function yet. Qt's "
        "'bool QAbstractSocketEngine::waitForRead(QDeadlineTimer deadline, "
        "bool *timedOut)': takes a number to change where it is.")

  @staticmethod
  def waitForReadOrWrite(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractSocketEngine::waitForReadOrWrite(bool *readyToRead,
    bool *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer
    deadline, bool *timedOut)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.waitForReadOrWrite' has no cute function "
        "yet. Qt's 'bool QAbstractSocketEngine::waitForReadOrWrite(bool "
        "*readyToRead, bool *readyToWrite, bool checkRead, bool checkWrite, "
        "QDeadlineTimer deadline, bool *timedOut)': takes a number to "
        "change where it is.")

  @staticmethod
  def waitForWrite(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractSocketEngine::waitForWrite(QDeadlineTimer deadline,
    bool *timedOut)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAbstractSocketEngine.waitForWrite' has no cute function yet. "
        "Qt's 'bool QAbstractSocketEngine::waitForWrite(QDeadlineTimer "
        "deadline, bool *timedOut)': takes a number to change where it is.")
