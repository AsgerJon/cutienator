"""
Qt3DRender::Render::FilterLayerEntityJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/filterlayerentityjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FilterLayerEntityJob to be private: it
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


class FilterLayerEntityJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::FilterLayerEntityJob: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::FilterLayerEntityJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::FilterLayerEntityJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FilterLayerEntityJob that has a
  ritual and that Python can call so far, 5 names in all: 'setManager',
  'hasLayerFilter', 'run', 'filterLayerAndEntity', 'selectAllEntities'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::setLayerFilters(const
    Qt3DCore::QNodeIdVector &layerIds)': takes a type Python has no way to
    hand over yet.
  - Qt's 'std::vector<Entity *>
    &Qt3DRender::Render::FilterLayerEntityJob::filteredEntities()': gives a
    type Python has no way to take yet.
  - Qt's 'Qt3DCore::QNodeIdVector
    Qt3DRender::Render::FilterLayerEntityJob::layerFilters() const': gives a
    type Python has no way to take yet.
  - Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterEntityAgainstLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds, const
    QLayerFilter::FilterMode filterMode)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAnyMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAllMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAnyMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAllMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FilterLayerEntityJob is created at the first
    use, not by 'Qt3DRender::Render::FilterLayerEntityJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::FilterLayerEntityJob.
  - Each name of Qt's Qt3DRender::Render::FilterLayerEntityJob that has no
    cute function yet, 'filterAcceptAllMatchingLayers',
    'filterAcceptAnyMatchingLayers', 'filterDiscardAllMatchingLayers',
    'filterDiscardAnyMatchingLayers', 'filterEntityAgainstLayers',
    'filteredEntities', 'layerFilters', 'setLayerFilters', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FilterLayerEntityJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasLayerFilter(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::FilterLayerEntityJob::hasLayerFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterlayerentityjob.html
    """
    #  bool Qt3DRender::Render::FilterLayerEntityJob::hasLayerFilter() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render20FilterLayerEntityJob14hasLayerFilte'
        'rEv',
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
    Qt3DRender::Render::FilterLayerEntityJob::setManager(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterlayerentityjob.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FilterLayerEntityJob::setManager(NodeManagers
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob10setManagerEPNS'
        '0_12NodeManagersE',
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
    'Qt3DRender::Render::FilterLayerEntityJob::FilterLayerEntityJob()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterlayerentityjob.html
    """
    #  Qt3DRender::Render::FilterLayerEntityJob::FilterLayerEntityJob()
    self._noteCreation(FilterLayerEntityJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render20FilterLayerEntityJobC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::FilterLayerEntityJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterlayerentityjob.html#run
    """
    #  void Qt3DRender::Render::FilterLayerEntityJob::run()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob3runEv',
    )

  def filterLayerAndEntity(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterLayerAndEntity()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterlayerentityjob.html
    """
    #  void Qt3DRender::Render::FilterLayerEntityJob::filterLayerAndEntity()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob20filterLayerAnd'
        'EntityEv',
    )

  def selectAllEntities(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::selectAllEntities()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-filterlayerentityjob.html
    """
    #  void Qt3DRender::Render::FilterLayerEntityJob::selectAllEntities()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob17selectAllEntit'
        'iesEv',
    )

  @staticmethod
  def filterAcceptAllMatchingLayers(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAllMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.filterAcceptAllMatchingLaye"
        "rs' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAllMatchingLa"
        "yers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def filterAcceptAnyMatchingLayers(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAnyMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.filterAcceptAnyMatchingLaye"
        "rs' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAnyMatchingLa"
        "yers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def filterDiscardAllMatchingLayers(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAllMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.filterDiscardAllMatchingLay"
        "ers' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAllMatchingL"
        "ayers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def filterDiscardAnyMatchingLayers(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAnyMatchingLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.filterDiscardAnyMatchingLay"
        "ers' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAnyMatchingL"
        "ayers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def filterEntityAgainstLayers(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::filterEntityAgainstLayers(
    Entity *entity, const Qt3DCore::QNodeIdVector &layerIds, const
    QLayerFilter::FilterMode filterMode)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.filterEntityAgainstLayers' "
        "has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterLayerEntityJob::filterEntityAgainstLayers"
        "(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds, const "
        "QLayerFilter::FilterMode filterMode)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def filteredEntities(*__, **_) -> Never:
    """
    Qt's 'std::vector<Entity *>
    &Qt3DRender::Render::FilterLayerEntityJob::filteredEntities()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.filteredEntities' has no "
        "cute function yet. Qt's 'std::vector<Entity *> "
        "&Qt3DRender::Render::FilterLayerEntityJob::filteredEntities()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def layerFilters(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeIdVector
    Qt3DRender::Render::FilterLayerEntityJob::layerFilters() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.layerFilters' has no cute "
        "function yet. Qt's 'Qt3DCore::QNodeIdVector "
        "Qt3DRender::Render::FilterLayerEntityJob::layerFilters() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setLayerFilters(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::FilterLayerEntityJob::setLayerFilters(const
    Qt3DCore::QNodeIdVector &layerIds)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FilterLayerEntityJob.setLayerFilters' has no "
        "cute function yet. Qt's 'void "
        "Qt3DRender::Render::FilterLayerEntityJob::setLayerFilters(const "
        "Qt3DCore::QNodeIdVector &layerIds)': takes a type Python has no "
        "way to hand over yet.")
