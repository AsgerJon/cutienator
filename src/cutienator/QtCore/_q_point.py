"""
QPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qpoint.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QPointF


class QPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPoint: a plain Python object standing in front of
  one C++ QPoint.

  C++ hands a QPoint around as a copy, so every C++ QPoint behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPoint that has a ritual and that Python can call so
  far, 22 names in all: 'isNull', 'x', 'y', 'setX', 'setY',
  'manhattanLength', 'transposed', '__iadd__', '__isub__', '__imul__',
  '__itruediv__', 'dotProduct', '__eq__', '__ne__', '__add__', '__sub__',
  '__mul__', '__rmul__', '__pos__', '__neg__', '__truediv__', 'toPointF'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPoint &QPoint::operator*=(double factor)': takes in Python what
    'QPoint &QPoint::operator*=(float factor)' takes.
  - Qt's 'QPoint operator*(const QPoint &p, double factor)': takes in Python
    what 'QPoint operator*(const QPoint &p, float factor)' takes.
  - Qt's 'QPoint operator*(double factor, const QPoint &p)': takes in Python
    what 'QPoint operator*(float factor, const QPoint &p)' takes.
  - Qt's 'QPoint::QPoint(Representation xpos, Representation ypos)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPoint::~QPoint()': the destructor: Python removes its C++ QPoint
    by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPoint is created at the first use, not by 'QPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPoint back gives a copy the ritual made for Python,
    in a new cute QPoint.
  - Each name of Qt's QPoint that has no cute function yet, 'rx', 'ry', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(p1: QPoint, p2: QPoint) -> int:
    """
    Calls Qt's 'int QPoint::dotProduct(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#dotProduct

    Parameters
    ----------

    p1 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QPoint::dotProduct(const QPoint &p1, const QPoint &p2)
    return Rituals.call(
        'ritual_ZN6QPoint10dotProductERKS_S1_',
        CuteMixin._valueOf(p1), CuteMixin._valueOf(p2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPoint'

  #  Qt's '~QPoint()'. Naming it makes this a value class: Python owns every
  #  C++ QPoint behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QPointD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPoint::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#isNull
    """
    #  bool QPoint::isNull() const
    return self.uglySide.call('ritual_ZNK6QPoint6isNullEv')

  def x(self) -> int:
    """
    Calls Qt's 'int QPoint::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#x
    """
    #  int QPoint::x() const
    return self.uglySide.call('ritual_ZNK6QPoint1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QPoint::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#y
    """
    #  int QPoint::y() const
    return self.uglySide.call('ritual_ZNK6QPoint1yEv')

  def manhattanLength(self) -> int:
    """
    Calls Qt's 'int QPoint::manhattanLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#manhattanLength
    """
    #  int QPoint::manhattanLength() const
    return self.uglySide.call('ritual_ZNK6QPoint15manhattanLengthEv')

  def transposed(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPoint::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#transposed

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPoint::transposed() const
    address = self.uglySide.call('ritual_ZNK6QPoint10transposedEv')
    return QPoint._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPoint::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPoint::toPointF() const
    address = self.uglySide.call('ritual_ZNK6QPoint8toPointFEv')
    from . import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setX(self, x: int) -> None:
    """
    Calls Qt's 'void QPoint::setX(int x)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#setX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  void QPoint::setX(int x)
    self.uglySide.call('ritual_ZN6QPoint4setXEi', x)

  @overload(int)
  def setY(self, y: int) -> None:
    """
    Calls Qt's 'void QPoint::setY(int y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#setY

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  void QPoint::setY(int y)
    self.uglySide.call('ritual_ZN6QPoint4setYEi', y)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __iadd__(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint &QPoint::operator+=(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator+=

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QPoint &QPoint::operator+=(const QPoint &p)
    self.uglySide.call('ritual_ZN6QPointpLERKS_', self._valueOf(p))
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
  def __isub__(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint &QPoint::operator-=(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator-=

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QPoint &QPoint::operator-=(const QPoint &p)
    self.uglySide.call('ritual_ZN6QPointmIERKS_', self._valueOf(p))
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __imul__(self, factor: float) -> QPoint:
    """
    Calls Qt's 'QPoint &QPoint::operator*=(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator*=

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  QPoint &QPoint::operator*=(float factor)
    self.uglySide.call('ritual_ZN6QPointmLEf', factor)
    return self

  @overload(int)
  def __imul__(self, factor: int) -> QPoint:
    """
    Calls Qt's 'QPoint &QPoint::operator*=(int factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator*=

    Parameters
    ----------

    factor : int
      Passed on as it is.
    """
    #  QPoint &QPoint::operator*=(int factor)
    self.uglySide.call('ritual_ZN6QPointmLEi', factor)
    return self

  @overload.fallback
  def __imul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __itruediv__(self, divisor: float) -> QPoint:
    """
    Calls Qt's 'QPoint &QPoint::operator/=(qreal divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator/=

    Parameters
    ----------

    divisor : float
      Passed on as it is.
    """
    #  QPoint &QPoint::operator/=(qreal divisor)
    self.uglySide.call('ritual_ZN6QPointdVEd', divisor)
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
  def __eq__(self, rhs: QPoint) -> bool:
    """
    Calls Qt's 'bool operator==(const QPoint &lhs, const QPoint &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator==

    Parameters
    ----------

    rhs : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool operator==(const QPoint &lhs, const QPoint &rhs)
    return Rituals.call(
        'ritual_ZeqRK6QPointS1_',
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
  def __ne__(self, rhs: QPoint) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPoint &lhs, const QPoint &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator!=

    Parameters
    ----------

    rhs : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool operator!=(const QPoint &lhs, const QPoint &rhs)
    return Rituals.call(
        'ritual_ZneRK6QPointS1_',
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
  def __add__(self, p2: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint operator+(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator+

    Parameters
    ----------

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator+(const QPoint &p1, const QPoint &p2)
    address = Rituals.call(
        'ritual_ZplRK6QPointS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(p2),
    )
    return QPoint._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, p2: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint operator-(const QPoint &p1, const QPoint &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator-

    Parameters
    ----------

    p2 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator-(const QPoint &p1, const QPoint &p2)
    address = Rituals.call(
        'ritual_ZmiRK6QPointS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(p2),
    )
    return QPoint._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __mul__(self, factor: float) -> QPoint:
    """
    Calls Qt's 'QPoint operator*(const QPoint &p, float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator*(const QPoint &p, float factor)
    address = Rituals.call(
        'ritual_ZmlRK6QPointf', CuteMixin._valueOf(self), factor,
    )
    return QPoint._cuteOwning(address)

  @overload(int)
  def __mul__(self, factor: int) -> QPoint:
    """
    Calls Qt's 'QPoint operator*(const QPoint &p, int factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator*

    Parameters
    ----------

    factor : int
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator*(const QPoint &p, int factor)
    address = Rituals.call(
        'ritual_ZmlRK6QPointi', CuteMixin._valueOf(self), factor,
    )
    return QPoint._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, factor: float) -> QPoint:
    """
    Calls Qt's 'QPoint operator*(float factor, const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator*(float factor, const QPoint &p)
    address = Rituals.call(
        'ritual_ZmlfRK6QPoint', factor, CuteMixin._valueOf(self),
    )
    return QPoint._cuteOwning(address)

  @overload(int)
  def __rmul__(self, factor: int) -> QPoint:
    """
    Calls Qt's 'QPoint operator*(int factor, const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator*

    Parameters
    ----------

    factor : int
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator*(int factor, const QPoint &p)
    address = Rituals.call(
        'ritual_ZmliRK6QPoint', factor, CuteMixin._valueOf(self),
    )
    return QPoint._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __pos__(self) -> QPoint:
    """
    Calls Qt's 'QPoint operator+(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator+

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator+(const QPoint &p)
    address = Rituals.call('ritual_ZpsRK6QPoint', CuteMixin._valueOf(self))
    return QPoint._cuteOwning(address)

  def __neg__(self) -> QPoint:
    """
    Calls Qt's 'QPoint operator-(const QPoint &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator-

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator-(const QPoint &p)
    address = Rituals.call('ritual_ZngRK6QPoint', CuteMixin._valueOf(self))
    return QPoint._cuteOwning(address)

  @overload(float)
  def __truediv__(self, c: float) -> QPoint:
    """
    Calls Qt's 'QPoint operator/(const QPoint &p, qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#operator/

    Parameters
    ----------

    c : float
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator/(const QPoint &p, qreal c)
    address = Rituals.call(
        'ritual_ZdvRK6QPointd', CuteMixin._valueOf(self), c,
    )
    return QPoint._cuteOwning(address)

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QPoint::QPoint()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#QPoint
    """
    #  QPoint::QPoint()
    self._noteCreation(QPoint, lambda: Rituals.call('ritual_ZN6QPointC1Ev'))

  @overload(int, int)
  def __init__(self, xpos: int, ypos: int) -> None:
    """
    Notes what was given, for Qt's 'QPoint::QPoint(int xpos, int ypos)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpoint.html#QPoint

    Parameters
    ----------

    xpos : int
      Passed on as it is.

    ypos : int
      Passed on as it is.
    """
    #  QPoint::QPoint(int xpos, int ypos)
    self._noteCreation(QPoint, lambda: Rituals.call(
        'ritual_ZN6QPointC1Eii', xpos, ypos,
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

  @staticmethod
  def rx(*__, **_) -> Never:
    """
    Qt's 'int &QPoint::rx()': takes or gives a type that cannot be passed
    yet: int &.
    """
    raise NotImplementedError(
        "'QPoint.rx' has no cute function yet. Qt's 'int &QPoint::rx()': "
        "takes or gives a type that cannot be passed yet: int &.")

  @staticmethod
  def ry(*__, **_) -> Never:
    """
    Qt's 'int &QPoint::ry()': takes or gives a type that cannot be passed
    yet: int &.
    """
    raise NotImplementedError(
        "'QPoint.ry' has no cute function yet. Qt's 'int &QPoint::ry()': "
        "takes or gives a type that cannot be passed yet: int &.")


#  Qt's 'QList<QPoint>': the list of QPoint, which 'QList[QPoint]' gives. It
#  is made here, so that there is one as soon as there can be a QPoint.
QList.createKind(
    QPoint, 'value',
    make='ritual_list_make_QPoint',
    add='ritual_list_add_QPoint',
    size='ritual_list_size_QPoint',
    at='ritual_list_at_QPoint',
    drop='ritual_list_drop_QPoint',
)
