"""
QDoubleMatrix4x4 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qdoublematrix4x4_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDoubleMatrix4x4 to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QPoint, QPointF, QRect, QRectF
  from . import QDoubleVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QDoubleVector3D = WAIT['QDoubleVector3D']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']


class QDoubleMatrix4x4(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDoubleMatrix4x4: a plain Python object standing in
  front of one C++ QDoubleMatrix4x4.

  C++ hands a QDoubleMatrix4x4 around as a copy, so every C++
  QDoubleMatrix4x4 behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDoubleMatrix4x4 that has a ritual and that Python
  can call so far, 35 names in all: '__call__', 'isAffine', 'isIdentity',
  'setToIdentity', 'fill', 'determinant', 'transposed', '__iadd__',
  '__isub__', '__imul__', '__itruediv__', '__eq__', '__ne__', '__add__',
  '__sub__', '__mul__', '__rmul__', '__neg__', '__truediv__', 'scale',
  'translate', 'rotate', 'ortho', 'frustum', 'perspective', 'lookAt',
  'viewport', 'flipCoordinates', 'map', 'mapVector', 'mapRect', 'optimize',
  '__rlshift__', 'orthonormalInverse', 'projectedRotate'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDoubleMatrix4x4::QDoubleMatrix4x4(const double *values)': names
    'double', which has no cute class yet.
  - Qt's 'QDoubleMatrix4x4::QDoubleMatrix4x4(const double *values, int cols,
    int rows)': names 'double', which has no cute class yet.
  - Qt's 'QDoubleMatrix4x4 QDoubleMatrix4x4::inverted(bool *invertible)
    const': takes a number to change where it is.
  - Qt's 'void QDoubleMatrix4x4::copyDataTo(double *values) const': takes a
    number to change where it is.
  - Qt's 'const double *QDoubleMatrix4x4::data() const': gives 'double',
    which has no cute class yet.
  - Qt's 'const double *QDoubleMatrix4x4::constData() const': gives 'double',
    which has no cute class yet.
  - Qt's 'QDoubleMatrix4x4::~QDoubleMatrix4x4()': the destructor: Python
    removes its C++ QDoubleMatrix4x4 by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 68 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QDoubleMatrix4x4 is created at the first use, not by
    'QDoubleMatrix4x4(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDoubleMatrix4x4 back gives a copy the ritual made
    for Python, in a new cute QDoubleMatrix4x4.
  - Each name of Qt's QDoubleMatrix4x4 that has no cute function yet,
    'constData', 'copyDataTo', 'data', 'inverted', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDoubleMatrix4x4'

  #  Qt's '~QDoubleMatrix4x4()'. Naming it makes this a value class: Python
  #  owns every C++ QDoubleMatrix4x4 behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDoubleMatrix4x4D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isAffine(self) -> bool:
    """
    Calls Qt's 'bool QDoubleMatrix4x4::isAffine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#isAffine
    """
    #  bool QDoubleMatrix4x4::isAffine() const
    return self.uglySide.call('ritual_ZNK16QDoubleMatrix4x48isAffineEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QDoubleMatrix4x4::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#isIdentity
    """
    #  bool QDoubleMatrix4x4::isIdentity() const
    return self.uglySide.call('ritual_ZNK16QDoubleMatrix4x410isIdentityEv')

  def determinant(self) -> float:
    """
    Calls Qt's 'double QDoubleMatrix4x4::determinant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#determinant
    """
    #  double QDoubleMatrix4x4::determinant() const
    return self.uglySide.call('ritual_ZNK16QDoubleMatrix4x411determinantEv')

  def transposed(self) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 QDoubleMatrix4x4::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#transposed

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 QDoubleMatrix4x4::transposed() const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x410transposedEv',
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload(QPoint)
  def map(self, point: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QDoubleMatrix4x4::map(const QPoint &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#map

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QDoubleMatrix4x4::map(const QPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x43mapERK6QPoint', self._valueOf(point),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def map(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QDoubleMatrix4x4::map(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#map

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QDoubleMatrix4x4::map(const QPointF &point) const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x43mapERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QDoubleVector3D)
  def map(self, point: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleMatrix4x4::map(const QDoubleVector3D
    &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#map

    Parameters
    ----------

    point : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleMatrix4x4::map(const QDoubleVector3D &point)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x43mapERK15QDoubleVector3D',
        self._valueOf(point),
    )
    from . import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  @overload(QDoubleVector3D)
  def mapVector(self, vector: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QDoubleMatrix4x4::mapVector(const
    QDoubleVector3D &vector) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#mapVector

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QDoubleMatrix4x4::mapVector(const QDoubleVector3D
    #      &vector) const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x49mapVectorERK15QDoubleVector3D',
        self._valueOf(vector),
    )
    from . import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  @overload(QRect)
  def mapRect(self, rect: QRect) -> QRect:
    """
    Calls Qt's 'QRect QDoubleMatrix4x4::mapRect(const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#mapRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDoubleMatrix4x4::mapRect(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x47mapRectERK5QRect', self._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRectF)
  def mapRect(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QDoubleMatrix4x4::mapRect(const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#mapRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QDoubleMatrix4x4::mapRect(const QRectF &rect) const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x47mapRectERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def orthonormalInverse(self) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 QDoubleMatrix4x4::orthonormalInverse()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#orthonormalInverse

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 QDoubleMatrix4x4::orthonormalInverse() const
    address = self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x418orthonormalInverseEv',
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setToIdentity(self) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::setToIdentity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#setToIdentity
    """
    #  void QDoubleMatrix4x4::setToIdentity()
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x413setToIdentityEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def __call__(self, row: int, column: int) -> float:
    """
    Calls Qt's 'const double &QDoubleMatrix4x4::operator()(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator()

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  const double &QDoubleMatrix4x4::operator()(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x4clEii', row, column,
    )

  @overload(THIS)
  def __iadd__(self, other: QDoubleMatrix4x4) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 &QDoubleMatrix4x4::operator+=(const
    QDoubleMatrix4x4 &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator+=

    Parameters
    ----------

    other : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.
    """
    #  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator+=(const QDoubleMatrix4x4
    #      &other)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x4pLERKS_', self._valueOf(other),
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
  def __isub__(self, other: QDoubleMatrix4x4) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 &QDoubleMatrix4x4::operator-=(const
    QDoubleMatrix4x4 &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator-=

    Parameters
    ----------

    other : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.
    """
    #  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator-=(const QDoubleMatrix4x4
    #      &other)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x4mIERKS_', self._valueOf(other),
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

  @overload(THIS)
  def __imul__(self, other: QDoubleMatrix4x4) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 &QDoubleMatrix4x4::operator*=(const
    QDoubleMatrix4x4 &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*=

    Parameters
    ----------

    other : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.
    """
    #  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator*=(const QDoubleMatrix4x4
    #      &other)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x4mLERKS_', self._valueOf(other),
    )
    return self

  @overload(float)
  def __imul__(self, factor: float) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 &QDoubleMatrix4x4::operator*=(double
    factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*=

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator*=(double factor)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x4mLEd', factor)
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
  def __itruediv__(self, divisor: float) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 &QDoubleMatrix4x4::operator/=(double
    divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator/=

    Parameters
    ----------

    divisor : float
      Passed on as it is.
    """
    #  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator/=(double divisor)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x4dVEd', divisor)
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
  def __eq__(self, other: QDoubleMatrix4x4) -> bool:
    """
    Calls Qt's 'bool QDoubleMatrix4x4::operator==(const QDoubleMatrix4x4
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator==

    Parameters
    ----------

    other : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.
    """
    #  bool QDoubleMatrix4x4::operator==(const QDoubleMatrix4x4 &other) const
    return self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x4eqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QDoubleMatrix4x4) -> bool:
    """
    Calls Qt's 'bool QDoubleMatrix4x4::operator!=(const QDoubleMatrix4x4
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator!=

    Parameters
    ----------

    other : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.
    """
    #  bool QDoubleMatrix4x4::operator!=(const QDoubleMatrix4x4 &other) const
    return self.uglySide.call(
        'ritual_ZNK16QDoubleMatrix4x4neERKS_', self._valueOf(other),
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
  def __add__(self, m2: QDoubleMatrix4x4) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator+(const QDoubleMatrix4x4 &m1, const
    QDoubleMatrix4x4 &m2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator+

    Parameters
    ----------

    m2 : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator+(const QDoubleMatrix4x4 &m1, const
    #      QDoubleMatrix4x4 &m2)
    address = Rituals.call(
        'ritual_ZplRK16QDoubleMatrix4x4S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(m2),
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, m2: QDoubleMatrix4x4) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator-(const QDoubleMatrix4x4 &m1, const
    QDoubleMatrix4x4 &m2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator-

    Parameters
    ----------

    m2 : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator-(const QDoubleMatrix4x4 &m1, const
    #      QDoubleMatrix4x4 &m2)
    address = Rituals.call(
        'ritual_ZmiRK16QDoubleMatrix4x4S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(m2),
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __mul__(self, m2: QDoubleMatrix4x4) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator*(const QDoubleMatrix4x4 &m1, const
    QDoubleMatrix4x4 &m2)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    m2 : QDoubleMatrix4x4
      Passed on as a value: Qt reads the C++ QDoubleMatrix4x4, which stays
      Python's own.

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator*(const QDoubleMatrix4x4 &m1, const
    #      QDoubleMatrix4x4 &m2)
    address = Rituals.call(
        'ritual_ZmlRK16QDoubleMatrix4x4S1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(m2),
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload(QDoubleVector3D)
  def __mul__(self, vector: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D operator*(const QDoubleMatrix4x4 &matrix,
    const QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D operator*(const QDoubleMatrix4x4 &matrix, const
    #      QDoubleVector3D &vector)
    address = Rituals.call(
        'ritual_ZmlRK16QDoubleMatrix4x4RK15QDoubleVector3D',
        CuteMixin._valueOf(self), CuteMixin._valueOf(vector),
    )
    from . import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  @overload(QPoint)
  def __mul__(self, point: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint operator*(const QDoubleMatrix4x4 &matrix, const QPoint
    &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator*(const QDoubleMatrix4x4 &matrix, const QPoint &point)
    address = Rituals.call(
        'ritual_ZmlRK16QDoubleMatrix4x4RK6QPoint',
        CuteMixin._valueOf(self), CuteMixin._valueOf(point),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def __mul__(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF operator*(const QDoubleMatrix4x4 &matrix, const
    QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator*(const QDoubleMatrix4x4 &matrix, const QPointF
    #      &point)
    address = Rituals.call(
        'ritual_ZmlRK16QDoubleMatrix4x4RK7QPointF',
        CuteMixin._valueOf(self), CuteMixin._valueOf(point, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def __mul__(self, factor: float) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator*(const QDoubleMatrix4x4 &matrix,
    double factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator*(const QDoubleMatrix4x4 &matrix, double
    #      factor)
    address = Rituals.call(
        'ritual_ZmlRK16QDoubleMatrix4x4d', CuteMixin._valueOf(self), factor,
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDoubleVector3D)
  def __rmul__(self, vector: QDoubleVector3D) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D operator*(const QDoubleVector3D &vector,
    const QDoubleMatrix4x4 &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D operator*(const QDoubleVector3D &vector, const
    #      QDoubleMatrix4x4 &matrix)
    address = Rituals.call(
        'ritual_ZmlRK15QDoubleVector3DRK16QDoubleMatrix4x4',
        CuteMixin._valueOf(vector), CuteMixin._valueOf(self),
    )
    from . import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  @overload(QPoint)
  def __rmul__(self, point: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint operator*(const QPoint &point, const QDoubleMatrix4x4
    &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint operator*(const QPoint &point, const QDoubleMatrix4x4 &matrix)
    address = Rituals.call(
        'ritual_ZmlRK6QPointRK16QDoubleMatrix4x4',
        CuteMixin._valueOf(point), CuteMixin._valueOf(self),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QPointF)
  def __rmul__(self, point: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF operator*(const QPointF &point, const
    QDoubleMatrix4x4 &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF operator*(const QPointF &point, const QDoubleMatrix4x4
    #      &matrix)
    address = Rituals.call(
        'ritual_ZmlRK7QPointFRK16QDoubleMatrix4x4',
        CuteMixin._valueOf(point, 'QPointF'), CuteMixin._valueOf(self),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def __rmul__(self, factor: float) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator*(double factor, const
    QDoubleMatrix4x4 &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator*

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator*(double factor, const QDoubleMatrix4x4
    #      &matrix)
    address = Rituals.call(
        'ritual_ZmldRK16QDoubleMatrix4x4', factor, CuteMixin._valueOf(self),
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload.fallback
  def __rmul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  def __neg__(self) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator-(const QDoubleMatrix4x4 &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator-

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator-(const QDoubleMatrix4x4 &matrix)
    address = Rituals.call(
        'ritual_ZngRK16QDoubleMatrix4x4', CuteMixin._valueOf(self),
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload(float)
  def __truediv__(self, divisor: float) -> QDoubleMatrix4x4:
    """
    Calls Qt's 'QDoubleMatrix4x4 operator/(const QDoubleMatrix4x4 &matrix,
    double divisor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator/

    Parameters
    ----------

    divisor : float
      Passed on as it is.

    Returns
    -------

    QDoubleMatrix4x4
      A new cute QDoubleMatrix4x4 around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleMatrix4x4 operator/(const QDoubleMatrix4x4 &matrix, double
    #      divisor)
    address = Rituals.call(
        'ritual_ZdvRK16QDoubleMatrix4x4d', CuteMixin._valueOf(self), divisor,
    )
    return QDoubleMatrix4x4._cuteOwning(address)

  @overload.fallback
  def __truediv__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QDoubleMatrix4x4 &m)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QDoubleMatrix4x4 &m)
    address = Rituals.call(
        'ritual_Zls6QDebugRK16QDoubleMatrix4x4',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
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
    Notes what was given, for Qt's 'QDoubleMatrix4x4::QDoubleMatrix4x4()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#QDoubleMatrix4x4
    """
    #  QDoubleMatrix4x4::QDoubleMatrix4x4()
    self._noteCreation(QDoubleMatrix4x4, lambda: Rituals.call(
        'ritual_ZN16QDoubleMatrix4x4C1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's
    'QDoubleMatrix4x4::QDoubleMatrix4x4(Qt::Initialization a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#QDoubleMatrix4x4

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QDoubleMatrix4x4::QDoubleMatrix4x4(Qt::Initialization a0)
    self._noteCreation(QDoubleMatrix4x4, lambda: Rituals.call(
        'ritual_ZN16QDoubleMatrix4x4C1EN2Qt14InitializationE', a0.value,
    ))

  @overload(
      float, float, float, float, float, float, float, float, float, float,
      float, float, float, float, float, float,
  )
  def __init__(
      self,
      m11: float,
      m12: float,
      m13: float,
      m14: float,
      m21: float,
      m22: float,
      m23: float,
      m24: float,
      m31: float,
      m32: float,
      m33: float,
      m34: float,
      m41: float,
      m42: float,
      m43: float,
      m44: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDoubleMatrix4x4::QDoubleMatrix4x4(double
    m11, double m12, double m13, double m14, double m21, double m22, double
    m23, double m24, double m31, double m32, double m33, double m34, double
    m41, double m42, double m43, double m44)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#QDoubleMatrix4x4

    Parameters
    ----------

    m11 : float
      Passed on as it is.

    m12 : float
      Passed on as it is.

    m13 : float
      Passed on as it is.

    m14 : float
      Passed on as it is.

    m21 : float
      Passed on as it is.

    m22 : float
      Passed on as it is.

    m23 : float
      Passed on as it is.

    m24 : float
      Passed on as it is.

    m31 : float
      Passed on as it is.

    m32 : float
      Passed on as it is.

    m33 : float
      Passed on as it is.

    m34 : float
      Passed on as it is.

    m41 : float
      Passed on as it is.

    m42 : float
      Passed on as it is.

    m43 : float
      Passed on as it is.

    m44 : float
      Passed on as it is.
    """
    #  QDoubleMatrix4x4::QDoubleMatrix4x4(double m11, double m12, double m13,
    #      double m14, double m21, double m22, double m23, double m24, double
    #      m31, double m32, double m33, double m34, double m41, double m42,
    #      double m43, double m44)
    self._noteCreation(QDoubleMatrix4x4, lambda: Rituals.call(
        'ritual_ZN16QDoubleMatrix4x4C1Edddddddddddddddd',
        m11, m12, m13, m14, m21, m22, m23, m24, m31, m32, m33, m34, m41, m42,
        m43, m44,
    ))

  @overload(int)
  def __init__(self, a0: int) -> None:
    """
    Notes what was given, for Qt's 'QDoubleMatrix4x4::QDoubleMatrix4x4(int
    a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#QDoubleMatrix4x4

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QDoubleMatrix4x4::QDoubleMatrix4x4(int a0)
    self._noteCreation(QDoubleMatrix4x4, lambda: Rituals.call(
        'ritual_ZN16QDoubleMatrix4x4C1Ei', a0,
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

  @overload(float)
  def fill(self, value: float) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::fill(double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#fill

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::fill(double value)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x44fillEd', value)

  @overload(QDoubleVector3D)
  def scale(self, vector: QDoubleVector3D) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::scale(const QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#scale

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  void QDoubleMatrix4x4::scale(const QDoubleVector3D &vector)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x45scaleERK15QDoubleVector3D',
        self._valueOf(vector),
    )

  @overload(float, float)
  def scale(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::scale(double x, double y)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#scale

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::scale(double x, double y)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x45scaleEdd', x, y)

  @overload(float, float, float)
  def scale(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::scale(double x, double y, double z)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#scale

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::scale(double x, double y, double z)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x45scaleEddd', x, y, z)

  @overload(float)
  def scale(self, factor: float) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::scale(double factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#scale

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::scale(double factor)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x45scaleEd', factor)

  @overload(QDoubleVector3D)
  def translate(self, vector: QDoubleVector3D) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::translate(const QDoubleVector3D
    &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#translate

    Parameters
    ----------

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  void QDoubleMatrix4x4::translate(const QDoubleVector3D &vector)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x49translateERK15QDoubleVector3D',
        self._valueOf(vector),
    )

  @overload(float, float)
  def translate(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::translate(double x, double y)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::translate(double x, double y)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x49translateEdd', x, y)

  @overload(float, float, float)
  def translate(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::translate(double x, double y, double
    z)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::translate(double x, double y, double z)
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x49translateEddd', x, y, z)

  @overload(float, QDoubleVector3D)
  def rotate(self, angle: float, vector: QDoubleVector3D) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::rotate(double angle, const
    QDoubleVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    vector : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  void QDoubleMatrix4x4::rotate(double angle, const QDoubleVector3D
    #      &vector)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x46rotateEdRK15QDoubleVector3D',
        angle, self._valueOf(vector),
    )

  @overload(float, float, float)
  @overload(float, float, float, float)
  def rotate(self, angle: float, x: float, y: float, z: float = 0.0) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::rotate(double angle, double x, double
    y, double z)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QDoubleMatrix4x4::rotate(double angle, double x, double y, double
    #      z)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x46rotateEdddd', angle, x, y, z,
    )

  @overload(QRect)
  def ortho(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::ortho(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#ortho

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QDoubleMatrix4x4::ortho(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x45orthoERK5QRect', self._valueOf(rect),
    )

  @overload(QRectF)
  def ortho(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::ortho(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#ortho

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDoubleMatrix4x4::ortho(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x45orthoERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float, float, float)
  def ortho(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::ortho(double left, double right,
    double bottom, double top, double nearPlane, double farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#ortho

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::ortho(double left, double right, double bottom,
    #      double top, double nearPlane, double farPlane)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x45orthoEdddddd',
        left, right, bottom, top, nearPlane, farPlane,
    )

  @overload(float, float, float, float, float, float)
  def frustum(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::frustum(double left, double right,
    double bottom, double top, double nearPlane, double farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#frustum

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::frustum(double left, double right, double
    #      bottom, double top, double nearPlane, double farPlane)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x47frustumEdddddd',
        left, right, bottom, top, nearPlane, farPlane,
    )

  @overload(float, float, float, float)
  def perspective(
      self,
      verticalAngle: float,
      aspectRatio: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::perspective(double verticalAngle,
    double aspectRatio, double nearPlane, double farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#perspective

    Parameters
    ----------

    verticalAngle : float
      Passed on as it is.

    aspectRatio : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void QDoubleMatrix4x4::perspective(double verticalAngle, double
    #      aspectRatio, double nearPlane, double farPlane)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x411perspectiveEdddd',
        verticalAngle, aspectRatio, nearPlane, farPlane,
    )

  @overload(QDoubleVector3D, QDoubleVector3D, QDoubleVector3D)
  def lookAt(
      self,
      eye: QDoubleVector3D,
      center: QDoubleVector3D,
      up: QDoubleVector3D,
  ) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::lookAt(const QDoubleVector3D &eye,
    const QDoubleVector3D &center, const QDoubleVector3D &up)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#lookAt

    Parameters
    ----------

    eye : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    center : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.

    up : QDoubleVector3D
      Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
      Python's own.
    """
    #  void QDoubleMatrix4x4::lookAt(const QDoubleVector3D &eye, const
    #      QDoubleVector3D &center, const QDoubleVector3D &up)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x46lookAtERK15QDoubleVector3DS2_S2_',
        self._valueOf(eye), self._valueOf(center), self._valueOf(up),
    )

  @overload(QRectF)
  def viewport(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::viewport(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#viewport

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDoubleMatrix4x4::viewport(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x48viewportERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, float)
  def viewport(
      self,
      left: float,
      bottom: float,
      width: float,
      height: float,
      nearPlane: float = 0.0,
      farPlane: float = 1.0,
  ) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::viewport(double left, double bottom,
    double width, double height, double nearPlane, double farPlane)'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#viewport

    Parameters
    ----------

    left : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    farPlane : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  void QDoubleMatrix4x4::viewport(double left, double bottom, double
    #      width, double height, double nearPlane, double farPlane)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x48viewportEdddddd',
        left, bottom, width, height, nearPlane, farPlane,
    )

  def flipCoordinates(self) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::flipCoordinates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#flipCoordinates
    """
    #  void QDoubleMatrix4x4::flipCoordinates()
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x415flipCoordinatesEv')

  def optimize(self) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::optimize()'.

    Qt's own words: https://doc.qt.io/qt-6/qdoublematrix4x4.html#optimize
    """
    #  void QDoubleMatrix4x4::optimize()
    self.uglySide.call('ritual_ZN16QDoubleMatrix4x48optimizeEv')

  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  def projectedRotate(
      self,
      angle: float,
      x: float,
      y: float,
      z: float,
      distanceToPlane: float = 1024.0,
  ) -> None:
    """
    Calls Qt's 'void QDoubleMatrix4x4::projectedRotate(double angle, double
    x, double y, double z, double distanceToPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdoublematrix4x4.html#projectedRotate

    Parameters
    ----------

    angle : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    distanceToPlane : float
      Passed on as it is. May be left out, as in Qt: it is then 1024.0.
    """
    #  void QDoubleMatrix4x4::projectedRotate(double angle, double x, double
    #      y, double z, double distanceToPlane)
    self.uglySide.call(
        'ritual_ZN16QDoubleMatrix4x415projectedRotateEddddd',
        angle, x, y, z, distanceToPlane,
    )

  @staticmethod
  def constData(*__, **_) -> Never:
    """
    Qt's 'const double *QDoubleMatrix4x4::constData() const': gives 'double',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDoubleMatrix4x4.constData' has no cute function yet. Qt's 'const "
        "double *QDoubleMatrix4x4::constData() const': gives 'double', "
        "which has no cute class yet.")

  @staticmethod
  def copyDataTo(*__, **_) -> Never:
    """
    Qt's 'void QDoubleMatrix4x4::copyDataTo(double *values) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QDoubleMatrix4x4.copyDataTo' has no cute function yet. Qt's 'void "
        "QDoubleMatrix4x4::copyDataTo(double *values) const': takes a "
        "number to change where it is.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    - Qt's 'const double *QDoubleMatrix4x4::data() const': gives 'double',
      which has no cute class yet.
    - Qt's 'double *QDoubleMatrix4x4::data()': takes or gives a type that
      cannot be passed yet: double *.
    """
    raise NotImplementedError(
        "'QDoubleMatrix4x4.data' has no cute function yet. Qt's 'const "
        "double *QDoubleMatrix4x4::data() const': gives 'double', which has "
        "no cute class yet. Qt's 'double *QDoubleMatrix4x4::data()': takes "
        "or gives a type that cannot be passed yet: double *.")

  @staticmethod
  def inverted(*__, **_) -> Never:
    """
    Qt's 'QDoubleMatrix4x4 QDoubleMatrix4x4::inverted(bool *invertible)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QDoubleMatrix4x4.inverted' has no cute function yet. Qt's "
        "'QDoubleMatrix4x4 QDoubleMatrix4x4::inverted(bool *invertible) "
        "const': takes a number to change where it is.")
