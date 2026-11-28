"""
QBluetoothSocketPrivateBluez binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluez_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QBluetoothSocketPrivateBluez to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QIODeviceBase
from . import QBluetoothServiceInfo, QBluetoothSocket
from . import QBluetoothSocketBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothSocketPrivateBluez(QBluetoothSocketBasePrivate):
  """
  The cute side of Qt's QBluetoothSocketPrivateBluez: a plain Python object
  standing in front of one C++ QBluetoothSocketPrivateBluez.

  It is built on the cute 'QBluetoothSocketBasePrivate', as Qt's
  QBluetoothSocketPrivateBluez is built on Qt's QBluetoothSocketBasePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothSocketPrivateBluez that has a ritual and
  that Python can call so far, 8 names in all: 'localName', 'abort', 'close',
  'writeData', 'setSocketDescriptor', 'bytesAvailable', 'canReadLine',
  'bytesToWrite'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qint64 QBluetoothSocketPrivateBluez::readData(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  20 of the 29 functions Qt declares: 10 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 6 leans on
  'QBluetoothSocketPrivateBluez; 2 not a gap; 1 leans on 'vtable for
  QBluetoothSocketPrivateBluez', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on 'vtable for
  QBluetoothSocketBasePrivate', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QBluetoothSocketPrivateBluez is created at the first use, not by
    'QBluetoothSocketPrivateBluez(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothSocketPrivateBluez.
  - Qt tells when it has removed the C++ QBluetoothSocketPrivateBluez. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBluetoothSocketPrivateBluez that has no cute function
    yet, '__init__', '_q_readNotify', '_q_writeNotify', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothSocketPrivateBluez'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def localName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocketPrivateBluez::localName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#localName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocketPrivateBluez::localName() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateBluez9localNameEv',
    )

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateBluez::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#bytesAvailable
    """
    #  qint64 QBluetoothSocketPrivateBluez::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateBluez14bytesAvailableEv',
    )

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocketPrivateBluez::canReadLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#canReadLine
    """
    #  bool QBluetoothSocketPrivateBluez::canReadLine() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateBluez11canReadLineEv',
    )

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateBluez::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#bytesToWrite
    """
    #  qint64 QBluetoothSocketPrivateBluez::bytesToWrite() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateBluez12bytesToWriteEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QBluetoothServiceInfo.Protocol)
  @overload(
      int, QBluetoothServiceInfo.Protocol, QBluetoothSocket.SocketState,
  )
  @overload(
      int, QBluetoothServiceInfo.Protocol, QBluetoothSocket.SocketState,
      QIODeviceBase.OpenMode,
  )
  def setSocketDescriptor(
      self,
      socketDescriptor: int,
      socketType: QBluetoothServiceInfo.Protocol,
      socketState: QBluetoothSocket.SocketState = (
          QBluetoothSocket.SocketState.ConnectedState),
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocketPrivateBluez::setSocketDescriptor(int
    socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
    openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    socketType : QBluetoothServiceInfo.Protocol
      Passed on as its number.

    socketState : QBluetoothSocket.SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      QBluetoothSocket.SocketState.ConnectedState.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QBluetoothSocketPrivateBluez::setSocketDescriptor(int
    #      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    #      QBluetoothSocket::SocketState socketState,
    #      QBluetoothSocket::OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateBluez19setSocketDescriptorEiN21Q'
        'BluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QF'
        'lagsIN13QIODeviceBase12OpenModeFlagEE',
        socketDescriptor, socketType.value, socketState.value,
        openMode.value,
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
    Qt's 'QBluetoothSocketPrivateBluez::QBluetoothSocketPrivateBluez()':
    leans on 'vtable for QBluetoothSocketPrivateBluez', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluez.__init__' has no cute function yet. "
        "Qt's "
        "'QBluetoothSocketPrivateBluez::QBluetoothSocketPrivateBluez()': "
        "leans on 'vtable for QBluetoothSocketPrivateBluez', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def abort(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateBluez::abort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#abort
    """
    #  void QBluetoothSocketPrivateBluez::abort()
    self.uglySide.call('ritual_ZN28QBluetoothSocketPrivateBluez5abortEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateBluez::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#close
    """
    #  void QBluetoothSocketPrivateBluez::close()
    self.uglySide.call('ritual_ZN28QBluetoothSocketPrivateBluez5closeEv')

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateBluez::writeData(const char
    *data, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluez.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QBluetoothSocketPrivateBluez::writeData(const char *data,
    #      qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateBluez9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )

  @staticmethod
  def _q_readNotify(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothSocketPrivateBluez::_q_readNotify()': leans on
    'QBluetoothSocketPrivateBluez::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluez._q_readNotify' has no cute function "
        "yet. Qt's 'void QBluetoothSocketPrivateBluez::_q_readNotify()': "
        "leans on "
        "'QBluetoothSocketPrivateBluez::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def _q_writeNotify(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothSocketPrivateBluez::_q_writeNotify()': leans on
    'QBluetoothSocketPrivateBluez::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluez._q_writeNotify' has no cute function "
        "yet. Qt's 'void QBluetoothSocketPrivateBluez::_q_writeNotify()': "
        "leans on "
        "'QBluetoothSocketPrivateBluez::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
