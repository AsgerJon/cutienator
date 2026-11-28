"""
QQnxNativeIo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qconnection_qnx_qiodevices.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QIODevice, QIODeviceBase, QObject
from ..QtNetwork import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQnxNativeIo(QIODevice):
  """
  The cute side of Qt's QQnxNativeIo: a plain Python object standing in front
  of one C++ QQnxNativeIo.

  It is built on the cute 'QIODevice', as Qt's QQnxNativeIo is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQnxNativeIo that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'connectToServer',
  'disconnectFromServer', 'setServerName', 'serverName', 'abort',
  'isSequential', 'bytesAvailable', 'bytesToWrite', 'open', 'close', 'state',
  'waitForBytesWritten', 'waitForReadyRead', 'connected', 'disconnected',
  'error', 'stateChanged', 'writeData'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQnxNativeIo::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQnxNativeIo::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQnxNativeIoPrivate *QQnxNativeIo::d_func()': gives
    'QQnxNativeIoPrivate', which has no cute class yet.
  - Qt's 'const QQnxNativeIoPrivate *QQnxNativeIo::d_func() const': gives
    'QQnxNativeIoPrivate', which has no cute class yet.
  - Qt's 'QQnxNativeIo::~QQnxNativeIo()': the destructor: Python never
    removes a C++ QQnxNativeIo.
  - Qt's 'qint64 QQnxNativeIo::readData(char *a0, qint64 a1)': names 'char',
    which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 37 functions Qt declares: 5 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQnxNativeIo is created at the first use, not by
    'QQnxNativeIo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQnxNativeIo.
  - Qt tells when it has removed the C++ QQnxNativeIo. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQnxNativeIo that has no cute function yet, 'flush',
    'isValid', 'waitForConnected', 'waitForDisconnected', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QQnxNativeIo::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#tr

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
    #  QString QQnxNativeIo::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQnxNativeIo2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQnxNativeIo'

  #  A C++ QQnxNativeIo Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQnxNativeIo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQnxNativeIo::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQnxNativeIo::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQnxNativeIo10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def serverName(self) -> str:
    """
    Calls Qt's 'QString QQnxNativeIo::serverName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#serverName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQnxNativeIo::serverName() const
    return self.uglySide.call('ritual_ZNK12QQnxNativeIo10serverNameEv')

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QQnxNativeIo::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#isSequential
    """
    #  bool QQnxNativeIo::isSequential() const
    ritual = 'ritual_ZNK12QQnxNativeIo12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQnxNativeIo12isSequentialEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QQnxNativeIo::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#bytesAvailable
    """
    #  qint64 QQnxNativeIo::bytesAvailable() const
    ritual = 'ritual_ZNK12QQnxNativeIo14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQnxNativeIo14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QQnxNativeIo::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#bytesToWrite
    """
    #  qint64 QQnxNativeIo::bytesToWrite() const
    ritual = 'ritual_ZNK12QQnxNativeIo12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQnxNativeIo12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def state(self) -> QAbstractSocket.SocketState:
    """
    Calls Qt's 'QAbstractSocket::SocketState QQnxNativeIo::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#state

    Returns
    -------

    QAbstractSocket.SocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketState(number)' gives.
    """
    #  QAbstractSocket::SocketState QQnxNativeIo::state() const
    return QAbstractSocket.SocketState(self.uglySide.call(
        'ritual_ZNK12QQnxNativeIo5stateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setServerName(self, name: str) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::setServerName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#setServerName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQnxNativeIo::setServerName(const QString &name)
    self.uglySide.call(
        'ritual_ZN12QQnxNativeIo13setServerNameERK7QString', name,
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
    Notes what was given, for Qt's 'QQnxNativeIo::QQnxNativeIo(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#QQnxNativeIo

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQnxNativeIo::QQnxNativeIo(QObject *parent)
    self._noteCreation(QQnxNativeIo, lambda: Rituals.call(
        'ritual_ZN12QQnxNativeIoC1EP7QObject',
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

  @overload()
  @overload(QIODeviceBase.OpenMode)
  def connectToServer(
      self,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QQnxNativeIo::connectToServer(OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#connectToServer

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QQnxNativeIo::connectToServer(OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN12QQnxNativeIo15connectToServerE6QFlagsIN13QIODeviceBase1'
        '2OpenModeFlagEE',
        openMode.value,
    )

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def connectToServer(
      self,
      name: str,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QQnxNativeIo::connectToServer(const QString &name,
    OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#connectToServer

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QQnxNativeIo::connectToServer(const QString &name, OpenMode
    #      openMode)
    return self.uglySide.call(
        'ritual_ZN12QQnxNativeIo15connectToServerERK7QString6QFlagsIN13QIOD'
        'eviceBase12OpenModeFlagEE',
        name, openMode.value,
    )

  def disconnectFromServer(self) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::disconnectFromServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqnxnativeio.html#disconnectFromServer
    """
    #  void QQnxNativeIo::disconnectFromServer()
    self.uglySide.call('ritual_ZN12QQnxNativeIo20disconnectFromServerEv')

  def abort(self) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#abort
    """
    #  void QQnxNativeIo::abort()
    self.uglySide.call('ritual_ZN12QQnxNativeIo5abortEv')

  @overload()
  @overload(QIODeviceBase.OpenMode)
  def open(
      self,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QQnxNativeIo::open(OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#open

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QQnxNativeIo::open(OpenMode openMode)
    ritual = (
        'ritual_ZN12QQnxNativeIo4openE6QFlagsIN13QIODeviceBase12OpenModeFla'
        'gEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQnxNativeIo4openE6QFlagsIN13QIODeviceBase12OpenM'
          'odeFlagEE')
    return self.uglySide.call(ritual, openMode.value)

  def close(self) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#close
    """
    #  void QQnxNativeIo::close()
    ritual = 'ritual_ZN12QQnxNativeIo5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQnxNativeIo5closeEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QQnxNativeIo::waitForBytesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqnxnativeio.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QQnxNativeIo::waitForBytesWritten(int msecs)
    ritual = 'ritual_ZN12QQnxNativeIo19waitForBytesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQnxNativeIo19waitForBytesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QQnxNativeIo::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QQnxNativeIo::waitForReadyRead(int msecs)
    ritual = 'ritual_ZN12QQnxNativeIo16waitForReadyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQnxNativeIo16waitForReadyReadEi'
    return self.uglySide.call(ritual, msecs)

  def connected(self) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#connected
    """
    #  void QQnxNativeIo::connected()
    self.uglySide.call('ritual_ZN12QQnxNativeIo9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#disconnected
    """
    #  void QQnxNativeIo::disconnected()
    self.uglySide.call('ritual_ZN12QQnxNativeIo12disconnectedEv')

  @overload(QAbstractSocket.SocketError)
  def error(self, socketError: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::error(QAbstractSocket::SocketError
    socketError)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#error

    Parameters
    ----------

    socketError : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QQnxNativeIo::error(QAbstractSocket::SocketError socketError)
    self.uglySide.call(
        'ritual_ZN12QQnxNativeIo5errorEN15QAbstractSocket11SocketErrorE',
        socketError.value,
    )

  @overload(QAbstractSocket.SocketState)
  def stateChanged(self, socketState: QAbstractSocket.SocketState) -> None:
    """
    Calls Qt's 'void QQnxNativeIo::stateChanged(QAbstractSocket::SocketState
    socketState)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#stateChanged

    Parameters
    ----------

    socketState : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QQnxNativeIo::stateChanged(QAbstractSocket::SocketState
    #      socketState)
    self.uglySide.call(
        'ritual_ZN12QQnxNativeIo12stateChangedEN15QAbstractSocket11SocketSt'
        'ateE',
        socketState.value,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, a0: Optional[str], a1: int) -> int:
    """
    Calls Qt's 'qint64 QQnxNativeIo::writeData(const char *a0, qint64 a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqnxnativeio.html#writeData

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : int
      Passed on as it is.
    """
    #  qint64 QQnxNativeIo::writeData(const char *a0, qint64 a1)
    return self.uglySide.call(
        'ritual_ZN12QQnxNativeIo9writeDataEPKcx', self._bytesOf(a0), a1,
    )

  @staticmethod
  def flush(*__, **_) -> Never:
    """
    Qt's 'bool QQnxNativeIo::flush()': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQnxNativeIo.flush' has no cute function yet. Qt's 'bool "
        "QQnxNativeIo::flush()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QQnxNativeIo::isValid() const': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQnxNativeIo.isValid' has no cute function yet. Qt's 'bool "
        "QQnxNativeIo::isValid() const': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def waitForConnected(*__, **_) -> Never:
    """
    Qt's 'bool QQnxNativeIo::waitForConnected(int msecs)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQnxNativeIo.waitForConnected' has no cute function yet. Qt's "
        "'bool QQnxNativeIo::waitForConnected(int msecs)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def waitForDisconnected(*__, **_) -> Never:
    """
    Qt's 'bool QQnxNativeIo::waitForDisconnected(int msecs)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQnxNativeIo.waitForDisconnected' has no cute function yet. Qt's "
        "'bool QQnxNativeIo::waitForDisconnected(int msecs)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
