"""
QFixed binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfixed_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFixed to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QFixed(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFixed: a plain Python object standing in front of
  one C++ QFixed.

  C++ hands a QFixed around as a copy, so every C++ QFixed behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFixed that has a ritual and that Python can call so
  far, 26 names in all: 'fromReal', 'fromFixed', 'value', 'setValue',
  'toInt', 'toReal', 'truncate', 'round', 'floor', 'ceil', '__add__',
  '__iadd__', '__sub__', '__isub__', '__neg__', '__eq__', '__ne__', '__lt__',
  '__gt__', '__le__', '__ge__', '__itruediv__', '__truediv__', '__rshift__',
  '__imul__', '__mul__'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFixed::QFixed(long i)': takes in Python what 'QFixed::QFixed(int
    i)' takes.
  - Qt's 'QFixed::QFixed(long long i)': takes in Python what
    'QFixed::QFixed(int i)' takes.
  - Qt's 'QFixed QFixed::operator+(uint i) const': takes in Python what
    'QFixed QFixed::operator+(int i) const' takes.
  - Qt's 'QFixed &QFixed::operator+=(uint i)': takes in Python what 'QFixed
    &QFixed::operator+=(int i)' takes.
  - Qt's 'QFixed QFixed::operator-(uint i) const': takes in Python what
    'QFixed QFixed::operator-(int i) const' takes.
  - Qt's 'QFixed &QFixed::operator-=(uint i)': takes in Python what 'QFixed
    &QFixed::operator-=(int i)' takes.
  - Qt's 'bool QFixed::operator!() const': an operator Python has no name
    for.
  - Qt's 'QFixed &QFixed::operator*=(uint i)': takes in Python what 'QFixed
    &QFixed::operator*=(int i)' takes.
  - Qt's 'QFixed QFixed::operator*(uint i) const': takes in Python what
    'QFixed QFixed::operator*(int i) const' takes.
  - Qt's 'QFixed::~QFixed()': the destructor: Python removes its C++ QFixed
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QFixed is created at the first use, not by 'QFixed(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFixed back gives a copy the ritual made for Python,
    in a new cute QFixed.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float)
  def fromReal(r: float) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::fromReal(qreal r)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#fromReal

    Parameters
    ----------

    r : float
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::fromReal(qreal r)
    address = Rituals.call('ritual_ZN6QFixed8fromRealEd', r)
    return QFixed._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromFixed(fixed: int) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::fromFixed(int fixed)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#fromFixed

    Parameters
    ----------

    fixed : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::fromFixed(int fixed)
    address = Rituals.call('ritual_ZN6QFixed9fromFixedEi', fixed)
    return QFixed._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFixed'

  #  Qt's '~QFixed()'. Naming it makes this a value class: Python owns every
  #  C++ QFixed behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QFixedD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> int:
    """
    Calls Qt's 'int QFixed::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#value
    """
    #  int QFixed::value() const
    return self.uglySide.call('ritual_ZNK6QFixed5valueEv')

  def toInt(self) -> int:
    """
    Calls Qt's 'int QFixed::toInt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#toInt
    """
    #  int QFixed::toInt() const
    return self.uglySide.call('ritual_ZNK6QFixed5toIntEv')

  def toReal(self) -> float:
    """
    Calls Qt's 'qreal QFixed::toReal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#toReal
    """
    #  qreal QFixed::toReal() const
    return self.uglySide.call('ritual_ZNK6QFixed6toRealEv')

  def truncate(self) -> int:
    """
    Calls Qt's 'int QFixed::truncate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#truncate
    """
    #  int QFixed::truncate() const
    return self.uglySide.call('ritual_ZNK6QFixed8truncateEv')

  def round(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::round() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#round

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::round() const
    address = self.uglySide.call('ritual_ZNK6QFixed5roundEv')
    return QFixed._cuteOwning(address)

  def floor(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::floor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#floor

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::floor() const
    address = self.uglySide.call('ritual_ZNK6QFixed5floorEv')
    return QFixed._cuteOwning(address)

  def ceil(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::ceil() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#ceil

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::ceil() const
    address = self.uglySide.call('ritual_ZNK6QFixed4ceilEv')
    return QFixed._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setValue(self, value: int) -> None:
    """
    Calls Qt's 'void QFixed::setValue(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#setValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QFixed::setValue(int value)
    self.uglySide.call('ritual_ZN6QFixed8setValueEi', value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __add__(self, i: int) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator+(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator+

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator+(int i) const
    address = self.uglySide.call('ritual_ZNK6QFixedplEi', i)
    return QFixed._cuteOwning(address)

  @overload(THIS)
  def __add__(self, other: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator+(QFixed other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator+

    Parameters
    ----------

    other : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator+(QFixed other) const
    address = self.uglySide.call(
        'ritual_ZNK6QFixedplES_', self._valueOf(other),
    )
    return QFixed._cuteOwning(address)

  @overload(float)
  def __add__(self, i: float) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator+(qreal i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator+

    Parameters
    ----------

    i : float
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator+(qreal i) const
    address = self.uglySide.call('ritual_ZNK6QFixedplEd', i)
    return QFixed._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __iadd__(self, i: int) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator+=(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator+=

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QFixed &QFixed::operator+=(int i)
    self.uglySide.call('ritual_ZN6QFixedpLEi', i)
    return self

  @overload(THIS)
  def __iadd__(self, other: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator+=(QFixed other)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator+=

    Parameters
    ----------

    other : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  QFixed &QFixed::operator+=(QFixed other)
    self.uglySide.call('ritual_ZN6QFixedpLES_', self._valueOf(other))
    return self

  @overload(float)
  def __iadd__(self, i: float) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator+=(qreal i)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator+=

    Parameters
    ----------

    i : float
      Passed on as it is.
    """
    #  QFixed &QFixed::operator+=(qreal i)
    self.uglySide.call('ritual_ZN6QFixedpLEd', i)
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __sub__(self, i: int) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator-(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator-(int i) const
    address = self.uglySide.call('ritual_ZNK6QFixedmiEi', i)
    return QFixed._cuteOwning(address)

  @overload(THIS)
  def __sub__(self, other: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator-(QFixed other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-

    Parameters
    ----------

    other : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator-(QFixed other) const
    address = self.uglySide.call(
        'ritual_ZNK6QFixedmiES_', self._valueOf(other),
    )
    return QFixed._cuteOwning(address)

  @overload(float)
  def __sub__(self, i: float) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator-(qreal i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-

    Parameters
    ----------

    i : float
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator-(qreal i) const
    address = self.uglySide.call('ritual_ZNK6QFixedmiEd', i)
    return QFixed._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __isub__(self, i: int) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator-=(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-=

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QFixed &QFixed::operator-=(int i)
    self.uglySide.call('ritual_ZN6QFixedmIEi', i)
    return self

  @overload(THIS)
  def __isub__(self, other: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator-=(QFixed other)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-=

    Parameters
    ----------

    other : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  QFixed &QFixed::operator-=(QFixed other)
    self.uglySide.call('ritual_ZN6QFixedmIES_', self._valueOf(other))
    return self

  @overload(float)
  def __isub__(self, i: float) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator-=(qreal i)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-=

    Parameters
    ----------

    i : float
      Passed on as it is.
    """
    #  QFixed &QFixed::operator-=(qreal i)
    self.uglySide.call('ritual_ZN6QFixedmIEd', i)
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __neg__(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator-() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator-

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator-() const
    address = self.uglySide.call('ritual_ZNK6QFixedngEv')
    return QFixed._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QFixed) -> bool:
    """
    Calls Qt's 'bool operator==(QFixed lhs, QFixed rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator==

    Parameters
    ----------

    rhs : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  bool operator==(QFixed lhs, QFixed rhs)
    return Rituals.call(
        'ritual_Zeq6QFixedS_',
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
  def __ne__(self, rhs: QFixed) -> bool:
    """
    Calls Qt's 'bool operator!=(QFixed lhs, QFixed rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator!=

    Parameters
    ----------

    rhs : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  bool operator!=(QFixed lhs, QFixed rhs)
    return Rituals.call(
        'ritual_Zne6QFixedS_',
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

  @overload(THIS)
  def __lt__(self, rhs: QFixed) -> bool:
    """
    Calls Qt's 'bool operator<(QFixed lhs, QFixed rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator<

    Parameters
    ----------

    rhs : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  bool operator<(QFixed lhs, QFixed rhs)
    return Rituals.call(
        'ritual_Zlt6QFixedS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __gt__(self, rhs: QFixed) -> bool:
    """
    Calls Qt's 'bool operator>(QFixed lhs, QFixed rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator>

    Parameters
    ----------

    rhs : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  bool operator>(QFixed lhs, QFixed rhs)
    return Rituals.call(
        'ritual_Zgt6QFixedS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QFixed) -> bool:
    """
    Calls Qt's 'bool operator<=(QFixed lhs, QFixed rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator<=

    Parameters
    ----------

    rhs : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  bool operator<=(QFixed lhs, QFixed rhs)
    return Rituals.call(
        'ritual_Zle6QFixedS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QFixed) -> bool:
    """
    Calls Qt's 'bool operator>=(QFixed lhs, QFixed rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator>=

    Parameters
    ----------

    rhs : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  bool operator>=(QFixed lhs, QFixed rhs)
    return Rituals.call(
        'ritual_Zge6QFixedS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __itruediv__(self, x: int) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator/=(int x)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator/=

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  QFixed &QFixed::operator/=(int x)
    self.uglySide.call('ritual_ZN6QFixeddVEi', x)
    return self

  @overload(THIS)
  def __itruediv__(self, o: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator/=(QFixed o)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator/=

    Parameters
    ----------

    o : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  QFixed &QFixed::operator/=(QFixed o)
    self.uglySide.call('ritual_ZN6QFixeddVES_', self._valueOf(o))
    return self

  @overload(float)
  def __itruediv__(self, r: float) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator/=(qreal r)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator/=

    Parameters
    ----------

    r : float
      Passed on as it is.
    """
    #  QFixed &QFixed::operator/=(qreal r)
    self.uglySide.call('ritual_ZN6QFixeddVEd', r)
    return self

  @overload.fallback
  def __itruediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __truediv__(self, d: int) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator/(int d) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator/

    Parameters
    ----------

    d : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator/(int d) const
    address = self.uglySide.call('ritual_ZNK6QFixeddvEi', d)
    return QFixed._cuteOwning(address)

  @overload(THIS)
  def __truediv__(self, b: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator/(QFixed b) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator/

    Parameters
    ----------

    b : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator/(QFixed b) const
    address = self.uglySide.call('ritual_ZNK6QFixeddvES_', self._valueOf(b))
    return QFixed._cuteOwning(address)

  @overload(float)
  def __truediv__(self, d: float) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator/(qreal d) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator/

    Parameters
    ----------

    d : float
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator/(qreal d) const
    address = self.uglySide.call('ritual_ZNK6QFixeddvEd', d)
    return QFixed._cuteOwning(address)

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __rshift__(self, d: int) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator>>(int d) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator>>

    Parameters
    ----------

    d : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator>>(int d) const
    address = self.uglySide.call('ritual_ZNK6QFixedrsEi', d)
    return QFixed._cuteOwning(address)

  @overload.fallback
  def __rshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __imul__(self, i: int) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator*=(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator*=

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QFixed &QFixed::operator*=(int i)
    self.uglySide.call('ritual_ZN6QFixedmLEi', i)
    return self

  @overload(THIS)
  def __imul__(self, o: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator*=(QFixed o)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator*=

    Parameters
    ----------

    o : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  QFixed &QFixed::operator*=(QFixed o)
    self.uglySide.call('ritual_ZN6QFixedmLES_', self._valueOf(o))
    return self

  @overload(float)
  def __imul__(self, d: float) -> QFixed:
    """
    Calls Qt's 'QFixed &QFixed::operator*=(qreal d)'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator*=

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  QFixed &QFixed::operator*=(qreal d)
    self.uglySide.call('ritual_ZN6QFixedmLEd', d)
    return self

  @overload.fallback
  def __imul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __mul__(self, i: int) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator*(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator*

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator*(int i) const
    address = self.uglySide.call('ritual_ZNK6QFixedmlEi', i)
    return QFixed._cuteOwning(address)

  @overload(THIS)
  def __mul__(self, o: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator*(QFixed o) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator*

    Parameters
    ----------

    o : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator*(QFixed o) const
    address = self.uglySide.call('ritual_ZNK6QFixedmlES_', self._valueOf(o))
    return QFixed._cuteOwning(address)

  @overload(float)
  def __mul__(self, d: float) -> QFixed:
    """
    Calls Qt's 'QFixed QFixed::operator*(qreal d) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#operator*

    Parameters
    ----------

    d : float
      Passed on as it is.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFixed::operator*(qreal d) const
    address = self.uglySide.call('ritual_ZNK6QFixedmlEd', d)
    return QFixed._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def __init__(self, val: int, a1: int) -> None:
    """
    Notes what was given, for Qt's 'QFixed::QFixed(int val, int a1)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#QFixed

    Parameters
    ----------

    val : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  QFixed::QFixed(int val, int a1)
    self._noteCreation(QFixed, lambda: Rituals.call(
        'ritual_ZN6QFixedC1Eii', val, a1,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFixed::QFixed()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#QFixed
    """
    #  QFixed::QFixed()
    self._noteCreation(QFixed, lambda: Rituals.call('ritual_ZN6QFixedC1Ev'))

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's 'QFixed::QFixed(int i)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#QFixed

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  QFixed::QFixed(int i)
    self._noteCreation(QFixed, lambda: Rituals.call(
        'ritual_ZN6QFixedC1Ei', i,
    ))

  @overload(float)
  def __init__(self, i: float) -> None:
    """
    Notes what was given, for Qt's 'QFixed::QFixed(qreal i)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfixed.html#QFixed

    Parameters
    ----------

    i : float
      Passed on as it is.
    """
    #  QFixed::QFixed(qreal i)
    self._noteCreation(QFixed, lambda: Rituals.call(
        'ritual_ZN6QFixedC1Ed', i,
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
