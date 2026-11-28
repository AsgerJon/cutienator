"""
Qt3DRender::Render::EntityAccumulator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/entityaccumulator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::EntityAccumulator to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EntityAccumulator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::EntityAccumulator: a plain Python
  object standing in front of one C++ Qt3DRender::Render::EntityAccumulator.

  C++ hands a Qt3DRender::Render::EntityAccumulator around as a copy, so
  every C++ Qt3DRender::Render::EntityAccumulator behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's Qt3DRender::Render::EntityAccumulator yet. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::EntityAccumulator::EntityAccumulator(std::
    function<bool (Entity *)> predicate, NodeManagers *manager)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<Entity *> Qt3DRender::Render::EntityAccumulator::apply(Entity
    *root) const': gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::Render::EntityAccumulator::~EntityAccumulator()': the
    destructor: Python removes its C++ Qt3DRender::Render::EntityAccumulator
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::EntityAccumulator is created at the first
    use, not by 'Qt3DRender::Render::EntityAccumulator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::EntityAccumulator back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::EntityAccumulator.
  - Each name of Qt's Qt3DRender::Render::EntityAccumulator that has no cute
    function yet, 'apply', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::EntityAccumulator'

  #  Qt's '~Qt3DRender::Render::EntityAccumulator()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::EntityAccumulator
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render17EntityAccumulatorD1Ev'

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

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def __init__(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::EntityAccumulator::EntityAccumulator(NodeManagers
    *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityaccumulator.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::EntityAccumulator::EntityAccumulator(NodeManagers
    #      *manager)
    self._noteCreation(EntityAccumulator, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render17EntityAccumulatorC1EPNS0_12NodeManag'
        'ersE',
        self._addressOf(manager),
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
  def apply(*__, **_) -> Never:
    """
    Qt's 'QList<Entity *> Qt3DRender::Render::EntityAccumulator::apply(Entity
    *root) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.EntityAccumulator.apply' has no cute function "
        "yet. Qt's 'QList<Entity *> "
        "Qt3DRender::Render::EntityAccumulator::apply(Entity *root) const': "
        "gives a type Python has no way to take yet.")
