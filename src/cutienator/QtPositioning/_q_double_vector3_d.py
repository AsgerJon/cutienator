"""
QDoubleVector3D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDoubleVector3D to be private: it declares the class in a header
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
  from . import QDoubleVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDoubleVector2D = WAIT['QDoubleVector2D']


class QDoubleVector3D(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDoubleVector3D: a plain Python object standing in
  front of one C++ QDoubleVector3D.

  C++ hands a QDoubleVector3D around as a copy, so every C++ QDoubleVector3D
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDoubleVector3D that has a ritual and that Python
  can call so far, 31 names in all: 'isNull', 'x', 'y', 'z', 'setX', 'setY',
  'setZ', 'get', 'set', 'length', 'lengthSquared', 'normalized', 'normalize',
  '__iadd__', '__isub__', '__imul__', '__itruediv__', 'dotProduct',
  'crossProduct', 'normal', 'distanceToPlane', 'distanceToLine', '__eq__',
  '__ne__', '__add__', '__sub__', '__rmul__', '__mul__', '__neg__',
  '__truediv__', 'toVector2D'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDoubleVector3D::~QDoubleVector3D()': the destructor: Python
    removes its C++ QDoubleVector3D by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDoubleVector3D is created at the first use, not by
    'QDoubleVector3D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDoubleVector3D back gives a copy the ritual made for
    Python, in a new cute QDoubleVector3D.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(v1: QDoubleVector3D, v2: QDoubleVector3D) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::dotProduct(const QDoubleVector3D &v1,
    const QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#dotProduct

    Parameters
    ----------

    v1 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  double QDoubleVector3D::dotProduct(const QDoubleVector3D &v1, const
    #      QDoubleVector3D &v2)
    return Rituals.call(
        'ritual_ZN15QDoubleVector3D10dotProductERKS_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  @staticmethod
  @overload(THIS, THIS)
  def crossProduct(
      v1: QDoubleVector3D,
      v2: QDoubleVector3D,
  ) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleVector3D::crossProduct(const
    QDoubleVector3D &v1, const QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#crossProduct

    Parameters
    ----------

    v1 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleVector3D::crossProduct(const QDoubleVector3D
    #      &v1, const QDoubleVector3D &v2)
    address = Rituals.call(
        'ritual_ZN15QDoubleVector3D12crossProductERKS_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )
    return QDoubleVector3D._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS)
  def normal(v1: QDoubleVector3D, v2: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleVector3D::normal(const QDoubleVector3D
    &v1, const QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#normal

    Parameters
    ----------

    v1 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleVector3D::normal(const QDoubleVector3D &v1,
    #      const QDoubleVector3D &v2)
    address = Rituals.call(
        'ritual_ZN15QDoubleVector3D6normalERKS_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )
    return QDoubleVector3D._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS, THIS)
  def normal(
      v1: QDoubleVector3D,
      v2: QDoubleVector3D,
      v3: QDoubleVector3D,
  ) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleVector3D::normal(const QDoubleVector3D
    &v1, const QDoubleVector3D &v2, const QDoubleVector3D &v3)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#normal

    Parameters
    ----------

    v1 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    v3 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleVector3D::normal(const QDoubleVector3D &v1,
    #      const QDoubleVector3D &v2, const QDoubleVector3D &v3)
    address = Rituals.call(
        'ritual_ZN15QDoubleVector3D6normalERKS_S1_S1_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
        CuteMixin._valueOf(v3),
    )
    return QDoubleVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDoubleVector3D'

  #  Qt's '~QDoubleVector3D()'. Naming it makes this a value class: Python
  #  owns every C++ QDoubleVector3D behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDoubleVector3DD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDoubleVector3D::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#isNull
    """
    #  bool QDoubleVector3D::isNull() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D6isNullEv')

  def x(self) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#x
    """
    #  double QDoubleVector3D::x() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#y
    """
    #  double QDoubleVector3D::y() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#z
    """
    #  double QDoubleVector3D::z() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D1zEv')

  @overload(int)
  def get(self, i: int) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::get(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#get

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  double QDoubleVector3D::get(int i) const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D3getEi', i)

  def length(self) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#length
    """
    #  double QDoubleVector3D::length() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D6lengthEv')

  def lengthSquared(self) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::lengthSquared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#lengthSquared
    """
    #  double QDoubleVector3D::lengthSquared() const
    return self.uglySide.call('ritual_ZNK15QDoubleVector3D13lengthSquaredEv')

  def normalized(self) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleVector3D::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#normalized

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleVector3D::normalized() const
    address = self.uglySide.call('ritual_ZNK15QDoubleVector3D10normalizedEv')
    return QDoubleVector3D._cuteOwning(address)

  @overload(THIS, THIS)
  def distanceToPlane(
      self,
      plane: QDoubleVector3D,
      normal: QDoubleVector3D,
  ) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::distanceToPlane(const QDoubleVector3D
    &plane, const QDoubleVector3D &normal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#distanceToPlane

    Parameters
    ----------

    plane : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    normal : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  double QDoubleVector3D::distanceToPlane(const QDoubleVector3D &plane,
    #      const QDoubleVector3D &normal) const
    return self.uglySide.call(
        'ritual_ZNK15QDoubleVector3D15distanceToPlaneERKS_S1_',
        self._valueOf(plane), self._valueOf(normal),
    )

  @overload(THIS, THIS, THIS)
  def distanceToPlane(
      self,
      plane1: QDoubleVector3D,
      plane2: QDoubleVector3D,
      plane3: QDoubleVector3D,
  ) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::distanceToPlane(const QDoubleVector3D
    &plane1, const QDoubleVector3D &plane2, const QDoubleVector3D &plane3)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#distanceToPlane

    Parameters
    ----------

    plane1 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    plane2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    plane3 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  double QDoubleVector3D::distanceToPlane(const QDoubleVector3D &plane1,
    #      const QDoubleVector3D &plane2, const QDoubleVector3D &plane3)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QDoubleVector3D15distanceToPlaneERKS_S1_S1_',
        self._valueOf(plane1), self._valueOf(plane2), self._valueOf(plane3),
    )

  @overload(THIS, THIS)
  def distanceToLine(
      self,
      point: QDoubleVector3D,
      direction: QDoubleVector3D,
  ) -> float:
    """
    Calls Qt's 'double QDoubleVector3D::distanceToLine(const QDoubleVector3D
    &point, const QDoubleVector3D &direction) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#distanceToLine

    Parameters
    ----------

    point : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    direction : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  double QDoubleVector3D::distanceToLine(const QDoubleVector3D &point,
    #      const QDoubleVector3D &direction) const
    return self.uglySide.call(
        'ritual_ZNK15QDoubleVector3D14distanceToLineERKS_S1_',
        self._valueOf(point), self._valueOf(direction),
    )

  def toVector2D(self) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D QDoubleVector3D::toVector2D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#toVector2D

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QDoubleVector3D::toVector2D() const
    address = self.uglySide.call('ritual_ZNK15QDoubleVector3D10toVector2DEv')
    from . import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QDoubleVector3D::setX(double x)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QDoubleVector3D::setX(double x)
    self.uglySide.call('ritual_ZN15QDoubleVector3D4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QDoubleVector3D::setY(double y)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QDoubleVector3D::setY(double y)
    self.uglySide.call('ritual_ZN15QDoubleVector3D4setYEd', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QDoubleVector3D::setZ(double z)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QDoubleVector3D::setZ(double z)
    self.uglySide.call('ritual_ZN15QDoubleVector3D4setZEd', z)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __iadd__(self, vector: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D &QDoubleVector3D::operator+=(const
    QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator+=

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  QDoubleVector3D &QDoubleVector3D::operator+=(const QDoubleVector3D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector3DpLERKS_', self._valueOf(vector),
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
  def __isub__(self, vector: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D &QDoubleVector3D::operator-=(const
    QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator-=

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  QDoubleVector3D &QDoubleVector3D::operator-=(const QDoubleVector3D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector3DmIERKS_', self._valueOf(vector),
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
  def __imul__(self, factor: float) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D &QDoubleVector3D::operator*=(double factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator*=

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  QDoubleVector3D &QDoubleVector3D::operator*=(double factor)
    self.uglySide.call('ritual_ZN15QDoubleVector3DmLEd', factor)
    return self

  @overload(THIS)
  def __imul__(self, vector: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D &QDoubleVector3D::operator*=(const
    QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator*=

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  QDoubleVector3D &QDoubleVector3D::operator*=(const QDoubleVector3D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN15QDoubleVector3DmLERKS_', self._valueOf(vector),
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
  def __itruediv__(self, divisor: float) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D &QDoubleVector3D::operator/=(double
    divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator/=

    Parameters
    ----------

    divisor : float
      Passed on as it is.
    """
    #  QDoubleVector3D &QDoubleVector3D::operator/=(double divisor)
    self.uglySide.call('ritual_ZN15QDoubleVector3DdVEd', divisor)
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
  def __eq__(self, v2: QDoubleVector3D) -> bool:
    """
    Calls Qt's 'bool operator==(const QDoubleVector3D &v1, const
    QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator==

    Parameters
    ----------

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  bool operator==(const QDoubleVector3D &v1, const QDoubleVector3D &v2)
    return Rituals.call(
        'ritual_ZeqRK15QDoubleVector3DS1_',
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
  def __ne__(self, v2: QDoubleVector3D) -> bool:
    """
    Calls Qt's 'bool operator!=(const QDoubleVector3D &v1, const
    QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator!=

    Parameters
    ----------

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  bool operator!=(const QDoubleVector3D &v1, const QDoubleVector3D &v2)
    return Rituals.call(
        'ritual_ZneRK15QDoubleVector3DS1_',
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
  def __add__(self, v2: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator+(const QDoubleVector3D &v1,
    const QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator+

    Parameters
    ----------

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator+(const QDoubleVector3D &v1, const
    #      QDoubleVector3D &v2)
    address = Rituals.call(
        'ritual_ZplRK15QDoubleVector3DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QDoubleVector3D._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, v2: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator-(const QDoubleVector3D &v1,
    const QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator-

    Parameters
    ----------

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator-(const QDoubleVector3D &v1, const
    #      QDoubleVector3D &v2)
    address = Rituals.call(
        'ritual_ZmiRK15QDoubleVector3DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QDoubleVector3D._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, factor: float) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator*(double factor, const
    QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator*(double factor, const QDoubleVector3D
    #      &vector)
    address = Rituals.call(
        'ritual_ZmldRK15QDoubleVector3D', factor, CuteMixin._valueOf(self),
    )
    return QDoubleVector3D._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __mul__(self, factor: float) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator*(const QDoubleVector3D
    &vector, double factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator*(const QDoubleVector3D &vector, double
    #      factor)
    address = Rituals.call(
        'ritual_ZmlRK15QDoubleVector3Dd', CuteMixin._valueOf(self), factor,
    )
    return QDoubleVector3D._cuteOwning(address)

  @overload(THIS)
  def __mul__(self, v2: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator*(const QDoubleVector3D &v1,
    const QDoubleVector3D &v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator*

    Parameters
    ----------

    v2 : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator*(const QDoubleVector3D &v1, const
    #      QDoubleVector3D &v2)
    address = Rituals.call(
        'ritual_ZmlRK15QDoubleVector3DS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QDoubleVector3D._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __neg__(self) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator-(const QDoubleVector3D
    &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator-

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator-(const QDoubleVector3D &vector)
    address = Rituals.call(
        'ritual_ZngRK15QDoubleVector3D', CuteMixin._valueOf(self),
    )
    return QDoubleVector3D._cuteOwning(address)

  @overload(float)
  def __truediv__(self, divisor: float) -> QDoubleVector3D:
    """
    Calls Qt's 'const QDoubleVector3D operator/(const QDoubleVector3D
    &vector, double divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#operator/

    Parameters
    ----------

    divisor : float
      Passed on as it is.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  const QDoubleVector3D operator/(const QDoubleVector3D &vector, double
    #      divisor)
    address = Rituals.call(
        'ritual_ZdvRK15QDoubleVector3Dd', CuteMixin._valueOf(self), divisor,
    )
    return QDoubleVector3D._cuteOwning(address)

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
    Notes what was given, for Qt's 'QDoubleVector3D::QDoubleVector3D()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#QDoubleVector3D
    """
    #  QDoubleVector3D::QDoubleVector3D()
    self._noteCreation(QDoubleVector3D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector3DC1Ev',
    ))

  @overload(float, float, float)
  def __init__(self, xpos: float, ypos: float, zpos: float) -> None:
    """
    Notes what was given, for Qt's 'QDoubleVector3D::QDoubleVector3D(double
    xpos, double ypos, double zpos)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#QDoubleVector3D

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.

    zpos : float
      Passed on as it is.
    """
    #  QDoubleVector3D::QDoubleVector3D(double xpos, double ypos, double
    #      zpos)
    self._noteCreation(QDoubleVector3D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector3DC1Eddd', xpos, ypos, zpos,
    ))

  @overload(QDoubleVector2D)
  def __init__(self, vector: QDoubleVector2D) -> None:
    """
    Notes what was given, for Qt's 'QDoubleVector3D::QDoubleVector3D(const
    QDoubleVector2D &vector)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#QDoubleVector3D

    Parameters
    ----------

    vector : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  QDoubleVector3D::QDoubleVector3D(const QDoubleVector2D &vector)
    self._noteCreation(QDoubleVector3D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector3DC1ERK15QDoubleVector2D',
        self._valueOf(vector),
    ))

  @overload(QDoubleVector2D, float)
  def __init__(self, vector: QDoubleVector2D, zpos: float) -> None:
    """
    Notes what was given, for Qt's 'QDoubleVector3D::QDoubleVector3D(const
    QDoubleVector2D &vector, double zpos)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublevector3d.html#QDoubleVector3D

    Parameters
    ----------

    vector : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    zpos : float
      Passed on as it is.
    """
    #  QDoubleVector3D::QDoubleVector3D(const QDoubleVector2D &vector, double
    #      zpos)
    self._noteCreation(QDoubleVector3D, lambda: Rituals.call(
        'ritual_ZN15QDoubleVector3DC1ERK15QDoubleVector2Dd',
        self._valueOf(vector), zpos,
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

  @overload(int, float)
  def set(self, i: int, value: float) -> None:
    """
    Calls Qt's 'void QDoubleVector3D::set(int i, double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#set

    Parameters
    ----------

    i : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QDoubleVector3D::set(int i, double value)
    self.uglySide.call('ritual_ZN15QDoubleVector3D3setEid', i, value)

  def normalize(self) -> None:
    """
    Calls Qt's 'void QDoubleVector3D::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublevector3d.html#normalize
    """
    #  void QDoubleVector3D::normalize()
    self.uglySide.call('ritual_ZN15QDoubleVector3D9normalizeEv')


#  Qt's 'QList<QDoubleVector3D>': the list of QDoubleVector3D, which
#  'QList[QDoubleVector3D]' gives. It is made here, so that there is one as
#  soon as there can be a QDoubleVector3D. Qt has a name of its own for it.
PolygonVector = QList.createKind(
    QDoubleVector3D, 'value',
    name='PolygonVector',
    make='ritual_list_make_QDoubleVector3D',
    add='ritual_list_add_QDoubleVector3D',
    size='ritual_list_size_QDoubleVector3D',
    at='ritual_list_at_QDoubleVector3D',
    drop='ritual_list_drop_QDoubleVector3D',
)
