"""
QLocalSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qlocalsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum
from ..occult import Rituals
from ..QtCore import QIODevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QLocalSocketPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLocalSocket(QIODevice):
  """
  The cute side of Qt's QLocalSocket: a plain Python object standing in front
  of one C++ QLocalSocket.

  It is built on the cute 'QIODevice', as Qt's QLocalSocket is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLocalSocket that has a ritual and that Python can
  call so far, 35 names in all: 'metaObject', 'tr', 'd_func',
  'connectToServer', 'disconnectFromServer', 'setServerName', 'serverName',
  'fullServerName', 'abort', 'isSequential', 'bytesAvailable',
  'bytesToWrite', 'canReadLine', 'open', 'close', 'error', 'flush',
  'isValid', 'readBufferSize', 'setReadBufferSize', 'setSocketDescriptor',
  'socketDescriptor', 'setSocketOptions', 'socketOptions', 'state',
  'waitForBytesWritten', 'waitForConnected', 'waitForDisconnected',
  'waitForReadyRead', 'connected', 'disconnected', 'errorOccurred',
  'stateChanged', 'skipData', 'writeData'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLocalSocket::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLocalSocket::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QLocalSocketPrivate *QLocalSocket::d_func() const': takes in
    Python what 'QLocalSocketPrivate *QLocalSocket::d_func()' takes.
  - Qt's 'QLocalSocket::~QLocalSocket()': the destructor: Python never
    removes a C++ QLocalSocket.
  - Qt's 'QBindable<SocketOptions> QLocalSocket::bindableSocketOptions()':
    gives a type Python has no way to take yet.
  - Qt's 'qint64 QLocalSocket::readData(char *a0, qint64 a1)': names 'char',
    which has no cute class yet.
  - Qt's 'qint64 QLocalSocket::readLineData(char *data, qint64 maxSize)':
    names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 48 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLocalSocket is created at the first use, not by
    'QLocalSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLocalSocket.
  - Qt tells when it has removed the C++ QLocalSocket. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QLocalSocket that has no cute function yet,
    'bindableSocketOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLocalSocket, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LocalSocketError(CuteNum):
    """
    The enum 'QLocalSocket::LocalSocketError' of Qt, with the 11 names Qt
    gives in it.
    """

    ConnectionRefusedError = Kee[int](0)
    PeerClosedError = Kee[int](1)
    ServerNotFoundError = Kee[int](2)
    SocketAccessError = Kee[int](3)
    SocketResourceError = Kee[int](4)
    SocketTimeoutError = Kee[int](5)
    DatagramTooLargeError = Kee[int](6)
    ConnectionError = Kee[int](7)
    UnsupportedSocketOperationError = Kee[int](10)
    UnknownSocketError = Kee[int](-1)
    OperationError = Kee[int](19)

  class LocalSocketState(CuteNum):
    """
    The enum 'QLocalSocket::LocalSocketState' of Qt, with the 4 names Qt
    gives in it.
    """

    UnconnectedState = Kee[int](0)
    ConnectingState = Kee[int](2)
    ConnectedState = Kee[int](3)
    ClosingState = Kee[int](6)

  class SocketOption(CuteFlags):
    """
    The flags enum 'QLocalSocket::SocketOption' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QLocalSocket::SocketOptions'.
    """

    NoOptions = 0x0
    AbstractNamespaceOption = 0x1

  SocketOptions = SocketOption

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
    Calls Qt's 'QString QLocalSocket::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#tr

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
    #  QString QLocalSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QLocalSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocalSocket'

  #  A C++ QLocalSocket Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLocalSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLocalSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLocalSocket::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QLocalSocket10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def serverName(self) -> str:
    """
    Calls Qt's 'QString QLocalSocket::serverName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#serverName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocalSocket::serverName() const
    return self.uglySide.call('ritual_ZNK12QLocalSocket10serverNameEv')

  def fullServerName(self) -> str:
    """
    Calls Qt's 'QString QLocalSocket::fullServerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#fullServerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocalSocket::fullServerName() const
    return self.uglySide.call('ritual_ZNK12QLocalSocket14fullServerNameEv')

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#isSequential
    """
    #  bool QLocalSocket::isSequential() const
    ritual = 'ritual_ZNK12QLocalSocket12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLocalSocket12isSequentialEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QLocalSocket::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#bytesAvailable
    """
    #  qint64 QLocalSocket::bytesAvailable() const
    ritual = 'ritual_ZNK12QLocalSocket14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLocalSocket14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QLocalSocket::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#bytesToWrite
    """
    #  qint64 QLocalSocket::bytesToWrite() const
    ritual = 'ritual_ZNK12QLocalSocket12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLocalSocket12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#canReadLine
    """
    #  bool QLocalSocket::canReadLine() const
    ritual = 'ritual_ZNK12QLocalSocket11canReadLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLocalSocket11canReadLineEv'
    return self.uglySide.call(ritual)

  def error(self) -> LocalSocketError:
    """
    Calls Qt's 'LocalSocketError QLocalSocket::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#error

    Returns
    -------

    LocalSocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LocalSocketError(number)'
      gives.
    """
    #  LocalSocketError QLocalSocket::error() const
    return QLocalSocket.LocalSocketError(self.uglySide.call(
        'ritual_ZNK12QLocalSocket5errorEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#isValid
    """
    #  bool QLocalSocket::isValid() const
    return self.uglySide.call('ritual_ZNK12QLocalSocket7isValidEv')

  def readBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QLocalSocket::readBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#readBufferSize
    """
    #  qint64 QLocalSocket::readBufferSize() const
    return self.uglySide.call('ritual_ZNK12QLocalSocket14readBufferSizeEv')

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QLocalSocket::socketDescriptor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#socketDescriptor
    """
    #  qintptr QLocalSocket::socketDescriptor() const
    return self.uglySide.call('ritual_ZNK12QLocalSocket16socketDescriptorEv')

  def socketOptions(self) -> SocketOptions:
    """
    Calls Qt's 'SocketOptions QLocalSocket::socketOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#socketOptions

    Returns
    -------

    SocketOptions
      The value standing for the combination Qt gave back.
    """
    #  SocketOptions QLocalSocket::socketOptions() const
    return QLocalSocket.SocketOptions(self.uglySide.call(
        'ritual_ZNK12QLocalSocket13socketOptionsEv',
    ))

  def state(self) -> LocalSocketState:
    """
    Calls Qt's 'LocalSocketState QLocalSocket::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#state

    Returns
    -------

    LocalSocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LocalSocketState(number)'
      gives.
    """
    #  LocalSocketState QLocalSocket::state() const
    return QLocalSocket.LocalSocketState(self.uglySide.call(
        'ritual_ZNK12QLocalSocket5stateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setServerName(self, name: str) -> None:
    """
    Calls Qt's 'void QLocalSocket::setServerName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#setServerName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLocalSocket::setServerName(const QString &name)
    self.uglySide.call(
        'ritual_ZN12QLocalSocket13setServerNameERK7QString', name,
    )

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QLocalSocket::setReadBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocket.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QLocalSocket::setReadBufferSize(qint64 size)
    self.uglySide.call('ritual_ZN12QLocalSocket17setReadBufferSizeEx', size)

  @overload(int)
  @overload(int, LocalSocketState)
  @overload(int, LocalSocketState, QIODeviceBase.OpenMode)
  def setSocketDescriptor(
      self,
      socketDescriptor: int,
      socketState: LocalSocketState = LocalSocketState.ConnectedState,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::setSocketDescriptor(qintptr
    socketDescriptor, LocalSocketState socketState, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocket.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    socketState : LocalSocketState
      Passed on as its number. May be left out, as in Qt: it is then
      LocalSocketState.ConnectedState.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QLocalSocket::setSocketDescriptor(qintptr socketDescriptor,
    #      LocalSocketState socketState, OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN12QLocalSocket19setSocketDescriptorExNS_16LocalSocketStat'
        'eE6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        socketDescriptor, socketState.value, openMode.value,
    )

  @overload(SocketOptions)
  def setSocketOptions(self, option: SocketOptions) -> None:
    """
    Calls Qt's 'void QLocalSocket::setSocketOptions(SocketOptions option)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#setSocketOptions

    Parameters
    ----------

    option : SocketOptions
      Passed on as its number.
    """
    #  void QLocalSocket::setSocketOptions(SocketOptions option)
    self.uglySide.call(
        'ritual_ZN12QLocalSocket16setSocketOptionsE6QFlagsINS_12SocketOptio'
        'nEE',
        option.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QLocalSocket::QLocalSocket(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#QLocalSocket

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLocalSocket::QLocalSocket(QObject *parent)
    self._noteCreation(QLocalSocket, lambda: Rituals.call(
        'ritual_ZN12QLocalSocketC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QLocalSocketPrivate]:
    """
    Calls Qt's 'QLocalSocketPrivate *QLocalSocket::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#d_func

    Returns
    -------

    Optional[QLocalSocketPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLocalSocketPrivate *QLocalSocket::d_func()
    address = self.uglySide.call('ritual_ZN12QLocalSocket6d_funcEv')
    from . import QLocalSocketPrivate
    return QLocalSocketPrivate._cuteAt(address)

  @overload()
  @overload(QIODeviceBase.OpenMode)
  def connectToServer(
      self,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QLocalSocket::connectToServer(OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#connectToServer

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QLocalSocket::connectToServer(OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN12QLocalSocket15connectToServerE6QFlagsIN13QIODeviceBase1'
        '2OpenModeFlagEE',
        openMode.value,
    )

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def connectToServer(
      self,
      name: str,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QLocalSocket::connectToServer(const QString &name,
    OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#connectToServer

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QLocalSocket::connectToServer(const QString &name, OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN12QLocalSocket15connectToServerERK7QString6QFlagsIN13QIOD'
        'eviceBase12OpenModeFlagEE',
        name, openMode.value,
    )

  def disconnectFromServer(self) -> None:
    """
    Calls Qt's 'void QLocalSocket::disconnectFromServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocket.html#disconnectFromServer
    """
    #  void QLocalSocket::disconnectFromServer()
    self.uglySide.call('ritual_ZN12QLocalSocket20disconnectFromServerEv')

  def abort(self) -> None:
    """
    Calls Qt's 'void QLocalSocket::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#abort
    """
    #  void QLocalSocket::abort()
    self.uglySide.call('ritual_ZN12QLocalSocket5abortEv')

  @overload()
  @overload(QIODeviceBase.OpenMode)
  def open(
      self,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::open(OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#open

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QLocalSocket::open(OpenMode openMode)
    ritual = (
        'ritual_ZN12QLocalSocket4openE6QFlagsIN13QIODeviceBase12OpenModeFla'
        'gEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QLocalSocket4openE6QFlagsIN13QIODeviceBase12OpenM'
          'odeFlagEE')
    return self.uglySide.call(ritual, openMode.value)

  def close(self) -> None:
    """
    Calls Qt's 'void QLocalSocket::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#close
    """
    #  void QLocalSocket::close()
    ritual = 'ritual_ZN12QLocalSocket5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLocalSocket5closeEv'
    self.uglySide.call(ritual)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#flush
    """
    #  bool QLocalSocket::flush()
    return self.uglySide.call('ritual_ZN12QLocalSocket5flushEv')

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::waitForBytesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocket.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QLocalSocket::waitForBytesWritten(int msecs)
    ritual = 'ritual_ZN12QLocalSocket19waitForBytesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLocalSocket19waitForBytesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForConnected(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::waitForConnected(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#waitForConnected

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QLocalSocket::waitForConnected(int msecs)
    return self.uglySide.call(
        'ritual_ZN12QLocalSocket16waitForConnectedEi', msecs,
    )

  @overload()
  @overload(int)
  def waitForDisconnected(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::waitForDisconnected(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocket.html#waitForDisconnected

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QLocalSocket::waitForDisconnected(int msecs)
    return self.uglySide.call(
        'ritual_ZN12QLocalSocket19waitForDisconnectedEi', msecs,
    )

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QLocalSocket::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QLocalSocket::waitForReadyRead(int msecs)
    ritual = 'ritual_ZN12QLocalSocket16waitForReadyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLocalSocket16waitForReadyReadEi'
    return self.uglySide.call(ritual, msecs)

  def connected(self) -> None:
    """
    Calls Qt's 'void QLocalSocket::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#connected
    """
    #  void QLocalSocket::connected()
    self.uglySide.call('ritual_ZN12QLocalSocket9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QLocalSocket::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#disconnected
    """
    #  void QLocalSocket::disconnected()
    self.uglySide.call('ritual_ZN12QLocalSocket12disconnectedEv')

  @overload(LocalSocketError)
  def errorOccurred(self, socketError: LocalSocketError) -> None:
    """
    Calls Qt's 'void
    QLocalSocket::errorOccurred(QLocalSocket::LocalSocketError socketError)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#errorOccurred

    Parameters
    ----------

    socketError : LocalSocketError
      Passed on as its number.
    """
    #  void QLocalSocket::errorOccurred(QLocalSocket::LocalSocketError
    #      socketError)
    self.uglySide.call(
        'ritual_ZN12QLocalSocket13errorOccurredENS_16LocalSocketErrorE',
        socketError.value,
    )

  @overload(LocalSocketState)
  def stateChanged(self, socketState: LocalSocketState) -> None:
    """
    Calls Qt's 'void
    QLocalSocket::stateChanged(QLocalSocket::LocalSocketState socketState)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#stateChanged

    Parameters
    ----------

    socketState : LocalSocketState
      Passed on as its number.
    """
    #  void QLocalSocket::stateChanged(QLocalSocket::LocalSocketState
    #      socketState)
    self.uglySide.call(
        'ritual_ZN12QLocalSocket12stateChangedENS_16LocalSocketStateE',
        socketState.value,
    )

  @overload(int)
  def skipData(self, maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QLocalSocket::skipData(qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#skipData

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QLocalSocket::skipData(qint64 maxSize)
    ritual = 'ritual_ZN12QLocalSocket8skipDataEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLocalSocket8skipDataEx'
    return self.uglySide.call(ritual, maxSize)

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, a0: Optional[str], a1: int) -> int:
    """
    Calls Qt's 'qint64 QLocalSocket::writeData(const char *a0, qint64 a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocket.html#writeData

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : int
      Passed on as it is.
    """
    #  qint64 QLocalSocket::writeData(const char *a0, qint64 a1)
    return self.uglySide.call(
        'ritual_ZN12QLocalSocket9writeDataEPKcx', self._bytesOf(a0), a1,
    )

  @staticmethod
  def bindableSocketOptions(*__, **_) -> Never:
    """
    Qt's 'QBindable<SocketOptions> QLocalSocket::bindableSocketOptions()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLocalSocket.bindableSocketOptions' has no cute function yet. "
        "Qt's 'QBindable<SocketOptions> "
        "QLocalSocket::bindableSocketOptions()': gives a type Python has no "
        "way to take yet.")
