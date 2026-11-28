"""
Qt3DRender::QCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qcamera.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

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


class QCamera(Qt3DCore.QEntity):
  """
  The cute side of Qt's Qt3DRender::QCamera: a plain Python object standing
  in front of one C++ Qt3DRender::QCamera.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's Qt3DRender::QCamera is
  built on Qt's Qt3DCore::QEntity, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QCamera that has a ritual and that
  Python can call so far, 68 names in all: 'metaObject', 'tr', 'lens',
  'transform', 'tiltRotation', 'panRotation', 'rollRotation', 'rotation',
  'translate', 'translateWorld', 'tilt', 'pan', 'roll',
  'tiltAboutViewCenter', 'panAboutViewCenter', 'rollAboutViewCenter',
  'rotate', 'rotateAboutViewCenter', 'projectionType', 'nearPlane',
  'farPlane', 'fieldOfView', 'aspectRatio', 'left', 'right', 'bottom', 'top',
  'projectionMatrix', 'exposure', 'position', 'upVector', 'viewCenter',
  'viewVector', 'viewMatrix', 'setProjectionType', 'setNearPlane',
  'setFarPlane', 'setFieldOfView', 'setAspectRatio', 'setLeft', 'setRight',
  'setBottom', 'setTop', 'setProjectionMatrix', 'setExposure', 'setPosition',
  'setUpVector', 'setViewCenter', 'viewAll', 'viewSphere', 'viewEntity',
  'projectionTypeChanged', 'nearPlaneChanged', 'farPlaneChanged',
  'fieldOfViewChanged', 'aspectRatioChanged', 'leftChanged', 'rightChanged',
  'bottomChanged', 'topChanged', 'projectionMatrixChanged',
  'exposureChanged', 'positionChanged', 'upVectorChanged',
  'viewCenterChanged', 'viewVectorChanged', 'viewMatrixChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QCamera::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QCamera::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QCamera::~QCamera()': the destructor: Python never
    removes a C++ Qt3DRender::QCamera.
  - Qt's 'const QCameraPrivate *Qt3DRender::QCamera::d_func() const': takes
    in Python what 'QCameraPrivate *Qt3DRender::QCamera::d_func()' takes.
  - Qt's 'Qt3DRender::QCamera::QCamera(QCameraPrivate &dd, QNode *parent)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 78 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QCamera is created at the first use, not by
    'Qt3DRender::QCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QCamera.
  - Qt tells when it has removed the C++ Qt3DRender::QCamera. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QCamera, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CameraTranslationOption(CuteNum):
    """
    The enum 'Qt3DRender::QCamera::CameraTranslationOption' of Qt, with the 2
    names Qt gives in it.
    """

    TranslateViewCenter = Kee[int](0)
    DontTranslateViewCenter = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QCamera::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#tr

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
    #  QString Qt3DRender::QCamera::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender7QCamera2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QCamera'

  #  A C++ Qt3DRender::QCamera Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QCamera::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QCamera::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lens(self) -> Optional[Qt3DRender.QCameraLens]:
    """
    Calls Qt's 'QCameraLens *Qt3DRender::QCamera::lens() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#lens

    Returns
    -------

    Optional[Qt3DRender.QCameraLens]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCameraLens *Qt3DRender::QCamera::lens() const
    address = self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera4lensEv')
    return Qt3DRender.QCameraLens._cuteAt(address)

  def transform(self) -> Optional[Qt3DCore.QTransform]:
    """
    Calls Qt's 'Qt3DCore::QTransform *Qt3DRender::QCamera::transform()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#transform

    Returns
    -------

    Optional[Qt3DCore.QTransform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QTransform *Qt3DRender::QCamera::transform() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera9transformEv',
    )
    return Qt3DCore.QTransform._cuteAt(address)

  @overload(float)
  def tiltRotation(self, angle: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DRender::QCamera::tiltRotation(float angle)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#tiltRotation

    Parameters
    ----------

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DRender::QCamera::tiltRotation(float angle) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera12tiltRotationEf', angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(float)
  def panRotation(self, angle: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DRender::QCamera::panRotation(float angle)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#panRotation

    Parameters
    ----------

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DRender::QCamera::panRotation(float angle) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera11panRotationEf', angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(float)
  def rollRotation(self, angle: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DRender::QCamera::rollRotation(float angle)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#rollRotation

    Parameters
    ----------

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DRender::QCamera::rollRotation(float angle) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera12rollRotationEf', angle,
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  @overload(float, QVector3D)
  def rotation(self, angle: float, axis: QVector3D) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion Qt3DRender::QCamera::rotation(float angle, const
    QVector3D &axis) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#rotation

    Parameters
    ----------

    angle : float
      Passed on as it is.

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion Qt3DRender::QCamera::rotation(float angle, const QVector3D
    #      &axis) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera8rotationEfRK9QVector3D',
        angle, self._valueOf(axis),
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def projectionType(self) -> Qt3DRender.QCameraLens.ProjectionType:
    """
    Calls Qt's 'QCameraLens::ProjectionType
    Qt3DRender::QCamera::projectionType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#projectionType

    Returns
    -------

    Qt3DRender.QCameraLens.ProjectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QCameraLens.ProjectionType(number)' gives.
    """
    #  QCameraLens::ProjectionType Qt3DRender::QCamera::projectionType()
    #      const
    return Qt3DRender.QCameraLens.ProjectionType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera14projectionTypeEv',
    ))

  def nearPlane(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::nearPlane() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#nearPlane
    """
    #  float Qt3DRender::QCamera::nearPlane() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera9nearPlaneEv')

  def farPlane(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::farPlane() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#farPlane
    """
    #  float Qt3DRender::QCamera::farPlane() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera8farPlaneEv')

  def fieldOfView(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::fieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#fieldOfView
    """
    #  float Qt3DRender::QCamera::fieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera11fieldOfViewEv',
    )

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::aspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#aspectRatio
    """
    #  float Qt3DRender::QCamera::aspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera11aspectRatioEv',
    )

  def left(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#left
    """
    #  float Qt3DRender::QCamera::left() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera4leftEv')

  def right(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#right
    """
    #  float Qt3DRender::QCamera::right() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera5rightEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#bottom
    """
    #  float Qt3DRender::QCamera::bottom() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera6bottomEv')

  def top(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#top
    """
    #  float Qt3DRender::QCamera::top() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera3topEv')

  def projectionMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DRender::QCamera::projectionMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#projectionMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DRender::QCamera::projectionMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera16projectionMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def exposure(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCamera::exposure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#exposure
    """
    #  float Qt3DRender::QCamera::exposure() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera8exposureEv')

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QCamera::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QCamera::position() const
    address = self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def upVector(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QCamera::upVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#upVector

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QCamera::upVector() const
    address = self.uglySide.call('ritual_ZNK10Qt3DRender7QCamera8upVectorEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def viewCenter(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QCamera::viewCenter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewCenter

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QCamera::viewCenter() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera10viewCenterEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def viewVector(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QCamera::viewVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewVector

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QCamera::viewVector() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera10viewVectorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def viewMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DRender::QCamera::viewMatrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DRender::QCamera::viewMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender7QCamera10viewMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DRender.QCameraLens.ProjectionType)
  def setProjectionType(
      self,
      type: Qt3DRender.QCameraLens.ProjectionType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCamera::setProjectionType(QCameraLens::ProjectionType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setProjectionType

    Parameters
    ----------

    type : Qt3DRender.QCameraLens.ProjectionType
      Passed on as its number.
    """
    #  void
    #      Qt3DRender::QCamera::setProjectionType(QCameraLens::ProjectionType
    #      type)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera17setProjectionTypeENS_11QCameraLens1'
        '4ProjectionTypeE',
        type.value,
    )

  @overload(float)
  def setNearPlane(self, nearPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setNearPlane(float nearPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setNearPlane

    Parameters
    ----------

    nearPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setNearPlane(float nearPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera12setNearPlaneEf', nearPlane,
    )

  @overload(float)
  def setFarPlane(self, farPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setFarPlane(float farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setFarPlane

    Parameters
    ----------

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setFarPlane(float farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera11setFarPlaneEf', farPlane,
    )

  @overload(float)
  def setFieldOfView(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setFieldOfView(float fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setFieldOfView

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setFieldOfView(float fieldOfView)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera14setFieldOfViewEf', fieldOfView,
    )

  @overload(float)
  def setAspectRatio(self, aspectRatio: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setAspectRatio(float aspectRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setAspectRatio

    Parameters
    ----------

    aspectRatio : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setAspectRatio(float aspectRatio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera14setAspectRatioEf', aspectRatio,
    )

  @overload(float)
  def setLeft(self, left: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setLeft(float left)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#setLeft

    Parameters
    ----------

    left : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setLeft(float left)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera7setLeftEf', left)

  @overload(float)
  def setRight(self, right: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setRight(float right)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#setRight

    Parameters
    ----------

    right : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setRight(float right)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera8setRightEf', right)

  @overload(float)
  def setBottom(self, bottom: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setBottom(float bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#setBottom

    Parameters
    ----------

    bottom : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setBottom(float bottom)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera9setBottomEf', bottom)

  @overload(float)
  def setTop(self, top: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setTop(float top)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#setTop

    Parameters
    ----------

    top : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setTop(float top)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera6setTopEf', top)

  @overload(QMatrix4x4)
  def setProjectionMatrix(self, projectionMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setProjectionMatrix(const
    QMatrix4x4 &projectionMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setProjectionMatrix

    Parameters
    ----------

    projectionMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::setProjectionMatrix(const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera19setProjectionMatrixERK10QMatrix4x4',
        self._valueOf(projectionMatrix),
    )

  @overload(float)
  def setExposure(self, exposure: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setExposure(float exposure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setExposure

    Parameters
    ----------

    exposure : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::setExposure(float exposure)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera11setExposureEf', exposure,
    )

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setPosition(const QVector3D
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::setPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera11setPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QVector3D)
  def setUpVector(self, upVector: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setUpVector(const QVector3D
    &upVector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setUpVector

    Parameters
    ----------

    upVector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::setUpVector(const QVector3D &upVector)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera11setUpVectorERK9QVector3D',
        self._valueOf(upVector),
    )

  @overload(QVector3D)
  def setViewCenter(self, viewCenter: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::setViewCenter(const QVector3D
    &viewCenter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#setViewCenter

    Parameters
    ----------

    viewCenter : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::setViewCenter(const QVector3D &viewCenter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera13setViewCenterERK9QVector3D',
        self._valueOf(viewCenter),
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
    Notes what was given, for Qt's 'Qt3DRender::QCamera::QCamera(QNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#QCamera

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QCamera::QCamera(QNode *parent)
    self._noteCreation(QCamera, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender7QCameraC1EPN8Qt3DCore5QNodeE',
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

  @overload(QVector3D)
  @overload(QVector3D, CameraTranslationOption)
  def translate(
      self,
      vLocal: QVector3D,
      option: CameraTranslationOption = (
          CameraTranslationOption.TranslateViewCenter),
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::translate(const QVector3D &vLocal,
    CameraTranslationOption option)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#translate

    Parameters
    ----------

    vLocal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    option : CameraTranslationOption
      Passed on as its number. May be left out, as in Qt: it is then
      CameraTranslationOption.TranslateViewCenter.
    """
    #  void Qt3DRender::QCamera::translate(const QVector3D &vLocal,
    #      CameraTranslationOption option)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera9translateERK9QVector3DNS0_23CameraTr'
        'anslationOptionE',
        self._valueOf(vLocal), option.value,
    )

  @overload(QVector3D)
  @overload(QVector3D, CameraTranslationOption)
  def translateWorld(
      self,
      vWorld: QVector3D,
      option: CameraTranslationOption = (
          CameraTranslationOption.TranslateViewCenter),
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::translateWorld(const QVector3D
    &vWorld, CameraTranslationOption option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#translateWorld

    Parameters
    ----------

    vWorld : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    option : CameraTranslationOption
      Passed on as its number. May be left out, as in Qt: it is then
      CameraTranslationOption.TranslateViewCenter.
    """
    #  void Qt3DRender::QCamera::translateWorld(const QVector3D &vWorld,
    #      CameraTranslationOption option)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera14translateWorldERK9QVector3DNS0_23Ca'
        'meraTranslationOptionE',
        self._valueOf(vWorld), option.value,
    )

  @overload(float)
  def tilt(self, angle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::tilt(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#tilt

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::tilt(float angle)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera4tiltEf', angle)

  @overload(float)
  def pan(self, angle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::pan(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#pan

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::pan(float angle)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera3panEf', angle)

  @overload(float, QVector3D)
  def pan(self, angle: float, axis: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::pan(float angle, const QVector3D
    &axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#pan

    Parameters
    ----------

    angle : float
      Passed on as it is.

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::pan(float angle, const QVector3D &axis)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera3panEfRK9QVector3D',
        angle, self._valueOf(axis),
    )

  @overload(float)
  def roll(self, angle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::roll(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#roll

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::roll(float angle)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera4rollEf', angle)

  @overload(float)
  def tiltAboutViewCenter(self, angle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::tiltAboutViewCenter(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#tiltAboutViewCenter

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::tiltAboutViewCenter(float angle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera19tiltAboutViewCenterEf', angle,
    )

  @overload(float)
  def panAboutViewCenter(self, angle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::panAboutViewCenter(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#panAboutViewCenter

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::panAboutViewCenter(float angle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera18panAboutViewCenterEf', angle,
    )

  @overload(float, QVector3D)
  def panAboutViewCenter(self, angle: float, axis: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::panAboutViewCenter(float angle,
    const QVector3D &axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#panAboutViewCenter

    Parameters
    ----------

    angle : float
      Passed on as it is.

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::panAboutViewCenter(float angle, const
    #      QVector3D &axis)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera18panAboutViewCenterEfRK9QVector3D',
        angle, self._valueOf(axis),
    )

  @overload(float)
  def rollAboutViewCenter(self, angle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::rollAboutViewCenter(float angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#rollAboutViewCenter

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::rollAboutViewCenter(float angle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera19rollAboutViewCenterEf', angle,
    )

  @overload(QQuaternion)
  def rotate(self, q: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::rotate(const QQuaternion &q)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#rotate

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DRender::QCamera::rotate(const QQuaternion &q)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera6rotateERK11QQuaternion',
        self._valueOf(q),
    )

  @overload(QQuaternion)
  def rotateAboutViewCenter(self, q: QQuaternion) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::rotateAboutViewCenter(const
    QQuaternion &q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#rotateAboutViewCenter

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void Qt3DRender::QCamera::rotateAboutViewCenter(const QQuaternion &q)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera21rotateAboutViewCenterERK11QQuaterni'
        'on',
        self._valueOf(q),
    )

  def viewAll(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::viewAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewAll
    """
    #  void Qt3DRender::QCamera::viewAll()
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera7viewAllEv')

  @overload(QVector3D, float)
  def viewSphere(self, center: QVector3D, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::viewSphere(const QVector3D &center,
    float radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewSphere

    Parameters
    ----------

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::viewSphere(const QVector3D &center, float
    #      radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera10viewSphereERK9QVector3Df',
        self._valueOf(center), radius,
    )

  @overload(Qt3DCore.QEntity)
  @overload(NoneType)
  def viewEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::viewEntity(Qt3DCore::QEntity
    *entity)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QCamera::viewEntity(Qt3DCore::QEntity *entity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera10viewEntityEPN8Qt3DCore7QEntityE',
        self._addressOf(entity),
    )

  @overload(Qt3DRender.QCameraLens.ProjectionType)
  def projectionTypeChanged(
      self,
      projectionType: Qt3DRender.QCameraLens.ProjectionType,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCamera::projectionTypeChanged(QCameraLens::ProjectionType
    projectionType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#projectionTypeChanged

    Parameters
    ----------

    projectionType : Qt3DRender.QCameraLens.ProjectionType
      Passed on as its number.
    """
    #  void Qt3DRender::QCamera::projectionTypeChanged(QCameraLens::
    #      ProjectionType projectionType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera21projectionTypeChangedENS_11QCameraL'
        'ens14ProjectionTypeE',
        projectionType.value,
    )

  @overload(float)
  def nearPlaneChanged(self, nearPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::nearPlaneChanged(float nearPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#nearPlaneChanged

    Parameters
    ----------

    nearPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::nearPlaneChanged(float nearPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera16nearPlaneChangedEf', nearPlane,
    )

  @overload(float)
  def farPlaneChanged(self, farPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::farPlaneChanged(float farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#farPlaneChanged

    Parameters
    ----------

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::farPlaneChanged(float farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera15farPlaneChangedEf', farPlane,
    )

  @overload(float)
  def fieldOfViewChanged(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::fieldOfViewChanged(float
    fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#fieldOfViewChanged

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::fieldOfViewChanged(float fieldOfView)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera18fieldOfViewChangedEf', fieldOfView,
    )

  @overload(float)
  def aspectRatioChanged(self, aspectRatio: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::aspectRatioChanged(float
    aspectRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#aspectRatioChanged

    Parameters
    ----------

    aspectRatio : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::aspectRatioChanged(float aspectRatio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera18aspectRatioChangedEf', aspectRatio,
    )

  @overload(float)
  def leftChanged(self, left: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::leftChanged(float left)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#leftChanged

    Parameters
    ----------

    left : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::leftChanged(float left)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera11leftChangedEf', left)

  @overload(float)
  def rightChanged(self, right: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::rightChanged(float right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#rightChanged

    Parameters
    ----------

    right : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::rightChanged(float right)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera12rightChangedEf', right,
    )

  @overload(float)
  def bottomChanged(self, bottom: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::bottomChanged(float bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#bottomChanged

    Parameters
    ----------

    bottom : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::bottomChanged(float bottom)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera13bottomChangedEf', bottom,
    )

  @overload(float)
  def topChanged(self, top: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::topChanged(float top)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#topChanged

    Parameters
    ----------

    top : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::topChanged(float top)
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera10topChangedEf', top)

  @overload(QMatrix4x4)
  def projectionMatrixChanged(self, projectionMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::projectionMatrixChanged(const
    QMatrix4x4 &projectionMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#projectionMatrixChanged

    Parameters
    ----------

    projectionMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::projectionMatrixChanged(const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera23projectionMatrixChangedERK10QMatrix'
        '4x4',
        self._valueOf(projectionMatrix),
    )

  @overload(float)
  def exposureChanged(self, exposure: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::exposureChanged(float exposure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#exposureChanged

    Parameters
    ----------

    exposure : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCamera::exposureChanged(float exposure)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera15exposureChangedEf', exposure,
    )

  @overload(QVector3D)
  def positionChanged(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::positionChanged(const QVector3D
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#positionChanged

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::positionChanged(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera15positionChangedERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QVector3D)
  def upVectorChanged(self, upVector: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::upVectorChanged(const QVector3D
    &upVector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#upVectorChanged

    Parameters
    ----------

    upVector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::upVectorChanged(const QVector3D &upVector)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera15upVectorChangedERK9QVector3D',
        self._valueOf(upVector),
    )

  @overload(QVector3D)
  def viewCenterChanged(self, viewCenter: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::viewCenterChanged(const QVector3D
    &viewCenter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewCenterChanged

    Parameters
    ----------

    viewCenter : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::viewCenterChanged(const QVector3D
    #      &viewCenter)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera17viewCenterChangedERK9QVector3D',
        self._valueOf(viewCenter),
    )

  @overload(QVector3D)
  def viewVectorChanged(self, viewVector: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::viewVectorChanged(const QVector3D
    &viewVector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewVectorChanged

    Parameters
    ----------

    viewVector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QCamera::viewVectorChanged(const QVector3D
    #      &viewVector)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender7QCamera17viewVectorChangedERK9QVector3D',
        self._valueOf(viewVector),
    )

  def viewMatrixChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCamera::viewMatrixChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcamera.html#viewMatrixChanged
    """
    #  void Qt3DRender::QCamera::viewMatrixChanged()
    self.uglySide.call('ritual_ZN10Qt3DRender7QCamera17viewMatrixChangedEv')

  def d_func(self) -> Optional[Qt3DRender.QCameraPrivate]:
    """
    Calls Qt's 'QCameraPrivate *Qt3DRender::QCamera::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcamera.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QCameraPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCameraPrivate *Qt3DRender::QCamera::d_func()
    address = self.uglySide.call('ritual_ZN10Qt3DRender7QCamera6d_funcEv')
    return Qt3DRender.QCameraPrivate._cuteAt(address)
