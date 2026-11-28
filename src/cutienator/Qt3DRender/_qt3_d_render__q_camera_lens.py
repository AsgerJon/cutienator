"""
Qt3DRender::QCameraLens binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qcameralens.h, Qt 6.12.0. Changes made here are lost.
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
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCameraLens(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QCameraLens: a plain Python object
  standing in front of one C++ Qt3DRender::QCameraLens.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QCameraLens is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QCameraLens that has a ritual and that
  Python can call so far, 42 names in all: 'metaObject', 'tr',
  'projectionType', 'nearPlane', 'farPlane', 'fieldOfView', 'aspectRatio',
  'left', 'right', 'bottom', 'top', 'projectionMatrix',
  'setOrthographicProjection', 'setFrustumProjection',
  'setPerspectiveProjection', 'exposure', 'viewAll', 'viewEntity',
  'setProjectionType', 'setNearPlane', 'setFarPlane', 'setFieldOfView',
  'setAspectRatio', 'setLeft', 'setRight', 'setBottom', 'setTop',
  'setProjectionMatrix', 'setExposure', 'projectionTypeChanged',
  'nearPlaneChanged', 'farPlaneChanged', 'fieldOfViewChanged',
  'aspectRatioChanged', 'leftChanged', 'rightChanged', 'bottomChanged',
  'topChanged', 'projectionMatrixChanged', 'exposureChanged', 'viewSphere',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QCameraLens::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QCameraLens::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QCameraLens::~QCameraLens()': the destructor: Python
    never removes a C++ Qt3DRender::QCameraLens.
  - Qt's 'Qt3DRender::QCameraLens::QCameraLens(QCameraLensPrivate &dd, QNode
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QCameraLensPrivate *Qt3DRender::QCameraLens::d_func() const':
    takes in Python what 'QCameraLensPrivate
    *Qt3DRender::QCameraLens::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 50 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QCameraLens is created at the first use, not by
    'Qt3DRender::QCameraLens(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QCameraLens.
  - Qt tells when it has removed the C++ Qt3DRender::QCameraLens. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QCameraLens, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ProjectionType(CuteNum):
    """
    The enum 'Qt3DRender::QCameraLens::ProjectionType' of Qt, with the 4
    names Qt gives in it.
    """

    OrthographicProjection = Kee[int](0)
    PerspectiveProjection = Kee[int](1)
    FrustumProjection = Kee[int](2)
    CustomProjection = Kee[int](3)

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
    Calls Qt's 'QString Qt3DRender::QCameraLens::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#tr

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
    #  QString Qt3DRender::QCameraLens::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender11QCameraLens2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QCameraLens'

  #  A C++ Qt3DRender::QCameraLens Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QCameraLens'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QCameraLens::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QCameraLens::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def projectionType(self) -> ProjectionType:
    """
    Calls Qt's 'ProjectionType Qt3DRender::QCameraLens::projectionType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#projectionType

    Returns
    -------

    ProjectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProjectionType(number)'
      gives.
    """
    #  ProjectionType Qt3DRender::QCameraLens::projectionType() const
    return QCameraLens.ProjectionType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens14projectionTypeEv',
    ))

  def nearPlane(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::nearPlane() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#nearPlane
    """
    #  float Qt3DRender::QCameraLens::nearPlane() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens9nearPlaneEv',
    )

  def farPlane(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::farPlane() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#farPlane
    """
    #  float Qt3DRender::QCameraLens::farPlane() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens8farPlaneEv',
    )

  def fieldOfView(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::fieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#fieldOfView
    """
    #  float Qt3DRender::QCameraLens::fieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens11fieldOfViewEv',
    )

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::aspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#aspectRatio
    """
    #  float Qt3DRender::QCameraLens::aspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens11aspectRatioEv',
    )

  def left(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#left
    """
    #  float Qt3DRender::QCameraLens::left() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender11QCameraLens4leftEv')

  def right(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#right
    """
    #  float Qt3DRender::QCameraLens::right() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender11QCameraLens5rightEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#bottom
    """
    #  float Qt3DRender::QCameraLens::bottom() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender11QCameraLens6bottomEv')

  def top(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#top
    """
    #  float Qt3DRender::QCameraLens::top() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender11QCameraLens3topEv')

  def projectionMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 Qt3DRender::QCameraLens::projectionMatrix()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#projectionMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 Qt3DRender::QCameraLens::projectionMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens16projectionMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def exposure(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QCameraLens::exposure() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#exposure
    """
    #  float Qt3DRender::QCameraLens::exposure() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QCameraLens8exposureEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float, float, float)
  def setOrthographicProjection(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setOrthographicProjection(float
    left, float right, float bottom, float top, float nearPlane, float
    farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setOrthographicProjection(float left,
    #      float right, float bottom, float top, float nearPlane, float
    #      farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens25setOrthographicProjectionEffff'
        'ff',
        left, right, bottom, top, nearPlane, farPlane,
    )

  @overload(float, float, float, float, float, float)
  def setFrustumProjection(
      self,
      left: float,
      right: float,
      bottom: float,
      top: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setFrustumProjection(float
    left, float right, float bottom, float top, float nearPlane, float
    farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setFrustumProjection

    Parameters
    ----------

    left : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.

    top : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setFrustumProjection(float left, float
    #      right, float bottom, float top, float nearPlane, float farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens20setFrustumProjectionEffffff',
        left, right, bottom, top, nearPlane, farPlane,
    )

  @overload(float, float, float, float)
  def setPerspectiveProjection(
      self,
      fieldOfView: float,
      aspect: float,
      nearPlane: float,
      farPlane: float,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setPerspectiveProjection(float
    fieldOfView, float aspect, float nearPlane, float farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.

    aspect : float
      Passed on as it is.

    nearPlane : float
      Passed on as it is.

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setPerspectiveProjection(float
    #      fieldOfView, float aspect, float nearPlane, float farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens24setPerspectiveProjectionEffff',
        fieldOfView, aspect, nearPlane, farPlane,
    )

  @overload(ProjectionType)
  def setProjectionType(self, projectionType: ProjectionType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLens::setProjectionType(ProjectionType
    projectionType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setProjectionType

    Parameters
    ----------

    projectionType : ProjectionType
      Passed on as its number.
    """
    #  void Qt3DRender::QCameraLens::setProjectionType(ProjectionType
    #      projectionType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens17setProjectionTypeENS0_14Projec'
        'tionTypeE',
        projectionType.value,
    )

  @overload(float)
  def setNearPlane(self, nearPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setNearPlane(float nearPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setNearPlane

    Parameters
    ----------

    nearPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setNearPlane(float nearPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens12setNearPlaneEf', nearPlane,
    )

  @overload(float)
  def setFarPlane(self, farPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setFarPlane(float farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setFarPlane

    Parameters
    ----------

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setFarPlane(float farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens11setFarPlaneEf', farPlane,
    )

  @overload(float)
  def setFieldOfView(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setFieldOfView(float
    fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setFieldOfView

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setFieldOfView(float fieldOfView)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens14setFieldOfViewEf', fieldOfView,
    )

  @overload(float)
  def setAspectRatio(self, aspectRatio: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setAspectRatio(float
    aspectRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setAspectRatio

    Parameters
    ----------

    aspectRatio : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setAspectRatio(float aspectRatio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens14setAspectRatioEf', aspectRatio,
    )

  @overload(float)
  def setLeft(self, left: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setLeft(float left)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setLeft

    Parameters
    ----------

    left : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setLeft(float left)
    self.uglySide.call('ritual_ZN10Qt3DRender11QCameraLens7setLeftEf', left)

  @overload(float)
  def setRight(self, right: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setRight(float right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setRight

    Parameters
    ----------

    right : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setRight(float right)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens8setRightEf', right,
    )

  @overload(float)
  def setBottom(self, bottom: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setBottom(float bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setBottom

    Parameters
    ----------

    bottom : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setBottom(float bottom)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens9setBottomEf', bottom,
    )

  @overload(float)
  def setTop(self, top: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setTop(float top)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setTop

    Parameters
    ----------

    top : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setTop(float top)
    self.uglySide.call('ritual_ZN10Qt3DRender11QCameraLens6setTopEf', top)

  @overload(QMatrix4x4)
  def setProjectionMatrix(self, projectionMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setProjectionMatrix(const
    QMatrix4x4 &projectionMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setProjectionMatrix

    Parameters
    ----------

    projectionMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::QCameraLens::setProjectionMatrix(const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens19setProjectionMatrixERK10QMatri'
        'x4x4',
        self._valueOf(projectionMatrix),
    )

  @overload(float)
  def setExposure(self, exposure: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::setExposure(float exposure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#setExposure

    Parameters
    ----------

    exposure : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::setExposure(float exposure)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens11setExposureEf', exposure,
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
    Notes what was given, for Qt's
    'Qt3DRender::QCameraLens::QCameraLens(QNode *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#QCameraLens

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QCameraLens::QCameraLens(QNode *parent)
    self._noteCreation(QCameraLens, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender11QCameraLensC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def viewAll(self, cameraId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::viewAll(Qt3DCore::QNodeId
    cameraId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#viewAll

    Parameters
    ----------

    cameraId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::QCameraLens::viewAll(Qt3DCore::QNodeId cameraId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens7viewAllEN8Qt3DCore7QNodeIdE',
        self._valueOf(cameraId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DCore.QNodeId'])
  def viewEntity(
      self,
      entityId: Qt3DCore.QNodeId,
      cameraId: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::viewEntity(Qt3DCore::QNodeId
    entityId, Qt3DCore::QNodeId cameraId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#viewEntity

    Parameters
    ----------

    entityId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    cameraId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::QCameraLens::viewEntity(Qt3DCore::QNodeId entityId,
    #      Qt3DCore::QNodeId cameraId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens10viewEntityEN8Qt3DCore7QNodeIdE'
        'S2_',
        self._valueOf(entityId), self._valueOf(cameraId),
    )

  @overload(ProjectionType)
  def projectionTypeChanged(self, projectionType: ProjectionType) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QCameraLens::projectionTypeChanged(QCameraLens::
    ProjectionType projectionType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#projectionTypeChanged

    Parameters
    ----------

    projectionType : ProjectionType
      Passed on as its number.
    """
    #  void Qt3DRender::QCameraLens::projectionTypeChanged(QCameraLens::
    #      ProjectionType projectionType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens21projectionTypeChangedENS0_14Pr'
        'ojectionTypeE',
        projectionType.value,
    )

  @overload(float)
  def nearPlaneChanged(self, nearPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::nearPlaneChanged(float
    nearPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#nearPlaneChanged

    Parameters
    ----------

    nearPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::nearPlaneChanged(float nearPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens16nearPlaneChangedEf', nearPlane,
    )

  @overload(float)
  def farPlaneChanged(self, farPlane: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::farPlaneChanged(float
    farPlane)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#farPlaneChanged

    Parameters
    ----------

    farPlane : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::farPlaneChanged(float farPlane)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens15farPlaneChangedEf', farPlane,
    )

  @overload(float)
  def fieldOfViewChanged(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::fieldOfViewChanged(float
    fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#fieldOfViewChanged

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::fieldOfViewChanged(float fieldOfView)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens18fieldOfViewChangedEf',
        fieldOfView,
    )

  @overload(float)
  def aspectRatioChanged(self, aspectRatio: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::aspectRatioChanged(float
    aspectRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#aspectRatioChanged

    Parameters
    ----------

    aspectRatio : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::aspectRatioChanged(float aspectRatio)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens18aspectRatioChangedEf',
        aspectRatio,
    )

  @overload(float)
  def leftChanged(self, left: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::leftChanged(float left)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#leftChanged

    Parameters
    ----------

    left : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::leftChanged(float left)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens11leftChangedEf', left,
    )

  @overload(float)
  def rightChanged(self, right: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::rightChanged(float right)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#rightChanged

    Parameters
    ----------

    right : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::rightChanged(float right)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens12rightChangedEf', right,
    )

  @overload(float)
  def bottomChanged(self, bottom: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::bottomChanged(float bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#bottomChanged

    Parameters
    ----------

    bottom : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::bottomChanged(float bottom)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens13bottomChangedEf', bottom,
    )

  @overload(float)
  def topChanged(self, top: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::topChanged(float top)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#topChanged

    Parameters
    ----------

    top : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::topChanged(float top)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens10topChangedEf', top,
    )

  @overload(QMatrix4x4)
  def projectionMatrixChanged(self, projectionMatrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::projectionMatrixChanged(const
    QMatrix4x4 &projectionMatrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html

    Parameters
    ----------

    projectionMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::QCameraLens::projectionMatrixChanged(const QMatrix4x4
    #      &projectionMatrix)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens23projectionMatrixChangedERK10QM'
        'atrix4x4',
        self._valueOf(projectionMatrix),
    )

  @overload(float)
  def exposureChanged(self, exposure: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::exposureChanged(float
    exposure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#exposureChanged

    Parameters
    ----------

    exposure : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::exposureChanged(float exposure)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens15exposureChangedEf', exposure,
    )

  @overload(QVector3D, float)
  def viewSphere(self, center: QVector3D, radius: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QCameraLens::viewSphere(const QVector3D
    &center, float radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcameralens.html#viewSphere

    Parameters
    ----------

    center : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void Qt3DRender::QCameraLens::viewSphere(const QVector3D &center,
    #      float radius)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens10viewSphereERK9QVector3Df',
        self._valueOf(center), radius,
    )

  def d_func(self) -> Optional[Qt3DRender.QCameraLensPrivate]:
    """
    Calls Qt's 'QCameraLensPrivate *Qt3DRender::QCameraLens::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcameralens.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QCameraLensPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCameraLensPrivate *Qt3DRender::QCameraLens::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender11QCameraLens6d_funcEv',
    )
    return Qt3DRender.QCameraLensPrivate._cuteAt(address)
