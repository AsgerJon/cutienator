"""
QMargins binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmargins.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMarginsF


class QMargins(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMargins: a plain Python object standing in front of
  one C++ QMargins.

  C++ hands a QMargins around as a copy, so every C++ QMargins behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMargins that has a ritual and that Python can call
  so far, 23 names in all: 'isNull', 'left', 'top', 'right', 'bottom',
  'setLeft', 'setTop', 'setRight', 'setBottom', '__iadd__', '__isub__',
  '__imul__', '__itruediv__', 'toMarginsF', '__add__', '__sub__', '__radd__',
  '__mul__', '__rmul__', '__truediv__', '__or__', '__eq__', '__ne__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMargins::~QMargins()': the destructor: Python removes its C++
    QMargins by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 36 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QMargins is created at the first use, not by 'QMargins(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMargins back gives a copy the ritual made for
    Python, in a new cute QMargins.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMargins'

  #  Qt's '~QMargins()'. Naming it makes this a value class: Python owns
  #  every C++ QMargins behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QMarginsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QMargins::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#isNull
    """
    #  bool QMargins::isNull() const
    return self.uglySide.call('ritual_ZNK8QMargins6isNullEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QMargins::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#left
    """
    #  int QMargins::left() const
    return self.uglySide.call('ritual_ZNK8QMargins4leftEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QMargins::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#top
    """
    #  int QMargins::top() const
    return self.uglySide.call('ritual_ZNK8QMargins3topEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QMargins::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#right
    """
    #  int QMargins::right() const
    return self.uglySide.call('ritual_ZNK8QMargins5rightEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QMargins::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#bottom
    """
    #  int QMargins::bottom() const
    return self.uglySide.call('ritual_ZNK8QMargins6bottomEv')

  def toMarginsF(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QMargins::toMarginsF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#toMarginsF

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QMargins::toMarginsF() const
    address = self.uglySide.call('ritual_ZNK8QMargins10toMarginsFEv')
    from . import QMarginsF
    return QMarginsF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLeft(self, left: int) -> None:
    """
    Calls Qt's 'void QMargins::setLeft(int left)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setLeft

    Parameters
    ----------

    left : int
      Passed on as it is.
    """
    #  void QMargins::setLeft(int left)
    self.uglySide.call('ritual_ZN8QMargins7setLeftEi', left)

  @overload(int)
  def setTop(self, top: int) -> None:
    """
    Calls Qt's 'void QMargins::setTop(int top)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setTop

    Parameters
    ----------

    top : int
      Passed on as it is.
    """
    #  void QMargins::setTop(int top)
    self.uglySide.call('ritual_ZN8QMargins6setTopEi', top)

  @overload(int)
  def setRight(self, right: int) -> None:
    """
    Calls Qt's 'void QMargins::setRight(int right)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setRight

    Parameters
    ----------

    right : int
      Passed on as it is.
    """
    #  void QMargins::setRight(int right)
    self.uglySide.call('ritual_ZN8QMargins8setRightEi', right)

  @overload(int)
  def setBottom(self, bottom: int) -> None:
    """
    Calls Qt's 'void QMargins::setBottom(int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#setBottom

    Parameters
    ----------

    bottom : int
      Passed on as it is.
    """
    #  void QMargins::setBottom(int bottom)
    self.uglySide.call('ritual_ZN8QMargins9setBottomEi', bottom)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __iadd__(self, margins: QMargins) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator+=(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator+=

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QMargins &QMargins::operator+=(const QMargins &margins)
    self.uglySide.call('ritual_ZN8QMarginspLERKS_', self._valueOf(margins))
    return self

  @overload(int)
  def __iadd__(self, a0: int) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator+=(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator+=

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QMargins &QMargins::operator+=(int a0)
    self.uglySide.call('ritual_ZN8QMarginspLEi', a0)
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __isub__(self, margins: QMargins) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator-=(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator-=

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QMargins &QMargins::operator-=(const QMargins &margins)
    self.uglySide.call('ritual_ZN8QMarginsmIERKS_', self._valueOf(margins))
    return self

  @overload(int)
  def __isub__(self, a0: int) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator-=(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator-=

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QMargins &QMargins::operator-=(int a0)
    self.uglySide.call('ritual_ZN8QMarginsmIEi', a0)
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __imul__(self, a0: int) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator*=(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator*=

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QMargins &QMargins::operator*=(int a0)
    self.uglySide.call('ritual_ZN8QMarginsmLEi', a0)
    return self

  @overload(float)
  def __imul__(self, a0: float) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator*=(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator*=

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  QMargins &QMargins::operator*=(qreal a0)
    self.uglySide.call('ritual_ZN8QMarginsmLEd', a0)
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
  def __itruediv__(self, a0: int) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator/=(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator/=

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QMargins &QMargins::operator/=(int a0)
    self.uglySide.call('ritual_ZN8QMarginsdVEi', a0)
    return self

  @overload(float)
  def __itruediv__(self, a0: float) -> QMargins:
    """
    Calls Qt's 'QMargins &QMargins::operator/=(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator/=

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  QMargins &QMargins::operator/=(qreal a0)
    self.uglySide.call('ritual_ZN8QMarginsdVEd', a0)
    return self

  @overload.fallback
  def __itruediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __add__(self, m2: QMargins) -> QMargins:
    """
    Calls Qt's 'QMargins operator+(const QMargins &m1, const QMargins &m2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator+

    Parameters
    ----------

    m2 : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator+(const QMargins &m1, const QMargins &m2)
    address = Rituals.call(
        'ritual_ZplRK8QMarginsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(m2),
    )
    return QMargins._cuteOwning(address)

  @overload(int)
  def __add__(self, rhs: int) -> QMargins:
    """
    Calls Qt's 'QMargins operator+(const QMargins &lhs, int rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator+

    Parameters
    ----------

    rhs : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator+(const QMargins &lhs, int rhs)
    address = Rituals.call(
        'ritual_ZplRK8QMarginsi', CuteMixin._valueOf(self), rhs,
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, m2: QMargins) -> QMargins:
    """
    Calls Qt's 'QMargins operator-(const QMargins &m1, const QMargins &m2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator-

    Parameters
    ----------

    m2 : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator-(const QMargins &m1, const QMargins &m2)
    address = Rituals.call(
        'ritual_ZmiRK8QMarginsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(m2),
    )
    return QMargins._cuteOwning(address)

  @overload(int)
  def __sub__(self, rhs: int) -> QMargins:
    """
    Calls Qt's 'QMargins operator-(const QMargins &lhs, int rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator-

    Parameters
    ----------

    rhs : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator-(const QMargins &lhs, int rhs)
    address = Rituals.call(
        'ritual_ZmiRK8QMarginsi', CuteMixin._valueOf(self), rhs,
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __radd__(self, lhs: int) -> QMargins:
    """
    Calls Qt's 'QMargins operator+(int lhs, const QMargins &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator+

    Parameters
    ----------

    lhs : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator+(int lhs, const QMargins &rhs)
    address = Rituals.call(
        'ritual_ZpliRK8QMargins', lhs, CuteMixin._valueOf(self),
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __radd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __mul__(self, factor: int) -> QMargins:
    """
    Calls Qt's 'QMargins operator*(const QMargins &margins, int factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator*

    Parameters
    ----------

    factor : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator*(const QMargins &margins, int factor)
    address = Rituals.call(
        'ritual_ZmlRK8QMarginsi', CuteMixin._valueOf(self), factor,
    )
    return QMargins._cuteOwning(address)

  @overload(float)
  def __mul__(self, factor: float) -> QMargins:
    """
    Calls Qt's 'QMargins operator*(const QMargins &margins, qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator*(const QMargins &margins, qreal factor)
    address = Rituals.call(
        'ritual_ZmlRK8QMarginsd', CuteMixin._valueOf(self), factor,
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __rmul__(self, factor: int) -> QMargins:
    """
    Calls Qt's 'QMargins operator*(int factor, const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator*

    Parameters
    ----------

    factor : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator*(int factor, const QMargins &margins)
    address = Rituals.call(
        'ritual_ZmliRK8QMargins', factor, CuteMixin._valueOf(self),
    )
    return QMargins._cuteOwning(address)

  @overload(float)
  def __rmul__(self, factor: float) -> QMargins:
    """
    Calls Qt's 'QMargins operator*(qreal factor, const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator*(qreal factor, const QMargins &margins)
    address = Rituals.call(
        'ritual_ZmldRK8QMargins', factor, CuteMixin._valueOf(self),
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __truediv__(self, divisor: int) -> QMargins:
    """
    Calls Qt's 'QMargins operator/(const QMargins &margins, int divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator/

    Parameters
    ----------

    divisor : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator/(const QMargins &margins, int divisor)
    address = Rituals.call(
        'ritual_ZdvRK8QMarginsi', CuteMixin._valueOf(self), divisor,
    )
    return QMargins._cuteOwning(address)

  @overload(float)
  def __truediv__(self, divisor: float) -> QMargins:
    """
    Calls Qt's 'QMargins operator/(const QMargins &margins, qreal divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator/

    Parameters
    ----------

    divisor : float
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator/(const QMargins &margins, qreal divisor)
    address = Rituals.call(
        'ritual_ZdvRK8QMarginsd', CuteMixin._valueOf(self), divisor,
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __or__(self, m2: QMargins) -> QMargins:
    """
    Calls Qt's 'QMargins operator|(const QMargins &m1, const QMargins &m2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator|

    Parameters
    ----------

    m2 : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins operator|(const QMargins &m1, const QMargins &m2)
    address = Rituals.call(
        'ritual_ZorRK8QMarginsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(m2),
    )
    return QMargins._cuteOwning(address)

  @overload.fallback
  def __or__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QMargins) -> bool:
    """
    Calls Qt's 'bool operator==(const QMargins &lhs, const QMargins &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator==

    Parameters
    ----------

    rhs : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  bool operator==(const QMargins &lhs, const QMargins &rhs)
    return Rituals.call(
        'ritual_ZeqRK8QMarginsS1_',
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
  def __ne__(self, rhs: QMargins) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMargins &lhs, const QMargins &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#operator!=

    Parameters
    ----------

    rhs : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  bool operator!=(const QMargins &lhs, const QMargins &rhs)
    return Rituals.call(
        'ritual_ZneRK8QMarginsS1_',
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
    Notes what was given, for Qt's 'QMargins::QMargins()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#QMargins
    """
    #  QMargins::QMargins()
    self._noteCreation(QMargins, lambda: Rituals.call(
        'ritual_ZN8QMarginsC1Ev',
    ))

  @overload(int, int, int, int)
  def __init__(self, left: int, top: int, right: int, bottom: int) -> None:
    """
    Notes what was given, for Qt's 'QMargins::QMargins(int left, int top, int
    right, int bottom)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmargins.html#QMargins

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    right : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  QMargins::QMargins(int left, int top, int right, int bottom)
    self._noteCreation(QMargins, lambda: Rituals.call(
        'ritual_ZN8QMarginsC1Eiiii', left, top, right, bottom,
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
