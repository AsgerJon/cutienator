"""
QNetworkDatagram binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkdatagram.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QHostAddress, QNetworkDatagramPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHostAddress = WAIT['QHostAddress']
  QNetworkDatagramPrivate = WAIT['QNetworkDatagramPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkDatagram(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkDatagram: a plain Python object standing in
  front of one C++ QNetworkDatagram.

  C++ hands a QNetworkDatagram around as a copy, so every C++
  QNetworkDatagram behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkDatagram that has a ritual and that Python
  can call so far, 19 names in all: 'clear', 'isValid', 'isNull',
  'interfaceIndex', 'setInterfaceIndex', 'senderAddress',
  'destinationAddress', 'senderPort', 'destinationPort', 'setSender',
  'setDestination', 'hopLimit', 'setHopLimit', 'data', 'setData',
  'makeReply', 'makeReply_helper', 'makeReply_helper_inplace', 'destroy'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkDatagram &QNetworkDatagram::operator=(const
    QNetworkDatagram &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QNetworkDatagram::~QNetworkDatagram()': the destructor: Python
    removes its C++ QNetworkDatagram by it, and has no other use for it.
  - Qt's 'QNetworkDatagram::QNetworkDatagram(QNetworkDatagram &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QNetworkDatagram &QNetworkDatagram::operator=(QNetworkDatagram
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QNetworkDatagram::swap(QNetworkDatagram &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QNetworkDatagram::QNetworkDatagram(QNetworkDatagramPrivate &dd)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 29 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QNetworkDatagram is created at the first use, not by
    'QNetworkDatagram(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkDatagram back gives a copy the ritual made
    for Python, in a new cute QNetworkDatagram.
  - Each name of Qt's QNetworkDatagram that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNetworkDatagramPrivate)
  @overload(NoneType)
  def destroy(d: Optional[QNetworkDatagramPrivate]) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::destroy(QNetworkDatagramPrivate *d)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#destroy

    Parameters
    ----------

    d : Optional[QNetworkDatagramPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkDatagram::destroy(QNetworkDatagramPrivate *d)
    Rituals.call(
        'ritual_ZN16QNetworkDatagram7destroyEP23QNetworkDatagramPrivate',
        CuteMixin._addressOf(d),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkDatagram'

  #  Qt's '~QNetworkDatagram()'. Naming it makes this a value class: Python
  #  owns every C++ QNetworkDatagram behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QNetworkDatagramD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QNetworkDatagram::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#isValid
    """
    #  bool QNetworkDatagram::isValid() const
    return self.uglySide.call('ritual_ZNK16QNetworkDatagram7isValidEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QNetworkDatagram::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#isNull
    """
    #  bool QNetworkDatagram::isNull() const
    return self.uglySide.call('ritual_ZNK16QNetworkDatagram6isNullEv')

  def interfaceIndex(self) -> int:
    """
    Calls Qt's 'uint QNetworkDatagram::interfaceIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#interfaceIndex
    """
    #  uint QNetworkDatagram::interfaceIndex() const
    return self.uglySide.call(
        'ritual_ZNK16QNetworkDatagram14interfaceIndexEv',
    )

  def senderAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QNetworkDatagram::senderAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#senderAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNetworkDatagram::senderAddress() const
    address = self.uglySide.call(
        'ritual_ZNK16QNetworkDatagram13senderAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def destinationAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QNetworkDatagram::destinationAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#destinationAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNetworkDatagram::destinationAddress() const
    address = self.uglySide.call(
        'ritual_ZNK16QNetworkDatagram18destinationAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def senderPort(self) -> int:
    """
    Calls Qt's 'int QNetworkDatagram::senderPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#senderPort
    """
    #  int QNetworkDatagram::senderPort() const
    return self.uglySide.call('ritual_ZNK16QNetworkDatagram10senderPortEv')

  def destinationPort(self) -> int:
    """
    Calls Qt's 'int QNetworkDatagram::destinationPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#destinationPort
    """
    #  int QNetworkDatagram::destinationPort() const
    return self.uglySide.call(
        'ritual_ZNK16QNetworkDatagram15destinationPortEv',
    )

  def hopLimit(self) -> int:
    """
    Calls Qt's 'int QNetworkDatagram::hopLimit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#hopLimit
    """
    #  int QNetworkDatagram::hopLimit() const
    return self.uglySide.call('ritual_ZNK16QNetworkDatagram8hopLimitEv')

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkDatagram::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkDatagram::data() const
    address = self.uglySide.call('ritual_ZNK16QNetworkDatagram4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray)
  def makeReply(self, payload: QByteArray) -> QNetworkDatagram:
    """
    Calls Qt's 'QNetworkDatagram QNetworkDatagram::makeReply(const QByteArray
    &payload) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#makeReply

    Parameters
    ----------

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QNetworkDatagram
      A new cute QNetworkDatagram around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkDatagram QNetworkDatagram::makeReply(const QByteArray
    #      &payload) const
    address = self.uglySide.call(
        'ritual_ZNKR16QNetworkDatagram9makeReplyERK10QByteArray',
        self._valueOf(payload),
    )
    return QNetworkDatagram._cuteOwning(address)

  @overload(QByteArray)
  def makeReply_helper(self, data: QByteArray) -> QNetworkDatagram:
    """
    Calls Qt's 'QNetworkDatagram QNetworkDatagram::makeReply_helper(const
    QByteArray &data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#makeReply_helper

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QNetworkDatagram
      A new cute QNetworkDatagram around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkDatagram QNetworkDatagram::makeReply_helper(const QByteArray
    #      &data) const
    address = self.uglySide.call(
        'ritual_ZNK16QNetworkDatagram16makeReply_helperERK10QByteArray',
        self._valueOf(data),
    )
    return QNetworkDatagram._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInterfaceIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::setInterfaceIndex(uint index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#setInterfaceIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QNetworkDatagram::setInterfaceIndex(uint index)
    self.uglySide.call(
        'ritual_ZN16QNetworkDatagram17setInterfaceIndexEj', index,
    )

  @overload(QHostAddress)
  @overload(QHostAddress, int)
  def setSender(self, address: QHostAddress, port: int = 0) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::setSender(const QHostAddress &address,
    quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#setSender

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QNetworkDatagram::setSender(const QHostAddress &address, quint16
    #      port)
    self.uglySide.call(
        'ritual_ZN16QNetworkDatagram9setSenderERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(QHostAddress, int)
  def setDestination(self, address: QHostAddress, port: int) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::setDestination(const QHostAddress
    &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#setDestination

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  void QNetworkDatagram::setDestination(const QHostAddress &address,
    #      quint16 port)
    self.uglySide.call(
        'ritual_ZN16QNetworkDatagram14setDestinationERK12QHostAddresst',
        self._valueOf(address), port,
    )

  @overload(int)
  def setHopLimit(self, count: int) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::setHopLimit(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#setHopLimit

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QNetworkDatagram::setHopLimit(int count)
    self.uglySide.call('ritual_ZN16QNetworkDatagram11setHopLimitEi', count)

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::setData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkDatagram::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN16QNetworkDatagram7setDataERK10QByteArray',
        self._valueOf(data),
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
    Notes what was given, for Qt's 'QNetworkDatagram::QNetworkDatagram()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#QNetworkDatagram
    """
    #  QNetworkDatagram::QNetworkDatagram()
    self._noteCreation(QNetworkDatagram, lambda: Rituals.call(
        'ritual_ZN16QNetworkDatagramC1Ev',
    ))

  @overload(QByteArray)
  @overload(QByteArray, QHostAddress)
  @overload(QByteArray, QHostAddress, int)
  def __init__(
      self,
      data: QByteArray,
      destinationAddress: Optional[QHostAddress] = None,
      port: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QNetworkDatagram::QNetworkDatagram(const
    QByteArray &data, const QHostAddress &destinationAddress, quint16 port)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#QNetworkDatagram

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    destinationAddress : Optional[QHostAddress]
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own. May be left out, as in Qt: a new 'QHostAddress()' is then
      passed on.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QNetworkDatagram::QNetworkDatagram(const QByteArray &data, const
    #      QHostAddress &destinationAddress, quint16 port)
    if destinationAddress is None:
      from . import QHostAddress
      destinationAddress = QHostAddress()
    self._noteCreation(QNetworkDatagram, lambda: Rituals.call(
        'ritual_ZN16QNetworkDatagramC1ERK10QByteArrayRK12QHostAddresst',
        self._valueOf(data), self._valueOf(destinationAddress), port,
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkDatagram) -> None:
    """
    Notes what was given, for Qt's 'QNetworkDatagram::QNetworkDatagram(const
    QNetworkDatagram &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#QNetworkDatagram

    Parameters
    ----------

    other : QNetworkDatagram
      Passed on as a value: Qt reads the C++ QNetworkDatagram, which stays
      Python's own.
    """
    #  QNetworkDatagram::QNetworkDatagram(const QNetworkDatagram &other)
    self._noteCreation(QNetworkDatagram, lambda: Rituals.call(
        'ritual_ZN16QNetworkDatagramC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkdatagram.html#clear
    """
    #  void QNetworkDatagram::clear()
    self.uglySide.call('ritual_ZN16QNetworkDatagram5clearEv')

  @overload(QByteArray)
  def makeReply_helper_inplace(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkDatagram::makeReply_helper_inplace(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagram.html#makeReply_helper_inplace

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkDatagram::makeReply_helper_inplace(const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN16QNetworkDatagram24makeReply_helper_inplaceERK10QByteArr'
        'ay',
        self._valueOf(data),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkDatagram::swap(QNetworkDatagram &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkDatagram.swap' has no cute function yet. Qt's 'void "
        "QNetworkDatagram::swap(QNetworkDatagram &other)': takes a type "
        "Python has no way to hand over yet.")
