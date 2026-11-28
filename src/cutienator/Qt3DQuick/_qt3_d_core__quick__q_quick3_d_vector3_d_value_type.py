"""
Qt3DCore::Quick::QQuick3DVector3DValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::QQuick3DVector3DValueType to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtGui import QMatrix4x4, QVector2D, QVector3D, QVector4D
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']


class QQuick3DVector3DValueType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::Quick::QQuick3DVector3DValueType: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::QQuick3DVector3DValueType.

  C++ hands a Qt3DCore::Quick::QQuick3DVector3DValueType around as a copy, so
  every C++ Qt3DCore::Quick::QQuick3DVector3DValueType behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::QQuick3DVector3DValueType that has
  a ritual and that Python can call so far, 18 names in all: 'create',
  'toString', 'x', 'y', 'z', 'setX', 'setY', 'setZ', 'crossProduct',
  'dotProduct', 'times', 'plus', 'minus', 'normalized', 'length',
  'toVector2d', 'toVector4d', 'fuzzyEquals'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DCore::Quick::QQuick3DVector3DValueType::qt_qmlMarker_foreign()': one
    of Qt's own inner workings.
  - Qt's 'void
    Qt3DCore::Quick::QQuick3DVector3DValueType::qt_qmlMarker_extended()': one
    of Qt's own inner workings.
  - Qt's
    'Qt3DCore::Quick::QQuick3DVector3DValueType::~QQuick3DVector3DValueType(
    )': the destructor: Python removes its C++
    Qt3DCore::Quick::QQuick3DVector3DValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 27 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::QQuick3DVector3DValueType is created at the
    first use, not by 'Qt3DCore::Quick::QQuick3DVector3DValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::Quick::QQuick3DVector3DValueType back gives
    a copy the ritual made for Python, in a new cute
    Qt3DCore::Quick::QQuick3DVector3DValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::Quick::QQuick3DVector3DValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    params : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::QQuick3DVector3DValueType::create(const
    #      QJSValue &params)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType6createERK8QJSV'
        'alue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::QQuick3DVector3DValueType'

  #  Qt's '~Qt3DCore::Quick::QQuick3DVector3DValueType()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DCore::Quick::QQuick3DVector3DValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueTypeD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::Quick::QQuick3DVector3DValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::Quick::QQuick3DVector3DValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType8toStringEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DVector3DValueType::x() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#x
    """
    #  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::x() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType1xEv',
    )

  def y(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DVector3DValueType::y() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#y
    """
    #  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::y() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType1yEv',
    )

  def z(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DVector3DValueType::z() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#z
    """
    #  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::z() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType1zEv',
    )

  @overload(QVector3D)
  def crossProduct(self, vec: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::crossProduct(const QVector3D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D
    #      Qt3DCore::Quick::QQuick3DVector3DValueType::crossProduct(const
    #      QVector3D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType12crossProduct'
        'ERK9QVector3D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def dotProduct(self, vec: QVector3D) -> float:
    """
    Calls Qt's 'qreal
    Qt3DCore::Quick::QQuick3DVector3DValueType::dotProduct(const QVector3D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::dotProduct(const
    #      QVector3D &vec) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10dotProductER'
        'K9QVector3D',
        self._valueOf(vec),
    )

  @overload(QMatrix4x4)
  def times(self, m: QMatrix4x4) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::times(const QMatrix4x4 &m)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::times(const
    #      QMatrix4x4 &m) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5timesERK10QMa'
        'trix4x4',
        self._valueOf(m),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def times(self, vec: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::times(const QVector3D &vec)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::times(const
    #      QVector3D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5timesERK9QVec'
        'tor3D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(float)
  def times(self, scalar: float) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::times(qreal scalar) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    scalar : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::times(qreal
    #      scalar) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5timesEd',
        scalar,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def plus(self, vec: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::plus(const QVector3D &vec)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#plus

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::plus(const
    #      QVector3D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType4plusERK9QVect'
        'or3D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def minus(self, vec: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::minus(const QVector3D &vec)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::minus(const
    #      QVector3D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5minusERK9QVec'
        'tor3D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def normalized(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    Qt3DCore::Quick::QQuick3DVector3DValueType::normalized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::normalized()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10normalizedEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def length(self) -> float:
    """
    Calls Qt's 'qreal Qt3DCore::Quick::QQuick3DVector3DValueType::length()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html
    """
    #  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::length() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType6lengthEv',
    )

  def toVector2d(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D
    Qt3DCore::Quick::QQuick3DVector3DValueType::toVector2d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D Qt3DCore::Quick::QQuick3DVector3DValueType::toVector2d()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10toVector2dEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def toVector4d(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D
    Qt3DCore::Quick::QQuick3DVector3DValueType::toVector4d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D Qt3DCore::Quick::QQuick3DVector3DValueType::toVector4d()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10toVector4dEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(QVector3D, float)
  def fuzzyEquals(self, vec: QVector3D, epsilon: float) -> bool:
    """
    Calls Qt's 'bool
    Qt3DCore::Quick::QQuick3DVector3DValueType::fuzzyEquals(const QVector3D
    &vec, qreal epsilon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    epsilon : float
      Passed on as it is.
    """
    #  bool Qt3DCore::Quick::QQuick3DVector3DValueType::fuzzyEquals(const
    #      QVector3D &vec, qreal epsilon) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType11fuzzyEqualsE'
        'RK9QVector3Dd',
        self._valueOf(vec), epsilon,
    )

  @overload(QVector3D)
  def fuzzyEquals(self, vec: QVector3D) -> bool:
    """
    Calls Qt's 'bool
    Qt3DCore::Quick::QQuick3DVector3DValueType::fuzzyEquals(const QVector3D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html

    Parameters
    ----------

    vec : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool Qt3DCore::Quick::QQuick3DVector3DValueType::fuzzyEquals(const
    #      QVector3D &vec) const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType11fuzzyEqualsE'
        'RK9QVector3D',
        self._valueOf(vec),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DVector3DValueType::setX(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DVector3DValueType::setX(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType4setXEd', a0,
    )

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DVector3DValueType::setY(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DVector3DValueType::setY(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType4setYEd', a0,
    )

  @overload(float)
  def setZ(self, a0: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::QQuick3DVector3DValueType::setZ(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-qquick3dvector3dvaluetype.html#setZ

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::QQuick3DVector3DValueType::setZ(qreal a0)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType4setZEd', a0,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
