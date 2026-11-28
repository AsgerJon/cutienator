"""
Qt3DRender::Render::AbstractPickingJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/abstractpickingjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::AbstractPickingJob to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QPoint, QRect, QRectF, QSize
  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QObject = WAIT['QObject']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractPickingJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::AbstractPickingJob: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::AbstractPickingJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::AbstractPickingJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::AbstractPickingJob that has a
  ritual and that Python can call so far, 9 names in all: 'setRoot',
  'setFrameGraphRoot', 'setRenderSettings', 'setManagers', 'runHelper',
  'intersectionRay', 'run', 'windowViewport', 'rayForViewportAndCamera'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::AbstractPickingJob::AbstractPickingJob(Qt3DCore::
    QAspectJobPrivate &dd)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::AbstractPickingJob is created at the first
    use, not by 'Qt3DRender::Render::AbstractPickingJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::AbstractPickingJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPoint, QMatrix4x4, QMatrix4x4, QRect)
  def intersectionRay(
      pos: QPoint,
      viewMatrix: QMatrix4x4,
      projectionMatrix: QMatrix4x4,
      viewport: QRect,
  ) -> Qt3DRender.RayCasting.QRay3D:
    """
    Calls Qt's 'RayCasting::QRay3D
    Qt3DRender::Render::AbstractPickingJob::intersectionRay(const QPoint
    &pos, const Matrix4x4 &viewMatrix, const Matrix4x4 &projectionMatrix,
    const QRect &viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    viewMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    projectionMatrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    Qt3DRender.RayCasting.QRay3D
      A new cute Qt3DRender::RayCasting::QRay3D around the copy Qt gave back.
      Python owns it.
    """
    #  RayCasting::QRay3D
    #      Qt3DRender::Render::AbstractPickingJob::intersectionRay(const
    #      QPoint &pos, const Matrix4x4 &viewMatrix, const Matrix4x4
    #      &projectionMatrix, const QRect &viewport)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob15intersectionRayE'
        'RK6QPointRK10QMatrix4x4S7_RK5QRect',
        CuteMixin._valueOf(pos), CuteMixin._valueOf(viewMatrix),
        CuteMixin._valueOf(projectionMatrix), CuteMixin._valueOf(viewport),
    )
    return Qt3DRender.RayCasting.QRay3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::AbstractPickingJob'

  #  A C++ Qt3DRender::Render::AbstractPickingJob Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_AbstractPickingJob'

  #  The functions Qt calls itself that
  #  Qt3DRender::Render::AbstractPickingJob is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'runHelper': (
          ('_ZN10Qt3DRender6Render18AbstractPickingJob9runHelperEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize, QRectF)
  def windowViewport(self, area: QSize, relativeViewport: QRectF) -> QRect:
    """
    Calls Qt's 'QRect
    Qt3DRender::Render::AbstractPickingJob::windowViewport(const QSize &area,
    const QRectF &relativeViewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html

    Parameters
    ----------

    area : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    relativeViewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Qt3DRender::Render::AbstractPickingJob::windowViewport(const
    #      QSize &area, const QRectF &relativeViewport) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18AbstractPickingJob14windowViewportE'
        'RK5QSizeRK6QRectF',
        self._valueOf(area), self._valueOf(relativeViewport),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(
      WAIT['Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails'],
      QObject, QPoint,
  )
  @overload(
      WAIT['Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails'],
      NoneType, QPoint,
  )
  def rayForViewportAndCamera(
      self,
      vca: Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails,
      eventSource: Optional[QObject],
      pos: QPoint,
  ) -> Qt3DRender.RayCasting.QRay3D:
    """
    Calls Qt's 'RayCasting::QRay3D
    Qt3DRender::Render::AbstractPickingJob::rayForViewportAndCamera(const
    PickingUtils::ViewportCameraAreaDetails &vca, QObject *eventSource, const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html

    Parameters
    ----------

    vca : Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails, which
      stays Python's own.

    eventSource : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Qt3DRender.RayCasting.QRay3D
      A new cute Qt3DRender::RayCasting::QRay3D around the copy Qt gave back.
      Python owns it.
    """
    #  RayCasting::QRay3D
    #      Qt3DRender::Render::AbstractPickingJob::rayForViewportAndCamera(
    #      const PickingUtils::ViewportCameraAreaDetails &vca, QObject
    #      *eventSource, const QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render18AbstractPickingJob23rayForViewportA'
        'ndCameraERKNS0_12PickingUtils25ViewportCameraAreaDetailsEP7QObject'
        'RK6QPoint',
        self._valueOf(vca), self._addressOf(eventSource, 'QObject'),
        self._valueOf(pos),
    )
    return Qt3DRender.RayCasting.QRay3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def setRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractPickingJob::setRoot(Entity
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html#setRoot

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractPickingJob::setRoot(Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob7setRootEPNS0_6Ent'
        'ityE',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DRender.Render.FrameGraphNode'])
  @overload(NoneType)
  def setFrameGraphRoot(
      self,
      frameGraphRoot: Optional[Qt3DRender.Render.FrameGraphNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractPickingJob::setFrameGraphRoot(FrameGraphNode
    *frameGraphRoot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html

    Parameters
    ----------

    frameGraphRoot : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractPickingJob::setFrameGraphRoot(
    #      FrameGraphNode *frameGraphRoot)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob17setFrameGraphRoo'
        'tEPNS0_14FrameGraphNodeE',
        self._addressOf(frameGraphRoot),
    )

  @overload(WAIT['Qt3DRender.Render.RenderSettings'])
  @overload(NoneType)
  def setRenderSettings(
      self,
      settings: Optional[Qt3DRender.Render.RenderSettings],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractPickingJob::setRenderSettings(RenderSettings
    *settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html

    Parameters
    ----------

    settings : Optional[Qt3DRender.Render.RenderSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractPickingJob::setRenderSettings(
    #      RenderSettings *settings)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob17setRenderSetting'
        'sEPNS0_14RenderSettingsE',
        self._addressOf(settings),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::AbstractPickingJob::setManagers(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::AbstractPickingJob::setManagers(NodeManagers
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob11setManagersEPNS0'
        '_12NodeManagersE',
        self._addressOf(manager),
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
    'Qt3DRender::Render::AbstractPickingJob::AbstractPickingJob()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html
    """
    #  Qt3DRender::Render::AbstractPickingJob::AbstractPickingJob()
    self._noteCreation(AbstractPickingJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJobC1Ev',
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

  def runHelper(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::AbstractPickingJob::runHelper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html
    """
    #  bool Qt3DRender::Render::AbstractPickingJob::runHelper()
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob9runHelperEv',
    )

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::AbstractPickingJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-abstractpickingjob.html#run
    """
    #  void Qt3DRender::Render::AbstractPickingJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render18AbstractPickingJob3runEv',
    )
