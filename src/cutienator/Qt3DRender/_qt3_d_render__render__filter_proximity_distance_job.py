"""
Qt3DRender::Render::FilterProximityDistanceJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/filterproximitydistancejob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FilterProximityDistanceJob to be private: it
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FilterProximityDistanceJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::FilterProximityDistanceJob: a
  plain Python object standing in front of one C++
  Qt3DRender::Render::FilterProximityDistanceJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::FilterProximityDistanceJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FilterProximityDistanceJob that
  has a ritual and that Python can call so far, 5 names in all: 'setManager',
  'hasProximityFilter', 'run', 'isRequired', 'selectAllEntities'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::FilterProximityDistanceJob::
    ~FilterProximityDistanceJob()': the destructor: Python never removes a
    C++ Qt3DRender::Render::FilterProximityDistanceJob.
  - Qt's 'void
    Qt3DRender::Render::FilterProximityDistanceJob::setProximityFilterIds(
    const Qt3DCore::QNodeIdVector &proximityFilterIds)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const std::vector<Entity *>
    &Qt3DRender::Render::FilterProximityDistanceJob::filteredEntities()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    Qt3DRender::Render::FilterProximityDistanceJob::filterEntities(const
    std::vector<Entity *> &entitiesToFilter)': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FilterProximityDistanceJob is created at the
    first use, not by 'Qt3DRender::Render::FilterProximityDistanceJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::FilterProximityDistanceJob.
  - Each name of Qt's Qt3DRender::Render::FilterProximityDistanceJob that has
    no cute function yet, 'filterEntities', 'filteredEntities',
    'setProximityFilterIds', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::FilterProximityDistanceJob'

  #  A C++ Qt3DRender::Render::FilterProximityDistanceJob Python makes is of
  #  a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_FilterProximityDistanceJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasProximityFilter(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::FilterProximityDistanceJob::hasProximityFilter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterproximitydistancejob.html
    """
    #  bool Qt3DRender::Render::FilterProximityDistanceJob::
    #      hasProximityFilter() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render26FilterProximityDistanceJob18hasProx'
        'imityFilterEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setManager(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FilterProximityDistanceJob::setManager(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterproximitydistancejob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FilterProximityDistanceJob::setManager(
    #      NodeManagers *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob10setManag'
        'erEPNS0_12NodeManagersE',
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
    'Qt3DRender::Render::FilterProximityDistanceJob::
    FilterProximityDistanceJob()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterproximitydistancejob.html
    """
    #  Qt3DRender::Render::FilterProximityDistanceJob::
    #      FilterProximityDistanceJob()
    self._noteCreation(FilterProximityDistanceJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJobC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::FilterProximityDistanceJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterproximitydistancejob.html
    """
    #  void Qt3DRender::Render::FilterProximityDistanceJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob3runEv',
    )

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::FilterProximityDistanceJob::isRequired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterproximitydistancejob.html
    """
    #  bool Qt3DRender::Render::FilterProximityDistanceJob::isRequired()
    ritual = (
        'ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob10isRequir'
        'edEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render26FilterProximityDistanceJob10is'
          'RequiredEv')
    return self.uglySide.call(ritual)

  def selectAllEntities(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FilterProximityDistanceJob::selectAllEntities()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterproximitydistancejob.html
    """
    #  void
    #      Qt3DRender::Render::FilterProximityDistanceJob::selectAllEntities(
    #      )
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob17selectAl'
        'lEntitiesEv',
    )

  @staticmethod
  def filterEntities(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterProximityDistanceJob::filterEntities(const
    std::vector<Entity *> &entitiesToFilter)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterProximityDistanceJob.filterEntities' has "
        "no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterProximityDistanceJob::filterEntities(cons"
        "t std::vector<Entity *> &entitiesToFilter)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def filteredEntities(*__, **_) -> Never:
    """
    Qt's 'const std::vector<Entity *>
    &Qt3DRender::Render::FilterProximityDistanceJob::filteredEntities()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterProximityDistanceJob.filteredEntities' "
        "has no cute function yet. Qt's 'const std::vector<Entity *> "
        "&Qt3DRender::Render::FilterProximityDistanceJob::filteredEntities()"
        " const': gives a type Python has no way to take yet.")

  @staticmethod
  def setProximityFilterIds(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterProximityDistanceJob::setProximityFilterIds(
    const Qt3DCore::QNodeIdVector &proximityFilterIds)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterProximityDistanceJob.setProximityFilterIds"
        "' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterProximityDistanceJob::setProximityFilterI"
        "ds(const Qt3DCore::QNodeIdVector &proximityFilterIds)': takes a "
        "type Python has no way to hand over yet.")
