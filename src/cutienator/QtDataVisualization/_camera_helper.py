"""
CameraHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/camerahelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means CameraHelper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import Q3DCamera

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QPointF
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QVector3D = WAIT['QVector3D']


class CameraHelper(QObject):
  """
  The cute side of Qt's CameraHelper: a plain Python object standing in front
  of one C++ CameraHelper.

  It is built on the cute 'QObject', as Qt's CameraHelper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's CameraHelper that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'setRotationSpeed',
  'setCameraRotation', 'getCameraRotations', 'setDefaultCameraOrientation',
  'calculateViewMatrix', 'calculateLightPosition', 'updateMousePos',
  'setCameraPreset'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CameraHelper::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int CameraHelper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'CameraHelper::~CameraHelper()': the destructor: Python never
    removes a C++ CameraHelper.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 leans on 'CameraHelper.

  What to expect
  --------------

  - The C++ CameraHelper is created at the first use, not by
    'CameraHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CameraHelper.
  - Qt tells when it has removed the C++ CameraHelper. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's CameraHelper that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CameraHelper'

  #  A C++ CameraHelper Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CameraHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CameraHelper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/camerahelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CameraHelper::metaObject() const
    address = self.uglySide.call('ritual_ZNK12CameraHelper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRotationSpeed(self, speed: int) -> None:
    """
    Calls Qt's 'void CameraHelper::setRotationSpeed(int speed)'.

    Qt's own words: https://doc.qt.io/qt-6/camerahelper.html#setRotationSpeed

    Parameters
    ----------

    speed : int
      Passed on as it is.
    """
    #  void CameraHelper::setRotationSpeed(int speed)
    self.uglySide.call('ritual_ZN12CameraHelper16setRotationSpeedEi', speed)

  @overload(QPointF)
  def setCameraRotation(self, rotation: QPointF) -> None:
    """
    Calls Qt's 'void CameraHelper::setCameraRotation(const QPointF
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/camerahelper.html#setCameraRotation

    Parameters
    ----------

    rotation : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void CameraHelper::setCameraRotation(const QPointF &rotation)
    self.uglySide.call(
        'ritual_ZN12CameraHelper17setCameraRotationERK7QPointF',
        self._valueOf(rotation, 'QPointF'),
    )

  @overload(QVector3D, QVector3D, QVector3D)
  def setDefaultCameraOrientation(
      self,
      defaultPosition: QVector3D,
      defaultTarget: QVector3D,
      defaultUp: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void CameraHelper::setDefaultCameraOrientation(const
    QVector3D &defaultPosition, const QVector3D &defaultTarget, const
    QVector3D &defaultUp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/camerahelper.html#setDefaultCameraOrientation

    Parameters
    ----------

    defaultPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    defaultTarget : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    defaultUp : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void CameraHelper::setDefaultCameraOrientation(const QVector3D
    #      &defaultPosition, const QVector3D &defaultTarget, const QVector3D
    #      &defaultUp)
    self.uglySide.call(
        'ritual_ZN12CameraHelper27setDefaultCameraOrientationERK9QVector3DS'
        '2_S2_',
        self._valueOf(defaultPosition), self._valueOf(defaultTarget),
        self._valueOf(defaultUp),
    )

  @overload(Q3DCamera.CameraPreset)
  def setCameraPreset(self, preset: Q3DCamera.CameraPreset) -> None:
    """
    Calls Qt's 'void CameraHelper::setCameraPreset(Q3DCamera::CameraPreset
    preset)'.

    Qt's own words: https://doc.qt.io/qt-6/camerahelper.html#setCameraPreset

    Parameters
    ----------

    preset : Q3DCamera.CameraPreset
      Passed on as its number.
    """
    #  void CameraHelper::setCameraPreset(Q3DCamera::CameraPreset preset)
    self.uglySide.call(
        'ritual_ZN12CameraHelper15setCameraPresetEN9Q3DCamera12CameraPreset'
        'E',
        preset.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'CameraHelper::CameraHelper(QObject *parent)': leans on
    'CameraHelper::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'CameraHelper.__init__' has no cute function yet. Qt's "
        "'CameraHelper::CameraHelper(QObject *parent)': leans on "
        "'CameraHelper::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def getCameraRotations(self) -> QPointF:
    """
    Calls Qt's 'QPointF CameraHelper::getCameraRotations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/camerahelper.html#getCameraRotations

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF CameraHelper::getCameraRotations()
    address = self.uglySide.call(
        'ritual_ZN12CameraHelper18getCameraRotationsEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPoint, int, int, int)
  @overload(QPoint, int, int, int, bool)
  def calculateViewMatrix(
      self,
      mousePos: QPoint,
      zoom: int,
      screenWidth: int,
      screenHeight: int,
      showUnder: bool = False,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 CameraHelper::calculateViewMatrix(const QPoint
    &mousePos, int zoom, int screenWidth, int screenHeight, bool showUnder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/camerahelper.html#calculateViewMatrix

    Parameters
    ----------

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    zoom : int
      Passed on as it is.

    screenWidth : int
      Passed on as it is.

    screenHeight : int
      Passed on as it is.

    showUnder : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 CameraHelper::calculateViewMatrix(const QPoint &mousePos,
    #      int zoom, int screenWidth, int screenHeight, bool showUnder)
    address = self.uglySide.call(
        'ritual_ZN12CameraHelper19calculateViewMatrixERK6QPointiiib',
        self._valueOf(mousePos), zoom, screenWidth, screenHeight, showUnder,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QVector3D)
  @overload(QVector3D, float)
  @overload(QVector3D, float, float)
  def calculateLightPosition(
      self,
      lightPosition: QVector3D,
      fixedRotation: float = 0.0,
      distanceModifier: float = 0.0,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D CameraHelper::calculateLightPosition(const
    QVector3D &lightPosition, GLfloat fixedRotation, GLfloat
    distanceModifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/camerahelper.html#calculateLightPosition

    Parameters
    ----------

    lightPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    fixedRotation : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    distanceModifier : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D CameraHelper::calculateLightPosition(const QVector3D
    #      &lightPosition, GLfloat fixedRotation, GLfloat distanceModifier)
    address = self.uglySide.call(
        'ritual_ZN12CameraHelper22calculateLightPositionERK9QVector3Dff',
        self._valueOf(lightPosition), fixedRotation, distanceModifier,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QPoint)
  def updateMousePos(self, mousePos: QPoint) -> None:
    """
    Calls Qt's 'void CameraHelper::updateMousePos(const QPoint &mousePos)'.

    Qt's own words: https://doc.qt.io/qt-6/camerahelper.html#updateMousePos

    Parameters
    ----------

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void CameraHelper::updateMousePos(const QPoint &mousePos)
    self.uglySide.call(
        'ritual_ZN12CameraHelper14updateMousePosERK6QPoint',
        self._valueOf(mousePos),
    )
