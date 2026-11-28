"""
QIOQnxSource binding of the Qt C++
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


class QIOQnxSource(QIODevice):
  """
  The cute side of Qt's QIOQnxSource: a plain Python object standing in front
  of one C++ QIOQnxSource.

  It is built on the cute 'QIODevice', as Qt's QIOQnxSource is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIOQnxSource that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'isSequential',
  'bytesAvailable', 'bytesToWrite', 'close', 'state', 'waitForBytesWritten',
  'waitForReadyRead', 'disconnected', 'error', 'stateChanged', 'writeData',
  'open', 'onDisconnected'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QIOQnxSource::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QIOQnxSource::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QIOQnxSourcePrivate *QIOQnxSource::d_func()': gives
    'QIOQnxSourcePrivate', which has no cute class yet.
  - Qt's 'const QIOQnxSourcePrivate *QIOQnxSource::d_func() const': gives
    'QIOQnxSourcePrivate', which has no cute class yet.
  - Qt's 'QIOQnxSource::~QIOQnxSource()': the destructor: Python never
    removes a C++ QIOQnxSource.
  - Qt's 'qint64 QIOQnxSource::readData(char *a0, qint64 a1)': names 'char',
    which has no cute class yet.

  What has no ritual
  ------------------

  8 of the 30 functions Qt declares: 4 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QIOQnxSource is created at the first use, not by
    'QIOQnxSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIOQnxSource.
  - Qt tells when it has removed the C++ QIOQnxSource. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QIOQnxSource that has no cute function yet, 'isValid',
    'waitForConnected', 'waitForDisconnected', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QIOQnxSource::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#tr

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
    #  QString QIOQnxSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QIOQnxSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIOQnxSource'

  #  A C++ QIOQnxSource Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIOQnxSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QIOQnxSource::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QIOQnxSource::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QIOQnxSource10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QIOQnxSource::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#isSequential
    """
    #  bool QIOQnxSource::isSequential() const
    ritual = 'ritual_ZNK12QIOQnxSource12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QIOQnxSource12isSequentialEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QIOQnxSource::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#bytesAvailable
    """
    #  qint64 QIOQnxSource::bytesAvailable() const
    ritual = 'ritual_ZNK12QIOQnxSource14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QIOQnxSource14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QIOQnxSource::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#bytesToWrite
    """
    #  qint64 QIOQnxSource::bytesToWrite() const
    ritual = 'ritual_ZNK12QIOQnxSource12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QIOQnxSource12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def state(self) -> QAbstractSocket.SocketState:
    """
    Calls Qt's 'QAbstractSocket::SocketState QIOQnxSource::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#state

    Returns
    -------

    QAbstractSocket.SocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketState(number)' gives.
    """
    #  QAbstractSocket::SocketState QIOQnxSource::state() const
    return QAbstractSocket.SocketState(self.uglySide.call(
        'ritual_ZNK12QIOQnxSource5stateEv',
    ))

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

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(self, rcvid: int, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QIOQnxSource::QIOQnxSource(int rcvid,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#QIOQnxSource

    Parameters
    ----------

    rcvid : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QIOQnxSource::QIOQnxSource(int rcvid, QObject *parent)
    self._noteCreation(QIOQnxSource, lambda: Rituals.call(
        'ritual_ZN12QIOQnxSourceC1EiP7QObject',
        rcvid, self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QIOQnxSource::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#close
    """
    #  void QIOQnxSource::close()
    ritual = 'ritual_ZN12QIOQnxSource5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QIOQnxSource5closeEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QIOQnxSource::waitForBytesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qioqnxsource.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QIOQnxSource::waitForBytesWritten(int msecs)
    ritual = 'ritual_ZN12QIOQnxSource19waitForBytesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QIOQnxSource19waitForBytesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QIOQnxSource::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QIOQnxSource::waitForReadyRead(int msecs)
    ritual = 'ritual_ZN12QIOQnxSource16waitForReadyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QIOQnxSource16waitForReadyReadEi'
    return self.uglySide.call(ritual, msecs)

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QIOQnxSource::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#disconnected
    """
    #  void QIOQnxSource::disconnected()
    self.uglySide.call('ritual_ZN12QIOQnxSource12disconnectedEv')

  @overload(QAbstractSocket.SocketError)
  def error(self, socketError: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void QIOQnxSource::error(QAbstractSocket::SocketError
    socketError)'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#error

    Parameters
    ----------

    socketError : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QIOQnxSource::error(QAbstractSocket::SocketError socketError)
    self.uglySide.call(
        'ritual_ZN12QIOQnxSource5errorEN15QAbstractSocket11SocketErrorE',
        socketError.value,
    )

  @overload(QAbstractSocket.SocketState)
  def stateChanged(self, socketState: QAbstractSocket.SocketState) -> None:
    """
    Calls Qt's 'void QIOQnxSource::stateChanged(QAbstractSocket::SocketState
    socketState)'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#stateChanged

    Parameters
    ----------

    socketState : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QIOQnxSource::stateChanged(QAbstractSocket::SocketState
    #      socketState)
    self.uglySide.call(
        'ritual_ZN12QIOQnxSource12stateChangedEN15QAbstractSocket11SocketSt'
        'ateE',
        socketState.value,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, a0: Optional[str], a1: int) -> int:
    """
    Calls Qt's 'qint64 QIOQnxSource::writeData(const char *a0, qint64 a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#writeData

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : int
      Passed on as it is.
    """
    #  qint64 QIOQnxSource::writeData(const char *a0, qint64 a1)
    return self.uglySide.call(
        'ritual_ZN12QIOQnxSource9writeDataEPKcx', self._bytesOf(a0), a1,
    )

  @overload(QIODeviceBase.OpenMode)
  def open(self, openMode: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QIOQnxSource::open(OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#open

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QIOQnxSource::open(OpenMode openMode)
    ritual = (
        'ritual_ZN12QIOQnxSource4openE6QFlagsIN13QIODeviceBase12OpenModeFla'
        'gEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QIOQnxSource4openE6QFlagsIN13QIODeviceBase12OpenM'
          'odeFlagEE')
    return self.uglySide.call(ritual, openMode.value)

  def onDisconnected(self) -> None:
    """
    Calls Qt's 'void QIOQnxSource::onDisconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qioqnxsource.html#onDisconnected
    """
    #  void QIOQnxSource::onDisconnected()
    self.uglySide.call('ritual_ZN12QIOQnxSource14onDisconnectedEv')

  @staticmethod
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QIOQnxSource::isValid() const': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QIOQnxSource.isValid' has no cute function yet. Qt's 'bool "
        "QIOQnxSource::isValid() const': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def waitForConnected(*__, **_) -> Never:
    """
    Qt's 'bool QIOQnxSource::waitForConnected(int msecs)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QIOQnxSource.waitForConnected' has no cute function yet. Qt's "
        "'bool QIOQnxSource::waitForConnected(int msecs)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def waitForDisconnected(*__, **_) -> Never:
    """
    Qt's 'bool QIOQnxSource::waitForDisconnected(int msecs)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QIOQnxSource.waitForDisconnected' has no cute function yet. Qt's "
        "'bool QIOQnxSource::waitForDisconnected(int msecs)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
