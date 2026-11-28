"""
QnxServerImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_qnx_backend_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QnxServerImpl to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtNetwork import QAbstractSocket
from . import QConnectionAbstractServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QtROServerIoDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QnxServerImpl(QConnectionAbstractServer):
  """
  The cute side of Qt's QnxServerImpl: a plain Python object standing in
  front of one C++ QnxServerImpl.

  It is built on the cute 'QConnectionAbstractServer', as Qt's QnxServerImpl
  is built on Qt's QConnectionAbstractServer, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QnxServerImpl that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'hasPendingConnections',
  'configureNewConnection', 'address', 'listen', 'serverError', 'close'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QnxServerImpl::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QnxServerImpl::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QnxServerImpl::~QnxServerImpl()': the destructor: Python never
    removes a C++ QnxServerImpl.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QnxServerImpl is created at the first use, not by
    'QnxServerImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QnxServerImpl.
  - Qt tells when it has removed the C++ QnxServerImpl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QnxServerImpl::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#tr

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
    #  QString QnxServerImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QnxServerImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QnxServerImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QnxServerImpl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QnxServerImpl::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QnxServerImpl10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool QnxServerImpl::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnxserverimpl.html#hasPendingConnections
    """
    #  bool QnxServerImpl::hasPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK13QnxServerImpl21hasPendingConnectionsEv',
    )

  def address(self) -> QUrl:
    """
    Calls Qt's 'QUrl QnxServerImpl::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#address

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QnxServerImpl::address() const
    address = self.uglySide.call('ritual_ZNK13QnxServerImpl7addressEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def serverError(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError QnxServerImpl::serverError()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#serverError

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError QnxServerImpl::serverError() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK13QnxServerImpl11serverErrorEv',
    ))

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QnxServerImpl::QnxServerImpl(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#QnxServerImpl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QnxServerImpl::QnxServerImpl(QObject *parent)
    self._noteCreation(QnxServerImpl, lambda: Rituals.call(
        'ritual_ZN13QnxServerImplC1EP7QObject',
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

  def configureNewConnection(self) -> Optional[QtROServerIoDevice]:
    """
    Calls Qt's 'QtROServerIoDevice *QnxServerImpl::configureNewConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnxserverimpl.html#configureNewConnection

    Returns
    -------

    Optional[QtROServerIoDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROServerIoDevice *QnxServerImpl::configureNewConnection()
    address = self.uglySide.call(
        'ritual_ZN13QnxServerImpl22configureNewConnectionEv',
    )
    from . import QtROServerIoDevice
    return QtROServerIoDevice._cuteAt(address)

  @overload(QUrl)
  def listen(self, address: QUrl) -> bool:
    """
    Calls Qt's 'bool QnxServerImpl::listen(const QUrl &address)'.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#listen

    Parameters
    ----------

    address : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QnxServerImpl::listen(const QUrl &address)
    return self.uglySide.call(
        'ritual_ZN13QnxServerImpl6listenERK4QUrl', self._valueOf(address),
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QnxServerImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnxserverimpl.html#close
    """
    #  void QnxServerImpl::close()
    self.uglySide.call('ritual_ZN13QnxServerImpl5closeEv')
