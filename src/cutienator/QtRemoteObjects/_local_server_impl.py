"""
LocalServerImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means LocalServerImpl to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtNetwork import QAbstractSocket, QLocalServer
from . import QConnectionAbstractServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QtROServerIoDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class LocalServerImpl(QConnectionAbstractServer):
  """
  The cute side of Qt's LocalServerImpl: a plain Python object standing in
  front of one C++ LocalServerImpl.

  It is built on the cute 'QConnectionAbstractServer', as Qt's
  LocalServerImpl is built on Qt's QConnectionAbstractServer, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's LocalServerImpl that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'hasPendingConnections',
  'configureNewConnection', 'address', 'listen', 'serverError', 'close',
  'setSocketOptions'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LocalServerImpl::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int LocalServerImpl::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'LocalServerImpl::~LocalServerImpl()': the destructor: Python never
    removes a C++ LocalServerImpl.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'LocalServerImpl.

  What to expect
  --------------

  - The C++ LocalServerImpl is created at the first use, not by
    'LocalServerImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LocalServerImpl.
  - Qt tells when it has removed the C++ LocalServerImpl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's LocalServerImpl that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LocalServerImpl'

  #  A C++ LocalServerImpl Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LocalServerImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LocalServerImpl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/localserverimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LocalServerImpl::metaObject() const
    address = self.uglySide.call('ritual_ZNK15LocalServerImpl10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool LocalServerImpl::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/localserverimpl.html#hasPendingConnections
    """
    #  bool LocalServerImpl::hasPendingConnections() const
    ritual = 'ritual_ZNK15LocalServerImpl21hasPendingConnectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15LocalServerImpl21hasPendingConnectionsEv'
    return self.uglySide.call(ritual)

  def address(self) -> QUrl:
    """
    Calls Qt's 'QUrl LocalServerImpl::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/localserverimpl.html#address

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl LocalServerImpl::address() const
    ritual = 'ritual_ZNK15LocalServerImpl7addressEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15LocalServerImpl7addressEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def serverError(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError LocalServerImpl::serverError()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/localserverimpl.html#serverError

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError LocalServerImpl::serverError() const
    ritual = 'ritual_ZNK15LocalServerImpl11serverErrorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15LocalServerImpl11serverErrorEv'
    return QAbstractSocket.SocketError(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocalServer.SocketOptions)
  def setSocketOptions(self, options: QLocalServer.SocketOptions) -> None:
    """
    Calls Qt's 'void
    LocalServerImpl::setSocketOptions(QLocalServer::SocketOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/localserverimpl.html#setSocketOptions

    Parameters
    ----------

    options : QLocalServer.SocketOptions
      Passed on as its number.
    """
    #  void LocalServerImpl::setSocketOptions(QLocalServer::SocketOptions
    #      options)
    self.uglySide.call(
        'ritual_ZN15LocalServerImpl16setSocketOptionsE6QFlagsIN12QLocalServ'
        'er12SocketOptionEE',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'LocalServerImpl::LocalServerImpl(QObject *parent)': leans on
    'LocalServerImpl::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'LocalServerImpl.__init__' has no cute function yet. Qt's "
        "'LocalServerImpl::LocalServerImpl(QObject *parent)': leans on "
        "'LocalServerImpl::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def configureNewConnection(self) -> Optional[QtROServerIoDevice]:
    """
    Calls Qt's 'QtROServerIoDevice
    *LocalServerImpl::configureNewConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/localserverimpl.html#configureNewConnection

    Returns
    -------

    Optional[QtROServerIoDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROServerIoDevice *LocalServerImpl::configureNewConnection()
    address = self.uglySide.call(
        'ritual_ZN15LocalServerImpl22configureNewConnectionEv',
    )
    from . import QtROServerIoDevice
    return QtROServerIoDevice._cuteAt(address)

  @overload(QUrl)
  def listen(self, address: QUrl) -> bool:
    """
    Calls Qt's 'bool LocalServerImpl::listen(const QUrl &address)'.

    Qt's own words: https://doc.qt.io/qt-6/localserverimpl.html#listen

    Parameters
    ----------

    address : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool LocalServerImpl::listen(const QUrl &address)
    ritual = 'ritual_ZN15LocalServerImpl6listenERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15LocalServerImpl6listenERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(address))

  def close(self) -> None:
    """
    Calls Qt's 'void LocalServerImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/localserverimpl.html#close
    """
    #  void LocalServerImpl::close()
    ritual = 'ritual_ZN15LocalServerImpl5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15LocalServerImpl5closeEv'
    self.uglySide.call(ritual)
