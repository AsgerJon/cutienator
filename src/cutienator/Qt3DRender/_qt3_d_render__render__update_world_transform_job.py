"""
Qt3DRender::Render::UpdateWorldTransformJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/updateworldtransformjob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::UpdateWorldTransformJob to be private: it
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


class UpdateWorldTransformJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::UpdateWorldTransformJob: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::UpdateWorldTransformJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::UpdateWorldTransformJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::UpdateWorldTransformJob that has
  a ritual and that Python can call so far, 3 names in all: 'setRoot',
  'setManagers', 'run'. It can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::UpdateWorldTransformJob is created at the
    first use, not by 'Qt3DRender::Render::UpdateWorldTransformJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::UpdateWorldTransformJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::UpdateWorldTransformJob'

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
    Qt3DRender::Render::UpdateWorldTransformJob::setRoot(Entity *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updateworldtransformjob.html

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::UpdateWorldTransformJob::setRoot(Entity
    #      *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render23UpdateWorldTransformJob7setRootEPNS0'
        '_6EntityE',
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
    Qt3DRender::Render::UpdateWorldTransformJob::setManagers(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updateworldtransformjob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::UpdateWorldTransformJob::setManagers(
    #      NodeManagers *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render23UpdateWorldTransformJob11setManagers'
        'EPNS0_12NodeManagersE',
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
    'Qt3DRender::Render::UpdateWorldTransformJob::UpdateWorldTransformJob()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updateworldtransformjob.html
    """
    #  Qt3DRender::Render::UpdateWorldTransformJob::UpdateWorldTransformJob()
    self._noteCreation(UpdateWorldTransformJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render23UpdateWorldTransformJobC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::UpdateWorldTransformJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-updateworldtransformjob.html#run
    """
    #  void Qt3DRender::Render::UpdateWorldTransformJob::run()
    ritual = 'ritual_ZN10Qt3DRender6Render23UpdateWorldTransformJob3runEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render23UpdateWorldTransformJob3runEv')
    self.uglySide.call(ritual)
