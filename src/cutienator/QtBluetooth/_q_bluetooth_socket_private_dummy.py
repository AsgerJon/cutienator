"""
QBluetoothSocketPrivateDummy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_dummy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QBluetoothSocketPrivateDummy to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QIODeviceBase
from . import QBluetoothServiceInfo, QBluetoothSocket
from . import QBluetoothSocketBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBluetoothAddress, QBluetoothUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothUuid = WAIT['QBluetoothUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothSocketPrivateDummy(QBluetoothSocketBasePrivate):
  """
  The cute side of Qt's QBluetoothSocketPrivateDummy: a plain Python object
  standing in front of one C++ QBluetoothSocketPrivateDummy.

  It is built on the cute 'QBluetoothSocketBasePrivate', as Qt's
  QBluetoothSocketPrivateDummy is built on Qt's QBluetoothSocketBasePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothSocketPrivateDummy that has a ritual and
  that Python can call so far, 16 names in all: 'connectToServiceHelper',
  'connectToService', 'ensureNativeSocket', 'localName', 'localAddress',
  'localPort', 'peerName', 'peerAddress', 'peerPort', 'abort', 'close',
  'writeData', 'setSocketDescriptor', 'bytesAvailable', 'canReadLine',
  'bytesToWrite'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qint64 QBluetoothSocketPrivateDummy::readData(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  8 of the 27 functions Qt declares: 4 leans on
  'QBluetoothSocketPrivateDummy; 2 not a gap; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'vtable for QBluetoothSocketBasePrivate', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QBluetoothSocketPrivateDummy is created at the first use, not by
    'QBluetoothSocketPrivateDummy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothSocketPrivateDummy.
  - Qt tells when it has removed the C++ QBluetoothSocketPrivateDummy. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBluetoothSocketPrivateDummy that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothSocketPrivateDummy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def localName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocketPrivateDummy::localName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#localName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocketPrivateDummy::localName() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy9localNameEv',
    )

  def localAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress
    QBluetoothSocketPrivateDummy::localAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#localAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothSocketPrivateDummy::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy12localAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothSocketPrivateDummy::localPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#localPort
    """
    #  quint16 QBluetoothSocketPrivateDummy::localPort() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy9localPortEv',
    )

  def peerName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocketPrivateDummy::peerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#peerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocketPrivateDummy::peerName() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy8peerNameEv',
    )

  def peerAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothSocketPrivateDummy::peerAddress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#peerAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothSocketPrivateDummy::peerAddress() const
    address = self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy11peerAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothSocketPrivateDummy::peerPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#peerPort
    """
    #  quint16 QBluetoothSocketPrivateDummy::peerPort() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy8peerPortEv',
    )

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateDummy::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#bytesAvailable
    """
    #  qint64 QBluetoothSocketPrivateDummy::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy14bytesAvailableEv',
    )

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocketPrivateDummy::canReadLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#canReadLine
    """
    #  bool QBluetoothSocketPrivateDummy::canReadLine() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy11canReadLineEv',
    )

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateDummy::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#bytesToWrite
    """
    #  qint64 QBluetoothSocketPrivateDummy::bytesToWrite() const
    return self.uglySide.call(
        'ritual_ZNK28QBluetoothSocketPrivateDummy12bytesToWriteEv',
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
    Calls Qt's 'bool QBluetoothSocketPrivateDummy::setSocketDescriptor(int
    socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
    openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html

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
    #  bool QBluetoothSocketPrivateDummy::setSocketDescriptor(int
    #      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    #      QBluetoothSocket::SocketState socketState,
    #      QBluetoothSocket::OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy19setSocketDescriptorEiN21Q'
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
    Qt's 'QBluetoothSocketPrivateDummy::QBluetoothSocketPrivateDummy()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'printDummyWarning'.
    """
    raise NotImplementedError(
        "'QBluetoothSocketPrivateDummy.__init__' has no cute function yet. "
        "Qt's "
        "'QBluetoothSocketPrivateDummy::QBluetoothSocketPrivateDummy()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'printDummyWarning'.")

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
    QBluetoothSocketPrivateDummy::connectToServiceHelper(const
    QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html

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
    #  void QBluetoothSocketPrivateDummy::connectToServiceHelper(const
    #      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy22connectToServiceHelperERK'
        '17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, openMode.value,
    )

  @overload(QBluetoothServiceInfo, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      service: QBluetoothServiceInfo,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateDummy::connectToService(const
    QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#connectToService

    Parameters
    ----------

    service : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  void QBluetoothSocketPrivateDummy::connectToService(const
    #      QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy16connectToServiceERK21QBlu'
        'etoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(service), openMode.value,
    )

  @overload(QBluetoothAddress, QBluetoothUuid, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      address: QBluetoothAddress,
      uuid: QBluetoothUuid,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateDummy::connectToService(const
    QBluetoothAddress &address, const QBluetoothUuid &uuid,
    QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#connectToService

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  void QBluetoothSocketPrivateDummy::connectToService(const
    #      QBluetoothAddress &address, const QBluetoothUuid &uuid,
    #      QIODevice::OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy16connectToServiceERK17QBlu'
        'etoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeF'
        'lagEE',
        self._valueOf(address), self._valueOf(uuid), openMode.value,
    )

  @overload(QBluetoothAddress, int, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      address: QBluetoothAddress,
      port: int,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateDummy::connectToService(const
    QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#connectToService

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
    #  void QBluetoothSocketPrivateDummy::connectToService(const
    #      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy16connectToServiceERK17QBlu'
        'etoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, openMode.value,
    )

  @overload(QBluetoothServiceInfo.Protocol)
  def ensureNativeSocket(self, type: QBluetoothServiceInfo.Protocol) -> bool:
    """
    Calls Qt's 'bool
    QBluetoothSocketPrivateDummy::ensureNativeSocket(QBluetoothServiceInfo::
    Protocol type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html

    Parameters
    ----------

    type : QBluetoothServiceInfo.Protocol
      Passed on as its number.
    """
    #  bool QBluetoothSocketPrivateDummy::ensureNativeSocket(
    #      QBluetoothServiceInfo::Protocol type)
    return self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy18ensureNativeSocketEN21QBl'
        'uetoothServiceInfo8ProtocolE',
        type.value,
    )

  def abort(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateDummy::abort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#abort
    """
    #  void QBluetoothSocketPrivateDummy::abort()
    self.uglySide.call('ritual_ZN28QBluetoothSocketPrivateDummy5abortEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocketPrivateDummy::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#close
    """
    #  void QBluetoothSocketPrivateDummy::close()
    self.uglySide.call('ritual_ZN28QBluetoothSocketPrivateDummy5closeEv')

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketPrivateDummy::writeData(const char
    *data, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketprivatedummy.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QBluetoothSocketPrivateDummy::writeData(const char *data,
    #      qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN28QBluetoothSocketPrivateDummy9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )
