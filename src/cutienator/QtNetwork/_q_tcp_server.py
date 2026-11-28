"""
QTcpServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qtcpserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHostAddress, QNetworkProxy, QTcpServerPrivate, QTcpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QNetworkProxy = WAIT['QNetworkProxy']
  QTcpSocket = WAIT['QTcpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTcpServer(QObject):
  """
  The cute side of Qt's QTcpServer: a plain Python object standing in front
  of one C++ QTcpServer.

  It is built on the cute 'QObject', as Qt's QTcpServer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTcpServer that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'listen', 'close',
  'isListening', 'setMaxPendingConnections', 'maxPendingConnections',
  'setListenBacklogSize', 'listenBacklogSize', 'serverPort', 'serverAddress',
  'socketDescriptor', 'setSocketDescriptor', 'hasPendingConnections',
  'nextPendingConnection', 'serverError', 'errorString', 'pauseAccepting',
  'resumeAccepting', 'setProxy', 'proxy', 'incomingConnection',
  'addPendingConnection', 'newConnection', 'pendingConnectionAvailable',
  'acceptError', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTcpServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTcpServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTcpServer::~QTcpServer()': the destructor: Python never removes a
    C++ QTcpServer.
  - Qt's 'bool QTcpServer::waitForNewConnection(int msec, bool *timedOut)':
    takes a number to change where it is.
  - Qt's 'QTcpServer::QTcpServer(QAbstractSocket::SocketType socketType,
    QTcpServerPrivate &dd, QObject *parent)': takes a type Python has no way
    to hand over yet.
  - Qt's 'const QTcpServerPrivate *QTcpServer::d_func() const': takes in
    Python what 'QTcpServerPrivate *QTcpServer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QTcpServer is created at the first use, not by 'QTcpServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTcpServer.
  - Qt tells when it has removed the C++ QTcpServer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QTcpServer that has no cute function yet,
    'waitForNewConnection', holds a function that raises
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
    Calls Qt's 'QString QTcpServer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#tr

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
    #  QString QTcpServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QTcpServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTcpServer'

  #  A C++ QTcpServer Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTcpServer'

  #  The functions Qt calls itself that QTcpServer is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'hasPendingConnections': (
          ('_ZNK10QTcpServer21hasPendingConnectionsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'nextPendingConnection': (
          ('_ZN10QTcpServer21nextPendingConnectionEv',
           ('address', 'address', 'QtNetwork:QTcpSocket'),
           ()),
      ),
      'incomingConnection': (
          ('_ZN10QTcpServer18incomingConnectionEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QTcpServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTcpServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTcpServer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QTcpServer::isListening() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#isListening
    """
    #  bool QTcpServer::isListening() const
    return self.uglySide.call('ritual_ZNK10QTcpServer11isListeningEv')

  def maxPendingConnections(self) -> int:
    """
    Calls Qt's 'int QTcpServer::maxPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#maxPendingConnections
    """
    #  int QTcpServer::maxPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK10QTcpServer21maxPendingConnectionsEv',
    )

  def listenBacklogSize(self) -> int:
    """
    Calls Qt's 'int QTcpServer::listenBacklogSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#listenBacklogSize
    """
    #  int QTcpServer::listenBacklogSize() const
    return self.uglySide.call('ritual_ZNK10QTcpServer17listenBacklogSizeEv')

  def serverPort(self) -> int:
    """
    Calls Qt's 'quint16 QTcpServer::serverPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#serverPort
    """
    #  quint16 QTcpServer::serverPort() const
    return self.uglySide.call('ritual_ZNK10QTcpServer10serverPortEv')

  def serverAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QTcpServer::serverAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#serverAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QTcpServer::serverAddress() const
    address = self.uglySide.call('ritual_ZNK10QTcpServer13serverAddressEv')
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QTcpServer::socketDescriptor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#socketDescriptor
    """
    #  qintptr QTcpServer::socketDescriptor() const
    return self.uglySide.call('ritual_ZNK10QTcpServer16socketDescriptorEv')

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool QTcpServer::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#hasPendingConnections
    """
    #  bool QTcpServer::hasPendingConnections() const
    ritual = 'ritual_ZNK10QTcpServer21hasPendingConnectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTcpServer21hasPendingConnectionsEv'
    return self.uglySide.call(ritual)

  def serverError(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError QTcpServer::serverError()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#serverError

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError QTcpServer::serverError() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK10QTcpServer11serverErrorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QTcpServer::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTcpServer::errorString() const
    return self.uglySide.call('ritual_ZNK10QTcpServer11errorStringEv')

  def proxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QTcpServer::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#proxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QTcpServer::proxy() const
    address = self.uglySide.call('ritual_ZNK10QTcpServer5proxyEv')
    from . import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxPendingConnections(self, numConnections: int) -> None:
    """
    Calls Qt's 'void QTcpServer::setMaxPendingConnections(int
    numConnections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#setMaxPendingConnections

    Parameters
    ----------

    numConnections : int
      Passed on as it is.
    """
    #  void QTcpServer::setMaxPendingConnections(int numConnections)
    self.uglySide.call(
        'ritual_ZN10QTcpServer24setMaxPendingConnectionsEi', numConnections,
    )

  @overload(int)
  def setListenBacklogSize(self, size: int) -> None:
    """
    Calls Qt's 'void QTcpServer::setListenBacklogSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#setListenBacklogSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QTcpServer::setListenBacklogSize(int size)
    self.uglySide.call('ritual_ZN10QTcpServer20setListenBacklogSizeEi', size)

  @overload(int)
  def setSocketDescriptor(self, socketDescriptor: int) -> bool:
    """
    Calls Qt's 'bool QTcpServer::setSocketDescriptor(qintptr
    socketDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.
    """
    #  bool QTcpServer::setSocketDescriptor(qintptr socketDescriptor)
    return self.uglySide.call(
        'ritual_ZN10QTcpServer19setSocketDescriptorEx', socketDescriptor,
    )

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QTcpServer::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QTcpServer::setProxy(const QNetworkProxy &networkProxy)
    self.uglySide.call(
        'ritual_ZN10QTcpServer8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
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
    Notes what was given, for Qt's 'QTcpServer::QTcpServer(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#QTcpServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTcpServer::QTcpServer(QObject *parent)
    self._noteCreation(QTcpServer, lambda: Rituals.call(
        'ritual_ZN10QTcpServerC1EP7QObject',
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

  @overload(QHostAddress)
  @overload(QHostAddress, int)
  def listen(self, address: QHostAddress, port: int = 0) -> bool:
    """
    Calls Qt's 'bool QTcpServer::listen(const QHostAddress &address, quint16
    port)'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#listen

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QTcpServer::listen(const QHostAddress &address, quint16 port)
    return self.uglySide.call(
        'ritual_ZN10QTcpServer6listenERK12QHostAddresst',
        self._valueOf(address), port,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QTcpServer::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#close
    """
    #  void QTcpServer::close()
    self.uglySide.call('ritual_ZN10QTcpServer5closeEv')

  def nextPendingConnection(self) -> Optional[QTcpSocket]:
    """
    Calls Qt's 'QTcpSocket *QTcpServer::nextPendingConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#nextPendingConnection

    Returns
    -------

    Optional[QTcpSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTcpSocket *QTcpServer::nextPendingConnection()
    ritual = 'ritual_ZN10QTcpServer21nextPendingConnectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTcpServer21nextPendingConnectionEv'
    address = self.uglySide.call(ritual)
    from . import QTcpSocket
    return QTcpSocket._cuteAt(address)

  def pauseAccepting(self) -> None:
    """
    Calls Qt's 'void QTcpServer::pauseAccepting()'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#pauseAccepting
    """
    #  void QTcpServer::pauseAccepting()
    self.uglySide.call('ritual_ZN10QTcpServer14pauseAcceptingEv')

  def resumeAccepting(self) -> None:
    """
    Calls Qt's 'void QTcpServer::resumeAccepting()'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#resumeAccepting
    """
    #  void QTcpServer::resumeAccepting()
    self.uglySide.call('ritual_ZN10QTcpServer15resumeAcceptingEv')

  @overload(int)
  def incomingConnection(self, handle: int) -> None:
    """
    Calls Qt's 'void QTcpServer::incomingConnection(qintptr handle)'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#incomingConnection

    Parameters
    ----------

    handle : int
      Passed on as it is.
    """
    #  void QTcpServer::incomingConnection(qintptr handle)
    ritual = 'ritual_ZN10QTcpServer18incomingConnectionEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTcpServer18incomingConnectionEx'
    self.uglySide.call(ritual, handle)

  @overload(QTcpSocket)
  @overload(NoneType)
  def addPendingConnection(self, socket: Optional[QTcpSocket]) -> None:
    """
    Calls Qt's 'void QTcpServer::addPendingConnection(QTcpSocket *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#addPendingConnection

    Parameters
    ----------

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTcpServer::addPendingConnection(QTcpSocket *socket)
    self.uglySide.call(
        'ritual_ZN10QTcpServer20addPendingConnectionEP10QTcpSocket',
        self._addressOf(socket),
    )

  def newConnection(self) -> None:
    """
    Calls Qt's 'void QTcpServer::newConnection()'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#newConnection
    """
    #  void QTcpServer::newConnection()
    self.uglySide.call('ritual_ZN10QTcpServer13newConnectionEv')

  def pendingConnectionAvailable(self) -> None:
    """
    Calls Qt's 'void QTcpServer::pendingConnectionAvailable(QPrivateSignal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserver.html#pendingConnectionAvailable
    """
    #  void QTcpServer::pendingConnectionAvailable(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN10QTcpServer26pendingConnectionAvailableENS_14QPrivateSig'
        'nalE',
    )

  @overload(QAbstractSocket.SocketError)
  def acceptError(self, socketError: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void QTcpServer::acceptError(QAbstractSocket::SocketError
    socketError)'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#acceptError

    Parameters
    ----------

    socketError : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QTcpServer::acceptError(QAbstractSocket::SocketError socketError)
    self.uglySide.call(
        'ritual_ZN10QTcpServer11acceptErrorEN15QAbstractSocket11SocketError'
        'E',
        socketError.value,
    )

  def d_func(self) -> Optional[QTcpServerPrivate]:
    """
    Calls Qt's 'QTcpServerPrivate *QTcpServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserver.html#d_func

    Returns
    -------

    Optional[QTcpServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTcpServerPrivate *QTcpServer::d_func()
    address = self.uglySide.call('ritual_ZN10QTcpServer6d_funcEv')
    from . import QTcpServerPrivate
    return QTcpServerPrivate._cuteAt(address)

  @staticmethod
  def waitForNewConnection(*__, **_) -> Never:
    """
    Qt's 'bool QTcpServer::waitForNewConnection(int msec, bool *timedOut)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QTcpServer.waitForNewConnection' has no cute function yet. Qt's "
        "'bool QTcpServer::waitForNewConnection(int msec, bool *timedOut)': "
        "takes a number to change where it is.")


#  Qt's 'QList<QTcpServer *>': the list of QTcpServer, which
#  'QList[QTcpServer]' gives. It is made here, so that there is one as soon
#  as there can be a QTcpServer.
QList.createKind(
    QTcpServer, 'address',
    make='ritual_list_make_QTcpServer_ptr',
    add='ritual_list_add_QTcpServer_ptr',
    size='ritual_list_size_QTcpServer_ptr',
    at='ritual_list_at_QTcpServer_ptr',
    drop='ritual_list_drop_QTcpServer_ptr',
)
