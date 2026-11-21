"""
QVector2D binding of the Qt C++
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
  from . import QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']


class QVector2D(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVector2D: a plain Python object standing in front of
  one C++ QVector2D.

  C++ hands a QVector2D around as a copy, so every C++ QVector2D behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVector2D that has a ritual and that Python can call
  so far, 16 names in all: 'isNull', 'x', 'y', 'setX', 'setY', 'length',
  'lengthSquared', 'normalized', 'normalize', 'distanceToPoint',
  'distanceToLine', 'dotProduct', 'toVector3D', 'toVector4D', 'toPoint',
  'toPointF'. It can be made from Python, in 7 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'float QVector2D::operator[](int i) const': an operator, which is
    not reflected yet.
  - Qt's 'QVariant QVector2D::operator QVariant() const': an operator, which
    is not reflected yet.
  - Qt's 'QVector2D::~QVector2D()': the destructor: Python removes its C++
    QVector2D by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 33 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QVector2D is created at the first use, not by 'QVector2D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVector2D back gives a copy the ritual made for
    Python, in a new cute QVector2D.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(v1: QVector2D, v2: QVector2D) -> float:
    """
    Calls Qt's 'float QVector2D::dotProduct(QVector2D v1, QVector2D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#dotProduct

    Parameters
    ----------

    v1 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    v2 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  float QVector2D::dotProduct(QVector2D v1, QVector2D v2)
    return Rituals.call(
        'ritual_ZN9QVector2D10dotProductES_S_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVector2D'

  #  Qt's '~QVector2D()'. Naming it makes this a value class: Python owns
  #  every C++ QVector2D behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QVector2DD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QVector2D::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#isNull
    """
    #  bool QVector2D::isNull() const
    return self.uglySide.call('ritual_ZNK9QVector2D6isNullEv')

  def x(self) -> float:
    """
    Calls Qt's 'float QVector2D::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#x
    """
    #  float QVector2D::x() const
    return self.uglySide.call('ritual_ZNK9QVector2D1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QVector2D::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#y
    """
    #  float QVector2D::y() const
    return self.uglySide.call('ritual_ZNK9QVector2D1yEv')

  def length(self) -> float:
    """
    Calls Qt's 'float QVector2D::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#length
    """
    #  float QVector2D::length() const
    return self.uglySide.call('ritual_ZNK9QVector2D6lengthEv')

  def lengthSquared(self) -> float:
    """
    Calls Qt's 'float QVector2D::lengthSquared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#lengthSquared
    """
    #  float QVector2D::lengthSquared() const
    return self.uglySide.call('ritual_ZNK9QVector2D13lengthSquaredEv')

  def normalized(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QVector2D::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#normalized

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QVector2D::normalized() const
    address = self.uglySide.call('ritual_ZNK9QVector2D10normalizedEv')
    return QVector2D._cuteOwning(address)

  @overload(THIS)
  def distanceToPoint(self, point: QVector2D) -> float:
    """
    Calls Qt's 'float QVector2D::distanceToPoint(QVector2D point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#distanceToPoint

    Parameters
    ----------

    point : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  float QVector2D::distanceToPoint(QVector2D point) const
    return self.uglySide.call(
        'ritual_ZNK9QVector2D15distanceToPointES_', self._valueOf(point),
    )

  @overload(THIS, THIS)
  def distanceToLine(self, point: QVector2D, direction: QVector2D) -> float:
    """
    Calls Qt's 'float QVector2D::distanceToLine(QVector2D point, QVector2D
    direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#distanceToLine

    Parameters
    ----------

    point : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    direction : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  float QVector2D::distanceToLine(QVector2D point, QVector2D direction)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QVector2D14distanceToLineES_S_',
        self._valueOf(point), self._valueOf(direction),
    )

  def toVector3D(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector2D::toVector3D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#toVector3D

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector2D::toVector3D() const
    address = self.uglySide.call('ritual_ZNK9QVector2D10toVector3DEv')
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  def toVector4D(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QVector2D::toVector4D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#toVector4D

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QVector2D::toVector4D() const
    address = self.uglySide.call('ritual_ZNK9QVector2D10toVector4DEv')
    from . import QVector4D
    return QVector4D._cuteOwning(address)

  def toPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QVector2D::toPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#toPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QVector2D::toPoint() const
    address = self.uglySide.call('ritual_ZNK9QVector2D7toPointEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QVector2D::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QVector2D::toPointF() const
    address = self.uglySide.call('ritual_ZNK9QVector2D8toPointFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QVector2D::setX(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QVector2D::setX(float x)
    self.uglySide.call('ritual_ZN9QVector2D4setXEf', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QVector2D::setY(float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QVector2D::setY(float y)
    self.uglySide.call('ritual_ZN9QVector2D4setYEf', y)

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
    Notes what was given, for Qt's 'QVector2D::QVector2D()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D
    """
    #  QVector2D::QVector2D()
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QVector2D::QVector2D(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QVector2D::QVector2D(Qt::Initialization a0)
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1EN2Qt14InitializationE', a0.value,
    ))

  @overload(float, float)
  def __init__(self, xpos: float, ypos: float) -> None:
    """
    Notes what was given, for Qt's 'QVector2D::QVector2D(float xpos, float
    ypos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.
    """
    #  QVector2D::QVector2D(float xpos, float ypos)
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1Eff', xpos, ypos,
    ))

  @overload(QPoint)
  def __init__(self, point: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QVector2D::QVector2D(QPoint point)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QVector2D::QVector2D(QPoint point)
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1E6QPoint', self._valueOf(point),
    ))

  @overload(QPointF)
  def __init__(self, point: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QVector2D::QVector2D(QPointF point)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QVector2D::QVector2D(QPointF point)
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1E7QPointF', self._valueOf(point),
    ))

  @overload(QVector3D)
  def __init__(self, vector: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QVector2D::QVector2D(QVector3D vector)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QVector2D::QVector2D(QVector3D vector)
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1E9QVector3D', self._valueOf(vector),
    ))

  @overload(QVector4D)
  def __init__(self, vector: QVector4D) -> None:
    """
    Notes what was given, for Qt's 'QVector2D::QVector2D(QVector4D vector)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#QVector2D

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QVector2D::QVector2D(QVector4D vector)
    self._noteCreation(QVector2D, lambda: Rituals.call(
        'ritual_ZN9QVector2DC1E9QVector4D', self._valueOf(vector),
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
    Calls Qt's 'void QVector2D::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvector2d.html#normalize
    """
    #  void QVector2D::normalize()
    self.uglySide.call('ritual_ZN9QVector2D9normalizeEv')
