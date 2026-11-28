"""
QBluetoothHostInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothhostinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QBluetoothAddress, QBluetoothHostInfoPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']


class QBluetoothHostInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothHostInfo: a plain Python object standing in
  front of one C++ QBluetoothHostInfo.

  C++ hands a QBluetoothHostInfo around as a copy, so every C++
  QBluetoothHostInfo behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBluetoothHostInfo that has a ritual and that Python
  can call so far, 8 names in all: '__eq__', '__ne__', 'address',
  'setAddress', 'name', 'setName', 'equals', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBluetoothHostInfo::~QBluetoothHostInfo()': the destructor: Python
    removes its C++ QBluetoothHostInfo by it, and has no other use for it.
  - Qt's 'QBluetoothHostInfo &QBluetoothHostInfo::operator=(const
    QBluetoothHostInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'const QBluetoothHostInfoPrivate *QBluetoothHostInfo::d_func()
    const': takes in Python what 'QBluetoothHostInfoPrivate
    *QBluetoothHostInfo::d_func()' takes.

  What to expect
  --------------

  - The C++ QBluetoothHostInfo is created at the first use, not by
    'QBluetoothHostInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBluetoothHostInfo back gives a copy the ritual made
    for Python, in a new cute QBluetoothHostInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(a: QBluetoothHostInfo, b: QBluetoothHostInfo) -> bool:
    """
    Calls Qt's 'bool QBluetoothHostInfo::equals(const QBluetoothHostInfo &a,
    const QBluetoothHostInfo &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#equals

    Parameters
    ----------

    a : QBluetoothHostInfo
      Passed on as a value: Qt reads the C++ QBluetoothHostInfo, which stays
      Python's own.

    b : QBluetoothHostInfo
      Passed on as a value: Qt reads the C++ QBluetoothHostInfo, which stays
      Python's own.
    """
    #  bool QBluetoothHostInfo::equals(const QBluetoothHostInfo &a, const
    #      QBluetoothHostInfo &b)
    return Rituals.call(
        'ritual_ZN18QBluetoothHostInfo6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothHostInfo'

  #  Qt's '~QBluetoothHostInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QBluetoothHostInfo behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QBluetoothHostInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def address(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothHostInfo::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#address

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothHostInfo::address() const
    address = self.uglySide.call('ritual_ZNK18QBluetoothHostInfo7addressEv')
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QBluetoothHostInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothHostInfo::name() const
    return self.uglySide.call('ritual_ZNK18QBluetoothHostInfo4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBluetoothAddress)
  def setAddress(self, address: QBluetoothAddress) -> None:
    """
    Calls Qt's 'void QBluetoothHostInfo::setAddress(const QBluetoothAddress
    &address)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#setAddress

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  void QBluetoothHostInfo::setAddress(const QBluetoothAddress &address)
    self.uglySide.call(
        'ritual_ZN18QBluetoothHostInfo10setAddressERK17QBluetoothAddress',
        self._valueOf(address),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QBluetoothHostInfo::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBluetoothHostInfo::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN18QBluetoothHostInfo7setNameERK7QString', name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QBluetoothHostInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QBluetoothHostInfo &a, const
    QBluetoothHostInfo &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#operator==

    Parameters
    ----------

    b : QBluetoothHostInfo
      Passed on as a value: Qt reads the C++ QBluetoothHostInfo, which stays
      Python's own.
    """
    #  bool operator==(const QBluetoothHostInfo &a, const QBluetoothHostInfo
    #      &b)
    return Rituals.call(
        'ritual_ZeqRK18QBluetoothHostInfoS1_',
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
  def __ne__(self, b: QBluetoothHostInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QBluetoothHostInfo &a, const
    QBluetoothHostInfo &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#operator!=

    Parameters
    ----------

    b : QBluetoothHostInfo
      Passed on as a value: Qt reads the C++ QBluetoothHostInfo, which stays
      Python's own.
    """
    #  bool operator!=(const QBluetoothHostInfo &a, const QBluetoothHostInfo
    #      &b)
    return Rituals.call(
        'ritual_ZneRK18QBluetoothHostInfoS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothHostInfo::QBluetoothHostInfo()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothhostinfo.html#QBluetoothHostInfo
    """
    #  QBluetoothHostInfo::QBluetoothHostInfo()
    self._noteCreation(QBluetoothHostInfo, lambda: Rituals.call(
        'ritual_ZN18QBluetoothHostInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QBluetoothHostInfo) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothHostInfo::QBluetoothHostInfo(const QBluetoothHostInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothhostinfo.html#QBluetoothHostInfo

    Parameters
    ----------

    other : QBluetoothHostInfo
      Passed on as a value: Qt reads the C++ QBluetoothHostInfo, which stays
      Python's own.
    """
    #  QBluetoothHostInfo::QBluetoothHostInfo(const QBluetoothHostInfo
    #      &other)
    self._noteCreation(QBluetoothHostInfo, lambda: Rituals.call(
        'ritual_ZN18QBluetoothHostInfoC1ERKS_', self._valueOf(other),
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

  def d_func(self) -> Optional[QBluetoothHostInfoPrivate]:
    """
    Calls Qt's 'QBluetoothHostInfoPrivate *QBluetoothHostInfo::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothhostinfo.html#d_func

    Returns
    -------

    Optional[QBluetoothHostInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothHostInfoPrivate *QBluetoothHostInfo::d_func()
    address = self.uglySide.call('ritual_ZN18QBluetoothHostInfo6d_funcEv')
    from . import QBluetoothHostInfoPrivate
    return QBluetoothHostInfoPrivate._cuteAt(address)


#  Qt's 'QList<QBluetoothHostInfo>': the list of QBluetoothHostInfo, which
#  'QList[QBluetoothHostInfo]' gives. It is made here, so that there is one
#  as soon as there can be a QBluetoothHostInfo.
QList.createKind(
    QBluetoothHostInfo, 'value',
    make='ritual_list_make_QBluetoothHostInfo',
    add='ritual_list_add_QBluetoothHostInfo',
    size='ritual_list_size_QBluetoothHostInfo',
    at='ritual_list_at_QBluetoothHostInfo',
    drop='ritual_list_drop_QBluetoothHostInfo',
)
