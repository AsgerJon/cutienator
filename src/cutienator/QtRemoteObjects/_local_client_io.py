"""
LocalClientIo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means LocalClientIo to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtNetwork import QLocalSocket
from . import QtROClientIoDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject


class LocalClientIo(QtROClientIoDevice):
  """
  The cute side of Qt's LocalClientIo: a plain Python object standing in
  front of one C++ LocalClientIo.

  It is built on the cute 'QtROClientIoDevice', as Qt's LocalClientIo is
  built on Qt's QtROClientIoDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's LocalClientIo that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'connection', 'connectToServer',
  'isOpen', 'onError', 'onStateChanged', 'doClose', 'doDisconnectFromServer'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LocalClientIo::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int LocalClientIo::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'LocalClientIo::~LocalClientIo()': the destructor: Python never
    removes a C++ LocalClientIo.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 leans on 'LocalClientIo.

  What to expect
  --------------

  - The C++ LocalClientIo is created at the first use, not by
    'LocalClientIo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LocalClientIo.
  - Qt tells when it has removed the C++ LocalClientIo. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's LocalClientIo that has no cute function yet,
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
  __qt_class__ = 'LocalClientIo'

  #  A C++ LocalClientIo Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LocalClientIo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LocalClientIo::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LocalClientIo::metaObject() const
    address = self.uglySide.call('ritual_ZNK13LocalClientIo10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def connection(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *LocalClientIo::connection() const'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#connection

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *LocalClientIo::connection() const
    ritual = 'ritual_ZNK13LocalClientIo10connectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13LocalClientIo10connectionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool LocalClientIo::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#isOpen
    """
    #  bool LocalClientIo::isOpen() const
    ritual = 'ritual_ZNK13LocalClientIo6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13LocalClientIo6isOpenEv'
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'LocalClientIo::LocalClientIo(QObject *parent)': leans on
    'LocalClientIo::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'LocalClientIo.__init__' has no cute function yet. Qt's "
        "'LocalClientIo::LocalClientIo(QObject *parent)': leans on "
        "'LocalClientIo::qt_metacall(QMetaObject::Call, int, void**)', "
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

  def connectToServer(self) -> None:
    """
    Calls Qt's 'void LocalClientIo::connectToServer()'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#connectToServer
    """
    #  void LocalClientIo::connectToServer()
    ritual = 'ritual_ZN13LocalClientIo15connectToServerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13LocalClientIo15connectToServerEv'
    self.uglySide.call(ritual)

  @overload(QLocalSocket.LocalSocketError)
  def onError(self, error: QLocalSocket.LocalSocketError) -> None:
    """
    Calls Qt's 'void LocalClientIo::onError(QLocalSocket::LocalSocketError
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#onError

    Parameters
    ----------

    error : QLocalSocket.LocalSocketError
      Passed on as its number.
    """
    #  void LocalClientIo::onError(QLocalSocket::LocalSocketError error)
    self.uglySide.call(
        'ritual_ZN13LocalClientIo7onErrorEN12QLocalSocket16LocalSocketError'
        'E',
        error.value,
    )

  @overload(QLocalSocket.LocalSocketState)
  def onStateChanged(self, state: QLocalSocket.LocalSocketState) -> None:
    """
    Calls Qt's 'void
    LocalClientIo::onStateChanged(QLocalSocket::LocalSocketState state)'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#onStateChanged

    Parameters
    ----------

    state : QLocalSocket.LocalSocketState
      Passed on as its number.
    """
    #  void LocalClientIo::onStateChanged(QLocalSocket::LocalSocketState
    #      state)
    self.uglySide.call(
        'ritual_ZN13LocalClientIo14onStateChangedEN12QLocalSocket16LocalSoc'
        'ketStateE',
        state.value,
    )

  def doClose(self) -> None:
    """
    Calls Qt's 'void LocalClientIo::doClose()'.

    Qt's own words: https://doc.qt.io/qt-6/localclientio.html#doClose
    """
    #  void LocalClientIo::doClose()
    ritual = 'ritual_ZN13LocalClientIo7doCloseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13LocalClientIo7doCloseEv'
    self.uglySide.call(ritual)

  def doDisconnectFromServer(self) -> None:
    """
    Calls Qt's 'void LocalClientIo::doDisconnectFromServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/localclientio.html#doDisconnectFromServer
    """
    #  void LocalClientIo::doDisconnectFromServer()
    ritual = 'ritual_ZN13LocalClientIo22doDisconnectFromServerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13LocalClientIo22doDisconnectFromServerEv'
    self.uglySide.call(ritual)
