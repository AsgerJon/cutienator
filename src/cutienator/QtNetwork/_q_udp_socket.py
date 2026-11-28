"""
QUdpSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qudpsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractSocket, QHostAddress

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QNetworkDatagram, QNetworkInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNetworkDatagram = WAIT['QNetworkDatagram']
  QNetworkInterface = WAIT['QNetworkInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUdpSocket(QAbstractSocket):
  """
  The cute side of Qt's QUdpSocket: a plain Python object standing in front
  of one C++ QUdpSocket.

  It is built on the cute 'QAbstractSocket', as Qt's QUdpSocket is built on
  Qt's QAbstractSocket, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUdpSocket that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'bind',
  'joinMulticastGroup', 'leaveMulticastGroup', 'multicastInterface',
  'setMulticastInterface', 'hasPendingDatagrams', 'pendingDatagramSize',
  'receiveDatagram', 'writeDatagram'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QUdpSocket::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QUdpSocket::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QUdpSocket::~QUdpSocket()': the destructor: Python never removes a
    C++ QUdpSocket.
  - Qt's 'qint64 QUdpSocket::readDatagram(char *data, qint64 maxlen,
    QHostAddress *host, quint16 *port)': names 'char', which has no cute
    class yet.
  - Qt's 'QUdpSocketPrivate *QUdpSocket::d_func()': gives
    'QUdpSocketPrivate', which has no cute class yet.
  - Qt's 'const QUdpSocketPrivate *QUdpSocket::d_func() const': gives
    'QUdpSocketPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 28 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QUdpSocket is created at the first use, not by 'QUdpSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUdpSocket.
  - Qt tells when it has removed the C++ QUdpSocket. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QUdpSocket that has no cute function yet,
    'readDatagram', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QUdpSocket::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#tr

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
    #  QString QUdpSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QUdpSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUdpSocket'

  #  A C++ QUdpSocket Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUdpSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUdpSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUdpSocket::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QUdpSocket10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def multicastInterface(self) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QUdpSocket::multicastInterface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#multicastInterface

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QUdpSocket::multicastInterface() const
    address = self.uglySide.call(
        'ritual_ZNK10QUdpSocket18multicastInterfaceEv',
    )
    from . import QNetworkInterface
    return QNetworkInterface._cuteOwning(address)

  def hasPendingDatagrams(self) -> bool:
    """
    Calls Qt's 'bool QUdpSocket::hasPendingDatagrams() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qudpsocket.html#hasPendingDatagrams
    """
    #  bool QUdpSocket::hasPendingDatagrams() const
    return self.uglySide.call(
        'ritual_ZNK10QUdpSocket19hasPendingDatagramsEv',
    )

  def pendingDatagramSize(self) -> int:
    """
    Calls Qt's 'qint64 QUdpSocket::pendingDatagramSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qudpsocket.html#pendingDatagramSize
    """
    #  qint64 QUdpSocket::pendingDatagramSize() const
    return self.uglySide.call(
        'ritual_ZNK10QUdpSocket19pendingDatagramSizeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkInterface)
  def setMulticastInterface(self, iface: QNetworkInterface) -> None:
    """
    Calls Qt's 'void QUdpSocket::setMulticastInterface(const
    QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qudpsocket.html#setMulticastInterface

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  void QUdpSocket::setMulticastInterface(const QNetworkInterface &iface)
    self.uglySide.call(
        'ritual_ZN10QUdpSocket21setMulticastInterfaceERK17QNetworkInterface',
        self._valueOf(iface),
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
    Notes what was given, for Qt's 'QUdpSocket::QUdpSocket(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#QUdpSocket

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUdpSocket::QUdpSocket(QObject *parent)
    self._noteCreation(QUdpSocket, lambda: Rituals.call(
        'ritual_ZN10QUdpSocketC1EP7QObject',
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

  @overload(QHostAddress.SpecialAddress)
  @overload(QHostAddress.SpecialAddress, int)
  @overload(QHostAddress.SpecialAddress, int, QAbstractSocket.BindMode)
  def bind(
      self,
      addr: QHostAddress.SpecialAddress,
      port: int = 0,
      mode: QAbstractSocket.BindMode = (
          QAbstractSocket.BindMode.DefaultForPlatform),
  ) -> bool:
    """
    Calls Qt's 'bool QUdpSocket::bind(QHostAddress::SpecialAddress addr,
    quint16 port, BindMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#bind

    Parameters
    ----------

    addr : QHostAddress.SpecialAddress
      Passed on as its number.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    mode : QAbstractSocket.BindMode
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.BindMode.DefaultForPlatform.
    """
    #  bool QUdpSocket::bind(QHostAddress::SpecialAddress addr, quint16 port,
    #      BindMode mode)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket4bindEN12QHostAddress14SpecialAddressEt6QFlag'
        'sIN15QAbstractSocket8BindFlagEE',
        addr.value, port, mode.value,
    )

  @overload(QHostAddress)
  def joinMulticastGroup(self, groupAddress: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QUdpSocket::joinMulticastGroup(const QHostAddress
    &groupAddress)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#joinMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QUdpSocket::joinMulticastGroup(const QHostAddress &groupAddress)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket18joinMulticastGroupERK12QHostAddress',
        self._valueOf(groupAddress),
    )

  @overload(QHostAddress, QNetworkInterface)
  def joinMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QUdpSocket::joinMulticastGroup(const QHostAddress
    &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#joinMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QUdpSocket::joinMulticastGroup(const QHostAddress &groupAddress,
    #      const QNetworkInterface &iface)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket18joinMulticastGroupERK12QHostAddressRK17QNet'
        'workInterface',
        self._valueOf(groupAddress), self._valueOf(iface),
    )

  @overload(QHostAddress)
  def leaveMulticastGroup(self, groupAddress: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QUdpSocket::leaveMulticastGroup(const QHostAddress
    &groupAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qudpsocket.html#leaveMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QUdpSocket::leaveMulticastGroup(const QHostAddress &groupAddress)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket19leaveMulticastGroupERK12QHostAddress',
        self._valueOf(groupAddress),
    )

  @overload(QHostAddress, QNetworkInterface)
  def leaveMulticastGroup(
      self,
      groupAddress: QHostAddress,
      iface: QNetworkInterface,
  ) -> bool:
    """
    Calls Qt's 'bool QUdpSocket::leaveMulticastGroup(const QHostAddress
    &groupAddress, const QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qudpsocket.html#leaveMulticastGroup

    Parameters
    ----------

    groupAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  bool QUdpSocket::leaveMulticastGroup(const QHostAddress &groupAddress,
    #      const QNetworkInterface &iface)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket19leaveMulticastGroupERK12QHostAddressRK17QNe'
        'tworkInterface',
        self._valueOf(groupAddress), self._valueOf(iface),
    )

  @overload()
  @overload(int)
  def receiveDatagram(self, maxSize: int = -1) -> QNetworkDatagram:
    """
    Calls Qt's 'QNetworkDatagram QUdpSocket::receiveDatagram(qint64
    maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#receiveDatagram

    Parameters
    ----------

    maxSize : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QNetworkDatagram
      A new cute QNetworkDatagram around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkDatagram QUdpSocket::receiveDatagram(qint64 maxSize)
    address = self.uglySide.call(
        'ritual_ZN10QUdpSocket15receiveDatagramEx', maxSize,
    )
    from . import QNetworkDatagram
    return QNetworkDatagram._cuteOwning(address)

  @overload(QNetworkDatagram)
  def writeDatagram(self, datagram: QNetworkDatagram) -> int:
    """
    Calls Qt's 'qint64 QUdpSocket::writeDatagram(const QNetworkDatagram
    &datagram)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#writeDatagram

    Parameters
    ----------

    datagram : QNetworkDatagram
      Passed on as a value: Qt reads the C++ QNetworkDatagram, which stays
      Python's own.
    """
    #  qint64 QUdpSocket::writeDatagram(const QNetworkDatagram &datagram)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket13writeDatagramERK16QNetworkDatagram',
        self._valueOf(datagram),
    )

  @overload(str, int, QHostAddress, int)
  @overload(NoneType, int, QHostAddress, int)
  def writeDatagram(
      self,
      data: Optional[str],
      len: int,
      host: QHostAddress,
      port: int,
  ) -> int:
    """
    Calls Qt's 'qint64 QUdpSocket::writeDatagram(const char *data, qint64
    len, const QHostAddress &host, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#writeDatagram

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    host : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  qint64 QUdpSocket::writeDatagram(const char *data, qint64 len, const
    #      QHostAddress &host, quint16 port)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket13writeDatagramEPKcxRK12QHostAddresst',
        self._bytesOf(data), len, self._valueOf(host), port,
    )

  @overload(QByteArray, QHostAddress, int)
  def writeDatagram(
      self,
      datagram: QByteArray,
      host: QHostAddress,
      port: int,
  ) -> int:
    """
    Calls Qt's 'qint64 QUdpSocket::writeDatagram(const QByteArray &datagram,
    const QHostAddress &host, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qudpsocket.html#writeDatagram

    Parameters
    ----------

    datagram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    host : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  qint64 QUdpSocket::writeDatagram(const QByteArray &datagram, const
    #      QHostAddress &host, quint16 port)
    return self.uglySide.call(
        'ritual_ZN10QUdpSocket13writeDatagramERK10QByteArrayRK12QHostAddres'
        'st',
        self._valueOf(datagram), self._valueOf(host), port,
    )

  @staticmethod
  def readDatagram(*__, **_) -> Never:
    """
    Qt's 'qint64 QUdpSocket::readDatagram(char *data, qint64 maxlen,
    QHostAddress *host, quint16 *port)': names 'char', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QUdpSocket.readDatagram' has no cute function yet. Qt's 'qint64 "
        "QUdpSocket::readDatagram(char *data, qint64 maxlen, QHostAddress "
        "*host, quint16 *port)': names 'char', which has no cute class yet.")
