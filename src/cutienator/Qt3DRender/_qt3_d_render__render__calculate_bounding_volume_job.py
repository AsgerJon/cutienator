"""
Qt3DRender::Render::CalculateBoundingVolumeJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/calcboundingvolumejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::CalculateBoundingVolumeJob to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CalculateBoundingVolumeJob(Qt3DCore.QAspectJob, Qt3DCore.BoundingVolumeJobProcessor):
  """
  The cute side of Qt's Qt3DRender::Render::CalculateBoundingVolumeJob: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::CalculateBoundingVolumeJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::CalculateBoundingVolumeJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has. It is built on the
  cute 'Qt3DCore::BoundingVolumeJobProcessor' as well, as Qt's
  Qt3DRender::Render::CalculateBoundingVolumeJob is built on Qt's
  Qt3DCore::BoundingVolumeJobProcessor too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::CalculateBoundingVolumeJob that
  has a ritual and that Python can call so far, 6 names in all: 'setRoot',
  'setManagers', 'setFrontEndNodeManager', 'run', 'postFrame', 'process'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::CalculateBoundingVolumeJob is created at the
    first use, not by 'Qt3DRender::Render::CalculateBoundingVolumeJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::CalculateBoundingVolumeJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::CalculateBoundingVolumeJob'

  #  Qt's Qt3DRender::Render::CalculateBoundingVolumeJob is built on more
  #  than one class. The part of a C++
  #  Qt3DRender::Render::CalculateBoundingVolumeJob that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'Qt3DCore::BoundingVolumeJobProcessor':
          'ritual_cast_Qt3DRender_Render_CalculateBoundingVolumeJob_Qt3DCore_BoundingVolumeJobProcessor',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def setRoot(self, node: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CalculateBoundingVolumeJob::setRoot(Entity *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::CalculateBoundingVolumeJob::setRoot(Entity
    #      *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob7setRootEP'
        'NS0_6EntityE',
        self._addressOf(node),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CalculateBoundingVolumeJob::setManagers(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::CalculateBoundingVolumeJob::setManagers(
    #      NodeManagers *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob11setManag'
        'ersEPNS0_12NodeManagersE',
        self._addressOf(manager),
    )

  @overload(WAIT['Qt3DCore.QAbstractFrontEndNodeManager'])
  @overload(NoneType)
  def setFrontEndNodeManager(
      self,
      manager: Optional[Qt3DCore.QAbstractFrontEndNodeManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CalculateBoundingVolumeJob::setFrontEndNodeManager(
    Qt3DCore::QAbstractFrontEndNodeManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html

    Parameters
    ----------

    manager : Optional[Qt3DCore.QAbstractFrontEndNodeManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::CalculateBoundingVolumeJob::
    #      setFrontEndNodeManager(Qt3DCore::QAbstractFrontEndNodeManager
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob22setFront'
        'EndNodeManagerEPN8Qt3DCore28QAbstractFrontEndNodeManagerE',
        self._addressOf(manager, 'Qt3DCore::QAbstractFrontEndNodeManager'),
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
    'Qt3DRender::Render::CalculateBoundingVolumeJob::
    CalculateBoundingVolumeJob()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html
    """
    #  Qt3DRender::Render::CalculateBoundingVolumeJob::
    #      CalculateBoundingVolumeJob()
    self._noteCreation(CalculateBoundingVolumeJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJobC1Ev',
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::CalculateBoundingVolumeJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html
    """
    #  void Qt3DRender::Render::CalculateBoundingVolumeJob::run()
    ritual = 'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob3runEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob3run'
          'Ev')
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def postFrame(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CalculateBoundingVolumeJob::postFrame(Qt3DCore::
    QAspectEngine *aspectEngine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::CalculateBoundingVolumeJob::postFrame(
    #      Qt3DCore::QAspectEngine *aspectEngine)
    ritual = (
        'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob9postFrame'
        'EPN8Qt3DCore13QAspectEngineE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob9pos'
          'tFrameEPN8Qt3DCore13QAspectEngineE')
    self.uglySide.call(ritual, self._addressOf(aspectEngine))

  @overload(WAIT['Qt3DCore.BoundingVolumeComputeResult'], bool)
  def process(
      self,
      result: Qt3DCore.BoundingVolumeComputeResult,
      computedResult: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::CalculateBoundingVolumeJob::process(const
    Qt3DCore::BoundingVolumeComputeResult &result, bool computedResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-calculateboundingvolumejob.html

    Parameters
    ----------

    result : Qt3DCore.BoundingVolumeComputeResult
      Passed on as a value: Qt reads the C++
      Qt3DCore::BoundingVolumeComputeResult, which stays Python's own.

    computedResult : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::CalculateBoundingVolumeJob::process(const
    #      Qt3DCore::BoundingVolumeComputeResult &result, bool
    #      computedResult)
    ritual = (
        'ritual_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob7processER'
        'KN8Qt3DCore27BoundingVolumeComputeResultEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render26CalculateBoundingVolumeJob7pro'
          'cessERKN8Qt3DCore27BoundingVolumeComputeResultEb')
    self.uglySide.call(ritual, self._valueOf(result), computedResult)
