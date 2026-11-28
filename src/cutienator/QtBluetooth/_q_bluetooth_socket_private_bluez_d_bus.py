"""
QBluetoothSocketPrivateBluezDBus binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QBluetoothSocketPrivateBluezDBus to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QIODeviceBase
from . import QBluetoothServiceInfo, QBluetoothSocket
from . import QBluetoothSocketBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBluetoothAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothSocketPrivateBluezDBus(QBluetoothSocketBasePrivate):
  """
  The cute side of Qt's QBluetoothSocketPrivateBluezDBus: a plain Python
  object standing in front of one C++ QBluetoothSocketPrivateBluezDBus.

  It is built on the cute 'QBluetoothSocketBasePrivate', as Qt's
  QBluetoothSocketPrivateBluezDBus is built on Qt's
  QBluetoothSocketBasePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothSocketPrivateBluezDBus that has a ritual
  and that Python can call so far, 7 names in all: 'connectToServiceHelper',
  'ensureNativeSocket', 'writeData', 'setSocketDescriptor', 'bytesAvailable',
  'canReadLine', 'bytesToWrite'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qint64 QBluetoothSocketPrivateBluezDBus::readData(char *data,
    qint64 maxSize)': names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  24 of the 32 functions Qt declares: 11 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 9 leans on
  'QBluetoothSocketPrivateBluezDBus; 2 not a gap; 1 leans on 'vtable for
  QBluetoothSocketPrivateBluezDBus', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken; 1 leans on 'vtable
  for QBluetoothSocketBasePrivate', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QBluetoothSocketPrivateBluezDBus is created at the first use, not
    by 'QBluetoothSocketPrivateBluezDBus(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothSocketPrivateBluezDBus.
  - Qt tells when it has removed the C++ QBluetoothSocketPrivateBluezDBus.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBluetoothSocketPrivateBluezDBus that has no cute
    function yet, '__init__', 'clearSocket', 'connectToServiceReplyHandler',
    'remoteConnected', 'socketStateChanged', holds a function that raises
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
  __qt_class__ = 'QBluetoothSocketPrivateBluezDBus'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateBluezDBus::bytesAvailable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html
    """
    #  qint64 QBluetoothSocketPrivateBluezDBus::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK32QBluetoothSocketPrivateBluezDBus14bytesAvailableEv',
    )

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocketPrivateBluezDBus::canReadLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html#canReadLine
    """
    #  bool QBluetoothSocketPrivateBluezDBus::canReadLine() const
    return self.uglySide.call(
        'ritual_ZNK32QBluetoothSocketPrivateBluezDBus11canReadLineEv',
    )

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateBluezDBus::bytesToWrite()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html#bytesToWrite
    """
    #  qint64 QBluetoothSocketPrivateBluezDBus::bytesToWrite() const
    return self.uglySide.call(
        'ritual_ZNK32QBluetoothSocketPrivateBluezDBus12bytesToWriteEv',
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
    Calls Qt's 'bool
    QBluetoothSocketPrivateBluezDBus::setSocketDescriptor(int
    socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
    openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html

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
    #  bool QBluetoothSocketPrivateBluezDBus::setSocketDescriptor(int
    #      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    #      QBluetoothSocket::SocketState socketState,
    #      QBluetoothSocket::OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN32QBluetoothSocketPrivateBluezDBus19setSocketDescriptorEi'
        'N21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketState'
        'E6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
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
    Qt's
    'QBluetoothSocketPrivateBluezDBus::QBluetoothSocketPrivateBluezDBus()':
    leans on 'vtable for QBluetoothSocketPrivateBluezDBus', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluezDBus.__init__' has no cute function "
        "yet. Qt's "
        "'QBluetoothSocketPrivateBluezDBus::QBluetoothSocketPrivateBluezDBus"
        "()': leans on 'vtable for QBluetoothSocketPrivateBluezDBus', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(QBluetoothAddress, int, QIODeviceBase.OpenMode)
  def connectToServiceHelper(
      self,
      address: QBluetoothAddress,
      port: int,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void
    QBluetoothSocketPrivateBluezDBus::connectToServiceHelper(const
    QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  void QBluetoothSocketPrivateBluezDBus::connectToServiceHelper(const
    #      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN32QBluetoothSocketPrivateBluezDBus22connectToServiceHelpe'
        'rERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, openMode.value,
    )

  @overload(QBluetoothServiceInfo.Protocol)
  def ensureNativeSocket(self, type: QBluetoothServiceInfo.Protocol) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocketPrivateBluezDBus::ensureNativeSocket(
    QBluetoothServiceInfo::Protocol type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html

    Parameters
    ----------

    type : QBluetoothServiceInfo.Protocol
      Passed on as its number.
    """
    #  bool QBluetoothSocketPrivateBluezDBus::ensureNativeSocket(
    #      QBluetoothServiceInfo::Protocol type)
    return self.uglySide.call(
        'ritual_ZN32QBluetoothSocketPrivateBluezDBus18ensureNativeSocketEN2'
        '1QBluetoothServiceInfo8ProtocolE',
        type.value,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateBluezDBus::writeData(const char
    *data, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatebluezdbus.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QBluetoothSocketPrivateBluezDBus::writeData(const char *data,
    #      qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN32QBluetoothSocketPrivateBluezDBus9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )

  @staticmethod
  def clearSocket(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothSocketPrivateBluezDBus::clearSocket()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluezDBus.clearSocket' has no cute "
        "function yet. Qt's 'void "
        "QBluetoothSocketPrivateBluezDBus::clearSocket()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def connectToServiceReplyHandler(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothSocketPrivateBluezDBus::connectToServiceReplyHandler(
    QDBusPendingCallWatcher *a0)': leans on
    'QBluetoothSocketPrivateBluezDBus::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluezDBus.connectToServiceReplyHandler' "
        "has no cute function yet. Qt's 'void "
        "QBluetoothSocketPrivateBluezDBus::connectToServiceReplyHandler(QDBu"
        "sPendingCallWatcher *a0)': leans on "
        "'QBluetoothSocketPrivateBluezDBus::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def remoteConnected(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothSocketPrivateBluezDBus::remoteConnected(const
    QDBusUnixFileDescriptor &fd)': leans on
    'QBluetoothSocketPrivateBluezDBus::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluezDBus.remoteConnected' has no cute "
        "function yet. Qt's 'void "
        "QBluetoothSocketPrivateBluezDBus::remoteConnected(const "
        "QDBusUnixFileDescriptor &fd)': leans on "
        "'QBluetoothSocketPrivateBluezDBus::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def socketStateChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothSocketPrivateBluezDBus::socketStateChanged(QLocalSocket::
    LocalSocketState newState)': leans on
    'QBluetoothSocketPrivateBluezDBus::clearSocket()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateBluezDBus.socketStateChanged' has no cute "
        "function yet. Qt's 'void "
        "QBluetoothSocketPrivateBluezDBus::socketStateChanged(QLocalSocket::"
        "LocalSocketState newState)': leans on "
        "'QBluetoothSocketPrivateBluezDBus::clearSocket()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
