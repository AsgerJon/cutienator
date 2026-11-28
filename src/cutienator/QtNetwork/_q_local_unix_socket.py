"""
QLocalUnixSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qlocalsocket_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLocalUnixSocket to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QAbstractSocket, QTcpSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLocalUnixSocket(QTcpSocket):
  """
  The cute side of Qt's QLocalUnixSocket: a plain Python object standing in
  front of one C++ QLocalUnixSocket.

  It is built on the cute 'QTcpSocket', as Qt's QLocalUnixSocket is built on
  Qt's QTcpSocket, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLocalUnixSocket that has a ritual and that Python
  can call so far, 4 names in all: 'setSocketState', 'setErrorString',
  'setSocketError', 'writeData'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qint64 QLocalUnixSocket::readData(char *data, qint64 maxSize)':
    names 'char', which has no cute class yet.

  What to expect
  --------------

  - The C++ QLocalUnixSocket is created at the first use, not by
    'QLocalUnixSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLocalUnixSocket.
  - Qt tells when it has removed the C++ QLocalUnixSocket. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocalUnixSocket'

  #  A C++ QLocalUnixSocket Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLocalUnixSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractSocket.SocketState)
  def setSocketState(self, state: QAbstractSocket.SocketState) -> None:
    """
    Calls Qt's 'void
    QLocalUnixSocket::setSocketState(QAbstractSocket::SocketState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalunixsocket.html#setSocketState

    Parameters
    ----------

    state : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QLocalUnixSocket::setSocketState(QAbstractSocket::SocketState
    #      state)
    self.uglySide.call(
        'ritual_ZN16QLocalUnixSocket14setSocketStateEN15QAbstractSocket11So'
        'cketStateE',
        state.value,
    )

  @overload(str)
  def setErrorString(self, string: str) -> None:
    """
    Calls Qt's 'void QLocalUnixSocket::setErrorString(const QString
    &string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalunixsocket.html#setErrorString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLocalUnixSocket::setErrorString(const QString &string)
    self.uglySide.call(
        'ritual_ZN16QLocalUnixSocket14setErrorStringERK7QString', string,
    )

  @overload(QAbstractSocket.SocketError)
  def setSocketError(self, error: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void
    QLocalUnixSocket::setSocketError(QAbstractSocket::SocketError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalunixsocket.html#setSocketError

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QLocalUnixSocket::setSocketError(QAbstractSocket::SocketError
    #      error)
    self.uglySide.call(
        'ritual_ZN16QLocalUnixSocket14setSocketErrorEN15QAbstractSocket11So'
        'cketErrorE',
        error.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLocalUnixSocket::QLocalUnixSocket()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalunixsocket.html#QLocalUnixSocket
    """
    #  QLocalUnixSocket::QLocalUnixSocket()
    self._noteCreation(QLocalUnixSocket, lambda: Rituals.call(
        'ritual_ZN16QLocalUnixSocketC1Ev',
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

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QLocalUnixSocket::writeData(const char *data, qint64
    maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalunixsocket.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QLocalUnixSocket::writeData(const char *data, qint64 maxSize)
    return self.uglySide.call(
        'ritual_ZN16QLocalUnixSocket9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )
