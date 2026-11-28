"""
Qt3DRender::Render::UpdateLevelOfDetailJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/updatelevelofdetailjob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::UpdateLevelOfDetailJob to be private: it
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


class UpdateLevelOfDetailJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::UpdateLevelOfDetailJob: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::UpdateLevelOfDetailJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::UpdateLevelOfDetailJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::UpdateLevelOfDetailJob that has
  a ritual and that Python can call so far, 6 names in all: 'setManagers',
  'setFrameGraphRoot', 'setRoot', 'run', 'managers', 'root'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::UpdateLevelOfDetailJob::~UpdateLevelOfDetailJob()':
    the destructor: Python never removes a C++
    Qt3DRender::Render::UpdateLevelOfDetailJob.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::UpdateLevelOfDetailJob is created at the
    first use, not by 'Qt3DRender::Render::UpdateLevelOfDetailJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::UpdateLevelOfDetailJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::UpdateLevelOfDetailJob'

  #  A C++ Qt3DRender::Render::UpdateLevelOfDetailJob Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_UpdateLevelOfDetailJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def managers(self) -> Optional[Qt3DRender.Render.NodeManagers]:
    """
    Calls Qt's 'NodeManagers
    *Qt3DRender::Render::UpdateLevelOfDetailJob::managers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html

    Returns
    -------

    Optional[Qt3DRender.Render.NodeManagers]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  NodeManagers *Qt3DRender::Render::UpdateLevelOfDetailJob::managers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22UpdateLevelOfDetailJob8managersEv',
    )
    return Qt3DRender.Render.NodeManagers._cuteAt(address)

  def root(self) -> Optional[Qt3DRender.Render.Entity]:
    """
    Calls Qt's 'Entity *Qt3DRender::Render::UpdateLevelOfDetailJob::root()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html#root

    Returns
    -------

    Optional[Qt3DRender.Render.Entity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Entity *Qt3DRender::Render::UpdateLevelOfDetailJob::root() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22UpdateLevelOfDetailJob4rootEv',
    )
    return Qt3DRender.Render.Entity._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::UpdateLevelOfDetailJob::setManagers(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::UpdateLevelOfDetailJob::setManagers(
    #      NodeManagers *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22UpdateLevelOfDetailJob11setManagersE'
        'PNS0_12NodeManagersE',
        self._addressOf(manager),
    )

  @overload(WAIT['Qt3DRender.Render.FrameGraphNode'])
  @overload(NoneType)
  def setFrameGraphRoot(
      self,
      frameGraphRoot: Optional[Qt3DRender.Render.FrameGraphNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::UpdateLevelOfDetailJob::setFrameGraphRoot(
    FrameGraphNode *frameGraphRoot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html

    Parameters
    ----------

    frameGraphRoot : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::UpdateLevelOfDetailJob::setFrameGraphRoot(
    #      FrameGraphNode *frameGraphRoot)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22UpdateLevelOfDetailJob17setFrameGrap'
        'hRootEPNS0_14FrameGraphNodeE',
        self._addressOf(frameGraphRoot),
    )

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def setRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::UpdateLevelOfDetailJob::setRoot(Entity *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::UpdateLevelOfDetailJob::setRoot(Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22UpdateLevelOfDetailJob7setRootEPNS0_'
        '6EntityE',
        self._addressOf(root),
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
    'Qt3DRender::Render::UpdateLevelOfDetailJob::UpdateLevelOfDetailJob()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html
    """
    #  Qt3DRender::Render::UpdateLevelOfDetailJob::UpdateLevelOfDetailJob()
    self._noteCreation(UpdateLevelOfDetailJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render22UpdateLevelOfDetailJobC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::UpdateLevelOfDetailJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updatelevelofdetailjob.html#run
    """
    #  void Qt3DRender::Render::UpdateLevelOfDetailJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22UpdateLevelOfDetailJob3runEv',
    )
