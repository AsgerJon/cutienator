"""
QBluetoothSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QIODevice, QIODeviceBase, QObject
from . import QBluetooth, QBluetoothServiceInfo, QBluetoothUuid

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QBluetoothAddress, QBluetoothSocketBasePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothSocketBasePrivate = WAIT['QBluetoothSocketBasePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothSocket(QIODevice):
  """
  The cute side of Qt's QBluetoothSocket: a plain Python object standing in
  front of one C++ QBluetoothSocket.

  It is built on the cute 'QIODevice', as Qt's QBluetoothSocket is built on
  Qt's QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothSocket that has a ritual and that Python
  can call so far, 35 names in all: 'metaObject', 'tr', 'd_func', 'abort',
  'close', 'isSequential', 'bytesAvailable', 'bytesToWrite', 'canReadLine',
  'connectToService', 'disconnectFromService', 'localName', 'localAddress',
  'localPort', 'peerName', 'peerAddress', 'peerPort', 'setSocketDescriptor',
  'socketDescriptor', 'socketType', 'state', 'error', 'errorString',
  'setPreferredSecurityFlags', 'preferredSecurityFlags', 'connected',
  'disconnected', 'errorOccurred', 'stateChanged', 'writeData',
  'setSocketState', 'setSocketError', 'doDeviceDiscovery',
  'serviceDiscovered', 'discoveryFinished'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBluetoothSocket::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QBluetoothSocket::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QBluetoothSocketBasePrivate *QBluetoothSocket::d_func()
    const': takes in Python what 'QBluetoothSocketBasePrivate
    *QBluetoothSocket::d_func()' takes.
  - Qt's 'QBluetoothSocket::~QBluetoothSocket()': the destructor: Python
    never removes a C++ QBluetoothSocket.
  - Qt's 'qint64 QBluetoothSocket::readData(char *data, qint64 maxSize)':
    names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 48 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothSocket is created at the first use, not by
    'QBluetoothSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothSocket.
  - Qt tells when it has removed the C++ QBluetoothSocket. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBluetoothSocket, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SocketError(CuteNum, scoped=True):
    """
    The enum 'QBluetoothSocket::SocketError' of Qt, with the 9 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoSocketError = Kee[int](0)
    UnknownSocketError = Kee[int](1)
    RemoteHostClosedError = Kee[int](2)
    HostNotFoundError = Kee[int](3)
    ServiceNotFoundError = Kee[int](4)
    NetworkError = Kee[int](5)
    UnsupportedProtocolError = Kee[int](6)
    OperationError = Kee[int](7)
    MissingPermissionsError = Kee[int](8)

  class SocketState(CuteNum, scoped=True):
    """
    The enum 'QBluetoothSocket::SocketState' of Qt, with the 7 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    UnconnectedState = Kee[int](0)
    ServiceLookupState = Kee[int](1)
    ConnectingState = Kee[int](2)
    ConnectedState = Kee[int](3)
    BoundState = Kee[int](4)
    ClosingState = Kee[int](5)
    ListeningState = Kee[int](6)

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
    Calls Qt's 'QString QBluetoothSocket::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#tr

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
    #  QString QBluetoothSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QBluetoothSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothSocket'

  #  A C++ QBluetoothSocket Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBluetoothSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBluetoothSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBluetoothSocket::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocket::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#isSequential
    """
    #  bool QBluetoothSocket::isSequential() const
    ritual = 'ritual_ZNK16QBluetoothSocket12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QBluetoothSocket12isSequentialEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocket::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#bytesAvailable
    """
    #  qint64 QBluetoothSocket::bytesAvailable() const
    ritual = 'ritual_ZNK16QBluetoothSocket14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QBluetoothSocket14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocket::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#bytesToWrite
    """
    #  qint64 QBluetoothSocket::bytesToWrite() const
    ritual = 'ritual_ZNK16QBluetoothSocket12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QBluetoothSocket12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocket::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#canReadLine
    """
    #  bool QBluetoothSocket::canReadLine() const
    ritual = 'ritual_ZNK16QBluetoothSocket11canReadLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QBluetoothSocket11canReadLineEv'
    return self.uglySide.call(ritual)

  def localName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocket::localName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#localName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocket::localName() const
    return self.uglySide.call('ritual_ZNK16QBluetoothSocket9localNameEv')

  def localAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothSocket::localAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#localAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothSocket::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket12localAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothSocket::localPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#localPort
    """
    #  quint16 QBluetoothSocket::localPort() const
    return self.uglySide.call('ritual_ZNK16QBluetoothSocket9localPortEv')

  def peerName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocket::peerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#peerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocket::peerName() const
    return self.uglySide.call('ritual_ZNK16QBluetoothSocket8peerNameEv')

  def peerAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothSocket::peerAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#peerAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothSocket::peerAddress() const
    address = self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket11peerAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothSocket::peerPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#peerPort
    """
    #  quint16 QBluetoothSocket::peerPort() const
    return self.uglySide.call('ritual_ZNK16QBluetoothSocket8peerPortEv')

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'int QBluetoothSocket::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#socketDescriptor
    """
    #  int QBluetoothSocket::socketDescriptor() const
    return self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket16socketDescriptorEv',
    )

  def socketType(self) -> QBluetoothServiceInfo.Protocol:
    """
    Calls Qt's 'QBluetoothServiceInfo::Protocol
    QBluetoothSocket::socketType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#socketType

    Returns
    -------

    QBluetoothServiceInfo.Protocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QBluetoothServiceInfo.Protocol(number)' gives.
    """
    #  QBluetoothServiceInfo::Protocol QBluetoothSocket::socketType() const
    return QBluetoothServiceInfo.Protocol(self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket10socketTypeEv',
    ))

  def state(self) -> SocketState:
    """
    Calls Qt's 'SocketState QBluetoothSocket::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#state

    Returns
    -------

    SocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SocketState(number)'
      gives.
    """
    #  SocketState QBluetoothSocket::state() const
    return QBluetoothSocket.SocketState(self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket5stateEv',
    ))

  def error(self) -> SocketError:
    """
    Calls Qt's 'SocketError QBluetoothSocket::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#error

    Returns
    -------

    SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SocketError(number)'
      gives.
    """
    #  SocketError QBluetoothSocket::error() const
    return QBluetoothSocket.SocketError(self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocket::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocket::errorString() const
    return self.uglySide.call('ritual_ZNK16QBluetoothSocket11errorStringEv')

  def preferredSecurityFlags(self) -> QBluetooth.SecurityFlags:
    """
    Calls Qt's 'QBluetooth::SecurityFlags
    QBluetoothSocket::preferredSecurityFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#preferredSecurityFlags

    Returns
    -------

    QBluetooth.SecurityFlags
      The value standing for the combination Qt gave back.
    """
    #  QBluetooth::SecurityFlags QBluetoothSocket::preferredSecurityFlags()
    #      const
    return QBluetooth.SecurityFlags(self.uglySide.call(
        'ritual_ZNK16QBluetoothSocket22preferredSecurityFlagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QBluetoothServiceInfo.Protocol)
  @overload(int, QBluetoothServiceInfo.Protocol, SocketState)
  @overload(
      int, QBluetoothServiceInfo.Protocol, SocketState,
      QIODeviceBase.OpenMode,
  )
  def setSocketDescriptor(
      self,
      socketDescriptor: int,
      socketType: QBluetoothServiceInfo.Protocol,
      socketState: SocketState = SocketState.ConnectedState,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocket::setSocketDescriptor(int
    socketDescriptor, QBluetoothServiceInfo::Protocol socketType, SocketState
    socketState, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    socketType : QBluetoothServiceInfo.Protocol
      Passed on as its number.

    socketState : SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      SocketState.ConnectedState.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QBluetoothSocket::setSocketDescriptor(int socketDescriptor,
    #      QBluetoothServiceInfo::Protocol socketType, SocketState
    #      socketState, OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN16QBluetoothSocket19setSocketDescriptorEiN21QBluetoothSer'
        'viceInfo8ProtocolENS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenM'
        'odeFlagEE',
        socketDescriptor, socketType.value, socketState.value,
        openMode.value,
    )

  @overload(QBluetooth.SecurityFlags)
  def setPreferredSecurityFlags(
      self,
      flags: QBluetooth.SecurityFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QBluetoothSocket::setPreferredSecurityFlags(QBluetooth::SecurityFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#setPreferredSecurityFlags

    Parameters
    ----------

    flags : QBluetooth.SecurityFlags
      Passed on as its number.
    """
    #  void QBluetoothSocket::setPreferredSecurityFlags(QBluetooth::
    #      SecurityFlags flags)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket25setPreferredSecurityFlagsE6QFlagsIN10'
        'QBluetooth8SecurityEE',
        flags.value,
    )

  @overload(SocketState)
  def setSocketState(self, state: SocketState) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::setSocketState(SocketState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#setSocketState

    Parameters
    ----------

    state : SocketState
      Passed on as its number.
    """
    #  void QBluetoothSocket::setSocketState(SocketState state)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket14setSocketStateENS_11SocketStateE',
        state.value,
    )

  @overload(SocketError)
  def setSocketError(self, error: SocketError) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::setSocketError(SocketError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#setSocketError

    Parameters
    ----------

    error : SocketError
      Passed on as its number.
    """
    #  void QBluetoothSocket::setSocketError(SocketError error)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket14setSocketErrorENS_11SocketErrorE',
        error.value,
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
      socketType: QBluetoothServiceInfo.Protocol,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothSocket::QBluetoothSocket(QBluetoothServiceInfo::Protocol
    socketType, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#QBluetoothSocket

    Parameters
    ----------

    socketType : QBluetoothServiceInfo.Protocol
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothSocket::QBluetoothSocket(QBluetoothServiceInfo::Protocol
    #      socketType, QObject *parent)
    self._noteCreation(QBluetoothSocket, lambda: Rituals.call(
        'ritual_ZN16QBluetoothSocketC1EN21QBluetoothServiceInfo8ProtocolEP7'
        'QObject',
        socketType.value, self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothSocket::QBluetoothSocket(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#QBluetoothSocket

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothSocket::QBluetoothSocket(QObject *parent)
    self._noteCreation(QBluetoothSocket, lambda: Rituals.call(
        'ritual_ZN16QBluetoothSocketC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QBluetoothSocketBasePrivate, QBluetoothServiceInfo.Protocol)
  @overload(NoneType, QBluetoothServiceInfo.Protocol)
  @overload(
      QBluetoothSocketBasePrivate, QBluetoothServiceInfo.Protocol, QObject,
  )
  @overload(
      QBluetoothSocketBasePrivate, QBluetoothServiceInfo.Protocol, NoneType,
  )
  @overload(NoneType, QBluetoothServiceInfo.Protocol, QObject)
  @overload(NoneType, QBluetoothServiceInfo.Protocol, NoneType)
  def __init__(
      self,
      d: Optional[QBluetoothSocketBasePrivate],
      socketType: QBluetoothServiceInfo.Protocol,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothSocket::QBluetoothSocket(QBluetoothSocketBasePrivate *d,
    QBluetoothServiceInfo::Protocol socketType, QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#QBluetoothSocket

    Parameters
    ----------

    d : Optional[QBluetoothSocketBasePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    socketType : QBluetoothServiceInfo.Protocol
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothSocket::QBluetoothSocket(QBluetoothSocketBasePrivate *d,
    #      QBluetoothServiceInfo::Protocol socketType, QObject *parent)
    self._noteCreation(QBluetoothSocket, lambda: Rituals.call(
        'ritual_ZN16QBluetoothSocketC1EP27QBluetoothSocketBasePrivateN21QBl'
        'uetoothServiceInfo8ProtocolEP7QObject',
        self._addressOf(d), socketType.value, self._addressOf(parent,
        'QObject'),
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

  def d_func(self) -> Optional[QBluetoothSocketBasePrivate]:
    """
    Calls Qt's 'QBluetoothSocketBasePrivate *QBluetoothSocket::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#d_func

    Returns
    -------

    Optional[QBluetoothSocketBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothSocketBasePrivate *QBluetoothSocket::d_func()
    address = self.uglySide.call('ritual_ZN16QBluetoothSocket6d_funcEv')
    from . import QBluetoothSocketBasePrivate
    return QBluetoothSocketBasePrivate._cuteAt(address)

  def abort(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#abort
    """
    #  void QBluetoothSocket::abort()
    self.uglySide.call('ritual_ZN16QBluetoothSocket5abortEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#close
    """
    #  void QBluetoothSocket::close()
    ritual = 'ritual_ZN16QBluetoothSocket5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QBluetoothSocket5closeEv'
    self.uglySide.call(ritual)

  @overload(QBluetoothServiceInfo)
  @overload(QBluetoothServiceInfo, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      service: QBluetoothServiceInfo,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::connectToService(const
    QBluetoothServiceInfo &service, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService

    Parameters
    ----------

    service : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QBluetoothSocket::connectToService(const QBluetoothServiceInfo
    #      &service, OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket16connectToServiceERK21QBluetoothServic'
        'eInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(service), openMode.value,
    )

  @overload(QBluetoothAddress, QBluetoothUuid)
  @overload(QBluetoothAddress, QBluetoothUuid, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      address: QBluetoothAddress,
      uuid: QBluetoothUuid,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::connectToService(const
    QBluetoothAddress &address, const QBluetoothUuid &uuid, OpenMode
    openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QBluetoothSocket::connectToService(const QBluetoothAddress
    #      &address, const QBluetoothUuid &uuid, OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket16connectToServiceERK17QBluetoothAddres'
        'sRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), self._valueOf(uuid), openMode.value,
    )

  @overload(QBluetoothAddress, int)
  @overload(QBluetoothAddress, int, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      address: QBluetoothAddress,
      port: int,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::connectToService(const
    QBluetoothAddress &address, quint16 port, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QBluetoothSocket::connectToService(const QBluetoothAddress
    #      &address, quint16 port, OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket16connectToServiceERK17QBluetoothAddres'
        'st6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, openMode.value,
    )

  @overload(QBluetoothAddress, QBluetoothUuid.ServiceClassUuid)
  @overload(
      QBluetoothAddress, QBluetoothUuid.ServiceClassUuid,
      QIODeviceBase.OpenMode,
  )
  def connectToService(
      self,
      address: QBluetoothAddress,
      uuid: QBluetoothUuid.ServiceClassUuid,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::connectToService(const
    QBluetoothAddress &address, QBluetoothUuid::ServiceClassUuid uuid,
    OpenMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#connectToService

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    uuid : QBluetoothUuid.ServiceClassUuid
      Passed on as its number.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QBluetoothSocket::connectToService(const QBluetoothAddress
    #      &address, QBluetoothUuid::ServiceClassUuid uuid, OpenMode mode)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket16connectToServiceERK17QBluetoothAddres'
        'sN14QBluetoothUuid16ServiceClassUuidE6QFlagsIN13QIODeviceBase12Ope'
        'nModeFlagEE',
        self._valueOf(address), uuid.value, mode.value,
    )

  def disconnectFromService(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::disconnectFromService()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#disconnectFromService
    """
    #  void QBluetoothSocket::disconnectFromService()
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket21disconnectFromServiceEv',
    )

  def connected(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#connected
    """
    #  void QBluetoothSocket::connected()
    self.uglySide.call('ritual_ZN16QBluetoothSocket9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#disconnected
    """
    #  void QBluetoothSocket::disconnected()
    self.uglySide.call('ritual_ZN16QBluetoothSocket12disconnectedEv')

  @overload(SocketError)
  def errorOccurred(self, error: SocketError) -> None:
    """
    Calls Qt's 'void
    QBluetoothSocket::errorOccurred(QBluetoothSocket::SocketError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#errorOccurred

    Parameters
    ----------

    error : SocketError
      Passed on as its number.
    """
    #  void QBluetoothSocket::errorOccurred(QBluetoothSocket::SocketError
    #      error)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket13errorOccurredENS_11SocketErrorE',
        error.value,
    )

  @overload(SocketState)
  def stateChanged(self, state: SocketState) -> None:
    """
    Calls Qt's 'void
    QBluetoothSocket::stateChanged(QBluetoothSocket::SocketState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#stateChanged

    Parameters
    ----------

    state : SocketState
      Passed on as its number.
    """
    #  void QBluetoothSocket::stateChanged(QBluetoothSocket::SocketState
    #      state)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket12stateChangedENS_11SocketStateE',
        state.value,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocket::writeData(const char *data, qint64
    maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothsocket.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QBluetoothSocket::writeData(const char *data, qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN16QBluetoothSocket9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )

  @overload(QBluetoothServiceInfo, QIODeviceBase.OpenMode)
  def doDeviceDiscovery(
      self,
      service: QBluetoothServiceInfo,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::doDeviceDiscovery(const
    QBluetoothServiceInfo &service, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#doDeviceDiscovery

    Parameters
    ----------

    service : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  void QBluetoothSocket::doDeviceDiscovery(const QBluetoothServiceInfo
    #      &service, OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket17doDeviceDiscoveryERK21QBluetoothServi'
        'ceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(service), openMode.value,
    )

  @overload(QBluetoothServiceInfo)
  def serviceDiscovered(self, service: QBluetoothServiceInfo) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::serviceDiscovered(const
    QBluetoothServiceInfo &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#serviceDiscovered

    Parameters
    ----------

    service : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.
    """
    #  void QBluetoothSocket::serviceDiscovered(const QBluetoothServiceInfo
    #      &service)
    self.uglySide.call(
        'ritual_ZN16QBluetoothSocket17serviceDiscoveredERK21QBluetoothServi'
        'ceInfo',
        self._valueOf(service),
    )

  def discoveryFinished(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocket::discoveryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocket.html#discoveryFinished
    """
    #  void QBluetoothSocket::discoveryFinished()
    self.uglySide.call('ritual_ZN16QBluetoothSocket17discoveryFinishedEv')
