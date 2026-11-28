"""
QPointF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qpoint.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QPointF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPointF: a plain Python object standing in front of
  one C++ QPointF.

  C++ hands a QPointF around as a copy, so every C++ QPointF behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPointF that has a ritual and that Python can call
  so far, 22 names in all: 'manhattanLength', 'isNull', 'x', 'y', 'setX',
  'setY', 'transposed', '__iadd__', '__isub__', '__imul__', '__itruediv__',
  'dotProduct', '__eq__', '__ne__', '__add__', '__sub__', '__mul__',
  '__rmul__', '__pos__', '__neg__', '__truediv__', 'toPoint'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool operator==(const QPoint &lhs, const QPointF &rhs)': takes in
    Python what 'bool operator==(const QPointF &lhs, const QPoint &rhs)'
    takes.
  - Qt's 'bool operator!=(const QPoint &lhs, const QPointF &rhs)': takes in
    Python what 'bool operator!=(const QPointF &lhs, const QPoint &rhs)'
    takes.
  - Qt's 'QPointF::~QPointF()': the destructor: Python removes its C++
    QPointF by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QPointF is created at the first use, not by 'QPointF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPointF back gives a copy the ritual made for Python,
    in a new cute QPointF.
  - Each name of Qt's QPointF that has no cute function yet, 'rx', 'ry',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(p1: QPointF, p2: QPointF) -> float:
    """
    Calls Qt's 'qreal QPointF::dotProduct(const QPointF &p1, const QPointF
    &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#dotProduct

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  qreal QPointF::dotProduct(const QPointF &p1, const QPointF &p2)
    return Rituals.call(
        'ritual_ZN7QPointF10dotProductERKS_S1_',
        CuteMixin._valueOf(p1, 'QPointF'), CuteMixin._valueOf(p2, 'QPointF'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPointF'

  #  Qt's '~QPointF()'. Naming it makes this a value class: Python owns every
  #  C++ QPointF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QPointFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def manhattanLength(self) -> float:
    """
    Calls Qt's 'qreal QPointF::manhattanLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#manhattanLength
    """
    #  qreal QPointF::manhattanLength() const
    return self._callAs('QPointF', 'ritual_ZNK7QPointF15manhattanLengthEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPointF::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#isNull
    """
    #  bool QPointF::isNull() const
    return self._callAs('QPointF', 'ritual_ZNK7QPointF6isNullEv')

  def x(self) -> float:
    """
    Calls Qt's 'qreal QPointF::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#x
    """
    #  qreal QPointF::x() const
    return self._callAs('QPointF', 'ritual_ZNK7QPointF1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QPointF::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#y
    """
    #  qreal QPointF::y() const
    return self._callAs('QPointF', 'ritual_ZNK7QPointF1yEv')

  def transposed(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPointF::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#transposed

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPointF::transposed() const
    address = self._callAs('QPointF', 'ritual_ZNK7QPointF10transposedEv')
    return QPointF._cuteOwning(address)

  def toPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPointF::toPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#toPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPointF::toPoint() const
    address = self._callAs('QPointF', 'ritual_ZNK7QPointF7toPointEv')
    from . import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QPointF::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QPointF::setX(qreal x)
    self._callAs('QPointF', 'ritual_ZN7QPointF4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QPointF::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QPointF::setY(qreal y)
    self._callAs('QPointF', 'ritual_ZN7QPointF4setYEd', y)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __iadd__(self, p: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF &QPointF::operator+=(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator+=

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QPointF &QPointF::operator+=(const QPointF &p)
    self._callAs(
        'QPointF', 'ritual_ZN7QPointFpLERKS_', self._valueOf(p, 'QPointF'),
    )
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
  def __isub__(self, p: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF &QPointF::operator-=(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator-=

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QPointF &QPointF::operator-=(const QPointF &p)
    self._callAs(
        'QPointF', 'ritual_ZN7QPointFmIERKS_', self._valueOf(p, 'QPointF'),
    )
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
  def __imul__(self, c: float) -> QPointF:
    """
    Calls Qt's 'QPointF &QPointF::operator*=(qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator*=

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  QPointF &QPointF::operator*=(qreal c)
    self._callAs('QPointF', 'ritual_ZN7QPointFmLEd', c)
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
  def __itruediv__(self, c: float) -> QPointF:
    """
    Calls Qt's 'QPointF &QPointF::operator/=(qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator/=

    Parameters
    ----------

    c : float
      Passed on as it is.
    """
    #  QPointF &QPointF::operator/=(qreal c)
    self._callAs('QPointF', 'ritual_ZN7QPointFdVEd', c)
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
  def __eq__(self, rhs: QPointF) -> bool:
    """
    Calls Qt's 'bool operator==(const QPointF &lhs, const QPointF &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator==

    Parameters
    ----------

    rhs : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool operator==(const QPointF &lhs, const QPointF &rhs)
    return Rituals.call(
        'ritual_ZeqRK7QPointFS1_',
        CuteMixin._valueOf(self, 'QPointF'), CuteMixin._valueOf(rhs,
        'QPointF'),
    )

  @overload(QPoint)
  def __eq__(self, rhs: QPoint) -> bool:
    """
    Calls Qt's 'bool operator==(const QPointF &lhs, const QPoint &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator==

    Parameters
    ----------

    rhs : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool operator==(const QPointF &lhs, const QPoint &rhs)
    return Rituals.call(
        'ritual_ZeqRK7QPointFRK6QPoint',
        CuteMixin._valueOf(self, 'QPointF'), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QPointF) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPointF &lhs, const QPointF &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator!=

    Parameters
    ----------

    rhs : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool operator!=(const QPointF &lhs, const QPointF &rhs)
    return Rituals.call(
        'ritual_ZneRK7QPointFS1_',
        CuteMixin._valueOf(self, 'QPointF'), CuteMixin._valueOf(rhs,
        'QPointF'),
    )

  @overload(QPoint)
  def __ne__(self, rhs: QPoint) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPointF &lhs, const QPoint &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator!=

    Parameters
    ----------

    rhs : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool operator!=(const QPointF &lhs, const QPoint &rhs)
    return Rituals.call(
        'ritual_ZneRK7QPointFRK6QPoint',
        CuteMixin._valueOf(self, 'QPointF'), CuteMixin._valueOf(rhs),
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
  def __add__(self, p2: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF operator+(const QPointF &p1, const QPointF &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator+

    Parameters
    ----------

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator+(const QPointF &p1, const QPointF &p2)
    address = Rituals.call(
        'ritual_ZplRK7QPointFS1_',
        CuteMixin._valueOf(self, 'QPointF'), CuteMixin._valueOf(p2,
        'QPointF'),
    )
    return QPointF._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, p2: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF operator-(const QPointF &p1, const QPointF &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator-

    Parameters
    ----------

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator-(const QPointF &p1, const QPointF &p2)
    address = Rituals.call(
        'ritual_ZmiRK7QPointFS1_',
        CuteMixin._valueOf(self, 'QPointF'), CuteMixin._valueOf(p2,
        'QPointF'),
    )
    return QPointF._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __mul__(self, c: float) -> QPointF:
    """
    Calls Qt's 'QPointF operator*(const QPointF &p, qreal c)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator*

    Parameters
    ----------

    c : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator*(const QPointF &p, qreal c)
    address = Rituals.call(
        'ritual_ZmlRK7QPointFd', CuteMixin._valueOf(self, 'QPointF'), c,
    )
    return QPointF._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, c: float) -> QPointF:
    """
    Calls Qt's 'QPointF operator*(qreal c, const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator*

    Parameters
    ----------

    c : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator*(qreal c, const QPointF &p)
    address = Rituals.call(
        'ritual_ZmldRK7QPointF', c, CuteMixin._valueOf(self, 'QPointF'),
    )
    return QPointF._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __pos__(self) -> QPointF:
    """
    Calls Qt's 'QPointF operator+(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator+

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator+(const QPointF &p)
    address = Rituals.call(
        'ritual_ZpsRK7QPointF', CuteMixin._valueOf(self, 'QPointF'),
    )
    return QPointF._cuteOwning(address)

  def __neg__(self) -> QPointF:
    """
    Calls Qt's 'QPointF operator-(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator-

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator-(const QPointF &p)
    address = Rituals.call(
        'ritual_ZngRK7QPointF', CuteMixin._valueOf(self, 'QPointF'),
    )
    return QPointF._cuteOwning(address)

  @overload(float)
  def __truediv__(self, divisor: float) -> QPointF:
    """
    Calls Qt's 'QPointF operator/(const QPointF &p, qreal divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#operator/

    Parameters
    ----------

    divisor : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator/(const QPointF &p, qreal divisor)
    address = Rituals.call(
        'ritual_ZdvRK7QPointFd',
        CuteMixin._valueOf(self, 'QPointF'), divisor,
    )
    return QPointF._cuteOwning(address)

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
    Notes what was given, for Qt's 'QPointF::QPointF()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#QPointF
    """
    #  QPointF::QPointF()
    self._noteCreation(QPointF, lambda: Rituals.call(
        'ritual_ZN7QPointFC1Ev',
    ))

  @overload(QPoint)
  def __init__(self, p: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QPointF::QPointF(const QPoint &p)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#QPointF

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QPointF::QPointF(const QPoint &p)
    self._noteCreation(QPointF, lambda: Rituals.call(
        'ritual_ZN7QPointFC1ERK6QPoint', self._valueOf(p),
    ))

  @overload(float, float)
  def __init__(self, xpos: float, ypos: float) -> None:
    """
    Notes what was given, for Qt's 'QPointF::QPointF(qreal xpos, qreal
    ypos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpointf.html#QPointF

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.
    """
    #  QPointF::QPointF(qreal xpos, qreal ypos)
    self._noteCreation(QPointF, lambda: Rituals.call(
        'ritual_ZN7QPointFC1Edd', xpos, ypos,
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
    Qt's 'qreal &QPointF::rx()': takes or gives a type that cannot be passed
    yet: qreal &.
    """
    raise NotImplementedError(
        "'QPointF.rx' has no cute function yet. Qt's 'qreal "
        "&QPointF::rx()': takes or gives a type that cannot be passed yet: "
        "qreal &.")

  @staticmethod
  def ry(*__, **_) -> Never:
    """
    Qt's 'qreal &QPointF::ry()': takes or gives a type that cannot be passed
    yet: qreal &.
    """
    raise NotImplementedError(
        "'QPointF.ry' has no cute function yet. Qt's 'qreal "
        "&QPointF::ry()': takes or gives a type that cannot be passed yet: "
        "qreal &.")


#  Qt's 'QList<QPointF>': the list of QPointF, which 'QList[QPointF]' gives.
#  It is made here, so that there is one as soon as there can be a QPointF.
QList.createKind(
    QPointF, 'value',
    make='ritual_list_make_QPointF',
    add='ritual_list_add_QPointF',
    size='ritual_list_size_QPointF',
    at='ritual_list_at_QPointF',
    drop='ritual_list_drop_QPointF',
)
