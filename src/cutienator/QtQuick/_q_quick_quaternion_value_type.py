"""
QQuickQuaternionValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickQuaternionValueType to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QQuaternion

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtGui import QVector3D, QVector4D
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QVector3D = WAIT['QVector3D']


class QQuickQuaternionValueType(QQuaternion):
  """
  The cute side of Qt's QQuickQuaternionValueType: a plain Python object
  standing in front of one C++ QQuickQuaternionValueType.

  It is built on the cute 'QQuaternion', as Qt's QQuickQuaternionValueType is
  built on Qt's QQuaternion, and has everything that class has.

  C++ hands a QQuickQuaternionValueType around as a copy, so every C++
  QQuickQuaternionValueType behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickQuaternionValueType that has a ritual and that
  Python can call so far, 21 names in all: 'create', 'toString', 'scalar',
  'x', 'y', 'z', 'setScalar', 'setX', 'setY', 'setZ', 'dotProduct', 'times',
  'plus', 'minus', 'normalized', 'inverted', 'conjugated', 'length',
  'toEulerAngles', 'toVector4d', 'fuzzyEquals'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickQuaternionValueType::qt_qmlMarker_foreign()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickQuaternionValueType::qt_qmlMarker_extended()': one of
    Qt's own inner workings.
  - Qt's 'QQuickQuaternionValueType::~QQuickQuaternionValueType()': the
    destructor: Python removes its C++ QQuickQuaternionValueType by it, and
    has no other use for it.

  What has no ritual
  ------------------

  3 of the 32 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickQuaternionValueType is created at the first use, not by
    'QQuickQuaternionValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickQuaternionValueType back gives a copy the
    ritual made for Python, in a new cute QQuickQuaternionValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickQuaternionValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#create

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
    #  QVariant QQuickQuaternionValueType::create(const QJSValue &params)
    address = Rituals.call(
        'ritual_ZN25QQuickQuaternionValueType6createERK8QJSValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickQuaternionValueType'

  #  Qt's '~QQuickQuaternionValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickQuaternionValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QQuickQuaternionValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQuickQuaternionValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickQuaternionValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType8toStringEv',
    )

  def scalar(self) -> float:
    """
    Calls Qt's 'qreal QQuickQuaternionValueType::scalar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#scalar
    """
    #  qreal QQuickQuaternionValueType::scalar() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType6scalarEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickQuaternionValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#x
    """
    #  qreal QQuickQuaternionValueType::x() const
    return self.uglySide.call('ritual_ZNK25QQuickQuaternionValueType1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickQuaternionValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#y
    """
    #  qreal QQuickQuaternionValueType::y() const
    return self.uglySide.call('ritual_ZNK25QQuickQuaternionValueType1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QQuickQuaternionValueType::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#z
    """
    #  qreal QQuickQuaternionValueType::z() const
    return self.uglySide.call('ritual_ZNK25QQuickQuaternionValueType1zEv')

  @overload(QQuaternion)
  def dotProduct(self, q: QQuaternion) -> float:
    """
    Calls Qt's 'qreal QQuickQuaternionValueType::dotProduct(const QQuaternion
    &q) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#dotProduct

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  qreal QQuickQuaternionValueType::dotProduct(const QQuaternion &q)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType10dotProductERK11QQuaternion',
        self._valueOf(q),
    )

  @overload(QQuaternion)
  def times(self, q: QQuaternion) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::times(const
    QQuaternion &q) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#times

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::times(const QQuaternion &q)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType5timesERK11QQuaternion',
        self._valueOf(q),
    )
    return QQuaternion._cuteOwning(address)

  @overload(QVector3D)
  def times(self, vec: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickQuaternionValueType::times(const QVector3D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#times

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
    #  QVector3D QQuickQuaternionValueType::times(const QVector3D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType5timesERK9QVector3D',
        self._valueOf(vec),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(float)
  def times(self, factor: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::times(qreal factor)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#times

    Parameters
    ----------

    factor : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::times(qreal factor) const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType5timesEd', factor,
    )
    return QQuaternion._cuteOwning(address)

  @overload(QQuaternion)
  def plus(self, q: QQuaternion) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::plus(const QQuaternion
    &q) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#plus

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::plus(const QQuaternion &q)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType4plusERK11QQuaternion',
        self._valueOf(q),
    )
    return QQuaternion._cuteOwning(address)

  @overload(QQuaternion)
  def minus(self, q: QQuaternion) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::minus(const
    QQuaternion &q) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#minus

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::minus(const QQuaternion &q)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType5minusERK11QQuaternion',
        self._valueOf(q),
    )
    return QQuaternion._cuteOwning(address)

  def normalized(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::normalized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#normalized

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::normalized() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType10normalizedEv',
    )
    return QQuaternion._cuteOwning(address)

  def inverted(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::inverted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#inverted

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::inverted() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType8invertedEv',
    )
    return QQuaternion._cuteOwning(address)

  def conjugated(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuickQuaternionValueType::conjugated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#conjugated

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuickQuaternionValueType::conjugated() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType10conjugatedEv',
    )
    return QQuaternion._cuteOwning(address)

  def length(self) -> float:
    """
    Calls Qt's 'qreal QQuickQuaternionValueType::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#length
    """
    #  qreal QQuickQuaternionValueType::length() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType6lengthEv',
    )

  def toEulerAngles(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickQuaternionValueType::toEulerAngles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#toEulerAngles

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickQuaternionValueType::toEulerAngles() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType13toEulerAnglesEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def toVector4d(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickQuaternionValueType::toVector4d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#toVector4d

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickQuaternionValueType::toVector4d() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType10toVector4dEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(QQuaternion, float)
  def fuzzyEquals(self, q: QQuaternion, epsilon: float) -> bool:
    """
    Calls Qt's 'bool QQuickQuaternionValueType::fuzzyEquals(const QQuaternion
    &q, qreal epsilon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#fuzzyEquals

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    epsilon : float
      Passed on as it is.
    """
    #  bool QQuickQuaternionValueType::fuzzyEquals(const QQuaternion &q,
    #      qreal epsilon) const
    return self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType11fuzzyEqualsERK11QQuaternion'
        'd',
        self._valueOf(q), epsilon,
    )

  @overload(QQuaternion)
  def fuzzyEquals(self, q: QQuaternion) -> bool:
    """
    Calls Qt's 'bool QQuickQuaternionValueType::fuzzyEquals(const QQuaternion
    &q) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#fuzzyEquals

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  bool QQuickQuaternionValueType::fuzzyEquals(const QQuaternion &q)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QQuickQuaternionValueType11fuzzyEqualsERK11QQuaternion',
        self._valueOf(q),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setScalar(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickQuaternionValueType::setScalar(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#setScalar

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickQuaternionValueType::setScalar(qreal a0)
    self.uglySide.call(
        'ritual_ZN25QQuickQuaternionValueType9setScalarEd', a0,
    )

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickQuaternionValueType::setX(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickQuaternionValueType::setX(qreal a0)
    self.uglySide.call('ritual_ZN25QQuickQuaternionValueType4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickQuaternionValueType::setY(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickQuaternionValueType::setY(qreal a0)
    self.uglySide.call('ritual_ZN25QQuickQuaternionValueType4setYEd', a0)

  @overload(float)
  def setZ(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickQuaternionValueType::setZ(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html#setZ

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickQuaternionValueType::setZ(qreal a0)
    self.uglySide.call('ritual_ZN25QQuickQuaternionValueType4setZEd', a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickQuaternionValueType::QQuickQuaternionValueType()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html
    """
    #  QQuickQuaternionValueType::QQuickQuaternionValueType()
    self._noteCreation(QQuickQuaternionValueType, lambda: Rituals.call(
        'ritual_ZN25QQuickQuaternionValueTypeC1Ev',
    ))

  @overload(QQuaternion)
  def __init__(self, quat: QQuaternion) -> None:
    """
    Notes what was given, for Qt's
    'QQuickQuaternionValueType::QQuickQuaternionValueType(const QQuaternion
    &quat)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickquaternionvaluetype.html

    Parameters
    ----------

    quat : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  QQuickQuaternionValueType::QQuickQuaternionValueType(const QQuaternion
    #      &quat)
    self._noteCreation(QQuickQuaternionValueType, lambda: Rituals.call(
        'ritual_ZN25QQuickQuaternionValueTypeC1ERK11QQuaternion',
        self._valueOf(quat),
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
