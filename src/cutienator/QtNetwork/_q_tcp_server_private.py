"""
QTcpServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtcpserver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTcpServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QAbstractSocketEngineReceiver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAuthenticator, QHostAddress, QNetworkProxy, QTcpServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QHostAddress = WAIT['QHostAddress']
  QNetworkProxy = WAIT['QNetworkProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTcpServerPrivate(QObjectPrivate, QAbstractSocketEngineReceiver):
  """
  The cute side of Qt's QTcpServerPrivate: a plain Python object standing in
  front of one C++ QTcpServerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QTcpServerPrivate is
  built on Qt's QObjectPrivate, and has everything that class has. It is
  built on the cute 'QAbstractSocketEngineReceiver' as well, as Qt's
  QTcpServerPrivate is built on Qt's QAbstractSocketEngineReceiver too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QTcpServerPrivate that has a ritual and that Python
  can call so far, 10 names in all: 'q_func', 'resolveProxy',
  'configureCreatedSocket', 'totalPendingConnections', 'readNotification',
  'closeNotification', 'writeNotification', 'exceptionNotification',
  'connectionNotification', 'proxyAuthenticationRequired'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTcpServer *QTcpServerPrivate::q_func() const': takes in
    Python what 'QTcpServer *QTcpServerPrivate::q_func()' takes.
  - Qt's 'QTcpServerPrivate::~QTcpServerPrivate()': the destructor: Python
    never removes a C++ QTcpServerPrivate.

  What to expect
  --------------

  - The C++ QTcpServerPrivate is created at the first use, not by
    'QTcpServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTcpServerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTcpServerPrivate'

  #  Qt's QTcpServerPrivate is built on more than one class. The part of a
  #  C++ QTcpServerPrivate that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractSocketEngineReceiver':
          'ritual_cast_QTcpServerPrivate_QAbstractSocketEngineReceiver',
  }

  #  A C++ QTcpServerPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTcpServerPrivate'

  #  The functions Qt calls itself that QTcpServerPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'configureCreatedSocket': (
          ('_ZN17QTcpServerPrivate22configureCreatedSocketEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'totalPendingConnections': (
          ('_ZNK17QTcpServerPrivate23totalPendingConnectionsEv',
           ('int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def totalPendingConnections(self) -> int:
    """
    Calls Qt's 'int QTcpServerPrivate::totalPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#totalPendingConnections
    """
    #  int QTcpServerPrivate::totalPendingConnections() const
    ritual = 'ritual_ZNK17QTcpServerPrivate23totalPendingConnectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QTcpServerPrivate23totalPendingConnectionsEv'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTcpServerPrivate::QTcpServerPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#QTcpServerPrivate
    """
    #  QTcpServerPrivate::QTcpServerPrivate()
    self._noteCreation(QTcpServerPrivate, lambda: Rituals.call(
        'ritual_ZN17QTcpServerPrivateC1Ev',
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

  def q_func(self) -> Optional[QTcpServer]:
    """
    Calls Qt's 'QTcpServer *QTcpServerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtcpserverprivate.html#q_func

    Returns
    -------

    Optional[QTcpServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTcpServer *QTcpServerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QTcpServerPrivate6q_funcEv')
    from . import QTcpServer
    return QTcpServer._cuteAt(address)

  @overload(QHostAddress, int)
  def resolveProxy(self, address: QHostAddress, port: int) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QTcpServerPrivate::resolveProxy(const
    QHostAddress &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#resolveProxy

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QTcpServerPrivate::resolveProxy(const QHostAddress
    #      &address, quint16 port)
    address = self.uglySide.call(
        'ritual_ZN17QTcpServerPrivate12resolveProxyERK12QHostAddresst',
        self._valueOf(address), port,
    )
    from . import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def configureCreatedSocket(self) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::configureCreatedSocket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#configureCreatedSocket
    """
    #  void QTcpServerPrivate::configureCreatedSocket()
    ritual = 'ritual_ZN17QTcpServerPrivate22configureCreatedSocketEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTcpServerPrivate22configureCreatedSocketEv'
    self.uglySide.call(ritual)

  def readNotification(self) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::readNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#readNotification
    """
    #  void QTcpServerPrivate::readNotification()
    ritual = 'ritual_ZN17QTcpServerPrivate16readNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTcpServerPrivate16readNotificationEv'
    self.uglySide.call(ritual)

  def closeNotification(self) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::closeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#closeNotification
    """
    #  void QTcpServerPrivate::closeNotification()
    ritual = 'ritual_ZN17QTcpServerPrivate17closeNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTcpServerPrivate17closeNotificationEv'
    self.uglySide.call(ritual)

  def writeNotification(self) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::writeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#writeNotification
    """
    #  void QTcpServerPrivate::writeNotification()
    ritual = 'ritual_ZN17QTcpServerPrivate17writeNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTcpServerPrivate17writeNotificationEv'
    self.uglySide.call(ritual)

  def exceptionNotification(self) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::exceptionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#exceptionNotification
    """
    #  void QTcpServerPrivate::exceptionNotification()
    ritual = 'ritual_ZN17QTcpServerPrivate21exceptionNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTcpServerPrivate21exceptionNotificationEv'
    self.uglySide.call(ritual)

  def connectionNotification(self) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::connectionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#connectionNotification
    """
    #  void QTcpServerPrivate::connectionNotification()
    ritual = 'ritual_ZN17QTcpServerPrivate22connectionNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QTcpServerPrivate22connectionNotificationEv'
    self.uglySide.call(ritual)

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      a0: QNetworkProxy,
      a1: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QTcpServerPrivate::proxyAuthenticationRequired(const
    QNetworkProxy &a0, QAuthenticator *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpserverprivate.html#proxyAuthenticationRequired

    Parameters
    ----------

    a0 : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    a1 : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTcpServerPrivate::proxyAuthenticationRequired(const
    #      QNetworkProxy &a0, QAuthenticator *a1)
    ritual = (
        'ritual_ZN17QTcpServerPrivate27proxyAuthenticationRequiredERK13QNet'
        'workProxyP14QAuthenticator')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QTcpServerPrivate27proxyAuthenticationRequiredERK'
          '13QNetworkProxyP14QAuthenticator')
    self.uglySide.call(ritual, self._valueOf(a0), self._addressOf(a1))
