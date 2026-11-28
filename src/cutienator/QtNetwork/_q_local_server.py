"""
QLocalServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qlocalserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QLocalServerPrivate, QLocalSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocalSocket = WAIT['QLocalSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLocalServer(QObject):
  """
  The cute side of Qt's QLocalServer: a plain Python object standing in front
  of one C++ QLocalServer.

  It is built on the cute 'QObject', as Qt's QLocalServer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLocalServer that has a ritual and that Python can
  call so far, 23 names in all: 'metaObject', 'tr', 'd_func',
  'newConnection', 'close', 'errorString', 'hasPendingConnections',
  'isListening', 'listen', 'maxPendingConnections', 'nextPendingConnection',
  'serverName', 'fullServerName', 'removeServer', 'serverError',
  'setMaxPendingConnections', 'setListenBacklogSize', 'listenBacklogSize',
  'setSocketOptions', 'socketOptions', 'socketDescriptor',
  'incomingConnection', 'addPendingConnection'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLocalServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLocalServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QLocalServerPrivate *QLocalServer::d_func() const': takes in
    Python what 'QLocalServerPrivate *QLocalServer::d_func()' takes.
  - Qt's 'QLocalServer::~QLocalServer()': the destructor: Python never
    removes a C++ QLocalServer.
  - Qt's 'bool QLocalServer::waitForNewConnection(int msec, bool *timedOut)':
    takes a number to change where it is.
  - Qt's 'QBindable<SocketOptions> QLocalServer::bindableSocketOptions()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLocalServer is created at the first use, not by
    'QLocalServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLocalServer.
  - Qt tells when it has removed the C++ QLocalServer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QLocalServer that has no cute function yet,
    'bindableSocketOptions', 'waitForNewConnection', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLocalServer, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SocketOption(CuteFlags):
    """
    The flags enum 'QLocalServer::SocketOption' of Qt, with the 6 names Qt
    gives in it. Qt names the type of its combinations
    'QLocalServer::SocketOptions'.
    """

    NoOptions = 0x0
    UserAccessOption = 0x1
    GroupAccessOption = 0x2
    OtherAccessOption = 0x4
    WorldAccessOption = 0x7
    AbstractNamespaceOption = 0x8

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
    Calls Qt's 'QString QLocalServer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#tr

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
    #  QString QLocalServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QLocalServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def removeServer(name: str) -> bool:
    """
    Calls Qt's 'bool QLocalServer::removeServer(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#removeServer

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QLocalServer::removeServer(const QString &name)
    return Rituals.call(
        'ritual_ZN12QLocalServer12removeServerERK7QString', name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocalServer'

  #  A C++ QLocalServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLocalServer'

  #  The functions Qt calls itself that QLocalServer is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'hasPendingConnections': (
          ('_ZNK12QLocalServer21hasPendingConnectionsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'nextPendingConnection': (
          ('_ZN12QLocalServer21nextPendingConnectionEv',
           ('address', 'address', 'QtNetwork:QLocalSocket'),
           ()),
      ),
      'incomingConnection': (
          ('_ZN12QLocalServer18incomingConnectionEy',
           ('nothing', 'nothing', ''),
           (
               ('unsigned long long', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QLocalServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLocalServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QLocalServer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QLocalServer::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocalServer::errorString() const
    return self.uglySide.call('ritual_ZNK12QLocalServer11errorStringEv')

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool QLocalServer::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#hasPendingConnections
    """
    #  bool QLocalServer::hasPendingConnections() const
    ritual = 'ritual_ZNK12QLocalServer21hasPendingConnectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLocalServer21hasPendingConnectionsEv'
    return self.uglySide.call(ritual)

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QLocalServer::isListening() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#isListening
    """
    #  bool QLocalServer::isListening() const
    return self.uglySide.call('ritual_ZNK12QLocalServer11isListeningEv')

  def maxPendingConnections(self) -> int:
    """
    Calls Qt's 'int QLocalServer::maxPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#maxPendingConnections
    """
    #  int QLocalServer::maxPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK12QLocalServer21maxPendingConnectionsEv',
    )

  def serverName(self) -> str:
    """
    Calls Qt's 'QString QLocalServer::serverName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#serverName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocalServer::serverName() const
    return self.uglySide.call('ritual_ZNK12QLocalServer10serverNameEv')

  def fullServerName(self) -> str:
    """
    Calls Qt's 'QString QLocalServer::fullServerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#fullServerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLocalServer::fullServerName() const
    return self.uglySide.call('ritual_ZNK12QLocalServer14fullServerNameEv')

  def serverError(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError QLocalServer::serverError()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#serverError

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError QLocalServer::serverError() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK12QLocalServer11serverErrorEv',
    ))

  def listenBacklogSize(self) -> int:
    """
    Calls Qt's 'int QLocalServer::listenBacklogSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#listenBacklogSize
    """
    #  int QLocalServer::listenBacklogSize() const
    return self.uglySide.call(
        'ritual_ZNK12QLocalServer17listenBacklogSizeEv',
    )

  def socketOptions(self) -> SocketOptions:
    """
    Calls Qt's 'SocketOptions QLocalServer::socketOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#socketOptions

    Returns
    -------

    SocketOptions
      The value standing for the combination Qt gave back.
    """
    #  SocketOptions QLocalServer::socketOptions() const
    return QLocalServer.SocketOptions(self.uglySide.call(
        'ritual_ZNK12QLocalServer13socketOptionsEv',
    ))

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QLocalServer::socketDescriptor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#socketDescriptor
    """
    #  qintptr QLocalServer::socketDescriptor() const
    return self.uglySide.call('ritual_ZNK12QLocalServer16socketDescriptorEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxPendingConnections(self, numConnections: int) -> None:
    """
    Calls Qt's 'void QLocalServer::setMaxPendingConnections(int
    numConnections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#setMaxPendingConnections

    Parameters
    ----------

    numConnections : int
      Passed on as it is.
    """
    #  void QLocalServer::setMaxPendingConnections(int numConnections)
    self.uglySide.call(
        'ritual_ZN12QLocalServer24setMaxPendingConnectionsEi',
        numConnections,
    )

  @overload(int)
  def setListenBacklogSize(self, size: int) -> None:
    """
    Calls Qt's 'void QLocalServer::setListenBacklogSize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#setListenBacklogSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QLocalServer::setListenBacklogSize(int size)
    self.uglySide.call(
        'ritual_ZN12QLocalServer20setListenBacklogSizeEi', size,
    )

  @overload(SocketOptions)
  def setSocketOptions(self, options: SocketOptions) -> None:
    """
    Calls Qt's 'void QLocalServer::setSocketOptions(SocketOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#setSocketOptions

    Parameters
    ----------

    options : SocketOptions
      Passed on as its number.
    """
    #  void QLocalServer::setSocketOptions(SocketOptions options)
    self.uglySide.call(
        'ritual_ZN12QLocalServer16setSocketOptionsE6QFlagsINS_12SocketOptio'
        'nEE',
        options.value,
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
    Notes what was given, for Qt's 'QLocalServer::QLocalServer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#QLocalServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLocalServer::QLocalServer(QObject *parent)
    self._noteCreation(QLocalServer, lambda: Rituals.call(
        'ritual_ZN12QLocalServerC1EP7QObject',
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

  def d_func(self) -> Optional[QLocalServerPrivate]:
    """
    Calls Qt's 'QLocalServerPrivate *QLocalServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#d_func

    Returns
    -------

    Optional[QLocalServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLocalServerPrivate *QLocalServer::d_func()
    address = self.uglySide.call('ritual_ZN12QLocalServer6d_funcEv')
    from . import QLocalServerPrivate
    return QLocalServerPrivate._cuteAt(address)

  def newConnection(self) -> None:
    """
    Calls Qt's 'void QLocalServer::newConnection()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#newConnection
    """
    #  void QLocalServer::newConnection()
    self.uglySide.call('ritual_ZN12QLocalServer13newConnectionEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QLocalServer::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#close
    """
    #  void QLocalServer::close()
    self.uglySide.call('ritual_ZN12QLocalServer5closeEv')

  @overload(str)
  def listen(self, name: str) -> bool:
    """
    Calls Qt's 'bool QLocalServer::listen(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#listen

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QLocalServer::listen(const QString &name)
    return self.uglySide.call(
        'ritual_ZN12QLocalServer6listenERK7QString', name,
    )

  @overload(int)
  def listen(self, socketDescriptor: int) -> bool:
    """
    Calls Qt's 'bool QLocalServer::listen(qintptr socketDescriptor)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalserver.html#listen

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.
    """
    #  bool QLocalServer::listen(qintptr socketDescriptor)
    return self.uglySide.call(
        'ritual_ZN12QLocalServer6listenEx', socketDescriptor,
    )

  def nextPendingConnection(self) -> Optional[QLocalSocket]:
    """
    Calls Qt's 'QLocalSocket *QLocalServer::nextPendingConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#nextPendingConnection

    Returns
    -------

    Optional[QLocalSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLocalSocket *QLocalServer::nextPendingConnection()
    ritual = 'ritual_ZN12QLocalServer21nextPendingConnectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLocalServer21nextPendingConnectionEv'
    address = self.uglySide.call(ritual)
    from . import QLocalSocket
    return QLocalSocket._cuteAt(address)

  @overload(int)
  def incomingConnection(self, socketDescriptor: int) -> None:
    """
    Calls Qt's 'void QLocalServer::incomingConnection(quintptr
    socketDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#incomingConnection

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.
    """
    #  void QLocalServer::incomingConnection(quintptr socketDescriptor)
    ritual = 'ritual_ZN12QLocalServer18incomingConnectionEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLocalServer18incomingConnectionEy'
    self.uglySide.call(ritual, socketDescriptor)

  @overload(QLocalSocket)
  @overload(NoneType)
  def addPendingConnection(self, socket: Optional[QLocalSocket]) -> None:
    """
    Calls Qt's 'void QLocalServer::addPendingConnection(QLocalSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalserver.html#addPendingConnection

    Parameters
    ----------

    socket : Optional[QLocalSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLocalServer::addPendingConnection(QLocalSocket *socket)
    self.uglySide.call(
        'ritual_ZN12QLocalServer20addPendingConnectionEP12QLocalSocket',
        self._addressOf(socket),
    )

  @staticmethod
  def bindableSocketOptions(*__, **_) -> Never:
    """
    Qt's 'QBindable<SocketOptions> QLocalServer::bindableSocketOptions()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLocalServer.bindableSocketOptions' has no cute function yet. "
        "Qt's 'QBindable<SocketOptions> "
        "QLocalServer::bindableSocketOptions()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def waitForNewConnection(*__, **_) -> Never:
    """
    Qt's 'bool QLocalServer::waitForNewConnection(int msec, bool *timedOut)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QLocalServer.waitForNewConnection' has no cute function yet. Qt's "
        "'bool QLocalServer::waitForNewConnection(int msec, bool "
        "*timedOut)': takes a number to change where it is.")


#  Qt's 'QList<QLocalServer *>': the list of QLocalServer, which
#  'QList[QLocalServer]' gives. It is made here, so that there is one as soon
#  as there can be a QLocalServer.
QList.createKind(
    QLocalServer, 'address',
    make='ritual_list_make_QLocalServer_ptr',
    add='ritual_list_add_QLocalServer_ptr',
    size='ritual_list_size_QLocalServer_ptr',
    at='ritual_list_at_QLocalServer_ptr',
    drop='ritual_list_drop_QLocalServer_ptr',
)
