"""
TcpServerImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means TcpServerImpl to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtNetwork import QAbstractSocket
from . import QConnectionAbstractServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class TcpServerImpl(QConnectionAbstractServer):
  """
  The cute side of Qt's TcpServerImpl: a plain Python object standing in
  front of one C++ TcpServerImpl.

  It is built on the cute 'QConnectionAbstractServer', as Qt's TcpServerImpl
  is built on Qt's QConnectionAbstractServer, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's TcpServerImpl that has a ritual and that Python can
  call so far, 5 names in all: 'hasPendingConnections', 'address', 'listen',
  'serverError', 'close'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TcpServerImpl::~TcpServerImpl()': the destructor: Python never
    removes a C++ TcpServerImpl.

  What has no ritual
  ------------------

  10 of the 16 functions Qt declares: 4 leans on 'TcpServerImpl; 2 not a gap;
  2 forbidden; 1 leans on 'vtable for TcpServerImpl', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken; 1
  leans on 'vtable for TcpServerIo', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ TcpServerImpl is created at the first use, not by
    'TcpServerImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ TcpServerImpl.
  - Qt tells when it has removed the C++ TcpServerImpl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's TcpServerImpl that has no cute function yet,
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
  __qt_class__ = 'TcpServerImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool TcpServerImpl::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/tcpserverimpl.html#hasPendingConnections
    """
    #  bool TcpServerImpl::hasPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK13TcpServerImpl21hasPendingConnectionsEv',
    )

  def address(self) -> QUrl:
    """
    Calls Qt's 'QUrl TcpServerImpl::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/tcpserverimpl.html#address

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl TcpServerImpl::address() const
    address = self.uglySide.call('ritual_ZNK13TcpServerImpl7addressEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def serverError(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError TcpServerImpl::serverError()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/tcpserverimpl.html#serverError

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError TcpServerImpl::serverError() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK13TcpServerImpl11serverErrorEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'TcpServerImpl::TcpServerImpl(QObject *parent)': leans on 'vtable
    for TcpServerImpl', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TcpServerImpl.__init__' has no cute function yet. Qt's "
        "'TcpServerImpl::TcpServerImpl(QObject *parent)': leans on 'vtable "
        "for TcpServerImpl', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QUrl)
  def listen(self, address: QUrl) -> bool:
    """
    Calls Qt's 'bool TcpServerImpl::listen(const QUrl &address)'.

    Qt's own words: https://doc.qt.io/qt-6/tcpserverimpl.html#listen

    Parameters
    ----------

    address : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool TcpServerImpl::listen(const QUrl &address)
    return self.uglySide.call(
        'ritual_ZN13TcpServerImpl6listenERK4QUrl', self._valueOf(address),
    )

  def close(self) -> None:
    """
    Calls Qt's 'void TcpServerImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/tcpserverimpl.html#close
    """
    #  void TcpServerImpl::close()
    self.uglySide.call('ritual_ZN13TcpServerImpl5closeEv')
