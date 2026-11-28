"""
Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class HierarchicalEntityPicker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker: a plain Python
  object standing in front of one C++
  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker.

  C++ hands a Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker
  around as a copy, so every C++
  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's
  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker yet. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    setLayerFilterIds(const Qt3DCore::QNodeIdVector &layerFilterIds)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::setLayerIds(
    const Qt3DCore::QNodeIdVector &layerIds, QAbstractRayCaster::FilterMode
    mode)': takes a type Python has no way to hand over yet.
  - Qt's 'HitList
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::hits()
    const': gives a type Python has no way to take yet.
  - Qt's 'const std::vector<Entity *>
    &Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::entities()
    const': gives a type Python has no way to take yet.
  - Qt's 'QHash<Qt3DCore::QNodeId, int>
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    entityToPriorityTable() const': gives a type Python has no way to take
    yet.
  - Qt's 'Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    ~HierarchicalEntityPicker()': the destructor: Python removes its C++
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'Qt3DCore.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker is
    created at the first use, not by
    'Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker.
  - Each name of Qt's
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker that has no
    cute function yet, 'collectHits', 'entities', 'entityToPriorityTable',
    'hits', 'setLayerFilterIds', 'setLayerIds', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker'

  #  Qt's '~Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker()'.
  #  Naming it makes this a value class: Python owns every C++
  #  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPickerD1Ev')

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

  @overload(WAIT['Qt3DRender.RayCasting.QRay3D'])
  @overload(WAIT['Qt3DRender.RayCasting.QRay3D'], bool)
  def __init__(
      self,
      ray: Qt3DRender.RayCasting.QRay3D,
      requireObjectPicker: bool = True,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    HierarchicalEntityPicker(const RayCasting::QRay3D &ray, bool
    requireObjectPicker)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingutils-hierarchicalentitypicker.html

    Parameters
    ----------

    ray : Qt3DRender.RayCasting.QRay3D
      Passed on as a value: Qt reads the C++ Qt3DRender::RayCasting::QRay3D,
      which stays Python's own.

    requireObjectPicker : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    #      HierarchicalEntityPicker(const RayCasting::QRay3D &ray, bool
    #      requireObjectPicker)
    self._noteCreation(HierarchicalEntityPicker, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPick'
        'erC1ERKNS_10RayCasting6QRay3DEb',
        self._valueOf(ray), requireObjectPicker,
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

  @staticmethod
  def collectHits(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::collectHits(
    NodeManagers *manager, Entity *root)': leans on
    'Qt3DCore::QHandle<Qt3DRender::Render::ObjectPicker>
    Qt3DRender::Render::Entity::componentHandle<Qt3DRender::Render::
    ObjectPicker>() const', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker.collectHit"
        "s' has no cute function yet. Qt's 'bool "
        "Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::collect"
        "Hits(NodeManagers *manager, Entity *root)': leans on "
        "'Qt3DCore::QHandle<Qt3DRender::Render::ObjectPicker> "
        "Qt3DRender::Render::Entity::componentHandle<Qt3DRender::Render::Obj"
        "ectPicker>() const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def entities(*__, **_) -> Never:
    """
    Qt's 'const std::vector<Entity *>
    &Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::entities()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker.entities' "
        "has no cute function yet. Qt's 'const std::vector<Entity *> "
        "&Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::entiti"
        "es() const': gives a type Python has no way to take yet.")

  @staticmethod
  def entityToPriorityTable(*__, **_) -> Never:
    """
    Qt's 'QHash<Qt3DCore::QNodeId, int>
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    entityToPriorityTable() const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker.entityToPr"
        "iorityTable' has no cute function yet. Qt's "
        "'QHash<Qt3DCore::QNodeId, int> "
        "Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::entityT"
        "oPriorityTable() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def hits(*__, **_) -> Never:
    """
    Qt's 'HitList
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::hits()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker.hits' has "
        "no cute function yet. Qt's 'HitList "
        "Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::hits() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setLayerFilterIds(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::
    setLayerFilterIds(const Qt3DCore::QNodeIdVector &layerFilterIds)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker.setLayerFi"
        "lterIds' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::setLaye"
        "rFilterIds(const Qt3DCore::QNodeIdVector &layerFilterIds)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def setLayerIds(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::setLayerIds(
    const Qt3DCore::QNodeIdVector &layerIds, QAbstractRayCaster::FilterMode
    mode)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.HierarchicalEntityPicker.setLayerId"
        "s' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::setLaye"
        "rIds(const Qt3DCore::QNodeIdVector &layerIds, "
        "QAbstractRayCaster::FilterMode mode)': takes a type Python has no "
        "way to hand over yet.")
