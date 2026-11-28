"""
QModbusTcpServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbustcpserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QModbusServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtNetwork import QTcpSocket
  from . import QModbusTcpConnectionObserver, QModbusTcpServerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusTcpConnectionObserver = WAIT['QModbusTcpConnectionObserver']
  QTcpSocket = WAIT['QTcpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusTcpServer(QModbusServer):
  """
  The cute side of Qt's QModbusTcpServer: a plain Python object standing in
  front of one C++ QModbusTcpServer.

  It is built on the cute 'QModbusServer', as Qt's QModbusTcpServer is built
  on Qt's QModbusServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusTcpServer that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'd_func',
  'installConnectionObserver', 'modbusClientDisconnected', 'open', 'close'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModbusTcpServer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QModbusTcpServer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QModbusTcpServerPrivate *QModbusTcpServer::d_func() const':
    takes in Python what 'QModbusTcpServerPrivate
    *QModbusTcpServer::d_func()' takes.
  - Qt's 'QModbusTcpServer::~QModbusTcpServer()': the destructor: Python
    never removes a C++ QModbusTcpServer.
  - Qt's 'QModbusTcpServer::QModbusTcpServer(QModbusTcpServerPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QModbusResponse QModbusTcpServer::processRequest(const QModbusPdu
    &request)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QModbusTcpServer is created at the first use, not by
    'QModbusTcpServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusTcpServer.
  - Qt tells when it has removed the C++ QModbusTcpServer. Every call on the
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
    Calls Qt's 'QString QModbusTcpServer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbustcpserver.html#tr

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
    #  QString QModbusTcpServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QModbusTcpServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusTcpServer'

  #  A C++ QModbusTcpServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusTcpServer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QModbusTcpServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbustcpserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QModbusTcpServer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QModbusTcpServer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QModbusTcpServer::QModbusTcpServer(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserver.html#QModbusTcpServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QModbusTcpServer::QModbusTcpServer(QObject *parent)
    self._noteCreation(QModbusTcpServer, lambda: Rituals.call(
        'ritual_ZN16QModbusTcpServerC1EP7QObject',
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

  def d_func(self) -> Optional[QModbusTcpServerPrivate]:
    """
    Calls Qt's 'QModbusTcpServerPrivate *QModbusTcpServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbustcpserver.html#d_func

    Returns
    -------

    Optional[QModbusTcpServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusTcpServerPrivate *QModbusTcpServer::d_func()
    address = self.uglySide.call('ritual_ZN16QModbusTcpServer6d_funcEv')
    from . import QModbusTcpServerPrivate
    return QModbusTcpServerPrivate._cuteAt(address)

  @overload(QModbusTcpConnectionObserver)
  @overload(NoneType)
  def installConnectionObserver(
      self,
      observer: Optional[QModbusTcpConnectionObserver],
  ) -> None:
    """
    Calls Qt's 'void
    QModbusTcpServer::installConnectionObserver(QModbusTcpConnectionObserver
    *observer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserver.html#installConnectionObserver

    Parameters
    ----------

    observer : Optional[QModbusTcpConnectionObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QModbusTcpServer::installConnectionObserver(
    #      QModbusTcpConnectionObserver *observer)
    self.uglySide.call(
        'ritual_ZN16QModbusTcpServer25installConnectionObserverEP28QModbusT'
        'cpConnectionObserver',
        self._addressOf(observer),
    )

  @overload(QTcpSocket)
  @overload(NoneType)
  def modbusClientDisconnected(
      self,
      modbusClient: Optional[QTcpSocket],
  ) -> None:
    """
    Calls Qt's 'void QModbusTcpServer::modbusClientDisconnected(QTcpSocket
    *modbusClient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbustcpserver.html#modbusClientDisconnected

    Parameters
    ----------

    modbusClient : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QModbusTcpServer::modbusClientDisconnected(QTcpSocket
    #      *modbusClient)
    self.uglySide.call(
        'ritual_ZN16QModbusTcpServer24modbusClientDisconnectedEP10QTcpSocke'
        't',
        self._addressOf(modbusClient),
    )

  def open(self) -> bool:
    """
    Calls Qt's 'bool QModbusTcpServer::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbustcpserver.html#open
    """
    #  bool QModbusTcpServer::open()
    ritual = 'ritual_ZN16QModbusTcpServer4openEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QModbusTcpServer4openEv'
    return self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QModbusTcpServer::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbustcpserver.html#close
    """
    #  void QModbusTcpServer::close()
    ritual = 'ritual_ZN16QModbusTcpServer5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QModbusTcpServer5closeEv'
    self.uglySide.call(ritual)
