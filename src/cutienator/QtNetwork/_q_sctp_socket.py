"""
QSctpSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsctpsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QTcpSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QNetworkDatagram, QSctpSocketPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkDatagram = WAIT['QNetworkDatagram']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSctpSocket(QTcpSocket):
  """
  The cute side of Qt's QSctpSocket: a plain Python object standing in front
  of one C++ QSctpSocket.

  It is built on the cute 'QTcpSocket', as Qt's QSctpSocket is built on Qt's
  QTcpSocket, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSctpSocket that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'close',
  'disconnectFromHost', 'setMaximumChannelCount', 'maximumChannelCount',
  'isInDatagramMode', 'readDatagram', 'writeDatagram', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSctpSocket::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSctpSocket::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSctpSocket::~QSctpSocket()': the destructor: Python never removes
    a C++ QSctpSocket.
  - Qt's 'qint64 QSctpSocket::readData(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'qint64 QSctpSocket::readLineData(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'const QSctpSocketPrivate *QSctpSocket::d_func() const': takes in
    Python what 'QSctpSocketPrivate *QSctpSocket::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSctpSocket is created at the first use, not by
    'QSctpSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSctpSocket.
  - Qt tells when it has removed the C++ QSctpSocket. Every call on the cute
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
    Calls Qt's 'QString QSctpSocket::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#tr

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
    #  QString QSctpSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QSctpSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSctpSocket'

  #  A C++ QSctpSocket Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSctpSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSctpSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSctpSocket::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QSctpSocket10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def maximumChannelCount(self) -> int:
    """
    Calls Qt's 'int QSctpSocket::maximumChannelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpsocket.html#maximumChannelCount
    """
    #  int QSctpSocket::maximumChannelCount() const
    return self.uglySide.call(
        'ritual_ZNK11QSctpSocket19maximumChannelCountEv',
    )

  def isInDatagramMode(self) -> bool:
    """
    Calls Qt's 'bool QSctpSocket::isInDatagramMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#isInDatagramMode
    """
    #  bool QSctpSocket::isInDatagramMode() const
    return self.uglySide.call('ritual_ZNK11QSctpSocket16isInDatagramModeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaximumChannelCount(self, count: int) -> None:
    """
    Calls Qt's 'void QSctpSocket::setMaximumChannelCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpsocket.html#setMaximumChannelCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSctpSocket::setMaximumChannelCount(int count)
    self.uglySide.call(
        'ritual_ZN11QSctpSocket22setMaximumChannelCountEi', count,
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
    Notes what was given, for Qt's 'QSctpSocket::QSctpSocket(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#QSctpSocket

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSctpSocket::QSctpSocket(QObject *parent)
    self._noteCreation(QSctpSocket, lambda: Rituals.call(
        'ritual_ZN11QSctpSocketC1EP7QObject',
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

  def close(self) -> None:
    """
    Calls Qt's 'void QSctpSocket::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#close
    """
    #  void QSctpSocket::close()
    ritual = 'ritual_ZN11QSctpSocket5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSctpSocket5closeEv'
    self.uglySide.call(ritual)

  def disconnectFromHost(self) -> None:
    """
    Calls Qt's 'void QSctpSocket::disconnectFromHost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsctpsocket.html#disconnectFromHost
    """
    #  void QSctpSocket::disconnectFromHost()
    ritual = 'ritual_ZN11QSctpSocket18disconnectFromHostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSctpSocket18disconnectFromHostEv'
    self.uglySide.call(ritual)

  def readDatagram(self) -> QNetworkDatagram:
    """
    Calls Qt's 'QNetworkDatagram QSctpSocket::readDatagram()'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#readDatagram

    Returns
    -------

    QNetworkDatagram
      A new cute QNetworkDatagram around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkDatagram QSctpSocket::readDatagram()
    address = self.uglySide.call('ritual_ZN11QSctpSocket12readDatagramEv')
    from . import QNetworkDatagram
    return QNetworkDatagram._cuteOwning(address)

  @overload(QNetworkDatagram)
  def writeDatagram(self, datagram: QNetworkDatagram) -> bool:
    """
    Calls Qt's 'bool QSctpSocket::writeDatagram(const QNetworkDatagram
    &datagram)'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#writeDatagram

    Parameters
    ----------

    datagram : QNetworkDatagram
      Passed on as a value: Qt reads the C++ QNetworkDatagram, which stays
      Python's own.
    """
    #  bool QSctpSocket::writeDatagram(const QNetworkDatagram &datagram)
    return self.uglySide.call(
        'ritual_ZN11QSctpSocket13writeDatagramERK16QNetworkDatagram',
        self._valueOf(datagram),
    )

  def d_func(self) -> Optional[QSctpSocketPrivate]:
    """
    Calls Qt's 'QSctpSocketPrivate *QSctpSocket::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsctpsocket.html#d_func

    Returns
    -------

    Optional[QSctpSocketPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSctpSocketPrivate *QSctpSocket::d_func()
    address = self.uglySide.call('ritual_ZN11QSctpSocket6d_funcEv')
    from . import QSctpSocketPrivate
    return QSctpSocketPrivate._cuteAt(address)
