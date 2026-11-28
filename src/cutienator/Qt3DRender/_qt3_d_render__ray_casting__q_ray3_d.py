"""
Qt3DRender::RayCasting::QRay3D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::RayCasting::QRay3D to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']


class QRay3D(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::RayCasting::QRay3D: a plain Python object
  standing in front of one C++ Qt3DRender::RayCasting::QRay3D.

  C++ hands a Qt3DRender::RayCasting::QRay3D around as a copy, so every C++
  Qt3DRender::RayCasting::QRay3D behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::RayCasting::QRay3D that has a ritual and
  that Python can call so far, 14 names in all: 'origin', 'setOrigin',
  'direction', 'setDirection', 'distance', 'setDistance', 'contains',
  'point', 'projectedDistance', 'project', 'transformed', '__eq__', '__ne__',
  'isValid'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::RayCasting::QRay3D::~QRay3D()': the destructor: Python
    removes its C++ Qt3DRender::RayCasting::QRay3D by it, and has no other
    use for it.
  - Qt's 'QRay3D &Qt3DRender::RayCasting::QRay3D::transform(const Matrix4x4
    &matrix)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::RayCasting::QRay3D is created at the first use, not
    by 'Qt3DRender::RayCasting::QRay3D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::RayCasting::QRay3D back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::RayCasting::QRay3D.
  - Each name of Qt's Qt3DRender::RayCasting::QRay3D that has no cute
    function yet, 'transform', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::RayCasting::QRay3D'

  #  Qt's '~Qt3DRender::RayCasting::QRay3D()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::RayCasting::QRay3D behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender10RayCasting6QRay3DD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::RayCasting::QRay3D::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::RayCasting::QRay3D::origin() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D6originEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def direction(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::RayCasting::QRay3D::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#direction

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::RayCasting::QRay3D::direction() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D9directionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload()
  def distance(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::RayCasting::QRay3D::distance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#distance
    """
    #  float Qt3DRender::RayCasting::QRay3D::distance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D8distanceEv',
    )

  @overload(QVector3D)
  def distance(self, point: QVector3D) -> float:
    """
    Calls Qt's 'float Qt3DRender::RayCasting::QRay3D::distance(const Vector3D
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#distance

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float Qt3DRender::RayCasting::QRay3D::distance(const Vector3D &point)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D8distanceERK9QVector3D',
        self._valueOf(point),
    )

  @overload(QVector3D)
  def contains(self, point: QVector3D) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::RayCasting::QRay3D::contains(const Vector3D
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#contains

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool Qt3DRender::RayCasting::QRay3D::contains(const Vector3D &point)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D8containsERK9QVector3D',
        self._valueOf(point),
    )

  @overload(THIS)
  def contains(self, ray: QRay3D) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::RayCasting::QRay3D::contains(const QRay3D
    &ray) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#contains

    Parameters
    ----------

    ray : QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.
    """
    #  bool Qt3DRender::RayCasting::QRay3D::contains(const QRay3D &ray) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D8containsERKS1_',
        self._valueOf(ray),
    )

  @overload(float)
  def point(self, t: float) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::RayCasting::QRay3D::point(float t)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#point

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::RayCasting::QRay3D::point(float t) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D5pointEf', t,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def projectedDistance(self, point: QVector3D) -> float:
    """
    Calls Qt's 'float Qt3DRender::RayCasting::QRay3D::projectedDistance(const
    Vector3D &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  float Qt3DRender::RayCasting::QRay3D::projectedDistance(const Vector3D
    #      &point) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D17projectedDistanceERK9QV'
        'ector3D',
        self._valueOf(point),
    )

  @overload(QVector3D)
  def project(self, vector: QVector3D) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::RayCasting::QRay3D::project(const
    Vector3D &vector) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#project

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::RayCasting::QRay3D::project(const Vector3D
    #      &vector) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D7projectERK9QVector3D',
        self._valueOf(vector),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QMatrix4x4)
  def transformed(self, matrix: QMatrix4x4) -> QRay3D:
    """
    Calls Qt's 'QRay3D Qt3DRender::RayCasting::QRay3D::transformed(const
    Matrix4x4 &matrix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#transformed

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QRay3D
      A new cute Qt3DRender::RayCasting::QRay3D around the copy Qt gave back.
      Python owns it.
    """
    #  QRay3D Qt3DRender::RayCasting::QRay3D::transformed(const Matrix4x4
    #      &matrix) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D11transformedERK10QMatrix'
        '4x4',
        self._valueOf(matrix),
    )
    return QRay3D._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::RayCasting::QRay3D::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#isValid
    """
    #  bool Qt3DRender::RayCasting::QRay3D::isValid() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3D7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, value: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::RayCasting::QRay3D::setOrigin(const Vector3D
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#setOrigin

    Parameters
    ----------

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::RayCasting::QRay3D::setOrigin(const Vector3D &value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting6QRay3D9setOriginERK9QVector3D',
        self._valueOf(value),
    )

  @overload(QVector3D)
  def setDirection(self, value: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::RayCasting::QRay3D::setDirection(const
    Vector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#setDirection

    Parameters
    ----------

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::RayCasting::QRay3D::setDirection(const Vector3D
    #      &value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting6QRay3D12setDirectionERK9QVector3'
        'D',
        self._valueOf(value),
    )

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::RayCasting::QRay3D::setDistance(float
    distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void Qt3DRender::RayCasting::QRay3D::setDistance(float distance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10RayCasting6QRay3D11setDistanceEf', distance,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QRay3D) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::RayCasting::QRay3D::operator==(const QRay3D
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#operator==

    Parameters
    ----------

    other : QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.
    """
    #  bool Qt3DRender::RayCasting::QRay3D::operator==(const QRay3D &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3DeqERKS1_',
        self._valueOf(other),
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
  def __ne__(self, other: QRay3D) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::RayCasting::QRay3D::operator!=(const QRay3D
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#operator!=

    Parameters
    ----------

    other : QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.
    """
    #  bool Qt3DRender::RayCasting::QRay3D::operator!=(const QRay3D &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10RayCasting6QRay3DneERKS1_',
        self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QRay3D::QRay3D()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#QRay3D
    """
    #  Qt3DRender::RayCasting::QRay3D::QRay3D()
    self._noteCreation(QRay3D, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting6QRay3DC1Ev',
    ))

  @overload(QVector3D)
  @overload(QVector3D, QVector3D)
  @overload(QVector3D, QVector3D, float)
  def __init__(
      self,
      origin: QVector3D,
      direction: Optional[QVector3D] = None,
      distance: float = 1.0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::RayCasting::QRay3D::QRay3D(const Vector3D &origin, const
    Vector3D &direction, float distance)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-raycasting-qray3d.html#QRay3D

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D(0.0, 0.0, 1.0)' is
      then passed on.

    distance : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  Qt3DRender::RayCasting::QRay3D::QRay3D(const Vector3D &origin, const
    #      Vector3D &direction, float distance)
    if direction is None:
      from ..QtGui import QVector3D
      direction = QVector3D(0.0, 0.0, 1.0)
    self._noteCreation(QRay3D, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10RayCasting6QRay3DC1ERK9QVector3DS4_f',
        self._valueOf(origin), self._valueOf(direction), distance,
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

  @staticmethod
  def transform(*__, **_) -> Never:
    """
    Qt's 'QRay3D &Qt3DRender::RayCasting::QRay3D::transform(const Matrix4x4
    &matrix)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.RayCasting.QRay3D.transform' has no cute function yet. "
        "Qt's 'QRay3D &Qt3DRender::RayCasting::QRay3D::transform(const "
        "Matrix4x4 &matrix)': gives a type Python has no way to take yet.")
