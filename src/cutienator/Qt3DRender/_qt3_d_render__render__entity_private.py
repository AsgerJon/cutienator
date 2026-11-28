"""
Qt3DRender::Render::EntityPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/entity_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::EntityPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EntityPrivate(Qt3DCore.QBackendNodePrivate):
  """
  The cute side of Qt's Qt3DRender::Render::EntityPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::Render::EntityPrivate.

  It is built on the cute 'Qt3DCore::QBackendNodePrivate', as Qt's
  Qt3DRender::Render::EntityPrivate is built on Qt's
  Qt3DCore::QBackendNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::EntityPrivate that has a ritual
  and that Python can call so far, 4 names in all: 'q_func', 'get',
  'componentAdded', 'componentRemoved'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Entity *Qt3DRender::Render::EntityPrivate::q_func() const':
    takes in Python what 'Entity
    *Qt3DRender::Render::EntityPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::EntityPrivate is created at the first use,
    not by 'Qt3DRender::Render::EntityPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::EntityPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def get(
      node: Optional[Qt3DRender.Render.Entity],
  ) -> Optional[EntityPrivate]:
    """
    Calls Qt's 'EntityPrivate *Qt3DRender::Render::EntityPrivate::get(Entity
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityprivate.html#get

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[EntityPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EntityPrivate *Qt3DRender::Render::EntityPrivate::get(Entity *node)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render13EntityPrivate3getEPNS0_6EntityE',
        CuteMixin._addressOf(node),
    )
    return EntityPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::EntityPrivate'

  #  A C++ Qt3DRender::Render::EntityPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_EntityPrivate'

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
    'Qt3DRender::Render::EntityPrivate::EntityPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityprivate.html#EntityPrivate
    """
    #  Qt3DRender::Render::EntityPrivate::EntityPrivate()
    self._noteCreation(EntityPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13EntityPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.Render.Entity]:
    """
    Calls Qt's 'Entity *Qt3DRender::Render::EntityPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.Render.Entity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Entity *Qt3DRender::Render::EntityPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13EntityPrivate6q_funcEv',
    )
    return Qt3DRender.Render.Entity._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def componentAdded(self, frontend: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::EntityPrivate::componentAdded(Qt3DCore::QNode
    *frontend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityprivate.html

    Parameters
    ----------

    frontend : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::EntityPrivate::componentAdded(Qt3DCore::QNode
    #      *frontend)
    ritual = (
        'ritual_ZN10Qt3DRender6Render13EntityPrivate14componentAddedEPN8Qt3'
        'DCore5QNodeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render13EntityPrivate14componentAddedE'
          'PN8Qt3DCore5QNodeE')
    self.uglySide.call(ritual, self._addressOf(frontend))

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def componentRemoved(self, frontend: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::EntityPrivate::componentRemoved(Qt3DCore::QNode
    *frontend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityprivate.html

    Parameters
    ----------

    frontend : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::EntityPrivate::componentRemoved(Qt3DCore::
    #      QNode *frontend)
    ritual = (
        'ritual_ZN10Qt3DRender6Render13EntityPrivate16componentRemovedEPN8Q'
        't3DCore5QNodeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render13EntityPrivate16componentRemove'
          'dEPN8Qt3DCore5QNodeE')
    self.uglySide.call(ritual, self._addressOf(frontend))
