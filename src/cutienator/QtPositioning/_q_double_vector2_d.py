"""
QDoubleVector2D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDoubleVector2D to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
  from . import QDoubleVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDoubleVector3D = WAIT['QDoubleVector3D']
  QPointF = WAIT['QPointF']


class QDoubleVector2D(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDoubleVector2D: a plain Python object standing in
  front of one C++ QDoubleVector2D.

  C++ hands a QDoubleVector2D around as a copy, so every C++ QDoubleVector2D
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDoubleVector2D that has a ritual and that Python
  can call so far, 26 names in all: 'manhattanLength', 'isNull', 'isFinite',
  'x', 'y', 'setX', 'setY', 'length', 'lengthSquared', 'normalized',
  'normalize', '__iadd__', '__isub__', '__imul__', '__itruediv__',
  'dotProduct', '__eq__', '__ne__', '__add__', '__sub__', '__rmul__',
  '__mul__', '__neg__', '__truediv__', 'toVector3D', 'toPointF'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDoubleVector2D::~QDoubleVector2D()': the destructor: Python
    removes its C++ QDoubleVector2D by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDoubleVector2D is created at the first use, not by
    'QDoubleVector2D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDoubleVector2D back gives a copy the ritual made for
    Python, in a new cute QDoubleVector2D.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(v1: QDoubleVector2D, v2: QDoubleVector2D) -> float:
    """
    Calls Qt's 'double QDoubleVector2D::dotProduct(const QDoubleVector2D &v1,
    const QDoubleVector2D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#dotProduct

    Parameters
    ----------

    v1 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    v2 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  double QDoubleVector2D::dotProduct(const QDoubleVector2D &v1, const
    #      QDoubleVector2D &v2)
    return Rituals.call(
        'ritual_ZN15QDoubleVector2D10dotProductERKS_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDoubleVector2D'

  #  Qt's '~QDoubleVector2D()'. Naming it makes this a value class: Python
  #  owns every C++ QDoubleVector2D behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDoubleVector2DD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def manhattanLength(self) -> float:
    """
    Calls Qt's 'double QDoubleVector2D::manhattanLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector2d.html#manhattanLength
    """
    #  double QDoubleVector2D::manhattanLength() const
    return self.uglySide.call(
        'ritual_ZNK15QDoubleVector2D15manhattanLengthEv',
    )

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDoubleVector2D::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#isNull
    """
    #  bool QDoubleVector2D::isNull() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector2D6isNullEv')

  def isFinite(self) -> bool:
    """
    Calls Qt's 'bool QDoubleVector2D::isFinite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#isFinite
    """
    #  bool QDoubleVector2D::isFinite() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector2D8isFiniteEv')

  def x(self) -> float:
    """
    Calls Qt's 'double QDoubleVector2D::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#x
    """
    #  double QDoubleVector2D::x() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector2D1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'double QDoubleVector2D::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#y
    """
    #  double QDoubleVector2D::y() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector2D1yEv')

  def length(self) -> float:
    """
    Calls Qt's 'double QDoubleVector2D::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#length
    """
    #  double QDoubleVector2D::length() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector2D6lengthEv')

  def lengthSquared(self) -> float:
    """
    Calls Qt's 'double QDoubleVector2D::lengthSquared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#lengthSquared
    """
    #  double QDoubleVector2D::lengthSquared() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector2D13lengthSquaredEv')

  def normalized(self) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D QDoubleVector2D::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#normalized

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QDoubleVector2D::normalized() const
    address = self.uglySide.call('ritual_ZNK15QDoubleVector2D10normalizedEv')
    return QDoubleVector2D._cuteOwning(address)

  def toVector3D(self) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleVector2D::toVector3D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#toVector3D

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleVector2D::toVector3D() const
    address = self.uglySide.call('ritual_ZNK15QDoubleVector2D10toVector3DEv')
    from . import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QDoubleVector2D::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QDoubleVector2D::toPointF() const
    address = self.uglySide.call('ritual_ZNK15QDoubleVector2D8toPointFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QDoubleVector2D::setX(double x)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QDoubleVector2D::setX(double x)
    self.uglySide.call('ritual_ZN15QDoubleVector2D4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QDoubleVector2D::setY(double y)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QDoubleVector2D::setY(double y)
    self.uglySide.call('ritual_ZN15QDoubleVector2D4setYEd', y)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __iadd__(self, vector: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D &QDoubleVector2D::operator+=(const
    QDoubleVector2D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator+=

    Parameters
    ----------

    vector : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  QDoubleVector2D &QDoubleVector2D::operator+=(const QDoubleVector2D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector2DpLERKS_', self._valueOf(vector),
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
  def __isub__(self, vector: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D &QDoubleVector2D::operator-=(const
    QDoubleVector2D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator-=

    Parameters
    ----------

    vector : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  QDoubleVector2D &QDoubleVector2D::operator-=(const QDoubleVector2D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector2DmIERKS_', self._valueOf(vector),
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
  def __imul__(self, factor: float) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D &QDoubleVector2D::operator*=(double factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator*=

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  QDoubleVector2D &QDoubleVector2D::operator*=(double factor)
    self.uglySide.call('ritual_ZN15QDoubleVector2DmLEd', factor)
    return self

  @overload(THIS)
  def __imul__(self, vector: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D &QDoubleVector2D::operator*=(const
    QDoubleVector2D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator*=

    Parameters
    ----------

    vector : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  QDoubleVector2D &QDoubleVector2D::operator*=(const QDoubleVector2D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector2DmLERKS_', self._valueOf(vector),
    )
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
  def __itruediv__(self, divisor: float) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D &QDoubleVector2D::operator/=(double
    divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator/=

    Parameters
    ----------

    divisor : float
      Passed on as it is.
    """
    #  QDoubleVector2D &QDoubleVector2D::operator/=(double divisor)
    self.uglySide.call('ritual_ZN15QDoubleVector2DdVEd', divisor)
    return self

  @overload(THIS)
  def __itruediv__(self, vector: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D &QDoubleVector2D::operator/=(const
    QDoubleVector2D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator/=

    Parameters
    ----------

    vector : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  QDoubleVector2D &QDoubleVector2D::operator/=(const QDoubleVector2D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector2DdVERKS_', self._valueOf(vector),
    )
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
  def __eq__(self, v2: QDoubleVector2D) -> bool:
    """
    Calls Qt's 'bool operator==(const QDoubleVector2D &v1, const
    QDoubleVector2D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator==

    Parameters
    ----------

    v2 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  bool operator==(const QDoubleVector2D &v1, const QDoubleVector2D &v2)
    return Rituals.call(
        'ritual_ZeqRK15QDoubleVector2DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
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
  def __ne__(self, v2: QDoubleVector2D) -> bool:
    """
    Calls Qt's 'bool operator!=(const QDoubleVector2D &v1, const
    QDoubleVector2D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator!=

    Parameters
    ----------

    v2 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  bool operator!=(const QDoubleVector2D &v1, const QDoubleVector2D &v2)
    return Rituals.call(
        'ritual_ZneRK15QDoubleVector2DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
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
  def __add__(self, v2: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator+(const QDoubleVector2D &v1,
    const QDoubleVector2D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator+

    Parameters
    ----------

    v2 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator+(const QDoubleVector2D &v1, const
    #      QDoubleVector2D &v2)
    address = Rituals.call(
        'ritual_ZplRK15QDoubleVector2DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QDoubleVector2D._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, v2: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator-(const QDoubleVector2D &v1,
    const QDoubleVector2D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator-

    Parameters
    ----------

    v2 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator-(const QDoubleVector2D &v1, const
    #      QDoubleVector2D &v2)
    address = Rituals.call(
        'ritual_ZmiRK15QDoubleVector2DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QDoubleVector2D._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, factor: float) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator*(double factor, const
    QDoubleVector2D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator*(double factor, const QDoubleVector2D
    #      &vector)
    address = Rituals.call(
        'ritual_ZmldRK15QDoubleVector2D', factor, CuteMixin._valueOf(self),
    )
    return QDoubleVector2D._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __mul__(self, factor: float) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator*(const QDoubleVector2D
    &vector, double factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator*(const QDoubleVector2D &vector, double
    #      factor)
    address = Rituals.call(
        'ritual_ZmlRK15QDoubleVector2Dd', CuteMixin._valueOf(self), factor,
    )
    return QDoubleVector2D._cuteOwning(address)

  @overload(THIS)
  def __mul__(self, v2: QDoubleVector2D) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator*(const QDoubleVector2D &v1,
    const QDoubleVector2D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator*

    Parameters
    ----------

    v2 : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator*(const QDoubleVector2D &v1, const
    #      QDoubleVector2D &v2)
    address = Rituals.call(
        'ritual_ZmlRK15QDoubleVector2DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QDoubleVector2D._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __neg__(self) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator-(const QDoubleVector2D
    &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator-

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator-(const QDoubleVector2D &vector)
    address = Rituals.call(
        'ritual_ZngRK15QDoubleVector2D', CuteMixin._valueOf(self),
    )
    return QDoubleVector2D._cuteOwning(address)

  @overload(float)
  def __truediv__(self, divisor: float) -> QDoubleVector2D:
    """
    Calls Qt's 'const QDoubleVector2D operator/(const QDoubleVector2D
    &vector, double divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#operator/

    Parameters
    ----------

    divisor : float
      Passed on as it is.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector2D operator/(const QDoubleVector2D &vector, double
    #      divisor)
    address = Rituals.call(
        'ritual_ZdvRK15QDoubleVector2Dd', CuteMixin._valueOf(self), divisor,
    )
    return QDoubleVector2D._cuteOwning(address)

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
    Notes what was given, for Qt's 'QDoubleVector2D::QDoubleVector2D()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector2d.html#QDoubleVector2D
    """
    #  QDoubleVector2D::QDoubleVector2D()
    self._noteCreation(QDoubleVector2D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector2DC1Ev',
    ))

  @overload(float, float)
  def __init__(self, xpos: float, ypos: float) -> None:
    """
    Notes what was given, for Qt's 'QDoubleVector2D::QDoubleVector2D(double
    xpos, double ypos)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector2d.html#QDoubleVector2D

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.
    """
    #  QDoubleVector2D::QDoubleVector2D(double xpos, double ypos)
    self._noteCreation(QDoubleVector2D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector2DC1Edd', xpos, ypos,
    ))

  @overload(QPointF)
  def __init__(self, p: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QDoubleVector2D::QDoubleVector2D(const
    QPointF &p)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector2d.html#QDoubleVector2D

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QDoubleVector2D::QDoubleVector2D(const QPointF &p)
    self._noteCreation(QDoubleVector2D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector2DC1ERK7QPointF',
        self._valueOf(p, 'QPointF'),
    ))

  @overload(QDoubleVector3D)
  def __init__(self, vector: QDoubleVector3D) -> None:
    """
    Notes what was given, for Qt's 'QDoubleVector2D::QDoubleVector2D(const
    QDoubleVector3D &vector)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector2d.html#QDoubleVector2D

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  QDoubleVector2D::QDoubleVector2D(const QDoubleVector3D &vector)
    self._noteCreation(QDoubleVector2D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector2DC1ERK15QDoubleVector3D',
        self._valueOf(vector),
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

  def normalize(self) -> None:
    """
    Calls Qt's 'void QDoubleVector2D::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector2d.html#normalize
    """
    #  void QDoubleVector2D::normalize()
    self.uglySide.call('ritual_ZN15QDoubleVector2D9normalizeEv')


#  Qt's 'QList<QDoubleVector2D>': the list of QDoubleVector2D, which
#  'QList[QDoubleVector2D]' gives. It is made here, so that there is one as
#  soon as there can be a QDoubleVector2D.
QList.createKind(
    QDoubleVector2D, 'value',
    make='ritual_list_make_QDoubleVector2D',
    add='ritual_list_add_QDoubleVector2D',
    size='ritual_list_size_QDoubleVector2D',
    at='ritual_list_at_QDoubleVector2D',
    drop='ritual_list_drop_QDoubleVector2D',
)
