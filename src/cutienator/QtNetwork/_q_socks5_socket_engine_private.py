"""
QSocks5SocketEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSocks5SocketEnginePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QAbstractSocketEnginePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSocks5SocketEngine


class QSocks5SocketEnginePrivate(QAbstractSocketEnginePrivate):
  """
  The cute side of Qt's QSocks5SocketEnginePrivate: a plain Python object
  standing in front of one C++ QSocks5SocketEnginePrivate.

  It is built on the cute 'QAbstractSocketEnginePrivate', as Qt's
  QSocks5SocketEnginePrivate is built on Qt's QAbstractSocketEnginePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSocks5SocketEnginePrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSocks5SocketEngine *QSocks5SocketEnginePrivate::q_func()
    const': takes in Python what 'QSocks5SocketEngine
    *QSocks5SocketEnginePrivate::q_func()' takes.
  - Qt's 'QSocks5SocketEnginePrivate::~QSocks5SocketEnginePrivate()': the
    destructor: Python never removes a C++ QSocks5SocketEnginePrivate.

  What has no ritual
  ------------------

  23 of the 27 functions Qt declares: 21 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied; 1
  leans on 'QSocks5SocketEngine.

  What to expect
  --------------

  - The C++ QSocks5SocketEnginePrivate is created at the first use, not by
    'QSocks5SocketEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSocks5SocketEnginePrivate.
  - Each name of Qt's QSocks5SocketEnginePrivate that has no cute function
    yet, '_q_controlSocketBytesWritten', '_q_controlSocketConnected',
    '_q_controlSocketDisconnected', '_q_controlSocketErrorOccurred',
    '_q_controlSocketReadNotification', '_q_controlSocketStateChanged',
    '_q_emitPendingConnectionNotification', '_q_emitPendingReadNotification',
    '_q_emitPendingWriteNotification', '_q_udpSocketReadNotification',
    'emitConnectionNotification', 'emitReadNotification',
    'emitWriteNotification', 'initialize', 'parseAuthenticatingReply',
    'parseAuthenticationMethodReply', 'parseNewConnection',
    'parseRequestMethodReply', 'reauthenticate', 'sendRequestMethod',
    'setErrorState', 'waitForConnected', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSocks5SocketEnginePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Socks5Error(CuteNum):
    """
    The enum 'QSocks5SocketEnginePrivate::Socks5Error' of Qt, with the 10
    names Qt gives in it.
    """

    SocksFailure = Kee[int](1)
    ConnectionNotAllowed = Kee[int](2)
    NetworkUnreachable = Kee[int](3)
    HostUnreachable = Kee[int](4)
    ConnectionRefused = Kee[int](5)
    TTLExpired = Kee[int](6)
    CommandNotSupported = Kee[int](7)
    AddressTypeNotSupported = Kee[int](8)
    LastKnownError = Kee[int](8)
    UnknownError = Kee[int](9)

  class Socks5Mode(CuteNum):
    """
    The enum 'QSocks5SocketEnginePrivate::Socks5Mode' of Qt, with the 4 names
    Qt gives in it.
    """

    NoMode = Kee[int](0)
    ConnectMode = Kee[int](1)
    BindMode = Kee[int](2)
    UdpAssociateMode = Kee[int](3)

  class Socks5State(CuteNum):
    """
    The enum 'QSocks5SocketEnginePrivate::Socks5State' of Qt, with the 13
    names Qt gives in it.
    """

    Uninitialized = Kee[int](0)
    ConnectError = Kee[int](1)
    AuthenticationMethodsSent = Kee[int](2)
    Authenticating = Kee[int](3)
    AuthenticatingError = Kee[int](4)
    RequestMethodSent = Kee[int](5)
    RequestError = Kee[int](6)
    Connected = Kee[int](7)
    UdpAssociateSuccess = Kee[int](8)
    BindSuccess = Kee[int](9)
    ControlSocketError = Kee[int](10)
    SocksError = Kee[int](11)
    HostNameLookupError = Kee[int](12)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSocks5SocketEnginePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QSocks5SocketEnginePrivate::QSocks5SocketEnginePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengineprivate.html
    """
    #  QSocks5SocketEnginePrivate::QSocks5SocketEnginePrivate()
    self._noteCreation(QSocks5SocketEnginePrivate, lambda: Rituals.call(
        'ritual_ZN26QSocks5SocketEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QSocks5SocketEngine]:
    """
    Calls Qt's 'QSocks5SocketEngine *QSocks5SocketEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5socketengineprivate.html#q_func

    Returns
    -------

    Optional[QSocks5SocketEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSocks5SocketEngine *QSocks5SocketEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QSocks5SocketEnginePrivate6q_funcEv',
    )
    from . import QSocks5SocketEngine
    return QSocks5SocketEngine._cuteAt(address)

  @staticmethod
  def _q_controlSocketBytesWritten(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_controlSocketBytesWritten()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QSOCKS5_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_controlSocketBytesWritten' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_controlSocketBytesWritten()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_DEBUG'.")

  @staticmethod
  def _q_controlSocketConnected(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_controlSocketConnected()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QSOCKS5_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_controlSocketConnected' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_controlSocketConnected()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_DEBUG'.")

  @staticmethod
  def _q_controlSocketDisconnected(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_controlSocketDisconnected()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_controlSocketDisconnected' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_controlSocketDisconnected()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def _q_controlSocketErrorOccurred(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_controlSocketErrorOccurred(
    QAbstractSocket::SocketError a0)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_controlSocketErrorOccurred' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_controlSocketErrorOccurred(QAbstract"
        "Socket::SocketError a0)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def _q_controlSocketReadNotification(*__, **_) -> Never:
    """
    Qt's 'void
    QSocks5SocketEnginePrivate::_q_controlSocketReadNotification()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QSocks5Data'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_controlSocketReadNotification' has "
        "no cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_controlSocketReadNotification()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QSocks5Data'.")

  @staticmethod
  def _q_controlSocketStateChanged(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_controlSocketStateChanged(
    QAbstractSocket::SocketState a0)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_controlSocketStateChanged' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_controlSocketStateChanged(QAbstractS"
        "ocket::SocketState a0)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def _q_emitPendingConnectionNotification(*__, **_) -> Never:
    """
    Qt's 'void
    QSocks5SocketEnginePrivate::_q_emitPendingConnectionNotification()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_emitPendingConnectionNotification' "
        "has no cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_emitPendingConnectionNotification()'"
        ": Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def _q_emitPendingReadNotification(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_emitPendingReadNotification()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_emitPendingReadNotification' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_emitPendingReadNotification()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def _q_emitPendingWriteNotification(*__, **_) -> Never:
    """
    Qt's 'void
    QSocks5SocketEnginePrivate::_q_emitPendingWriteNotification()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_emitPendingWriteNotification' has "
        "no cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_emitPendingWriteNotification()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def _q_udpSocketReadNotification(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::_q_udpSocketReadNotification()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate._q_udpSocketReadNotification' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::_q_udpSocketReadNotification()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def emitConnectionNotification(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::emitConnectionNotification()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.emitConnectionNotification' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::emitConnectionNotification()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def emitReadNotification(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::emitReadNotification()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.emitReadNotification' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::emitReadNotification()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def emitWriteNotification(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::emitWriteNotification()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QSOCKS5_D_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.emitWriteNotification' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::emitWriteNotification()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'QSOCKS5_D_DEBUG'.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::initialize(Socks5Mode
    socks5Mode)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: incompatible pointer types
    assigning to 'QSocks5Data *' from 'QSocks5ConnectData *'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.initialize' has no cute function yet. "
        "Qt's 'void QSocks5SocketEnginePrivate::initialize(Socks5Mode "
        "socks5Mode)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: incompatible "
        "pointer types assigning to 'QSocks5Data *' from "
        "'QSocks5ConnectData *'.")

  @staticmethod
  def parseAuthenticatingReply(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::parseAuthenticatingReply()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'QSocks5Data'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.parseAuthenticatingReply' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::parseAuthenticatingReply()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QSocks5Data'.")

  @staticmethod
  def parseAuthenticationMethodReply(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::parseAuthenticationMethodReply()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QSocks5Data'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.parseAuthenticationMethodReply' has no "
        "cute function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::parseAuthenticationMethodReply()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QSocks5Data'.")

  @staticmethod
  def parseNewConnection(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::parseNewConnection()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.parseNewConnection' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::parseNewConnection()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def parseRequestMethodReply(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::parseRequestMethodReply()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QSOCKS5_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.parseRequestMethodReply' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::parseRequestMethodReply()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QSOCKS5_DEBUG'.")

  @staticmethod
  def reauthenticate(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::reauthenticate()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QSocks5Data'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.reauthenticate' has no cute function "
        "yet. Qt's 'void QSocks5SocketEnginePrivate::reauthenticate()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QSocks5Data'.")

  @staticmethod
  def sendRequestMethod(*__, **_) -> Never:
    """
    Qt's 'void QSocks5SocketEnginePrivate::sendRequestMethod()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'QSOCKS5_DEBUG'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.sendRequestMethod' has no cute "
        "function yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::sendRequestMethod()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'QSOCKS5_DEBUG'.")

  @staticmethod
  def setErrorState(*__, **_) -> Never:
    """
    - Qt's 'void QSocks5SocketEnginePrivate::setErrorState(Socks5State state,
      const QString &extraMessage)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: member access
      into incomplete type 'QSocks5Data'.
    - Qt's 'void QSocks5SocketEnginePrivate::setErrorState(Socks5State state,
      Socks5Error socks5error)': leans on
      'QSocks5SocketEngine::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.setErrorState' has no cute function "
        "yet. Qt's 'void "
        "QSocks5SocketEnginePrivate::setErrorState(Socks5State state, const "
        "QString &extraMessage)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QSocks5Data'. Qt's 'void "
        "QSocks5SocketEnginePrivate::setErrorState(Socks5State state, "
        "Socks5Error socks5error)': leans on "
        "'QSocks5SocketEngine::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def waitForConnected(*__, **_) -> Never:
    """
    Qt's 'bool QSocks5SocketEnginePrivate::waitForConnected(QDeadlineTimer
    deadline, bool *timedOut)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: member access into
    incomplete type 'QSocks5Data'.
    """
    raise NotImplementedError(
        "'QSocks5SocketEnginePrivate.waitForConnected' has no cute function "
        "yet. Qt's 'bool "
        "QSocks5SocketEnginePrivate::waitForConnected(QDeadlineTimer "
        "deadline, bool *timedOut)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QSocks5Data'.")
