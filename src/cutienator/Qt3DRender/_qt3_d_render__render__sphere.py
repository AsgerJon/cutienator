"""
Qt3DRender::Render::Sphere binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/sphere_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Sphere to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']


class Sphere(Qt3DRender.RayCasting.BoundingSphere):
  """
  The cute side of Qt's Qt3DRender::Render::Sphere: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Sphere.

  It is built on the cute 'Qt3DRender::RayCasting::BoundingSphere', as Qt's
  Qt3DRender::Render::Sphere is built on Qt's
  Qt3DRender::RayCasting::BoundingSphere, and has everything that class has.

  C++ hands a Qt3DRender::Render::Sphere around as a copy, so every C++
  Qt3DRender::Render::Sphere behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Sphere that has a ritual and
  that Python can call so far, 10 names in all: 'setCenter', 'center',
  'isNull', 'setRadius', 'radius', 'clear', 'expandToContain', 'transformed',
  'id', 'type'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DRender::Render::Sphere::initializeFromPoints(const
    QList<Vector3D> &points)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void Qt3DRender::Render::Sphere::expandToContain(const
    QList<Vector3D> &points)': takes a type Python has no way to hand over
    yet.
  - Qt's 'Sphere &Qt3DRender::Render::Sphere::transform(const Matrix4x4
    &mat)': gives a type Python has no way to take yet.
  - Qt's 'bool Qt3DRender::Render::Sphere::intersects(const
    RayCasting::QRay3D &ray, Vector3D *q, Vector3D *uvw) const': names
    'Vector3D', which has no cute class yet.
  - Qt's 'Sphere Qt3DRender::Render::Sphere::fromPoints(const QList<Vector3D>
    &points)': takes a type Python has no way to hand over yet.
  - Qt's 'Qt3DRender::Render::Sphere::~Sphere()': the destructor: Python
    removes its C++ Qt3DRender::Render::Sphere by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Sphere is created at the first use, not by
    'Qt3DRender::Render::Sphere(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::Sphere back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::Render::Sphere.
  - Each name of Qt's Qt3DRender::Render::Sphere that has no cute function
    yet, 'fromPoints', 'initializeFromPoints', 'transform', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Sphere'

  #  Qt's '~Qt3DRender::Render::Sphere()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Render::Sphere behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render6SphereD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::Render::Sphere::center() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#center

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::Render::Sphere::center() const
    ritual = 'ritual_ZNK10Qt3DRender6Render6Sphere6centerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DRender6Render6Sphere6centerEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Sphere::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#isNull
    """
    #  bool Qt3DRender::Render::Sphere::isNull() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Sphere6isNullEv',
    )

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::Sphere::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#radius
    """
    #  float Qt3DRender::Render::Sphere::radius() const
    ritual = 'ritual_ZNK10Qt3DRender6Render6Sphere6radiusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DRender6Render6Sphere6radiusEv'
    return self.uglySide.call(ritual)

  @overload(QMatrix4x4)
  def transformed(self, mat: QMatrix4x4) -> Sphere:
    """
    Calls Qt's 'Sphere Qt3DRender::Render::Sphere::transformed(const
    Matrix4x4 &mat) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#transformed

    Parameters
    ----------

    mat : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    Sphere
      A new cute Qt3DRender::Render::Sphere around the copy Qt gave back.
      Python owns it.
    """
    #  Sphere Qt3DRender::Render::Sphere::transformed(const Matrix4x4 &mat)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Sphere11transformedERK10QMatrix4x4',
        self._valueOf(mat),
    )
    return Sphere._cuteOwning(address)

  def id(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId Qt3DRender::Render::Sphere::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-sphere.html#id

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::Sphere::id() const
    address = self.uglySide.call('ritual_ZNK10Qt3DRender6Render6Sphere2idEv')
    return Qt3DCore.QNodeId._cuteOwning(address)

  def type(self) -> Qt3DRender.RayCasting.QBoundingVolume.Type:
    """
    Calls Qt's 'Type Qt3DRender::Render::Sphere::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-sphere.html#type

    Returns
    -------

    Qt3DRender.RayCasting.QBoundingVolume.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.RayCasting.QBoundingVolume.Type(number)' gives.
    """
    #  Type Qt3DRender::Render::Sphere::type() const
    return Qt3DRender.RayCasting.QBoundingVolume.Type(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Sphere4typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setCenter(self, c: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Sphere::setCenter(const Vector3D
    &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#setCenter

    Parameters
    ----------

    c : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::Sphere::setCenter(const Vector3D &c)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Sphere9setCenterERK9QVector3D',
        self._valueOf(c),
    )

  @overload(float)
  def setRadius(self, r: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Sphere::setRadius(float r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#setRadius

    Parameters
    ----------

    r : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Sphere::setRadius(float r)
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Sphere9setRadiusEf', r)

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
  @overload(WAIT['Qt3DCore.QNodeId'])
  def __init__(self, i: Optional[Qt3DCore.QNodeId] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::Sphere::Sphere(Qt3DCore::QNodeId i)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#Sphere

    Parameters
    ----------

    i : Optional[Qt3DCore.QNodeId]
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own. May be left out, as in Qt: a new 'Qt3DCore.QNodeId()' is
      then passed on.
    """
    #  Qt3DRender::Render::Sphere::Sphere(Qt3DCore::QNodeId i)
    if i is None:
      i = Qt3DCore.QNodeId()
    self._noteCreation(Sphere, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render6SphereC1EN8Qt3DCore7QNodeIdE',
        self._valueOf(i),
    ))

  @overload(QVector3D, float)
  @overload(QVector3D, float, WAIT['Qt3DCore.QNodeId'])
  def __init__(
      self,
      c: QVector3D,
      r: float,
      i: Optional[Qt3DCore.QNodeId] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Qt3DRender::Render::Sphere::Sphere(const
    Vector3D &c, float r, Qt3DCore::QNodeId i)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#Sphere

    Parameters
    ----------

    c : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    r : float
      Passed on as it is.

    i : Optional[Qt3DCore.QNodeId]
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own. May be left out, as in Qt: a new 'Qt3DCore.QNodeId()' is
      then passed on.
    """
    #  Qt3DRender::Render::Sphere::Sphere(const Vector3D &c, float r,
    #      Qt3DCore::QNodeId i)
    if i is None:
      i = Qt3DCore.QNodeId()
    self._noteCreation(Sphere, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render6SphereC1ERK9QVector3DfN8Qt3DCore7QNod'
        'eIdE',
        self._valueOf(c), r, self._valueOf(i),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Sphere::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#clear
    """
    #  void Qt3DRender::Render::Sphere::clear()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Sphere5clearEv')

  @overload(QVector3D)
  def expandToContain(self, point: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Sphere::expandToContain(const
    Vector3D &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#expandToContain

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::Sphere::expandToContain(const Vector3D
    #      &point)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Sphere15expandToContainERK9QVector3D',
        self._valueOf(point),
    )

  @overload(THIS)
  def expandToContain(self, sphere: Sphere) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Sphere::expandToContain(const Sphere
    &sphere)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-sphere.html#expandToContain

    Parameters
    ----------

    sphere : Sphere
      Passed on as a value: Qt reads the C++ Qt3DRender::Render::Sphere,
      which stays Python's own.
    """
    #  void Qt3DRender::Render::Sphere::expandToContain(const Sphere &sphere)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Sphere15expandToContainERKS1_',
        self._valueOf(sphere),
    )

  @staticmethod
  def fromPoints(*__, **_) -> Never:
    """
    Qt's 'Sphere Qt3DRender::Render::Sphere::fromPoints(const QList<Vector3D>
    &points)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Sphere.fromPoints' has no cute function yet. "
        "Qt's 'Sphere Qt3DRender::Render::Sphere::fromPoints(const "
        "QList<Vector3D> &points)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def initializeFromPoints(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Sphere::initializeFromPoints(const
    QList<Vector3D> &points)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Sphere.initializeFromPoints' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::Sphere::initializeFromPoints(const "
        "QList<Vector3D> &points)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def transform(*__, **_) -> Never:
    """
    Qt's 'Sphere &Qt3DRender::Render::Sphere::transform(const Matrix4x4
    &mat)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Sphere.transform' has no cute function yet. "
        "Qt's 'Sphere &Qt3DRender::Render::Sphere::transform(const "
        "Matrix4x4 &mat)': gives a type Python has no way to take yet.")
