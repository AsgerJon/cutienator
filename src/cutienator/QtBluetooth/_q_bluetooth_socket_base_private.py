"""
QBluetoothSocketBasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocketbase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QBluetoothSocketBasePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QIODeviceBase, QObject
from . import QBluetoothServiceInfo, QBluetoothSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
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


class QBluetoothSocketBasePrivate(QObject):
  """
  The cute side of Qt's QBluetoothSocketBasePrivate: a plain Python object
  standing in front of one C++ QBluetoothSocketBasePrivate.

  It is built on the cute 'QObject', as Qt's QBluetoothSocketBasePrivate is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothSocketBasePrivate that has a ritual and
  that Python can call so far, 18 names in all: 'metaObject',
  'ensureNativeSocket', 'localName', 'localAddress', 'localPort', 'peerName',
  'peerAddress', 'peerPort', 'abort', 'close', 'writeData', 'bytesAvailable',
  'canReadLine', 'bytesToWrite', 'setSocketDescriptor',
  'connectToServiceHelper', 'connectToService', 'q_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBluetoothSocketBasePrivate::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QBluetoothSocketBasePrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBluetoothSocketBasePrivate::~QBluetoothSocketBasePrivate()': the
    destructor: Python never removes a C++ QBluetoothSocketBasePrivate.
  - Qt's 'qint64 QBluetoothSocketBasePrivate::readData(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.
  - Qt's 'const QBluetoothSocket *QBluetoothSocketBasePrivate::q_func()
    const': takes in Python what 'QBluetoothSocket
    *QBluetoothSocketBasePrivate::q_func()' takes.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 leans on 'QBluetoothSocketBasePrivate.

  What to expect
  --------------

  - The C++ QBluetoothSocketBasePrivate is created at the first use, not by
    'QBluetoothSocketBasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothSocketBasePrivate.
  - Qt tells when it has removed the C++ QBluetoothSocketBasePrivate. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBluetoothSocketBasePrivate that has no cute function
    yet, '__init__', 'readData', holds a function that raises
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
  __qt_class__ = 'QBluetoothSocketBasePrivate'

  #  A C++ QBluetoothSocketBasePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBluetoothSocketBasePrivate'

  #  The functions Qt calls itself that QBluetoothSocketBasePrivate is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'writeData': (
          'qint64 QBluetoothSocketBasePrivate::writeData(const char *, '
          'qint64)',
      ),
      'readData': (
          'qint64 QBluetoothSocketBasePrivate::readData(char *, qint64)',
      ),
  }

  #  The functions Qt calls itself that QBluetoothSocketBasePrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'ensureNativeSocket': (
          ('_ZN27QBluetoothSocketBasePrivate18ensureNativeSocketEN21QBlueto'
           'othServiceInfo8ProtocolE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtBluetooth:QBluetoothServiceInfo.Protocol'),
           )),
      ),
      'localName': (
          ('_ZNK27QBluetoothSocketBasePrivate9localNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'localAddress': (
          ('_ZNK27QBluetoothSocketBasePrivate12localAddressEv',
           ('address', 'value', 'QtBluetooth:QBluetoothAddress'),
           ()),
      ),
      'localPort': (
          ('_ZNK27QBluetoothSocketBasePrivate9localPortEv',
           ('unsigned short', 'number', ''),
           ()),
      ),
      'peerName': (
          ('_ZNK27QBluetoothSocketBasePrivate8peerNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'peerAddress': (
          ('_ZNK27QBluetoothSocketBasePrivate11peerAddressEv',
           ('address', 'value', 'QtBluetooth:QBluetoothAddress'),
           ()),
      ),
      'peerPort': (
          ('_ZNK27QBluetoothSocketBasePrivate8peerPortEv',
           ('unsigned short', 'number', ''),
           ()),
      ),
      'abort': (
          ('_ZN27QBluetoothSocketBasePrivate5abortEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'close': (
          ('_ZN27QBluetoothSocketBasePrivate5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bytesAvailable': (
          ('_ZNK27QBluetoothSocketBasePrivate14bytesAvailableEv',
           ('long long', 'number', ''),
           ()),
      ),
      'canReadLine': (
          ('_ZNK27QBluetoothSocketBasePrivate11canReadLineEv',
           ('bool', 'number', ''),
           ()),
      ),
      'bytesToWrite': (
          ('_ZNK27QBluetoothSocketBasePrivate12bytesToWriteEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setSocketDescriptor': (
          ('_ZN27QBluetoothSocketBasePrivate19setSocketDescriptorEiN21QBlue'
           'toothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFl'
           'agsIN13QIODeviceBase12OpenModeFlagEE',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtBluetooth:QBluetoothServiceInfo.Protocol'),
               ('int', 'enum', 'QtBluetooth:QBluetoothSocket.SocketState'),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
           )),
      ),
      'connectToServiceHelper': (
          ('_ZN27QBluetoothSocketBasePrivate22connectToServiceHelperERK17QB'
           'luetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtBluetooth:QBluetoothAddress'),
               ('unsigned short', 'number', ''),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
           )),
      ),
      'connectToService': (
          ('_ZN27QBluetoothSocketBasePrivate16connectToServiceERK21QBluetoo'
           'thServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtBluetooth:QBluetoothServiceInfo'),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
           )),
          ('_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBluetoo'
           'thAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFl'
           'agEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtBluetooth:QBluetoothAddress'),
               ('address', 'value', 'QtBluetooth:QBluetoothUuid'),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
           )),
          ('_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBluetoo'
           'thAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtBluetooth:QBluetoothAddress'),
               ('unsigned short', 'number', ''),
               ('int', 'flags', 'QtCore:QIODeviceBase.OpenModeFlag'),
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
    Calls Qt's 'const QMetaObject *QBluetoothSocketBasePrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBluetoothSocketBasePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def localName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocketBasePrivate::localName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#localName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocketBasePrivate::localName() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate9localNameEv',
    )

  def localAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothSocketBasePrivate::localAddress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#localAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothSocketBasePrivate::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate12localAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothSocketBasePrivate::localPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#localPort
    """
    #  quint16 QBluetoothSocketBasePrivate::localPort() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate9localPortEv',
    )

  def peerName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothSocketBasePrivate::peerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#peerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothSocketBasePrivate::peerName() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate8peerNameEv',
    )

  def peerAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothSocketBasePrivate::peerAddress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#peerAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothSocketBasePrivate::peerAddress() const
    address = self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate11peerAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QBluetoothSocketBasePrivate::peerPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#peerPort
    """
    #  quint16 QBluetoothSocketBasePrivate::peerPort() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate8peerPortEv',
    )

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketBasePrivate::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#bytesAvailable
    """
    #  qint64 QBluetoothSocketBasePrivate::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate14bytesAvailableEv',
    )

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothSocketBasePrivate::canReadLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#canReadLine
    """
    #  bool QBluetoothSocketBasePrivate::canReadLine() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate11canReadLineEv',
    )

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketBasePrivate::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#bytesToWrite
    """
    #  qint64 QBluetoothSocketBasePrivate::bytesToWrite() const
    return self.uglySide.call(
        'ritual_ZNK27QBluetoothSocketBasePrivate12bytesToWriteEv',
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
    Calls Qt's 'bool QBluetoothSocketBasePrivate::setSocketDescriptor(int
    socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
    openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html

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
    #  bool QBluetoothSocketBasePrivate::setSocketDescriptor(int
    #      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
    #      QBluetoothSocket::SocketState socketState,
    #      QBluetoothSocket::OpenMode openMode)
    return self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate19setSocketDescriptorEiN21QB'
        'luetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFl'
        'agsIN13QIODeviceBase12OpenModeFlagEE',
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
    Qt's 'QBluetoothSocketBasePrivate::QBluetoothSocketBasePrivate(QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QBluetoothSocketBasePrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QBluetoothSocketBasePrivate::QBluetoothSocketBasePrivate(QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(QBluetoothServiceInfo.Protocol)
  def ensureNativeSocket(self, type: QBluetoothServiceInfo.Protocol) -> bool:
    """
    Calls Qt's 'bool
    QBluetoothSocketBasePrivate::ensureNativeSocket(QBluetoothServiceInfo::
    Protocol type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html

    Parameters
    ----------

    type : QBluetoothServiceInfo.Protocol
      Passed on as its number.
    """
    #  bool QBluetoothSocketBasePrivate::ensureNativeSocket(
    #      QBluetoothServiceInfo::Protocol type)
    return self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate18ensureNativeSocketEN21QBlu'
        'etoothServiceInfo8ProtocolE',
        type.value,
    )

  def abort(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocketBasePrivate::abort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#abort
    """
    #  void QBluetoothSocketBasePrivate::abort()
    self.uglySide.call('ritual_ZN27QBluetoothSocketBasePrivate5abortEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QBluetoothSocketBasePrivate::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#close
    """
    #  void QBluetoothSocketBasePrivate::close()
    self.uglySide.call('ritual_ZN27QBluetoothSocketBasePrivate5closeEv')

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QBluetoothSocketBasePrivate::writeData(const char
    *data, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QBluetoothSocketBasePrivate::writeData(const char *data, qint64
    #      maxSize)
    return self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )

  @overload(QBluetoothAddress, int, QIODeviceBase.OpenMode)
  def connectToServiceHelper(
      self,
      address: QBluetoothAddress,
      port: int,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void
    QBluetoothSocketBasePrivate::connectToServiceHelper(const
    QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html

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
    #  void QBluetoothSocketBasePrivate::connectToServiceHelper(const
    #      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate22connectToServiceHelperERK1'
        '7QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, openMode.value,
    )

  @overload(QBluetoothServiceInfo, QIODeviceBase.OpenMode)
  def connectToService(
      self,
      service: QBluetoothServiceInfo,
      openMode: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothSocketBasePrivate::connectToService(const
    QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#connectToService

    Parameters
    ----------

    service : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  void QBluetoothSocketBasePrivate::connectToService(const
    #      QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate16connectToServiceERK21QBlue'
        'toothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
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
    Calls Qt's 'void QBluetoothSocketBasePrivate::connectToService(const
    QBluetoothAddress &address, const QBluetoothUuid &uuid,
    QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#connectToService

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
    #  void QBluetoothSocketBasePrivate::connectToService(const
    #      QBluetoothAddress &address, const QBluetoothUuid &uuid,
    #      QIODevice::OpenMode openMode)
    self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBlue'
        'toothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFl'
        'agEE',
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
    Calls Qt's 'void QBluetoothSocketBasePrivate::connectToService(const
    QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#connectToService

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
    #  void QBluetoothSocketBasePrivate::connectToService(const
    #      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBlue'
        'toothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        self._valueOf(address), port, openMode.value,
    )

  def q_func(self) -> Optional[QBluetoothSocket]:
    """
    Calls Qt's 'QBluetoothSocket *QBluetoothSocketBasePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothsocketbaseprivate.html#q_func

    Returns
    -------

    Optional[QBluetoothSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothSocket *QBluetoothSocketBasePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QBluetoothSocketBasePrivate6q_funcEv',
    )
    return QBluetoothSocket._cuteAt(address)

  @staticmethod
  def readData(*__, **_) -> Never:
    """
    Qt's 'qint64 QBluetoothSocketBasePrivate::readData(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBluetoothSocketBasePrivate.readData' has no cute function yet. "
        "Qt's 'qint64 QBluetoothSocketBasePrivate::readData(char *data, "
        "qint64 maxSize)': names 'char', which has no cute class yet.")
