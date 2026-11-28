"""
QSctpServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsctpserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QTcpServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QSctpServerPrivate, QSctpSocket

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSctpServer(QTcpServer):
  """
  The cute side of Qt's QSctpServer: a plain Python object standing in front
  of one C++ QSctpServer.

  It is built on the cute 'QTcpServer', as Qt's QSctpServer is built on Qt's
  QTcpServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSctpServer that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'setMaximumChannelCount',
  'maximumChannelCount', 'nextPendingDatagramConnection',
  'incomingConnection', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSctpServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSctpServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSctpServer::~QSctpServer()': the destructor: Python never removes
    a C++ QSctpServer.
  - Qt's 'const QSctpServerPrivate *QSctpServer::d_func() const': takes in
    Python what 'QSctpServerPrivate *QSctpServer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSctpServer is created at the first use, not by
    'QSctpServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSctpServer.
  - Qt tells when it has removed the C++ QSctpServer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QSctpServer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpserver.html#tr

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
    #  QString QSctpServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QSctpServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSctpServer'

  #  A C++ QSctpServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSctpServer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSctpServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSctpServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QSctpServer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def maximumChannelCount(self) -> int:
    """
    Calls Qt's 'int QSctpServer::maximumChannelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpserver.html#maximumChannelCount
    """
    #  int QSctpServer::maximumChannelCount() const
    return self.uglySide.call(
        'ritual_ZNK11QSctpServer19maximumChannelCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaximumChannelCount(self, count: int) -> None:
    """
    Calls Qt's 'void QSctpServer::setMaximumChannelCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpserver.html#setMaximumChannelCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSctpServer::setMaximumChannelCount(int count)
    self.uglySide.call(
        'ritual_ZN11QSctpServer22setMaximumChannelCountEi', count,
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
    Notes what was given, for Qt's 'QSctpServer::QSctpServer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsctpserver.html#QSctpServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSctpServer::QSctpServer(QObject *parent)
    self._noteCreation(QSctpServer, lambda: Rituals.call(
        'ritual_ZN11QSctpServerC1EP7QObject',
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

  def nextPendingDatagramConnection(self) -> Optional[QSctpSocket]:
    """
    Calls Qt's 'QSctpSocket *QSctpServer::nextPendingDatagramConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpserver.html#nextPendingDatagramConnection

    Returns
    -------

    Optional[QSctpSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSctpSocket *QSctpServer::nextPendingDatagramConnection()
    address = self.uglySide.call(
        'ritual_ZN11QSctpServer29nextPendingDatagramConnectionEv',
    )
    from . import QSctpSocket
    return QSctpSocket._cuteAt(address)

  @overload(int)
  def incomingConnection(self, handle: int) -> None:
    """
    Calls Qt's 'void QSctpServer::incomingConnection(qintptr handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpserver.html#incomingConnection

    Parameters
    ----------

    handle : int
      Passed on as it is.
    """
    #  void QSctpServer::incomingConnection(qintptr handle)
    ritual = 'ritual_ZN11QSctpServer18incomingConnectionEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSctpServer18incomingConnectionEx'
    self.uglySide.call(ritual, handle)

  def d_func(self) -> Optional[QSctpServerPrivate]:
    """
    Calls Qt's 'QSctpServerPrivate *QSctpServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpserver.html#d_func

    Returns
    -------

    Optional[QSctpServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSctpServerPrivate *QSctpServer::d_func()
    address = self.uglySide.call('ritual_ZN11QSctpServer6d_funcEv')
    from . import QSctpServerPrivate
    return QSctpServerPrivate._cuteAt(address)
