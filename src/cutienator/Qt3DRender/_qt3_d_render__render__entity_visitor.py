"""
Qt3DRender::Render::EntityVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/entityvisitor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::EntityVisitor to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EntityVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::EntityVisitor: a plain Python
  object standing in front of one C++ Qt3DRender::Render::EntityVisitor.

  C++ hands a Qt3DRender::Render::EntityVisitor around as a copy, so every
  C++ Qt3DRender::Render::EntityVisitor behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::EntityVisitor that has a ritual
  and that Python can call so far, 4 names in all: 'visit', 'pruneDisabled',
  'setPruneDisabled', 'apply'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::EntityVisitor::~EntityVisitor()': the
    destructor: Python removes its C++ Qt3DRender::Render::EntityVisitor by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::EntityVisitor is created at the first use,
    not by 'Qt3DRender::Render::EntityVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::EntityVisitor back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::EntityVisitor.
  """

  #  The enums Qt writes inside Qt3DRender::Render::EntityVisitor, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Operation(CuteNum):
    """
    The enum 'Qt3DRender::Render::EntityVisitor::Operation' of Qt, with the 3
    names Qt gives in it.
    """

    Continue = Kee[int](0)
    Prune = Kee[int](1)
    Stop = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::EntityVisitor'

  #  A C++ Qt3DRender::Render::EntityVisitor Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_EntityVisitor'

  #  The functions Qt calls itself that Qt3DRender::Render::EntityVisitor is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'visit': (
          ('_ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6EntityE',
           ('int', 'enum',
            'Qt3DRender:Qt3DRender.Render.EntityVisitor.Operation'),
           (
               ('address', 'address', 'Qt3DRender:Qt3DRender.Render.Entity'),
           )),
      ),
  }

  #  Qt's '~Qt3DRender::Render::EntityVisitor()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::EntityVisitor
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render13EntityVisitorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pruneDisabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::EntityVisitor::pruneDisabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityvisitor.html#pruneDisabled
    """
    #  bool Qt3DRender::Render::EntityVisitor::pruneDisabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render13EntityVisitor13pruneDisabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPruneDisabled(self, pruneDisabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::EntityVisitor::setPruneDisabled(bool
    pruneDisabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityvisitor.html

    Parameters
    ----------

    pruneDisabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::EntityVisitor::setPruneDisabled(bool
    #      pruneDisabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13EntityVisitor16setPruneDisabledEb',
        pruneDisabled,
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

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def __init__(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::EntityVisitor::EntityVisitor(NodeManagers
    *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityvisitor.html#EntityVisitor

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::EntityVisitor::EntityVisitor(NodeManagers
    #      *manager)
    self._noteCreation(EntityVisitor, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13EntityVisitorC1EPNS0_12NodeManagersE',
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

  @overload()
  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def visit(
      self,
      entity: Optional[Qt3DRender.Render.Entity] = None,
  ) -> Operation:
    """
    Calls Qt's 'Operation Qt3DRender::Render::EntityVisitor::visit(Entity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityvisitor.html#visit

    Parameters
    ----------

    entity : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation Qt3DRender::Render::EntityVisitor::visit(Entity *entity)
    ritual = (
        'ritual_ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6EntityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render13EntityVisitor5visitEPNS0_6Enti'
          'tyE')
    return EntityVisitor.Operation(self.uglySide.call(
        ritual, self._addressOf(entity),
    ))

  @overload(WAIT['Qt3DRender.Render.Entity'])
  @overload(NoneType)
  def apply(self, root: Optional[Qt3DRender.Render.Entity]) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::EntityVisitor::apply(Entity *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entityvisitor.html#apply

    Parameters
    ----------

    root : Optional[Qt3DRender.Render.Entity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::Render::EntityVisitor::apply(Entity *root)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13EntityVisitor5applyEPNS0_6EntityE',
        self._addressOf(root),
    )
