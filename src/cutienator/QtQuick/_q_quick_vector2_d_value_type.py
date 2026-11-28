"""
QQuickVector2DValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickVector2DValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QVector2D

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtGui import QVector3D, QVector4D
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QQuickVector2DValueType(QVector2D):
  """
  The cute side of Qt's QQuickVector2DValueType: a plain Python object
  standing in front of one C++ QQuickVector2DValueType.

  It is built on the cute 'QVector2D', as Qt's QQuickVector2DValueType is
  built on Qt's QVector2D, and has everything that class has.

  C++ hands a QQuickVector2DValueType around as a copy, so every C++
  QQuickVector2DValueType behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickVector2DValueType that has a ritual and that
  Python can call so far, 15 names in all: 'create', 'toString', 'x', 'y',
  'setX', 'setY', 'dotProduct', 'times', 'plus', 'minus', 'normalized',
  'length', 'toVector3d', 'toVector4d', 'fuzzyEquals'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickVector2DValueType::qt_qmlMarker_foreign()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickVector2DValueType::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'QQuickVector2DValueType::~QQuickVector2DValueType()': the
    destructor: Python removes its C++ QQuickVector2DValueType by it, and has
    no other use for it.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickVector2DValueType is created at the first use, not by
    'QQuickVector2DValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickVector2DValueType back gives a copy the ritual
    made for Python, in a new cute QQuickVector2DValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickVector2DValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#create

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
    #  QVariant QQuickVector2DValueType::create(const QJSValue &params)
    address = Rituals.call(
        'ritual_ZN23QQuickVector2DValueType6createERK8QJSValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVector2DValueType'

  #  Qt's '~QQuickVector2DValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickVector2DValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QQuickVector2DValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQuickVector2DValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickVector2DValueType::toString() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType8toStringEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector2DValueType::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#x
    """
    #  qreal QQuickVector2DValueType::x() const
    return self.uglySide.call('ritual_ZNK23QQuickVector2DValueType1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector2DValueType::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#y
    """
    #  qreal QQuickVector2DValueType::y() const
    return self.uglySide.call('ritual_ZNK23QQuickVector2DValueType1yEv')

  @overload(QVector2D)
  def dotProduct(self, vec: QVector2D) -> float:
    """
    Calls Qt's 'qreal QQuickVector2DValueType::dotProduct(const QVector2D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#dotProduct

    Parameters
    ----------

    vec : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  qreal QQuickVector2DValueType::dotProduct(const QVector2D &vec) const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType10dotProductERK9QVector2D',
        self._valueOf(vec),
    )

  @overload(QVector2D)
  def times(self, vec: QVector2D) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickVector2DValueType::times(const QVector2D
    &vec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#times

    Parameters
    ----------

    vec : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickVector2DValueType::times(const QVector2D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType5timesERK9QVector2D',
        self._valueOf(vec),
    )
    return QVector2D._cuteOwning(address)

  @overload(float)
  def times(self, scalar: float) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickVector2DValueType::times(qreal scalar)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#times

    Parameters
    ----------

    scalar : float
      Passed on as it is.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickVector2DValueType::times(qreal scalar) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType5timesEd', scalar,
    )
    return QVector2D._cuteOwning(address)

  @overload(QVector2D)
  def plus(self, vec: QVector2D) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickVector2DValueType::plus(const QVector2D &vec)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#plus

    Parameters
    ----------

    vec : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickVector2DValueType::plus(const QVector2D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType4plusERK9QVector2D',
        self._valueOf(vec),
    )
    return QVector2D._cuteOwning(address)

  @overload(QVector2D)
  def minus(self, vec: QVector2D) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickVector2DValueType::minus(const QVector2D
    &vec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#minus

    Parameters
    ----------

    vec : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickVector2DValueType::minus(const QVector2D &vec) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType5minusERK9QVector2D',
        self._valueOf(vec),
    )
    return QVector2D._cuteOwning(address)

  def normalized(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickVector2DValueType::normalized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#normalized

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickVector2DValueType::normalized() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType10normalizedEv',
    )
    return QVector2D._cuteOwning(address)

  def length(self) -> float:
    """
    Calls Qt's 'qreal QQuickVector2DValueType::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#length
    """
    #  qreal QQuickVector2DValueType::length() const
    return self.uglySide.call('ritual_ZNK23QQuickVector2DValueType6lengthEv')

  def toVector3d(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickVector2DValueType::toVector3d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#toVector3d

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickVector2DValueType::toVector3d() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType10toVector3dEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def toVector4d(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickVector2DValueType::toVector4d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#toVector4d

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickVector2DValueType::toVector4d() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType10toVector4dEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  @overload(QVector2D, float)
  def fuzzyEquals(self, vec: QVector2D, epsilon: float) -> bool:
    """
    Calls Qt's 'bool QQuickVector2DValueType::fuzzyEquals(const QVector2D
    &vec, qreal epsilon) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#fuzzyEquals

    Parameters
    ----------

    vec : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    epsilon : float
      Passed on as it is.
    """
    #  bool QQuickVector2DValueType::fuzzyEquals(const QVector2D &vec, qreal
    #      epsilon) const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType11fuzzyEqualsERK9QVector2Dd',
        self._valueOf(vec), epsilon,
    )

  @overload(QVector2D)
  def fuzzyEquals(self, vec: QVector2D) -> bool:
    """
    Calls Qt's 'bool QQuickVector2DValueType::fuzzyEquals(const QVector2D
    &vec) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#fuzzyEquals

    Parameters
    ----------

    vec : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  bool QQuickVector2DValueType::fuzzyEquals(const QVector2D &vec) const
    return self.uglySide.call(
        'ritual_ZNK23QQuickVector2DValueType11fuzzyEqualsERK9QVector2D',
        self._valueOf(vec),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickVector2DValueType::setX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickVector2DValueType::setX(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickVector2DValueType4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickVector2DValueType::setY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickvector2dvaluetype.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickVector2DValueType::setY(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickVector2DValueType4setYEd', a0)

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
    'QQuickVector2DValueType::QQuickVector2DValueType()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html
    """
    #  QQuickVector2DValueType::QQuickVector2DValueType()
    self._noteCreation(QQuickVector2DValueType, lambda: Rituals.call(
        'ritual_ZN23QQuickVector2DValueTypeC1Ev',
    ))

  @overload(QVector2D)
  def __init__(self, vector2D: QVector2D) -> None:
    """
    Notes what was given, for Qt's
    'QQuickVector2DValueType::QQuickVector2DValueType(const QVector2D
    &vector2D)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvector2dvaluetype.html

    Parameters
    ----------

    vector2D : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  QQuickVector2DValueType::QQuickVector2DValueType(const QVector2D
    #      &vector2D)
    self._noteCreation(QQuickVector2DValueType, lambda: Rituals.call(
        'ritual_ZN23QQuickVector2DValueTypeC1ERK9QVector2D',
        self._valueOf(vector2D),
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
