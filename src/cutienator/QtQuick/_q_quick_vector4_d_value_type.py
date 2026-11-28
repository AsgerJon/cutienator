"""
QQuickVector4DValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickVector4DValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QVector4D

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtGui import QMatrix4x4, QVector2D, QVector3D
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QMatrix4x4 = WAIT['QMatrix4x4']


class QQuickVector4DValueType(QVector4D):
  """
  The cute side of Qt's QQuickVector4DValueType: a plain Python object
  standing in front of one C++ QQuickVector4DValueType.

  It is built on the cute 'QVector4D', as Qt's QQuickVector4DValueType is
  built on Qt's QVector4D, and has everything that class has.

  C++ hands a QQuickVector4DValueType around as a copy, so every C++
  QQuickVector4DValueType behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickVector4DValueType that has a ritual and that
  Python can call so far, 19 names in all: 'create', 'toString', 'x', 'y',
  'z', 'w', 'setX', 'setY', 'setZ', 'setW', 'dotProduct', 'times', 'plus',
  'minus', 'normalized', 'length', 'toVector2d', 'toVector3d', 'fuzzyEquals'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickVector4DValueType::qt_qmlMarker_foreign()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickVector4DValueType::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'QQuickVector4DValueType::~QQuickVector4DValueType()': the
    destructor: Python removes its C++ QQuickVector4DValueType by it, and has
    no other use for it.

  What has no ritual
  ------------------

  3 of the 30 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickVector4DValueType is created at the first use, not by
    'QQuickVector4DValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickVector4DValueType back gives a copy the ritual
    made for Python, in a new cute QQuickVector4DValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickVector4DValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#create

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
    #  QVariant QQuickVector4DValueType::create(const QJSValue &params)
    address = Rituals.call(
        'ritual_ZN23QQuickVector4DValueType6createERK8QJSValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVector4DValueType'

  #  Qt's '~QQuickVector4DValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickVector4DValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQuickVector4DValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQuickVector4DValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickVector4DValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType8toStringEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector4DValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#x
    """
    #  qreal QQuickVector4DValueType::x() const
    return self.uglySide.call('ritual_ZNK23QQuickVector4DValueType1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector4DValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#y
    """
    #  qreal QQuickVector4DValueType::y() const
    return self.uglySide.call('ritual_ZNK23QQuickVector4DValueType1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector4DValueType::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#z
    """
    #  qreal QQuickVector4DValueType::z() const
    return self.uglySide.call('ritual_ZNK23QQuickVector4DValueType1zEv')

  def w(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector4DValueType::w() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#w
    """
    #  qreal QQuickVector4DValueType::w() const
    return self.uglySide.call('ritual_ZNK23QQuickVector4DValueType1wEv')

  @overload(QVector4D)
  def dotProduct(self, vec: QVector4D) -> float:
    """
    Calls Qt's 'qreal QQuickVector4DValueType::dotProduct(const QVector4D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#dotProduct

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  qreal QQuickVector4DValueType::dotProduct(const QVector4D &vec) const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType10dotProductERK9QVector4D',
        self._valueOf(vec),
    )

  @overload(QVector4D)
  def times(self, vec: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector4DValueType::times(const QVector4D
    &vec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#times

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector4DValueType::times(const QVector4D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType5timesERK9QVector4D',
        self._valueOf(vec),
    )
    return QVector4D._cuteOwning(address)

  @overload(QMatrix4x4)
  def times(self, m: QMatrix4x4) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector4DValueType::times(const QMatrix4x4 &m)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#times

    Parameters
    ----------

    m : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector4DValueType::times(const QMatrix4x4 &m) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType5timesERK10QMatrix4x4',
        self._valueOf(m),
    )
    return QVector4D._cuteOwning(address)

  @overload(float)
  def times(self, scalar: float) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector4DValueType::times(qreal scalar)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#times

    Parameters
    ----------

    scalar : float
      Passed on as it is.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector4DValueType::times(qreal scalar) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType5timesEd', scalar,
    )
    return QVector4D._cuteOwning(address)

  @overload(QVector4D)
  def plus(self, vec: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector4DValueType::plus(const QVector4D &vec)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#plus

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector4DValueType::plus(const QVector4D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType4plusERK9QVector4D',
        self._valueOf(vec),
    )
    return QVector4D._cuteOwning(address)

  @overload(QVector4D)
  def minus(self, vec: QVector4D) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector4DValueType::minus(const QVector4D
    &vec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#minus

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector4DValueType::minus(const QVector4D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType5minusERK9QVector4D',
        self._valueOf(vec),
    )
    return QVector4D._cuteOwning(address)

  def normalized(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector4DValueType::normalized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#normalized

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector4DValueType::normalized() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType10normalizedEv',
    )
    return QVector4D._cuteOwning(address)

  def length(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector4DValueType::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#length
    """
    #  qreal QQuickVector4DValueType::length() const
    return self.uglySide.call('ritual_ZNK23QQuickVector4DValueType6lengthEv')

  def toVector2d(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickVector4DValueType::toVector2d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#toVector2d

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickVector4DValueType::toVector2d() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType10toVector2dEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def toVector3d(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickVector4DValueType::toVector3d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#toVector3d

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickVector4DValueType::toVector3d() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType10toVector3dEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector4D, float)
  def fuzzyEquals(self, vec: QVector4D, epsilon: float) -> bool:
    """
    Calls Qt's 'bool QQuickVector4DValueType::fuzzyEquals(const QVector4D
    &vec, qreal epsilon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#fuzzyEquals

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    epsilon : float
      Passed on as it is.
    """
    #  bool QQuickVector4DValueType::fuzzyEquals(const QVector4D &vec, qreal
    #      epsilon) const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType11fuzzyEqualsERK9QVector4Dd',
        self._valueOf(vec), epsilon,
    )

  @overload(QVector4D)
  def fuzzyEquals(self, vec: QVector4D) -> bool:
    """
    Calls Qt's 'bool QQuickVector4DValueType::fuzzyEquals(const QVector4D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#fuzzyEquals

    Parameters
    ----------

    vec : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  bool QQuickVector4DValueType::fuzzyEquals(const QVector4D &vec) const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector4DValueType11fuzzyEqualsERK9QVector4D',
        self._valueOf(vec),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickVector4DValueType::setX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickVector4DValueType::setX(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickVector4DValueType4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickVector4DValueType::setY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickVector4DValueType::setY(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickVector4DValueType4setYEd', a0)

  @overload(float)
  def setZ(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickVector4DValueType::setZ(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#setZ

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickVector4DValueType::setZ(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickVector4DValueType4setZEd', a0)

  @overload(float)
  def setW(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickVector4DValueType::setW(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector4dvaluetype.html#setW

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickVector4DValueType::setW(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickVector4DValueType4setWEd', a0)

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
    'QQuickVector4DValueType::QQuickVector4DValueType()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html
    """
    #  QQuickVector4DValueType::QQuickVector4DValueType()
    self._noteCreation(QQuickVector4DValueType, lambda: Rituals.call(
        'ritual_ZN23QQuickVector4DValueTypeC1Ev',
    ))

  @overload(QVector4D)
  def __init__(self, vector4d: QVector4D) -> None:
    """
    Notes what was given, for Qt's
    'QQuickVector4DValueType::QQuickVector4DValueType(const QVector4D
    &vector4d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector4dvaluetype.html

    Parameters
    ----------

    vector4d : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QQuickVector4DValueType::QQuickVector4DValueType(const QVector4D
    #      &vector4d)
    self._noteCreation(QQuickVector4DValueType, lambda: Rituals.call(
        'ritual_ZN23QQuickVector4DValueTypeC1ERK9QVector4D',
        self._valueOf(vector4d),
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
