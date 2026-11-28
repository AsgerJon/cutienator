"""
Qt3DRender::Render::FrameCleanupJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/framecleanupjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FrameCleanupJob to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FrameCleanupJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::FrameCleanupJob: a plain Python
  object standing in front of one C++ Qt3DRender::Render::FrameCleanupJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::FrameCleanupJob is built on Qt's Qt3DCore::QAspectJob,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FrameCleanupJob that has a
  ritual and that Python can call so far, 4 names in all: 'setRoot',
  'setManagers', 'run', 'updateBoundingVolumesDebug'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::FrameCleanupJob::~FrameCleanupJob()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::FrameCleanupJob.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FrameCleanupJob is created at the first use,
    not by 'Qt3DRender::Render::FrameCleanupJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::FrameCleanupJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FrameCleanupJob'

  #  A C++ Qt3DRender::Render::FrameCleanupJob Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_FrameCleanupJob'

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
  def setRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::FrameCleanupJob::setRoot(Entity
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framecleanupjob.html#setRoot

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrameCleanupJob::setRoot(Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render15FrameCleanupJob7setRootEPNS0_6Entity'
        'E',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      managers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameCleanupJob::setManagers(NodeManagers
    *managers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framecleanupjob.html#setManagers

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrameCleanupJob::setManagers(NodeManagers
    #      *managers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render15FrameCleanupJob11setManagersEPNS0_12'
        'NodeManagersE',
        self._addressOf(managers),
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
    'Qt3DRender::Render::FrameCleanupJob::FrameCleanupJob()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framecleanupjob.html
    """
    #  Qt3DRender::Render::FrameCleanupJob::FrameCleanupJob()
    self._noteCreation(FrameCleanupJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render15FrameCleanupJobC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::FrameCleanupJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framecleanupjob.html#run
    """
    #  void Qt3DRender::Render::FrameCleanupJob::run()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render15FrameCleanupJob3runEv')

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def updateBoundingVolumesDebug(
      self,
      node: Optional[Qt3DRender.Render.Entity],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameCleanupJob::updateBoundingVolumesDebug(Entity
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framecleanupjob.html

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrameCleanupJob::updateBoundingVolumesDebug(
    #      Entity *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render15FrameCleanupJob26updateBoundingVolum'
        'esDebugEPNS0_6EntityE',
        self._addressOf(node),
    )
