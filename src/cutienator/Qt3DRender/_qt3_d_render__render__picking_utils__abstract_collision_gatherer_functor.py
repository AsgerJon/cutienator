"""
Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means
#  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractCollisionGathererFunctor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor.

  What exists
  -----------

  Every function of Qt's
  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor that has
  a ritual and that Python can call so far, 1 name in all: 'rayHitsEntity'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    ~AbstractCollisionGathererFunctor()': the destructor: Python never
    removes a C++
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor.
  - Qt's 'HitList
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    computeHits(const std::vector<Entity *> &entities,
    Qt3DRender::QPickingSettings::PickResultMode mode)': takes a type Python
    has no way to hand over yet.
  - Qt's 'HitList
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::pick(
    const Entity *entity) const': gives a type Python has no way to take yet.
  - Qt's 'void
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    sortHits(HitList &results)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open; 1 leans on 'Qt3DCore.

  What to expect
  --------------

  - The C++
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor is
    created at the first use, not by
    'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor(
    ...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor.
  - Each name of Qt's
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor that
    has no cute function yet, '__init__', 'computeHits', 'pick', 'sortHits',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor'

  #  The functions Qt calls itself that
  #  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'computeHits': (
          'HitList '
          'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunct'
          'or::computeHits(const std::vector<Entity *> &, '
          'Qt3DRender::QPickingSettings::PickResultMode)',
      ),
      'pick': (
          'HitList '
          'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunct'
          'or::pick(const Entity *) const',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def rayHitsEntity(
      self,
      entity: Optional[Qt3DRender.Render.Entity],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    rayHitsEntity(const Entity *entity) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingutils-abstractcollisiongathererfunctor.html

    Parameters
    ----------

    entity : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::PickingUtils::
    #      AbstractCollisionGathererFunctor::rayHitsEntity(const Entity
    #      *entity) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingUtils32AbstractCollisionGath'
        'ererFunctor13rayHitsEntityEPKNS0_6EntityE',
        self._addressOf(entity),
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    AbstractCollisionGathererFunctor()': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.AbstractCollisionGathererFunctor.__"
        "init__' has no cute function yet. Qt's "
        "'Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor"
        "::AbstractCollisionGathererFunctor()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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
  def computeHits(*__, **_) -> Never:
    """
    Qt's 'HitList
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    computeHits(const std::vector<Entity *> &entities,
    Qt3DRender::QPickingSettings::PickResultMode mode)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.AbstractCollisionGathererFunctor.co"
        "mputeHits' has no cute function yet. Qt's 'HitList "
        "Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor:"
        ":computeHits(const std::vector<Entity *> &entities, "
        "Qt3DRender::QPickingSettings::PickResultMode mode)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def pick(*__, **_) -> Never:
    """
    Qt's 'HitList
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::pick(
    const Entity *entity) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.AbstractCollisionGathererFunctor.pi"
        "ck' has no cute function yet. Qt's 'HitList "
        "Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor:"
        ":pick(const Entity *entity) const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def sortHits(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
    sortHits(HitList &results)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.AbstractCollisionGathererFunctor.so"
        "rtHits' has no cute function yet. Qt's 'void "
        "Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor:"
        ":sortHits(HitList &results)': takes a type Python has no way to "
        "hand over yet.")
