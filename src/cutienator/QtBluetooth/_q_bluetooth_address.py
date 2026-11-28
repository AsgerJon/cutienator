"""
QBluetoothAddress binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothaddress.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QBluetoothAddress(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothAddress: a plain Python object standing in
  front of one C++ QBluetoothAddress.

  C++ hands a QBluetoothAddress around as a copy, so every C++
  QBluetoothAddress behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBluetoothAddress that has a ritual and that Python
  can call so far, 9 names in all: 'isNull', 'clear', '__lt__', '__eq__',
  '__ne__', 'toUInt64', 'toString', '__rlshift__', 'streamingOperator'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBluetoothAddress::~QBluetoothAddress()': the destructor: Python
    removes its C++ QBluetoothAddress by it, and has no other use for it.
  - Qt's 'QBluetoothAddress &QBluetoothAddress::operator=(const
    QBluetoothAddress &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QBluetoothAddress::QBluetoothAddress(QBluetoothAddress &&a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QBluetoothAddress &QBluetoothAddress::operator=(QBluetoothAddress
    &&a0)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QBluetoothAddress is created at the first use, not by
    'QBluetoothAddress(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBluetoothAddress back gives a copy the ritual made
    for Python, in a new cute QBluetoothAddress.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDebug, THIS)
  def streamingOperator(a0: QDebug, address: QBluetoothAddress) -> QDebug:
    """
    Calls Qt's 'QDebug QBluetoothAddress::streamingOperator(QDebug a0, const
    QBluetoothAddress &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothaddress.html#streamingOperator

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QBluetoothAddress::streamingOperator(QDebug a0, const
    #      QBluetoothAddress &address)
    address = Rituals.call(
        'ritual_ZN17QBluetoothAddress17streamingOperatorE6QDebugRKS_',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(address),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothAddress'

  #  Qt's '~QBluetoothAddress()'. Naming it makes this a value class: Python
  #  owns every C++ QBluetoothAddress behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QBluetoothAddressD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothAddress::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#isNull
    """
    #  bool QBluetoothAddress::isNull() const
    return self.uglySide.call('ritual_ZNK17QBluetoothAddress6isNullEv')

  def toUInt64(self) -> int:
    """
    Calls Qt's 'quint64 QBluetoothAddress::toUInt64() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#toUInt64
    """
    #  quint64 QBluetoothAddress::toUInt64() const
    return self.uglySide.call('ritual_ZNK17QBluetoothAddress8toUInt64Ev')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QBluetoothAddress::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothAddress::toString() const
    return self.uglySide.call('ritual_ZNK17QBluetoothAddress8toStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __lt__(self, b: QBluetoothAddress) -> bool:
    """
    Calls Qt's 'bool operator<(const QBluetoothAddress &a, const
    QBluetoothAddress &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#operator<

    Parameters
    ----------

    b : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  bool operator<(const QBluetoothAddress &a, const QBluetoothAddress &b)
    return Rituals.call(
        'ritual_ZltRK17QBluetoothAddressS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, b: QBluetoothAddress) -> bool:
    """
    Calls Qt's 'bool operator==(const QBluetoothAddress &a, const
    QBluetoothAddress &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#operator==

    Parameters
    ----------

    b : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  bool operator==(const QBluetoothAddress &a, const QBluetoothAddress
    #      &b)
    return Rituals.call(
        'ritual_ZeqRK17QBluetoothAddressS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, b: QBluetoothAddress) -> bool:
    """
    Calls Qt's 'bool operator!=(const QBluetoothAddress &a, const
    QBluetoothAddress &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#operator!=

    Parameters
    ----------

    b : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  bool operator!=(const QBluetoothAddress &a, const QBluetoothAddress
    #      &b)
    return Rituals.call(
        'ritual_ZneRK17QBluetoothAddressS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, d: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug d, const QBluetoothAddress &a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#operator<<

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug d, const QBluetoothAddress &a)
    address = Rituals.call(
        'ritual_Zls6QDebugRK17QBluetoothAddress',
        CuteMixin._valueOf(d), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QBluetoothAddress::QBluetoothAddress()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothaddress.html#QBluetoothAddress
    """
    #  QBluetoothAddress::QBluetoothAddress()
    self._noteCreation(QBluetoothAddress, lambda: Rituals.call(
        'ritual_ZN17QBluetoothAddressC1Ev',
    ))

  @overload(int)
  def __init__(self, address: int) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothAddress::QBluetoothAddress(quint64 address)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothaddress.html#QBluetoothAddress

    Parameters
    ----------

    address : int
      Passed on as it is.
    """
    #  QBluetoothAddress::QBluetoothAddress(quint64 address)
    self._noteCreation(QBluetoothAddress, lambda: Rituals.call(
        'ritual_ZN17QBluetoothAddressC1Ey', address,
    ))

  @overload(str)
  def __init__(self, address: str) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothAddress::QBluetoothAddress(const QString &address)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothaddress.html#QBluetoothAddress

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QBluetoothAddress::QBluetoothAddress(const QString &address)
    self._noteCreation(QBluetoothAddress, lambda: Rituals.call(
        'ritual_ZN17QBluetoothAddressC1ERK7QString', address,
    ))

  @overload(THIS)
  def __init__(self, other: QBluetoothAddress) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothAddress::QBluetoothAddress(const QBluetoothAddress &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothaddress.html#QBluetoothAddress

    Parameters
    ----------

    other : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  QBluetoothAddress::QBluetoothAddress(const QBluetoothAddress &other)
    self._noteCreation(QBluetoothAddress, lambda: Rituals.call(
        'ritual_ZN17QBluetoothAddressC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QBluetoothAddress::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothaddress.html#clear
    """
    #  void QBluetoothAddress::clear()
    self.uglySide.call('ritual_ZN17QBluetoothAddress5clearEv')


#  Qt's 'QList<QBluetoothAddress>': the list of QBluetoothAddress, which
#  'QList[QBluetoothAddress]' gives. It is made here, so that there is one as
#  soon as there can be a QBluetoothAddress.
QList.createKind(
    QBluetoothAddress, 'value',
    make='ritual_list_make_QBluetoothAddress',
    add='ritual_list_add_QBluetoothAddress',
    size='ritual_list_size_QBluetoothAddress',
    at='ritual_list_at_QBluetoothAddress',
    drop='ritual_list_drop_QBluetoothAddress',
)
