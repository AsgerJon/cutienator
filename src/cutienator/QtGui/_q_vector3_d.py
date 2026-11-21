"""
QVector3D binding of the Qt C++
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
  from ..QtCore import QPoint, QPointF, QRect
  from . import QMatrix4x4, QVector2D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QVector2D = WAIT['QVector2D']
  QVector4D = WAIT['QVector4D']


class QVector3D(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVector3D: a plain Python object standing in front of
  one C++ QVector3D.

  C++ hands a QVector3D around as a copy, so every C++ QVector3D behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QVector3D that has a ritual and that Python can call
  so far, 23 names in all: 'isNull', 'x', 'y', 'z', 'setX', 'setY', 'setZ',
  'length', 'lengthSquared', 'normalized', 'normalize', 'dotProduct',
  'crossProduct', 'normal', 'project', 'unproject', 'distanceToPoint',
  'distanceToPlane', 'distanceToLine', 'toVector2D', 'toVector4D', 'toPoint',
  'toPointF'. It can be made from Python, in 8 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'float QVector3D::operator[](int i) const': an operator, which is
    not reflected yet.
  - Qt's 'QVariant QVector3D::operator QVariant() const': an operator, which
    is not reflected yet.
  - Qt's 'QVector3D::~QVector3D()': the destructor: Python removes its C++
    QVector3D by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 43 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QVector3D is created at the first use, not by 'QVector3D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QVector3D back gives a copy the ritual made for
    Python, in a new cute QVector3D.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(v1: QVector3D, v2: QVector3D) -> float:
    """
    Calls Qt's 'float QVector3D::dotProduct(QVector3D v1, QVector3D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#dotProduct

    Parameters
    ----------

    v1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    v2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QVector3D::dotProduct(QVector3D v1, QVector3D v2)
    return Rituals.call(
        'ritual_ZN9QVector3D10dotProductES_S_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )

  @staticmethod
  @overload(THIS, THIS)
  def crossProduct(v1: QVector3D, v2: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector3D::crossProduct(QVector3D v1, QVector3D
    v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#crossProduct

    Parameters
    ----------

    v1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    v2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector3D::crossProduct(QVector3D v1, QVector3D v2)
    address = Rituals.call(
        'ritual_ZN9QVector3D12crossProductES_S_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )
    return QVector3D._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS)
  def normal(v1: QVector3D, v2: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector3D::normal(QVector3D v1, QVector3D v2)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#normal

    Parameters
    ----------

    v1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    v2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector3D::normal(QVector3D v1, QVector3D v2)
    address = Rituals.call(
        'ritual_ZN9QVector3D6normalES_S_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
    )
    return QVector3D._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS, THIS)
  def normal(v1: QVector3D, v2: QVector3D, v3: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector3D::normal(QVector3D v1, QVector3D v2,
    QVector3D v3)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#normal

    Parameters
    ----------

    v1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    v2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    v3 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector3D::normal(QVector3D v1, QVector3D v2, QVector3D v3)
    address = Rituals.call(
        'ritual_ZN9QVector3D6normalES_S_S_',
        CuteMixin._valueOf(v1), CuteMixin._valueOf(v2),
        CuteMixin._valueOf(v3),
    )
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVector3D'

  #  Qt's '~QVector3D()'. Naming it makes this a value class: Python owns
  #  every C++ QVector3D behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QVector3DD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QVector3D::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#isNull
    """
    #  bool QVector3D::isNull() const
    return self.uglySide.call('ritual_ZNK9QVector3D6isNullEv')

  def x(self) -> float:
    """
    Calls Qt's 'float QVector3D::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#x
    """
    #  float QVector3D::x() const
    return self.uglySide.call('ritual_ZNK9QVector3D1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QVector3D::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#y
    """
    #  float QVector3D::y() const
    return self.uglySide.call('ritual_ZNK9QVector3D1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'float QVector3D::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#z
    """
    #  float QVector3D::z() const
    return self.uglySide.call('ritual_ZNK9QVector3D1zEv')

  def length(self) -> float:
    """
    Calls Qt's 'float QVector3D::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#length
    """
    #  float QVector3D::length() const
    return self.uglySide.call('ritual_ZNK9QVector3D6lengthEv')

  def lengthSquared(self) -> float:
    """
    Calls Qt's 'float QVector3D::lengthSquared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#lengthSquared
    """
    #  float QVector3D::lengthSquared() const
    return self.uglySide.call('ritual_ZNK9QVector3D13lengthSquaredEv')

  def normalized(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector3D::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#normalized

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector3D::normalized() const
    address = self.uglySide.call('ritual_ZNK9QVector3D10normalizedEv')
    return QVector3D._cuteOwning(address)

  @overload(QMatrix4x4, QMatrix4x4, QRect)
  def project(
      self,
      modelView: QMatrix4x4,
      projection: QMatrix4x4,
      viewport: QRect,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector3D::project(const QMatrix4x4 &modelView,
    const QMatrix4x4 &projection, const QRect &viewport) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#project

    Parameters
    ----------

    modelView : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    projection : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector3D::project(const QMatrix4x4 &modelView, const
    #      QMatrix4x4 &projection, const QRect &viewport) const
    address = self.uglySide.call(
        'ritual_ZNK9QVector3D7projectERK10QMatrix4x4S2_RK5QRect',
        self._valueOf(modelView), self._valueOf(projection),
        self._valueOf(viewport),
    )
    return QVector3D._cuteOwning(address)

  @overload(QMatrix4x4, QMatrix4x4, QRect)
  def unproject(
      self,
      modelView: QMatrix4x4,
      projection: QMatrix4x4,
      viewport: QRect,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QVector3D::unproject(const QMatrix4x4 &modelView,
    const QMatrix4x4 &projection, const QRect &viewport) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#unproject

    Parameters
    ----------

    modelView : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    projection : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QVector3D::unproject(const QMatrix4x4 &modelView, const
    #      QMatrix4x4 &projection, const QRect &viewport) const
    address = self.uglySide.call(
        'ritual_ZNK9QVector3D9unprojectERK10QMatrix4x4S2_RK5QRect',
        self._valueOf(modelView), self._valueOf(projection),
        self._valueOf(viewport),
    )
    return QVector3D._cuteOwning(address)

  @overload(THIS)
  def distanceToPoint(self, point: QVector3D) -> float:
    """
    Calls Qt's 'float QVector3D::distanceToPoint(QVector3D point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#distanceToPoint

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QVector3D::distanceToPoint(QVector3D point) const
    return self.uglySide.call(
        'ritual_ZNK9QVector3D15distanceToPointES_', self._valueOf(point),
    )

  @overload(THIS, THIS)
  def distanceToPlane(self, plane: QVector3D, normal: QVector3D) -> float:
    """
    Calls Qt's 'float QVector3D::distanceToPlane(QVector3D plane, QVector3D
    normal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#distanceToPlane

    Parameters
    ----------

    plane : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QVector3D::distanceToPlane(QVector3D plane, QVector3D normal)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QVector3D15distanceToPlaneES_S_',
        self._valueOf(plane), self._valueOf(normal),
    )

  @overload(THIS, THIS, THIS)
  def distanceToPlane(
      self,
      plane1: QVector3D,
      plane2: QVector3D,
      plane3: QVector3D,
  ) -> float:
    """
    Calls Qt's 'float QVector3D::distanceToPlane(QVector3D plane1, QVector3D
    plane2, QVector3D plane3) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#distanceToPlane

    Parameters
    ----------

    plane1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    plane2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    plane3 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QVector3D::distanceToPlane(QVector3D plane1, QVector3D plane2,
    #      QVector3D plane3) const
    return self.uglySide.call(
        'ritual_ZNK9QVector3D15distanceToPlaneES_S_S_',
        self._valueOf(plane1), self._valueOf(plane2), self._valueOf(plane3),
    )

  @overload(THIS, THIS)
  def distanceToLine(self, point: QVector3D, direction: QVector3D) -> float:
    """
    Calls Qt's 'float QVector3D::distanceToLine(QVector3D point, QVector3D
    direction) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#distanceToLine

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float QVector3D::distanceToLine(QVector3D point, QVector3D direction)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QVector3D14distanceToLineES_S_',
        self._valueOf(point), self._valueOf(direction),
    )

  def toVector2D(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QVector3D::toVector2D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#toVector2D

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QVector3D::toVector2D() const
    address = self.uglySide.call('ritual_ZNK9QVector3D10toVector2DEv')
    from . import QVector2D
    return QVector2D._cuteOwning(address)

  def toVector4D(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QVector3D::toVector4D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#toVector4D

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QVector3D::toVector4D() const
    address = self.uglySide.call('ritual_ZNK9QVector3D10toVector4DEv')
    from . import QVector4D
    return QVector4D._cuteOwning(address)

  def toPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QVector3D::toPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#toPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QVector3D::toPoint() const
    address = self.uglySide.call('ritual_ZNK9QVector3D7toPointEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def toPointF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QVector3D::toPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#toPointF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QVector3D::toPointF() const
    address = self.uglySide.call('ritual_ZNK9QVector3D8toPointFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QVector3D::setX(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QVector3D::setX(float x)
    self.uglySide.call('ritual_ZN9QVector3D4setXEf', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QVector3D::setY(float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QVector3D::setY(float y)
    self.uglySide.call('ritual_ZN9QVector3D4setYEf', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QVector3D::setZ(float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QVector3D::setZ(float z)
    self.uglySide.call('ritual_ZN9QVector3D4setZEf', z)

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
    Notes what was given, for Qt's 'QVector3D::QVector3D()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D
    """
    #  QVector3D::QVector3D()
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QVector3D::QVector3D(Qt::Initialization a0)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1EN2Qt14InitializationE', a0.value,
    ))

  @overload(float, float, float)
  def __init__(self, xpos: float, ypos: float, zpos: float) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(float xpos, float
    ypos, float zpos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.

    zpos : float
      Passed on as it is.
    """
    #  QVector3D::QVector3D(float xpos, float ypos, float zpos)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1Efff', xpos, ypos, zpos,
    ))

  @overload(QPoint)
  def __init__(self, point: QPoint) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(QPoint point)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  QVector3D::QVector3D(QPoint point)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1E6QPoint', self._valueOf(point),
    ))

  @overload(QPointF)
  def __init__(self, point: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(QPointF point)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QVector3D::QVector3D(QPointF point)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1E7QPointF', self._valueOf(point),
    ))

  @overload(QVector2D)
  def __init__(self, vector: QVector2D) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(QVector2D vector)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    vector : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  QVector3D::QVector3D(QVector2D vector)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1E9QVector2D', self._valueOf(vector),
    ))

  @overload(QVector2D, float)
  def __init__(self, vector: QVector2D, zpos: float) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(QVector2D vector,
    float zpos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    vector : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    zpos : float
      Passed on as it is.
    """
    #  QVector3D::QVector3D(QVector2D vector, float zpos)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1E9QVector2Df', self._valueOf(vector), zpos,
    ))

  @overload(QVector4D)
  def __init__(self, vector: QVector4D) -> None:
    """
    Notes what was given, for Qt's 'QVector3D::QVector3D(QVector4D vector)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#QVector3D

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QVector3D::QVector3D(QVector4D vector)
    self._noteCreation(QVector3D, lambda: Rituals.call(
        'ritual_ZN9QVector3DC1E9QVector4D', self._valueOf(vector),
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
    Calls Qt's 'void QVector3D::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qvector3d.html#normalize
    """
    #  void QVector3D::normalize()
    self.uglySide.call('ritual_ZN9QVector3D9normalizeEv')
