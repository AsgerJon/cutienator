"""
Qt3DRender::Render::CameraLens binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/cameralens_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::CameraLens to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CameraLens(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::CameraLens: a plain Python object
  standing in front of one C++ Qt3DRender::Render::CameraLens.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::CameraLens is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::CameraLens that has a ritual and
  that Python can call so far, 10 names in all: 'cleanup', 'setRenderAspect',
  'viewMatrix', 'setProjection', 'projection', 'setExposure', 'exposure',
  'syncFromFrontEnd', 'processViewAllResult', 'computeSceneBoundingVolume'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::CameraLens::~CameraLens()': the destructor:
    Python never removes a C++ Qt3DRender::Render::CameraLens.
  - Qt's 'bool
    Qt3DRender::Render::CameraLens::viewMatrixForCamera(EntityManager
    *manager, Qt3DCore::QNodeId cameraId, Matrix4x4 &viewMatrix, Matrix4x4
    &projectionMatrix)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::CameraLens is created at the first use, not
    by 'Qt3DRender::Render::CameraLens(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::CameraLens.
  - Each name of Qt's Qt3DRender::Render::CameraLens that has no cute
    function yet, 'viewMatrixForCamera', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::CameraLens'

  #  A C++ Qt3DRender::Render::CameraLens Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_CameraLens'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def projection(self) -> QMatrix4x4:
    """
    Calls Qt's 'Matrix4x4 Qt3DRender::Render::CameraLens::projection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#projection

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  Matrix4x4 Qt3DRender::Render::CameraLens::projection() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render10CameraLens10projectionEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def exposure(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::CameraLens::exposure() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#exposure
    """
    #  float Qt3DRender::Render::CameraLens::exposure() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render10CameraLens8exposureEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QRenderAspect'])
  @overload(NoneType)
  def setRenderAspect(
      self,
      renderAspect: Optional[Qt3DRender.QRenderAspect],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CameraLens::setRenderAspect(QRenderAspect
    *renderAspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#setRenderAspect

    Parameters
    ----------

    renderAspect : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::CameraLens::setRenderAspect(QRenderAspect
    #      *renderAspect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10CameraLens15setRenderAspectEPNS_13QR'
        'enderAspectE',
        self._addressOf(renderAspect),
    )

  @overload(QMatrix4x4)
  def setProjection(self, projection: QMatrix4x4) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::CameraLens::setProjection(const
    Matrix4x4 &projection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#setProjection

    Parameters
    ----------

    projection : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::CameraLens::setProjection(const Matrix4x4
    #      &projection)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10CameraLens13setProjectionERK10QMatri'
        'x4x4',
        self._valueOf(projection),
    )

  @overload(float)
  def setExposure(self, exposure: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::CameraLens::setExposure(float
    exposure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#setExposure

    Parameters
    ----------

    exposure : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::CameraLens::setExposure(float exposure)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10CameraLens11setExposureEf', exposure,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::CameraLens::CameraLens()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#CameraLens
    """
    #  Qt3DRender::Render::CameraLens::CameraLens()
    self._noteCreation(CameraLens, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render10CameraLensC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::CameraLens::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#cleanup
    """
    #  void Qt3DRender::Render::CameraLens::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render10CameraLens7cleanupEv')

  @overload(QMatrix4x4)
  def viewMatrix(self, worldTransform: QMatrix4x4) -> QMatrix4x4:
    """
    Calls Qt's 'Matrix4x4 Qt3DRender::Render::CameraLens::viewMatrix(const
    Matrix4x4 &worldTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#viewMatrix

    Parameters
    ----------

    worldTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  Matrix4x4 Qt3DRender::Render::CameraLens::viewMatrix(const Matrix4x4
    #      &worldTransform)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10CameraLens10viewMatrixERK10QMatrix4x'
        '4',
        self._valueOf(worldTransform),
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::CameraLens::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::CameraLens::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render10CameraLens16syncFromFrontEndEPKN8Qt3'
        'DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render10CameraLens16syncFromFrontEndEP'
          'KN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(
      WAIT['Qt3DCore.QAspectManager'], WAIT['Qt3DRender.Render.Sphere'],
      WAIT['Qt3DCore.QNodeId'],
  )
  @overload(
      NoneType, WAIT['Qt3DRender.Render.Sphere'], WAIT['Qt3DCore.QNodeId'],
  )
  def processViewAllResult(
      self,
      aspectManager: Optional[Qt3DCore.QAspectManager],
      sphere: Qt3DRender.Render.Sphere,
      commandId: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CameraLens::processViewAllResult(Qt3DCore::
    QAspectManager *aspectManager, const Sphere &sphere, Qt3DCore::QNodeId
    commandId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html

    Parameters
    ----------

    aspectManager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sphere : Qt3DRender.Render.Sphere
      Passed on as a value: Qt reads the C++ Qt3DRender::Render::Sphere,
      which stays Python's own.

    commandId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::CameraLens::processViewAllResult(Qt3DCore::
    #      QAspectManager *aspectManager, const Sphere &sphere,
    #      Qt3DCore::QNodeId commandId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10CameraLens20processViewAllResultEPN8'
        'Qt3DCore14QAspectManagerERKNS0_6SphereENS2_7QNodeIdE',
        self._addressOf(aspectManager), self._valueOf(sphere),
        self._valueOf(commandId),
    )

  @overload(
      WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DCore.QNodeId'],
      WAIT['Qt3DCore.QNodeId'],
  )
  def computeSceneBoundingVolume(
      self,
      entityId: Qt3DCore.QNodeId,
      cameraId: Qt3DCore.QNodeId,
      requestId: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CameraLens::computeSceneBoundingVolume(Qt3DCore::
    QNodeId entityId, Qt3DCore::QNodeId cameraId, Qt3DCore::QNodeId
    requestId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-cameralens.html

    Parameters
    ----------

    entityId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    cameraId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    requestId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::CameraLens::computeSceneBoundingVolume(
    #      Qt3DCore::QNodeId entityId, Qt3DCore::QNodeId cameraId,
    #      Qt3DCore::QNodeId requestId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10CameraLens26computeSceneBoundingVolu'
        'meEN8Qt3DCore7QNodeIdES3_S3_',
        self._valueOf(entityId), self._valueOf(cameraId),
        self._valueOf(requestId),
    )

  @staticmethod
  def viewMatrixForCamera(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::CameraLens::viewMatrixForCamera(EntityManager
    *manager, Qt3DCore::QNodeId cameraId, Matrix4x4 &viewMatrix, Matrix4x4
    &projectionMatrix)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.CameraLens.viewMatrixForCamera' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DRender::Render::CameraLens::viewMatrixForCamera(EntityManager "
        "*manager, Qt3DCore::QNodeId cameraId, Matrix4x4 &viewMatrix, "
        "Matrix4x4 &projectionMatrix)': takes a type Python has no way to "
        "hand over yet.")
