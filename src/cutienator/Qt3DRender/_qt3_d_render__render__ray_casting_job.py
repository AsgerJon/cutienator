"""
Qt3DRender::Render::RayCastingJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/raycastingjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::RayCastingJob to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class RayCastingJob(Qt3DRender.Render.AbstractPickingJob):
  """
  The cute side of Qt's Qt3DRender::Render::RayCastingJob: a plain Python
  object standing in front of one C++ Qt3DRender::Render::RayCastingJob.

  It is built on the cute 'Qt3DRender::Render::AbstractPickingJob', as Qt's
  Qt3DRender::Render::RayCastingJob is built on Qt's
  Qt3DRender::Render::AbstractPickingJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RayCastingJob that has a ritual
  and that Python can call so far, 2 names in all: 'markCastersDirty',
  'runHelper'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractRayCaster::Hits
    Qt3DRender::Render::RayCastingJob::pick(QAbstractRayCaster *rayCaster)':
    gives a type Python has no way to take yet.
  - Qt's 'bool Qt3DRender::Render::RayCastingJob::pick(const
    QList<QPair<Entity *, RayCaster *>> &entities)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void Qt3DRender::Render::RayCastingJob::dispatchHits(RayCaster
    *rayCaster, const PickingUtils::HitList &sphereHits)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RayCastingJob is created at the first use,
    not by 'Qt3DRender::Render::RayCastingJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RayCastingJob.
  - Each name of Qt's Qt3DRender::Render::RayCastingJob that has no cute
    function yet, 'dispatchHits', 'pick', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::RayCastingJob'

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
    'Qt3DRender::Render::RayCastingJob::RayCastingJob()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycastingjob.html#RayCastingJob
    """
    #  Qt3DRender::Render::RayCastingJob::RayCastingJob()
    self._noteCreation(RayCastingJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13RayCastingJobC1Ev',
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

  def markCastersDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RayCastingJob::markCastersDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycastingjob.html
    """
    #  void Qt3DRender::Render::RayCastingJob::markCastersDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13RayCastingJob16markCastersDirtyEv',
    )

  def runHelper(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::RayCastingJob::runHelper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-raycastingjob.html#runHelper
    """
    #  bool Qt3DRender::Render::RayCastingJob::runHelper()
    ritual = 'ritual_ZN10Qt3DRender6Render13RayCastingJob9runHelperEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender6Render13RayCastingJob9runHelperEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def dispatchHits(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::RayCastingJob::dispatchHits(RayCaster
    *rayCaster, const PickingUtils::HitList &sphereHits)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RayCastingJob.dispatchHits' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::RayCastingJob::dispatchHits(RayCaster "
        "*rayCaster, const PickingUtils::HitList &sphereHits)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def pick(*__, **_) -> Never:
    """
    - Qt's 'QAbstractRayCaster::Hits
      Qt3DRender::Render::RayCastingJob::pick(QAbstractRayCaster
      *rayCaster)': gives a type Python has no way to take yet.
    - Qt's 'bool Qt3DRender::Render::RayCastingJob::pick(const
      QList<QPair<Entity *, RayCaster *>> &entities)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RayCastingJob.pick' has no cute function yet. "
        "Qt's 'QAbstractRayCaster::Hits "
        "Qt3DRender::Render::RayCastingJob::pick(QAbstractRayCaster "
        "*rayCaster)': gives a type Python has no way to take yet. Qt's "
        "'bool Qt3DRender::Render::RayCastingJob::pick(const "
        "QList<QPair<Entity *, RayCaster *>> &entities)': takes a type "
        "Python has no way to hand over yet.")
