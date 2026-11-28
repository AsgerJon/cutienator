"""
Qt3DRender::Render::ComputeFilteredBoundingVolumeJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/computefilteredboundingvolumejob_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::ComputeFilteredBoundingVolumeJob to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
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


class ComputeFilteredBoundingVolumeJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::ComputeFilteredBoundingVolumeJob:
  a plain Python object standing in front of one C++
  Qt3DRender::Render::ComputeFilteredBoundingVolumeJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::ComputeFilteredBoundingVolumeJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ComputeFilteredBoundingVolumeJob
  that has a ritual and that Python can call so far, 5 names in all:
  'setRoot', 'setManagers', 'ignoreSubTree', 'run', 'finished'. It can be
  made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ComputeFilteredBoundingVolumeJob is created
    at the first use, not by
    'Qt3DRender::Render::ComputeFilteredBoundingVolumeJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ComputeFilteredBoundingVolumeJob'

  #  The functions Qt calls itself that
  #  Qt3DRender::Render::ComputeFilteredBoundingVolumeJob is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'finished': (
          ('_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8finish'
           'edEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QAspectManager'),
               ('address', 'value', 'Qt3DRender:Qt3DRender.Render.Sphere'),
           )),
      ),
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
  def setRoot(self, root: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::setRoot(Entity
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computefilteredboundingvolumejob.html

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::setRoot(
    #      Entity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob7set'
        'RootEPNS0_6EntityE',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::setManagers(
    NodeManagers *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computefilteredboundingvolumejob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::setManagers(
    #      NodeManagers *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob11se'
        'tManagersEPNS0_12NodeManagersE',
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
    'Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::
    ComputeFilteredBoundingVolumeJob()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computefilteredboundingvolumejob.html
    """
    #  Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::
    #      ComputeFilteredBoundingVolumeJob()
    self._noteCreation(
        ComputeFilteredBoundingVolumeJob, lambda: Rituals.call(
            'ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob'
            'C1Ev',
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

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def ignoreSubTree(self, node: Optional[Qt3DRender.Render.Entity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::ignoreSubTree(
    Entity *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computefilteredboundingvolumejob.html

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::
    #      ignoreSubTree(Entity *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob13ig'
        'noreSubTreeEPNS0_6EntityE',
        self._addressOf(node),
    )

  def run(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computefilteredboundingvolumejob.html
    """
    #  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run()
    ritual = (
        'ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob3run'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJ'
          'ob3runEv')
    self.uglySide.call(ritual)

  @overload(
      WAIT['Qt3DCore.QAspectManager'], WAIT['Qt3DRender.Render.Sphere'],
  )
  @overload(NoneType, WAIT['Qt3DRender.Render.Sphere'])
  def finished(
      self,
      aspectManager: Optional[Qt3DCore.QAspectManager],
      sphere: Qt3DRender.Render.Sphere,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(
    Qt3DCore::QAspectManager *aspectManager, const Qt3DRender::Render::Sphere
    &sphere)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-computefilteredboundingvolumejob.html

    Parameters
    ----------

    aspectManager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sphere : Qt3DRender.Render.Sphere
      Passed on as a value: Qt reads the C++ Qt3DRender::Render::Sphere,
      which stays Python's own.
    """
    #  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(
    #      Qt3DCore::QAspectManager *aspectManager, const
    #      Qt3DRender::Render::Sphere &sphere)
    ritual = (
        'ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8fin'
        'ishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJ'
          'ob8finishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE')
    self.uglySide.call(
        ritual, self._addressOf(aspectManager), self._valueOf(sphere),
    )
