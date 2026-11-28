"""
Qt3DCore::QTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qtransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTransform(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DCore::QTransform: a plain Python object standing
  in front of one C++ Qt3DCore::QTransform.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DCore::QTransform is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QTransform that has a ritual and that
  Python can call so far, 35 names in all: 'metaObject', 'tr', 'scale',
  'scale3D', 'rotation', 'translation', 'fromAxisAndAngle',
  'fromAxesAndAngles', 'fromAxes', 'fromEulerAngles', 'rotateAround',
  'rotateFromAxes', 'matrix', 'worldMatrix', 'rotationX', 'rotationY',
  'rotationZ', 'setScale', 'setScale3D', 'setRotation', 'setTranslation',
  'setMatrix', 'setRotationX', 'setRotationY', 'setRotationZ',
  'scaleChanged', 'scale3DChanged', 'rotationChanged', 'translationChanged',
  'matrixChanged', 'rotationXChanged', 'rotationYChanged',
  'rotationZChanged', 'worldMatrixChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QTransform::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QTransform::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QTransform::~QTransform()': the destructor: Python never
    removes a C++ Qt3DCore::QTransform.
  - Qt's 'Qt3DCore::QTransform::QTransform(QTransformPrivate &dd, QNode
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QTransformPrivate *Qt3DCore::QTransform::d_func() const':
    takes in Python what 'QTransformPrivate *Qt3DCore::QTransform::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QTransform is created at the first use, not by
    'Qt3DCore::QTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QTransform.
  - Qt tells when it has removed the C++ Qt3DCore::QTransform. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QTransform::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QTransform::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QVector3D, float)
  def fromAxisAndAngle(axis: QVector3D, angle: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromAxisAndAngle(const
    QVector3D &axis, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromAxisAndAngle

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromAxisAndAngle(const QVector3D
    #      &axis, float angle)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform16fromAxisAndAngleERK9QVector3Df',
        CuteMixin._valueOf(axis), angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(float, float, float, float)
  def fromAxisAndAngle(
      x: float,
      y: float,
      z: float,
      angle: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromAxisAndAngle(float x,
    float y, float z, float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromAxisAndAngle

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromAxisAndAngle(float x, float y,
    #      float z, float angle)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform16fromAxisAndAngleEffff',
        x, y, z, angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, float, QVector3D, float)
  def fromAxesAndAngles(
      axis1: QVector3D,
      angle1: float,
      axis2: QVector3D,
      angle2: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromAxesAndAngles(const
    QVector3D &axis1, float angle1, const QVector3D &axis2, float angle2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromAxesAndAngles

    Parameters
    ----------

    axis1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle1 : float
      Passed on as it is.

    axis2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle2 : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromAxesAndAngles(const QVector3D
    #      &axis1, float angle1, const QVector3D &axis2, float angle2)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform17fromAxesAndAnglesERK9QVector3DfS3_'
        'f',
        CuteMixin._valueOf(axis1), angle1, CuteMixin._valueOf(axis2), angle2,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, float, QVector3D, float, QVector3D, float)
  def fromAxesAndAngles(
      axis1: QVector3D,
      angle1: float,
      axis2: QVector3D,
      angle2: float,
      axis3: QVector3D,
      angle3: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromAxesAndAngles(const
    QVector3D &axis1, float angle1, const QVector3D &axis2, float angle2,
    const QVector3D &axis3, float angle3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromAxesAndAngles

    Parameters
    ----------

    axis1 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle1 : float
      Passed on as it is.

    axis2 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle2 : float
      Passed on as it is.

    axis3 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle3 : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromAxesAndAngles(const QVector3D
    #      &axis1, float angle1, const QVector3D &axis2, float angle2, const
    #      QVector3D &axis3, float angle3)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform17fromAxesAndAnglesERK9QVector3DfS3_'
        'fS3_f',
        CuteMixin._valueOf(axis1), angle1, CuteMixin._valueOf(axis2), angle2,
        CuteMixin._valueOf(axis3), angle3,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D, QVector3D)
  def fromAxes(
      xAxis: QVector3D,
      yAxis: QVector3D,
      zAxis: QVector3D,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromAxes(const QVector3D
    &xAxis, const QVector3D &yAxis, const QVector3D &zAxis)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromAxes

    Parameters
    ----------

    xAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    yAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    zAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromAxes(const QVector3D &xAxis,
    #      const QVector3D &yAxis, const QVector3D &zAxis)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform8fromAxesERK9QVector3DS3_S3_',
        CuteMixin._valueOf(xAxis), CuteMixin._valueOf(yAxis),
        CuteMixin._valueOf(zAxis),
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D)
  def fromEulerAngles(eulerAngles: QVector3D) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromEulerAngles(const
    QVector3D &eulerAngles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromEulerAngles

    Parameters
    ----------

    eulerAngles : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromEulerAngles(const QVector3D
    #      &eulerAngles)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform15fromEulerAnglesERK9QVector3D',
        CuteMixin._valueOf(eulerAngles),
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(float, float, float)
  def fromEulerAngles(pitch: float, yaw: float, roll: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::fromEulerAngles(float
    pitch, float yaw, float roll)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#fromEulerAngles

    Parameters
    ----------

    pitch : float
      Passed on as it is.

    yaw : float
      Passed on as it is.

    roll : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::fromEulerAngles(float pitch, float
    #      yaw, float roll)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform15fromEulerAnglesEfff',
        pitch, yaw, roll,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, float, QVector3D)
  def rotateAround(
      point: QVector3D,
      angle: float,
      axis: QVector3D,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DCore::QTransform::rotateAround(const QVector3D
    &point, float angle, const QVector3D &axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotateAround

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle : float
      Passed on as it is.

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::QTransform::rotateAround(const QVector3D &point,
    #      float angle, const QVector3D &axis)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform12rotateAroundERK9QVector3DfS3_',
        CuteMixin._valueOf(point), angle, CuteMixin._valueOf(axis),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D, QVector3D)
  def rotateFromAxes(
      xAxis: QVector3D,
      yAxis: QVector3D,
      zAxis: QVector3D,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DCore::QTransform::rotateFromAxes(const
    QVector3D &xAxis, const QVector3D &yAxis, const QVector3D &zAxis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotateFromAxes

    Parameters
    ----------

    xAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    yAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    zAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::QTransform::rotateFromAxes(const QVector3D
    #      &xAxis, const QVector3D &yAxis, const QVector3D &zAxis)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore10QTransform14rotateFromAxesERK9QVector3DS3_S3_',
        CuteMixin._valueOf(xAxis), CuteMixin._valueOf(yAxis),
        CuteMixin._valueOf(zAxis),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QTransform'

  #  A C++ Qt3DCore::QTransform Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QTransform'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QTransform::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QTransform::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QTransform10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scale(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QTransform::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#scale
    """
    #  float Qt3DCore::QTransform::scale() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QTransform5scaleEv')

  def scale3D(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QTransform::scale3D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#scale3D

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QTransform::scale3D() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore10QTransform7scale3DEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DCore::QTransform::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DCore::QTransform::rotation() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QTransform8rotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def translation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DCore::QTransform::translation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#translation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DCore::QTransform::translation() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QTransform11translationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def matrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DCore::QTransform::matrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#matrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::QTransform::matrix() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore10QTransform6matrixEv')
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def worldMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DCore::QTransform::worldMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#worldMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DCore::QTransform::worldMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QTransform11worldMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def rotationX(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QTransform::rotationX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationX
    """
    #  float Qt3DCore::QTransform::rotationX() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QTransform9rotationXEv')

  def rotationY(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QTransform::rotationY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationY
    """
    #  float Qt3DCore::QTransform::rotationY() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QTransform9rotationYEv')

  def rotationZ(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::QTransform::rotationZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationZ
    """
    #  float Qt3DCore::QTransform::rotationZ() const
    return self.uglySide.call('ritual_ZNK8Qt3DCore10QTransform9rotationZEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setScale(float scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::setScale(float scale)
    self.uglySide.call('ritual_ZN8Qt3DCore10QTransform8setScaleEf', scale)

  @overload(QVector3D)
  def setScale3D(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setScale3D(const QVector3D
    &scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setScale3D

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QTransform::setScale3D(const QVector3D &scale)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform10setScale3DERK9QVector3D',
        self._valueOf(scale),
    )

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setRotation(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DCore::QTransform::setRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform11setRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def setTranslation(self, translation: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setTranslation(const QVector3D
    &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setTranslation

    Parameters
    ----------

    translation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QTransform::setTranslation(const QVector3D
    #      &translation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform14setTranslationERK9QVector3D',
        self._valueOf(translation),
    )

  @overload(QMatrix4x4)
  def setMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setMatrix(const QMatrix4x4
    &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DCore::QTransform::setMatrix(const QMatrix4x4 &matrix)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform9setMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
    )

  @overload(float)
  def setRotationX(self, rotationX: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setRotationX(float rotationX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setRotationX

    Parameters
    ----------

    rotationX : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::setRotationX(float rotationX)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform12setRotationXEf', rotationX,
    )

  @overload(float)
  def setRotationY(self, rotationY: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setRotationY(float rotationY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setRotationY

    Parameters
    ----------

    rotationY : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::setRotationY(float rotationY)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform12setRotationYEf', rotationY,
    )

  @overload(float)
  def setRotationZ(self, rotationZ: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::setRotationZ(float rotationZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#setRotationZ

    Parameters
    ----------

    rotationZ : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::setRotationZ(float rotationZ)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform12setRotationZEf', rotationZ,
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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QTransform::QTransform(QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#QTransform

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QTransform::QTransform(QNode *parent)
    self._noteCreation(QTransform, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QTransformC1EPNS_5QNodeE',
        self._addressOf(parent),
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
  def scaleChanged(self, scale: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::scaleChanged(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#scaleChanged

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::scaleChanged(float scale)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform12scaleChangedEf', scale,
    )

  @overload(QVector3D)
  def scale3DChanged(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::scale3DChanged(const QVector3D
    &scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#scale3DChanged

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QTransform::scale3DChanged(const QVector3D &scale)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform14scale3DChangedERK9QVector3D',
        self._valueOf(scale),
    )

  @overload(QQuaternion)
  def rotationChanged(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::rotationChanged(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationChanged

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DCore::QTransform::rotationChanged(const QQuaternion
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform15rotationChangedERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def translationChanged(self, translation: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::translationChanged(const QVector3D
    &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#translationChanged

    Parameters
    ----------

    translation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DCore::QTransform::translationChanged(const QVector3D
    #      &translation)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform18translationChangedERK9QVector3D',
        self._valueOf(translation),
    )

  def matrixChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::matrixChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#matrixChanged
    """
    #  void Qt3DCore::QTransform::matrixChanged()
    self.uglySide.call('ritual_ZN8Qt3DCore10QTransform13matrixChangedEv')

  @overload(float)
  def rotationXChanged(self, rotationX: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::rotationXChanged(float
    rotationX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationXChanged

    Parameters
    ----------

    rotationX : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::rotationXChanged(float rotationX)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform16rotationXChangedEf', rotationX,
    )

  @overload(float)
  def rotationYChanged(self, rotationY: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::rotationYChanged(float
    rotationY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationYChanged

    Parameters
    ----------

    rotationY : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::rotationYChanged(float rotationY)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform16rotationYChangedEf', rotationY,
    )

  @overload(float)
  def rotationZChanged(self, rotationZ: float) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::rotationZChanged(float
    rotationZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#rotationZChanged

    Parameters
    ----------

    rotationZ : float
      Passed on as it is.
    """
    #  void Qt3DCore::QTransform::rotationZChanged(float rotationZ)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform16rotationZChangedEf', rotationZ,
    )

  @overload(QMatrix4x4)
  def worldMatrixChanged(self, worldMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTransform::worldMatrixChanged(const
    QMatrix4x4 &worldMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtransform.html#worldMatrixChanged

    Parameters
    ----------

    worldMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DCore::QTransform::worldMatrixChanged(const QMatrix4x4
    #      &worldMatrix)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QTransform18worldMatrixChangedERK10QMatrix4x4',
        self._valueOf(worldMatrix),
    )

  def d_func(self) -> Optional[Qt3DCore.QTransformPrivate]:
    """
    Calls Qt's 'QTransformPrivate *Qt3DCore::QTransform::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtransform.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QTransformPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTransformPrivate *Qt3DCore::QTransform::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore10QTransform6d_funcEv')
    return Qt3DCore.QTransformPrivate._cuteAt(address)
