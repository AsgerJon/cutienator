"""
QBitArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbitarray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSysInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QBitRef

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBitArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBitArray: a plain Python object standing in front of
  one C++ QBitArray.

  C++ hands a QBitArray around as a copy, so every C++ QBitArray behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBitArray that has a ritual and that Python can call
  so far, 27 names in all: '__and__', '__or__', '__xor__', '__invert__',
  'size', 'count', 'isEmpty', 'isNull', 'resize', 'detach', 'isDetached',
  'clear', 'testBit', 'setBit', 'clearBit', 'toggleBit', 'at', '__getitem__',
  '__iand__', '__ior__', '__ixor__', 'fill', 'truncate', 'bits', 'fromBits',
  '__eq__', '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QBitArray::operator[](qsizetype i) const': takes in Python
    what 'QBitRef QBitArray::operator[](qsizetype i)' takes.
  - Qt's 'quint32 QBitArray::toUInt32(QSysInfo::Endian endianness, bool *ok)
    const': takes a number to change where it is.
  - Qt's 'QBitArray::~QBitArray()': the destructor: Python removes its C++
    QBitArray by it, and has no other use for it.

  What has no ritual
  ------------------

  23 of the 59 functions Qt declares: 20 takes or gives a type that cannot be
  passed yet; 2 private; 1 a template.

  What to expect
  --------------

  - The C++ QBitArray is created at the first use, not by 'QBitArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBitArray back gives a copy the ritual made for
    Python, in a new cute QBitArray.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def fromBits(data: Optional[str], len: int) -> QBitArray:
    """
    Calls Qt's 'QBitArray QBitArray::fromBits(const char *data, qsizetype
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#fromBits

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray QBitArray::fromBits(const char *data, qsizetype len)
    address = Rituals.call(
        'ritual_ZN9QBitArray8fromBitsEPKcx', CuteMixin._bytesOf(data), len,
    )
    return QBitArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBitArray'

  #  Qt's '~QBitArray()'. Naming it makes this a value class: Python owns
  #  every C++ QBitArray behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QBitArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QBitArray::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#size
    """
    #  qsizetype QBitArray::size() const
    return self.uglySide.call('ritual_ZNK9QBitArray4sizeEv')

  @overload()
  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QBitArray::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#count
    """
    #  qsizetype QBitArray::count() const
    return self.uglySide.call('ritual_ZNK9QBitArray5countEv')

  @overload(bool)
  def count(self, on: bool) -> int:
    """
    Calls Qt's 'qsizetype QBitArray::count(bool on) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#count

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  qsizetype QBitArray::count(bool on) const
    return self.uglySide.call('ritual_ZNK9QBitArray5countEb', on)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QBitArray::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#isEmpty
    """
    #  bool QBitArray::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QBitArray7isEmptyEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QBitArray::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#isNull
    """
    #  bool QBitArray::isNull() const
    return self.uglySide.call('ritual_ZNK9QBitArray6isNullEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QBitArray::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#isDetached
    """
    #  bool QBitArray::isDetached() const
    return self.uglySide.call('ritual_ZNK9QBitArray10isDetachedEv')

  @overload(int)
  def testBit(self, i: int) -> bool:
    """
    Calls Qt's 'bool QBitArray::testBit(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#testBit

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QBitArray::testBit(qsizetype i) const
    return self.uglySide.call('ritual_ZNK9QBitArray7testBitEx', i)

  @overload(int)
  def at(self, i: int) -> bool:
    """
    Calls Qt's 'bool QBitArray::at(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QBitArray::at(qsizetype i) const
    return self.uglySide.call('ritual_ZNK9QBitArray2atEx', i)

  def bits(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QBitArray::bits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#bits

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QBitArray::bits() const
    chars = self.uglySide.call('ritual_ZNK9QBitArray4bitsEv')
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBit(self, i: int) -> None:
    """
    Calls Qt's 'void QBitArray::setBit(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#setBit

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QBitArray::setBit(qsizetype i)
    self.uglySide.call('ritual_ZN9QBitArray6setBitEx', i)

  @overload(int, bool)
  def setBit(self, i: int, val: bool) -> None:
    """
    Calls Qt's 'void QBitArray::setBit(qsizetype i, bool val)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#setBit

    Parameters
    ----------

    i : int
      Passed on as it is.

    val : bool
      Passed on as it is.
    """
    #  void QBitArray::setBit(qsizetype i, bool val)
    self.uglySide.call('ritual_ZN9QBitArray6setBitExb', i, val)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __and__(self, a2: QBitArray) -> QBitArray:
    """
    Calls Qt's 'QBitArray operator&(const QBitArray &a1, const QBitArray
    &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator&

    Parameters
    ----------

    a2 : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray operator&(const QBitArray &a1, const QBitArray &a2)
    address = Rituals.call(
        'ritual_ZanRK9QBitArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a2),
    )
    return QBitArray._cuteOwning(address)

  @overload.fallback
  def __and__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __or__(self, a2: QBitArray) -> QBitArray:
    """
    Calls Qt's 'QBitArray operator|(const QBitArray &a1, const QBitArray
    &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator|

    Parameters
    ----------

    a2 : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray operator|(const QBitArray &a1, const QBitArray &a2)
    address = Rituals.call(
        'ritual_ZorRK9QBitArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a2),
    )
    return QBitArray._cuteOwning(address)

  @overload.fallback
  def __or__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __xor__(self, a2: QBitArray) -> QBitArray:
    """
    Calls Qt's 'QBitArray operator^(const QBitArray &a1, const QBitArray
    &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator^

    Parameters
    ----------

    a2 : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray operator^(const QBitArray &a1, const QBitArray &a2)
    address = Rituals.call(
        'ritual_ZeoRK9QBitArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a2),
    )
    return QBitArray._cuteOwning(address)

  @overload.fallback
  def __xor__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __invert__(self) -> QBitArray:
    """
    Calls Qt's 'QBitArray operator~(QBitArray a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator~

    Returns
    -------

    QBitArray
      A new cute QBitArray around the copy Qt gave back. Python owns it.
    """
    #  QBitArray operator~(QBitArray a)
    address = Rituals.call('ritual_Zco9QBitArray', CuteMixin._valueOf(self))
    return QBitArray._cuteOwning(address)

  @overload(int)
  def __getitem__(self, i: int) -> QBitRef:
    """
    Calls Qt's 'QBitRef QBitArray::operator[](qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QBitRef
      A new cute QBitRef around the copy Qt gave back. Python owns it.
    """
    #  QBitRef QBitArray::operator[](qsizetype i)
    address = self.uglySide.call('ritual_ZN9QBitArrayixEx', i)
    from . import QBitRef
    return QBitRef._cuteOwning(address)

  @overload(THIS)
  def __iand__(self, a0: QBitArray) -> QBitArray:
    """
    Calls Qt's 'QBitArray &QBitArray::operator&=(const QBitArray &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator&=

    Parameters
    ----------

    a0 : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  QBitArray &QBitArray::operator&=(const QBitArray &a0)
    self.uglySide.call('ritual_ZN9QBitArrayaNERKS_', self._valueOf(a0))
    return self

  @overload.fallback
  def __iand__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ior__(self, a0: QBitArray) -> QBitArray:
    """
    Calls Qt's 'QBitArray &QBitArray::operator|=(const QBitArray &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator|=

    Parameters
    ----------

    a0 : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  QBitArray &QBitArray::operator|=(const QBitArray &a0)
    self.uglySide.call('ritual_ZN9QBitArrayoRERKS_', self._valueOf(a0))
    return self

  @overload.fallback
  def __ior__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ixor__(self, a0: QBitArray) -> QBitArray:
    """
    Calls Qt's 'QBitArray &QBitArray::operator^=(const QBitArray &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator^=

    Parameters
    ----------

    a0 : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  QBitArray &QBitArray::operator^=(const QBitArray &a0)
    self.uglySide.call('ritual_ZN9QBitArrayeOERKS_', self._valueOf(a0))
    return self

  @overload.fallback
  def __ixor__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QBitArray) -> bool:
    """
    Calls Qt's 'bool operator==(const QBitArray &lhs, const QBitArray &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator==

    Parameters
    ----------

    rhs : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  bool operator==(const QBitArray &lhs, const QBitArray &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QBitArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QBitArray) -> bool:
    """
    Calls Qt's 'bool operator!=(const QBitArray &lhs, const QBitArray &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#operator!=

    Parameters
    ----------

    rhs : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  bool operator!=(const QBitArray &lhs, const QBitArray &rhs)
    return Rituals.call(
        'ritual_ZneRK9QBitArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's 'QBitArray::QBitArray()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#QBitArray
    """
    #  QBitArray::QBitArray()
    self._noteCreation(QBitArray, lambda: Rituals.call(
        'ritual_ZN9QBitArrayC1Ev',
    ))

  @overload(int)
  @overload(int, bool)
  def __init__(self, size: int, val: bool = False) -> None:
    """
    Notes what was given, for Qt's 'QBitArray::QBitArray(qsizetype size, bool
    val)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#QBitArray

    Parameters
    ----------

    size : int
      Passed on as it is.

    val : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QBitArray::QBitArray(qsizetype size, bool val)
    self._noteCreation(QBitArray, lambda: Rituals.call(
        'ritual_ZN9QBitArrayC1Exb', size, val,
    ))

  @overload(THIS)
  def __init__(self, other: QBitArray) -> None:
    """
    Notes what was given, for Qt's 'QBitArray::QBitArray(const QBitArray
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#QBitArray

    Parameters
    ----------

    other : QBitArray
      Passed on as a value: Qt reads the C++ QBitArray, which stays Python's
      own.
    """
    #  QBitArray::QBitArray(const QBitArray &other)
    self._noteCreation(QBitArray, lambda: Rituals.call(
        'ritual_ZN9QBitArrayC1ERKS_', self._valueOf(other),
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

  @overload(int)
  def resize(self, size: int) -> None:
    """
    Calls Qt's 'void QBitArray::resize(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#resize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QBitArray::resize(qsizetype size)
    self.uglySide.call('ritual_ZN9QBitArray6resizeEx', size)

  def detach(self) -> None:
    """
    Calls Qt's 'void QBitArray::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#detach
    """
    #  void QBitArray::detach()
    self.uglySide.call('ritual_ZN9QBitArray6detachEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QBitArray::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#clear
    """
    #  void QBitArray::clear()
    self.uglySide.call('ritual_ZN9QBitArray5clearEv')

  @overload(int)
  def clearBit(self, i: int) -> None:
    """
    Calls Qt's 'void QBitArray::clearBit(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#clearBit

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QBitArray::clearBit(qsizetype i)
    self.uglySide.call('ritual_ZN9QBitArray8clearBitEx', i)

  @overload(int)
  def toggleBit(self, i: int) -> bool:
    """
    Calls Qt's 'bool QBitArray::toggleBit(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#toggleBit

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QBitArray::toggleBit(qsizetype i)
    return self.uglySide.call('ritual_ZN9QBitArray9toggleBitEx', i)

  @overload(bool)
  @overload(bool, int)
  def fill(self, aval: bool, asize: int = -1) -> bool:
    """
    Calls Qt's 'bool QBitArray::fill(bool aval, qsizetype asize)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#fill

    Parameters
    ----------

    aval : bool
      Passed on as it is.

    asize : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QBitArray::fill(bool aval, qsizetype asize)
    return self.uglySide.call('ritual_ZN9QBitArray4fillEbx', aval, asize)

  @overload(bool, int, int)
  def fill(self, val: bool, first: int, last: int) -> None:
    """
    Calls Qt's 'void QBitArray::fill(bool val, qsizetype first, qsizetype
    last)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#fill

    Parameters
    ----------

    val : bool
      Passed on as it is.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QBitArray::fill(bool val, qsizetype first, qsizetype last)
    self.uglySide.call('ritual_ZN9QBitArray4fillEbxx', val, first, last)

  @overload(int)
  def truncate(self, pos: int) -> None:
    """
    Calls Qt's 'void QBitArray::truncate(qsizetype pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qbitarray.html#truncate

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QBitArray::truncate(qsizetype pos)
    self.uglySide.call('ritual_ZN9QBitArray8truncateEx', pos)
