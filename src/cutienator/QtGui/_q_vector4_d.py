"""
QVector4D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvectornd.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QPointF
  from . import QMatrix4x4, QVector2D, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']


class QVector4D(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVector4D: a plain Python object standing in front of
  one C++ QVector4D.

  C++ hands a QVector4D around as a copy, so every C++ QVector4D behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVector4D that has a ritual and that Python can call
  so far, 33 names in all: 'isNull', 'x', 'y', 'z', 'w', 'setX', 'setY',
  'setZ', 'setW', '__getitem__', 'length', 'lengthSquared', 'normalized',
  'normalize', '__iadd__', '__isub__', '__imul__', '__itruediv__',
  'dotProduct', '__eq__', '__ne__', '__add__', '__sub__', '__rmul__',
  '__mul__', '__neg__', '__truediv__', 'toVector2D', 'toVector2DAffine',
  'toVector3D', 'toVector3DAffine', 'toPoint', 'toPointF'. It can be made
  from Python, in 9 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant QVector4D::operator QVariant() const': an operator Python
    has no name for.
  - Qt's 'QVector4D::~QVector4D()': the destructor: Python removes its C++
    QVector4D by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet; 1 written with the class 'QMatrix4x4', which declares it as
  well and stands first in it.

  What to expect
  --------------

  - The C++ QVector4D is created at the first use, not by 'QVector4D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVector4D back gives a copy the ritual made for
    Python, in a new cute QVector4D.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(v1: QVector4D, v2: QVector4D) -> float:
    """
    Calls Qt's 'float QVector4D::dotProduct(QVector4D v1, QVector4D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#dotProduct

    Parameters
    ----------

    v1 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    v2 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  float QVector4D::dotProduct(QVector4D v1, QVector4D v2)
    return Rituals.call(
        'ritual_ZN9QVector4D10dotProductES_S_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVector4D'

  #  Qt's '~QVector4D()'. Naming it makes this a value class: Python owns
  #  every C++ QVector4D behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QVector4DD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QVector4D::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#isNull
    """
    #  bool QVector4D::isNull() const
    return self.uglySide.call('ritual_ZNK9QVector4D6isNullEv')

  def x(self) -> float:
    """
    Calls Qt's 'float QVector4D::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#x
    """
    #  float QVector4D::x() const
    return self.uglySide.call('ritual_ZNK9QVector4D1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QVector4D::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#y
    """
    #  float QVector4D::y() const
    return self.uglySide.call('ritual_ZNK9QVector4D1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'float QVector4D::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#z
    """
    #  float QVector4D::z() const
    return self.uglySide.call('ritual_ZNK9QVector4D1zEv')

  def w(self) -> float:
    """
    Calls Qt's 'float QVector4D::w() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#w
    """
    #  float QVector4D::w() const
    return self.uglySide.call('ritual_ZNK9QVector4D1wEv')

  def length(self) -> float:
    """
    Calls Qt's 'float QVector4D::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#length
    """
    #  float QVector4D::length() const
    return self.uglySide.call('ritual_ZNK9QVector4D6lengthEv')

  def lengthSquared(self) -> float:
    """
    Calls Qt's 'float QVector4D::lengthSquared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#lengthSquared
    """
    #  float QVector4D::lengthSquared() const
    return self.uglySide.call('ritual_ZNK9QVector4D13lengthSquaredEv')

  def normalized(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QVector4D::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#normalized

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QVector4D::normalized() const
    address = self.uglySide.call('ritual_ZNK9QVector4D10normalizedEv')
    return QVector4D._cuteOwning(address)

  def toVector2D(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QVector4D::toVector2D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#toVector2D

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QVector4D::toVector2D() const
    address = self.uglySide.call('ritual_ZNK9QVector4D10toVector2DEv')
    from . import QVector2D
    return QVector2D._cuteOwning(address)

  def toVector2DAffine(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QVector4D::toVector2DAffine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#toVector2DAffine

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QVector4D::toVector2DAffine() const
    address = self.uglySide.call('ritual_ZNK9QVector4D16toVector2DAffineEv')
    from . import QVector2D
    return QVector2D._cuteOwning(address)

  def toVector3D(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector4D::toVector3D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#toVector3D

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector4D::toVector3D() const
    address = self.uglySide.call('ritual_ZNK9QVector4D10toVector3DEv')
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  def toVector3DAffine(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector4D::toVector3DAffine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#toVector3DAffine

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector4D::toVector3DAffine() const
    address = self.uglySide.call('ritual_ZNK9QVector4D16toVector3DAffineEv')
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  def toPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QVector4D::toPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#toPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QVector4D::toPoint() const
    address = self.uglySide.call('ritual_ZNK9QVector4D7toPointEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QVector4D::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QVector4D::toPointF() const
    address = self.uglySide.call('ritual_ZNK9QVector4D8toPointFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QVector4D::setX(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QVector4D::setX(float x)
    self.uglySide.call('ritual_ZN9QVector4D4setXEf', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QVector4D::setY(float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QVector4D::setY(float y)
    self.uglySide.call('ritual_ZN9QVector4D4setYEf', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QVector4D::setZ(float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QVector4D::setZ(float z)
    self.uglySide.call('ritual_ZN9QVector4D4setZEf', z)

  @overload(float)
  def setW(self, w: float) -> None:
    """
    Calls Qt's 'void QVector4D::setW(float w)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#setW

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QVector4D::setW(float w)
    self.uglySide.call('ritual_ZN9QVector4D4setWEf', w)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, i: int) -> float:
    """
    Calls Qt's 'float QVector4D::operator[](int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  float QVector4D::operator[](int i) const
    return self.uglySide.call('ritual_ZNK9QVector4DixEi', i)

  @overload(THIS)
  def __iadd__(self, vector: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D &QVector4D::operator+=(QVector4D vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator+=

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QVector4D &QVector4D::operator+=(QVector4D vector)
    self.uglySide.call('ritual_ZN9QVector4DpLES_', self._valueOf(vector))
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
  def __isub__(self, vector: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D &QVector4D::operator-=(QVector4D vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator-=

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QVector4D &QVector4D::operator-=(QVector4D vector)
    self.uglySide.call('ritual_ZN9QVector4DmIES_', self._valueOf(vector))
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
  def __imul__(self, factor: float) -> QVector4D:
    """
    Calls Qt's 'QVector4D &QVector4D::operator*=(float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator*=

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  QVector4D &QVector4D::operator*=(float factor)
    self.uglySide.call('ritual_ZN9QVector4DmLEf', factor)
    return self

  @overload(THIS)
  def __imul__(self, vector: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D &QVector4D::operator*=(QVector4D vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator*=

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QVector4D &QVector4D::operator*=(QVector4D vector)
    self.uglySide.call('ritual_ZN9QVector4DmLES_', self._valueOf(vector))
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
  def __itruediv__(self, divisor: float) -> QVector4D:
    """
    Calls Qt's 'QVector4D &QVector4D::operator/=(float divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator/=

    Parameters
    ----------

    divisor : float
      Passed on as it is.
    """
    #  QVector4D &QVector4D::operator/=(float divisor)
    self.uglySide.call('ritual_ZN9QVector4DdVEf', divisor)
    return self

  @overload(THIS)
  def __itruediv__(self, vector: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D &QVector4D::operator/=(QVector4D vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator/=

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QVector4D &QVector4D::operator/=(QVector4D vector)
    self.uglySide.call('ritual_ZN9QVector4DdVES_', self._valueOf(vector))
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
  def __eq__(self, v2: QVector4D) -> bool:
    """
    Calls Qt's 'bool operator==(QVector4D v1, QVector4D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator==

    Parameters
    ----------

    v2 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  bool operator==(QVector4D v1, QVector4D v2)
    return Rituals.call(
        'ritual_Zeq9QVector4DS_',
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
  def __ne__(self, v2: QVector4D) -> bool:
    """
    Calls Qt's 'bool operator!=(QVector4D v1, QVector4D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator!=

    Parameters
    ----------

    v2 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  bool operator!=(QVector4D v1, QVector4D v2)
    return Rituals.call(
        'ritual_Zne9QVector4DS_',
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
  def __add__(self, v2: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator+(QVector4D v1, QVector4D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator+

    Parameters
    ----------

    v2 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator+(QVector4D v1, QVector4D v2)
    address = Rituals.call(
        'ritual_Zpl9QVector4DS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QVector4D._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, v2: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator-(QVector4D v1, QVector4D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator-

    Parameters
    ----------

    v2 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator-(QVector4D v1, QVector4D v2)
    address = Rituals.call(
        'ritual_Zmi9QVector4DS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QVector4D._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __rmul__(self, factor: float) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator*(float factor, QVector4D vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator*(float factor, QVector4D vector)
    address = Rituals.call(
        'ritual_Zmlf9QVector4D', factor, CuteMixin._valueOf(self),
    )
    return QVector4D._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(float)
  def __mul__(self, factor: float) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator*(QVector4D vector, float factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator*(QVector4D vector, float factor)
    address = Rituals.call(
        'ritual_Zml9QVector4Df', CuteMixin._valueOf(self), factor,
    )
    return QVector4D._cuteOwning(address)

  @overload(THIS)
  def __mul__(self, v2: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator*(QVector4D v1, QVector4D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator*

    Parameters
    ----------

    v2 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator*(QVector4D v1, QVector4D v2)
    address = Rituals.call(
        'ritual_Zml9QVector4DS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(v2),
    )
    return QVector4D._cuteOwning(address)

  @overload(QMatrix4x4)
  def __mul__(self, matrix: QMatrix4x4) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator*(const QVector4D &vector, const QMatrix4x4
    &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator*

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator*(const QVector4D &vector, const QMatrix4x4 &matrix)
    address = Rituals.call(
        'ritual_ZmlRK9QVector4DRK10QMatrix4x4',
        CuteMixin._valueOf(self), CuteMixin._valueOf(matrix),
    )
    return QVector4D._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __neg__(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator-(QVector4D vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator-

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator-(QVector4D vector)
    address = Rituals.call('ritual_Zng9QVector4D', CuteMixin._valueOf(self))
    return QVector4D._cuteOwning(address)

  @overload(float)
  def __truediv__(self, divisor: float) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator/(QVector4D vector, float divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator/

    Parameters
    ----------

    divisor : float
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator/(QVector4D vector, float divisor)
    address = Rituals.call(
        'ritual_Zdv9QVector4Df', CuteMixin._valueOf(self), divisor,
    )
    return QVector4D._cuteOwning(address)

  @overload(THIS)
  def __truediv__(self, divisor: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D operator/(QVector4D vector, QVector4D divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#operator/

    Parameters
    ----------

    divisor : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D operator/(QVector4D vector, QVector4D divisor)
    address = Rituals.call(
        'ritual_Zdv9QVector4DS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(divisor),
    )
    return QVector4D._cuteOwning(address)

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
    Notes what was given, for Qt's 'QVector4D::QVector4D()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D
    """
    #  QVector4D::QVector4D()
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QVector4D::QVector4D(Qt::Initialization a0)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1EN2Qt14InitializationE', a0.value,
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      xpos: float,
      ypos: float,
      zpos: float,
      wpos: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(float xpos, float
    ypos, float zpos, float wpos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.

    zpos : float
      Passed on as it is.

    wpos : float
      Passed on as it is.
    """
    #  QVector4D::QVector4D(float xpos, float ypos, float zpos, float wpos)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1Effff', xpos, ypos, zpos, wpos,
    ))

  @overload(QPoint)
  def __init__(self, point: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(QPoint point)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QVector4D::QVector4D(QPoint point)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1E6QPoint', self._valueOf(point),
    ))

  @overload(QPointF)
  def __init__(self, point: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(QPointF point)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QVector4D::QVector4D(QPointF point)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1E7QPointF', self._valueOf(point),
    ))

  @overload(QVector2D)
  def __init__(self, vector: QVector2D) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(QVector2D vector)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    vector : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  QVector4D::QVector4D(QVector2D vector)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1E9QVector2D', self._valueOf(vector),
    ))

  @overload(QVector2D, float, float)
  def __init__(self, vector: QVector2D, zpos: float, wpos: float) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(QVector2D vector,
    float zpos, float wpos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    vector : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    zpos : float
      Passed on as it is.

    wpos : float
      Passed on as it is.
    """
    #  QVector4D::QVector4D(QVector2D vector, float zpos, float wpos)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1E9QVector2Dff',
        self._valueOf(vector), zpos, wpos,
    ))

  @overload(QVector3D)
  def __init__(self, vector: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(QVector3D vector)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QVector4D::QVector4D(QVector3D vector)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1E9QVector3D', self._valueOf(vector),
    ))

  @overload(QVector3D, float)
  def __init__(self, vector: QVector3D, wpos: float) -> None:
    """
    Notes what was given, for Qt's 'QVector4D::QVector4D(QVector3D vector,
    float wpos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#QVector4D

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    wpos : float
      Passed on as it is.
    """
    #  QVector4D::QVector4D(QVector3D vector, float wpos)
    self._noteCreation(QVector4D, lambda: Rituals.call(
        'ritual_ZN9QVector4DC1E9QVector3Df', self._valueOf(vector), wpos,
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
    Calls Qt's 'void QVector4D::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvector4d.html#normalize
    """
    #  void QVector4D::normalize()
    self.uglySide.call('ritual_ZN9QVector4D9normalizeEv')
