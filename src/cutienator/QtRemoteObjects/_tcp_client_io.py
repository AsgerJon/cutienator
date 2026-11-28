"""
TcpClientIo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means TcpClientIo to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtROClientIoDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice


class TcpClientIo(QtROClientIoDevice):
  """
  The cute side of Qt's TcpClientIo: a plain Python object standing in front
  of one C++ TcpClientIo.

  It is built on the cute 'QtROClientIoDevice', as Qt's TcpClientIo is built
  on Qt's QtROClientIoDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's TcpClientIo that has a ritual and that Python can
  call so far, 5 names in all: 'connection', 'connectToServer', 'isOpen',
  'doClose', 'doDisconnectFromServer'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TcpClientIo::~TcpClientIo()': the destructor: Python never removes
    a C++ TcpClientIo.

  What has no ritual
  ------------------

  9 of the 15 functions Qt declares: 7 leans on 'TcpClientIo; 2 not a gap.

  What to expect
  --------------

  - The C++ TcpClientIo is created at the first use, not by
    'TcpClientIo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ TcpClientIo.
  - Qt tells when it has removed the C++ TcpClientIo. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's TcpClientIo that has no cute function yet, '__init__',
    'onError', 'onStateChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'TcpClientIo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def connection(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *TcpClientIo::connection() const'.

    Qt's own words: https://doc.qt.io/qt-6/tcpclientio.html#connection

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *TcpClientIo::connection() const
    address = self.uglySide.call('ritual_ZNK11TcpClientIo10connectionEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool TcpClientIo::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/tcpclientio.html#isOpen
    """
    #  bool TcpClientIo::isOpen() const
    return self.uglySide.call('ritual_ZNK11TcpClientIo6isOpenEv')

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
    Qt's 'TcpClientIo::TcpClientIo(QObject *parent)': leans on
    'TcpClientIo::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TcpClientIo.__init__' has no cute function yet. Qt's "
        "'TcpClientIo::TcpClientIo(QObject *parent)': leans on "
        "'TcpClientIo::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void TcpClientIo::connectToServer()'.

    Qt's own words: https://doc.qt.io/qt-6/tcpclientio.html#connectToServer
    """
    #  void TcpClientIo::connectToServer()
    self.uglySide.call('ritual_ZN11TcpClientIo15connectToServerEv')

  def doClose(self) -> None:
    """
    Calls Qt's 'void TcpClientIo::doClose()'.

    Qt's own words: https://doc.qt.io/qt-6/tcpclientio.html#doClose
    """
    #  void TcpClientIo::doClose()
    self.uglySide.call('ritual_ZN11TcpClientIo7doCloseEv')

  def doDisconnectFromServer(self) -> None:
    """
    Calls Qt's 'void TcpClientIo::doDisconnectFromServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/tcpclientio.html#doDisconnectFromServer
    """
    #  void TcpClientIo::doDisconnectFromServer()
    self.uglySide.call('ritual_ZN11TcpClientIo22doDisconnectFromServerEv')

  @staticmethod
  def onError(*__, **_) -> Never:
    """
    Qt's 'void TcpClientIo::onError(QAbstractSocket::SocketError error)':
    leans on 'TcpClientIo::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'TcpClientIo.onError' has no cute function yet. Qt's 'void "
        "TcpClientIo::onError(QAbstractSocket::SocketError error)': leans "
        "on 'TcpClientIo::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def onStateChanged(*__, **_) -> Never:
    """
    Qt's 'void TcpClientIo::onStateChanged(QAbstractSocket::SocketState
    state)': leans on 'TcpClientIo::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'TcpClientIo.onStateChanged' has no cute function yet. Qt's 'void "
        "TcpClientIo::onStateChanged(QAbstractSocket::SocketState state)': "
        "leans on 'TcpClientIo::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
