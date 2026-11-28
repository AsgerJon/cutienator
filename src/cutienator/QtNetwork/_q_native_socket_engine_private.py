"""
QNativeSocketEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNativeSocketEnginePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QAbstractSocketEnginePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QHostAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']


class QNativeSocketEnginePrivate(QAbstractSocketEnginePrivate):
  """
  The cute side of Qt's QNativeSocketEnginePrivate: a plain Python object
  standing in front of one C++ QNativeSocketEnginePrivate.

  It is built on the cute 'QAbstractSocketEnginePrivate', as Qt's
  QNativeSocketEnginePrivate is built on Qt's QAbstractSocketEnginePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNativeSocketEnginePrivate that has a ritual and
  that Python can call so far, 1 name in all: 'adjustAddressProtocol'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeSocketEngine *QNativeSocketEnginePrivate::q_func()': gives
    'QNativeSocketEngine', which has no cute class yet.
  - Qt's 'const QNativeSocketEngine *QNativeSocketEnginePrivate::q_func()
    const': gives 'QNativeSocketEngine', which has no cute class yet.
  - Qt's 'QNativeSocketEnginePrivate::~QNativeSocketEnginePrivate()': the
    destructor: Python never removes a C++ QNativeSocketEnginePrivate.
  - Qt's 'void QNativeSocketEnginePrivate::setPortAndAddress(quint16 port,
    const QHostAddress &address, qt_sockaddr *aa, socklen_t *sockAddrSize)':
    names 'socklen_t', which has no cute class yet.

  What has no ritual
  ------------------

  25 of the 31 functions Qt declares: 23 cannot be called and cannot be
  called through the meta-object and cannot be copied; 2 leans on
  'QNativeSocketEngine.

  What to expect
  --------------

  - The C++ QNativeSocketEnginePrivate is created at the first use, not by
    'QNativeSocketEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeSocketEnginePrivate.
  - Each name of Qt's QNativeSocketEnginePrivate that has no cute function
    yet, 'checkProxy', 'createNewSocket', 'fetchConnectionParameters',
    'nativeAccept', 'nativeBind', 'nativeBytesAvailable',
    'nativeCheckConnection', 'nativeClose', 'nativeConnect',
    'nativeHasPendingDatagrams', 'nativeJoinMulticastGroup',
    'nativeLeaveMulticastGroup', 'nativeListen', 'nativeMulticastInterface',
    'nativePendingDatagramSize', 'nativeRead', 'nativeReceiveDatagram',
    'nativeSelect', 'nativeSendDatagram', 'nativeSetMulticastInterface',
    'nativeWrite', 'option', 'setError', 'setOption', 'setPortAndAddress',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QNativeSocketEnginePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ErrorString(CuteNum):
    """
    The enum 'QNativeSocketEnginePrivate::ErrorString' of Qt, with the 29
    names Qt gives in it.
    """

    NonBlockingInitFailedErrorString = Kee[int](0)
    BroadcastingInitFailedErrorString = Kee[int](1)
    NoIpV6ErrorString = Kee[int](2)
    RemoteHostClosedErrorString = Kee[int](3)
    TimeOutErrorString = Kee[int](4)
    ResourceErrorString = Kee[int](5)
    OperationUnsupportedErrorString = Kee[int](6)
    ProtocolUnsupportedErrorString = Kee[int](7)
    InvalidSocketErrorString = Kee[int](8)
    HostUnreachableErrorString = Kee[int](9)
    NetworkUnreachableErrorString = Kee[int](10)
    AccessErrorString = Kee[int](11)
    ConnectionTimeOutErrorString = Kee[int](12)
    ConnectionRefusedErrorString = Kee[int](13)
    AddressInuseErrorString = Kee[int](14)
    AddressNotAvailableErrorString = Kee[int](15)
    AddressProtectedErrorString = Kee[int](16)
    DatagramTooLargeErrorString = Kee[int](17)
    SendDatagramErrorString = Kee[int](18)
    ReceiveDatagramErrorString = Kee[int](19)
    WriteErrorString = Kee[int](20)
    ReadErrorString = Kee[int](21)
    PortInuseErrorString = Kee[int](22)
    NotSocketErrorString = Kee[int](23)
    InvalidProxyTypeString = Kee[int](24)
    TemporaryErrorString = Kee[int](25)
    NetworkDroppedConnectionErrorString = Kee[int](26)
    ConnectionResetErrorString = Kee[int](27)
    UnknownSocketErrorString = Kee[int](-1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeSocketEnginePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress)
  def adjustAddressProtocol(self, address: QHostAddress) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress
    QNativeSocketEnginePrivate::adjustAddressProtocol(const QHostAddress
    &address) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativesocketengineprivate.html

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNativeSocketEnginePrivate::adjustAddressProtocol(const
    #      QHostAddress &address) const
    address = self.uglySide.call(
        'ritual_ZNK26QNativeSocketEnginePrivate21adjustAddressProtocolERK12'
        'QHostAddress',
        self._valueOf(address),
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNativeSocketEnginePrivate::QNativeSocketEnginePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativesocketengineprivate.html
    """
    #  QNativeSocketEnginePrivate::QNativeSocketEnginePrivate()
    self._noteCreation(QNativeSocketEnginePrivate, lambda: Rituals.call(
        'ritual_ZN26QNativeSocketEnginePrivateC1Ev',
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

  @staticmethod
  def checkProxy(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::checkProxy(const QHostAddress
    &address)': leans on 'QNativeSocketEngine::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.checkProxy' has no cute function yet. "
        "Qt's 'bool QNativeSocketEnginePrivate::checkProxy(const "
        "QHostAddress &address)': leans on "
        "'QNativeSocketEngine::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def createNewSocket(*__, **_) -> Never:
    """
    Qt's 'bool
    QNativeSocketEnginePrivate::createNewSocket(QAbstractSocket::SocketType
    type, QAbstractSocket::NetworkLayerProtocol &protocol)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.createNewSocket' has no cute function "
        "yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::createNewSocket(QAbstractSocket::Socket"
        "Type type, QAbstractSocket::NetworkLayerProtocol &protocol)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def fetchConnectionParameters(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::fetchConnectionParameters()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.fetchConnectionParameters' has no cute "
        "function yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::fetchConnectionParameters()': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeAccept(*__, **_) -> Never:
    """
    Qt's 'qintptr QNativeSocketEnginePrivate::nativeAccept()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeAccept' has no cute function "
        "yet. Qt's 'qintptr QNativeSocketEnginePrivate::nativeAccept()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativeBind(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeBind(const QHostAddress
    &address, quint16 port)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeBind' has no cute function yet. "
        "Qt's 'bool QNativeSocketEnginePrivate::nativeBind(const "
        "QHostAddress &address, quint16 port)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def nativeBytesAvailable(*__, **_) -> Never:
    """
    Qt's 'qint64 QNativeSocketEnginePrivate::nativeBytesAvailable() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeBytesAvailable' has no cute "
        "function yet. Qt's 'qint64 "
        "QNativeSocketEnginePrivate::nativeBytesAvailable() const': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeCheckConnection(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeCheckConnection()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeCheckConnection' has no cute "
        "function yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::nativeCheckConnection()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeClose(*__, **_) -> Never:
    """
    Qt's 'void QNativeSocketEnginePrivate::nativeClose()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeClose' has no cute function yet. "
        "Qt's 'void QNativeSocketEnginePrivate::nativeClose()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeConnect(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeConnect(const QHostAddress
    &address, quint16 port)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeConnect' has no cute function "
        "yet. Qt's 'bool QNativeSocketEnginePrivate::nativeConnect(const "
        "QHostAddress &address, quint16 port)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def nativeHasPendingDatagrams(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeHasPendingDatagrams()
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeHasPendingDatagrams' has no cute "
        "function yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::nativeHasPendingDatagrams() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativeJoinMulticastGroup(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeJoinMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeJoinMulticastGroup' has no cute "
        "function yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::nativeJoinMulticastGroup(const "
        "QHostAddress &groupAddress, const QNetworkInterface &iface)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativeLeaveMulticastGroup(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeLeaveMulticastGroup(const
    QHostAddress &groupAddress, const QNetworkInterface &iface)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeLeaveMulticastGroup' has no cute "
        "function yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::nativeLeaveMulticastGroup(const "
        "QHostAddress &groupAddress, const QNetworkInterface &iface)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativeListen(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeListen(int backlog)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeListen' has no cute function "
        "yet. Qt's 'bool QNativeSocketEnginePrivate::nativeListen(int "
        "backlog)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def nativeMulticastInterface(*__, **_) -> Never:
    """
    Qt's 'QNetworkInterface
    QNativeSocketEnginePrivate::nativeMulticastInterface() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeMulticastInterface' has no cute "
        "function yet. Qt's 'QNetworkInterface "
        "QNativeSocketEnginePrivate::nativeMulticastInterface() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativePendingDatagramSize(*__, **_) -> Never:
    """
    Qt's 'qint64 QNativeSocketEnginePrivate::nativePendingDatagramSize()
    const': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativePendingDatagramSize' has no cute "
        "function yet. Qt's 'qint64 "
        "QNativeSocketEnginePrivate::nativePendingDatagramSize() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def nativeRead(*__, **_) -> Never:
    """
    Qt's 'qint64 QNativeSocketEnginePrivate::nativeRead(char *data, qint64
    maxLength)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeRead' has no cute function yet. "
        "Qt's 'qint64 QNativeSocketEnginePrivate::nativeRead(char *data, "
        "qint64 maxLength)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def nativeReceiveDatagram(*__, **_) -> Never:
    """
    Qt's 'qint64 QNativeSocketEnginePrivate::nativeReceiveDatagram(char
    *data, qint64 maxLength, QIpPacketHeader *header,
    QAbstractSocketEngine::PacketHeaderOptions options)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeReceiveDatagram' has no cute "
        "function yet. Qt's 'qint64 "
        "QNativeSocketEnginePrivate::nativeReceiveDatagram(char *data, "
        "qint64 maxLength, QIpPacketHeader *header, "
        "QAbstractSocketEngine::PacketHeaderOptions options)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def nativeSelect(*__, **_) -> Never:
    """
    - Qt's 'int QNativeSocketEnginePrivate::nativeSelect(QDeadlineTimer
      deadline, bool selectForRead) const': cannot be called and cannot be
      called through the meta-object and cannot be copied: no header file has
      its code, Qt's source does not mark it or its class for use from
      outside Qt or writes it 'inline' or nowhere, and it is no signal, slot
      or invokable function giving back nothing, of a class built on QObject,
      and Qt's source has no code for it that could be told from the rest.
    - Qt's 'int QNativeSocketEnginePrivate::nativeSelect(QDeadlineTimer
      deadline, bool checkRead, bool checkWrite, bool *selectForRead, bool
      *selectForWrite) const': cannot be called and cannot be called through
      the meta-object and cannot be copied: no header file has its code, Qt's
      source does not mark it or its class for use from outside Qt or writes
      it 'inline' or nowhere, and it is no signal, slot or invokable function
      giving back nothing, of a class built on QObject, and Qt's source has
      no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeSelect' has no cute function "
        "yet. Qt's 'int "
        "QNativeSocketEnginePrivate::nativeSelect(QDeadlineTimer deadline, "
        "bool selectForRead) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest. Qt's 'int "
        "QNativeSocketEnginePrivate::nativeSelect(QDeadlineTimer deadline, "
        "bool checkRead, bool checkWrite, bool *selectForRead, bool "
        "*selectForWrite) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def nativeSendDatagram(*__, **_) -> Never:
    """
    Qt's 'qint64 QNativeSocketEnginePrivate::nativeSendDatagram(const char
    *data, qint64 length, const QIpPacketHeader &header)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeSendDatagram' has no cute "
        "function yet. Qt's 'qint64 "
        "QNativeSocketEnginePrivate::nativeSendDatagram(const char *data, "
        "qint64 length, const QIpPacketHeader &header)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def nativeSetMulticastInterface(*__, **_) -> Never:
    """
    Qt's 'bool QNativeSocketEnginePrivate::nativeSetMulticastInterface(const
    QNetworkInterface &iface)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeSetMulticastInterface' has no "
        "cute function yet. Qt's 'bool "
        "QNativeSocketEnginePrivate::nativeSetMulticastInterface(const "
        "QNetworkInterface &iface)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def nativeWrite(*__, **_) -> Never:
    """
    Qt's 'qint64 QNativeSocketEnginePrivate::nativeWrite(const char *data,
    qint64 length)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.nativeWrite' has no cute function yet. "
        "Qt's 'qint64 QNativeSocketEnginePrivate::nativeWrite(const char "
        "*data, qint64 length)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def option(*__, **_) -> Never:
    """
    Qt's 'int
    QNativeSocketEnginePrivate::option(QNativeSocketEngine::SocketOption
    option) const': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.option' has no cute function yet. Qt's "
        "'int "
        "QNativeSocketEnginePrivate::option(QNativeSocketEngine::SocketOptio"
        "n option) const': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setError(*__, **_) -> Never:
    """
    Qt's 'void
    QNativeSocketEnginePrivate::setError(QAbstractSocket::SocketError error,
    ErrorString errorString) const': leans on
    'QNativeSocketEngine::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.setError' has no cute function yet. "
        "Qt's 'void "
        "QNativeSocketEnginePrivate::setError(QAbstractSocket::SocketError "
        "error, ErrorString errorString) const': leans on "
        "'QNativeSocketEngine::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setOption(*__, **_) -> Never:
    """
    Qt's 'bool
    QNativeSocketEnginePrivate::setOption(QNativeSocketEngine::SocketOption
    option, int value)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.setOption' has no cute function yet. "
        "Qt's 'bool "
        "QNativeSocketEnginePrivate::setOption(QNativeSocketEngine::SocketOp"
        "tion option, int value)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setPortAndAddress(*__, **_) -> Never:
    """
    Qt's 'void QNativeSocketEnginePrivate::setPortAndAddress(quint16 port,
    const QHostAddress &address, qt_sockaddr *aa, socklen_t *sockAddrSize)':
    names 'socklen_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeSocketEnginePrivate.setPortAndAddress' has no cute "
        "function yet. Qt's 'void "
        "QNativeSocketEnginePrivate::setPortAndAddress(quint16 port, const "
        "QHostAddress &address, qt_sockaddr *aa, socklen_t *sockAddrSize)': "
        "names 'socklen_t', which has no cute class yet.")
