"""
Qt3DRender::Render::FrameGraphVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/framegraphvisitor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FrameGraphVisitor to be private: it declares
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


class FrameGraphVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::FrameGraphVisitor: a plain Python
  object standing in front of one C++ Qt3DRender::Render::FrameGraphVisitor.

  C++ hands a Qt3DRender::Render::FrameGraphVisitor around as a copy, so
  every C++ Qt3DRender::Render::FrameGraphVisitor behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FrameGraphVisitor that has a
  ritual and that Python can call so far, 1 name in all: 'visit'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::FrameGraphVisitor::~FrameGraphVisitor()': the
    destructor: Python removes its C++ Qt3DRender::Render::FrameGraphVisitor
    by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FrameGraphVisitor is created at the first
    use, not by 'Qt3DRender::Render::FrameGraphVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::FrameGraphVisitor back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::FrameGraphVisitor.
  - Each name of Qt's Qt3DRender::Render::FrameGraphVisitor that has no cute
    function yet, 'takeEnablersToDisable', 'traverse', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FrameGraphVisitor'

  #  Qt's '~Qt3DRender::Render::FrameGraphVisitor()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::FrameGraphVisitor
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render17FrameGraphVisitorD1Ev'

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

  @overload(WAIT['Qt3DRender.Render.FrameGraphManager'])
  @overload(NoneType)
  def __init__(
      self,
      nodeManager: Optional[Qt3DRender.Render.FrameGraphManager],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::FrameGraphVisitor::FrameGraphVisitor(const
    FrameGraphManager *nodeManager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphvisitor.html

    Parameters
    ----------

    nodeManager : Optional[Qt3DRender.Render.FrameGraphManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::FrameGraphVisitor::FrameGraphVisitor(const
    #      FrameGraphManager *nodeManager)
    self._noteCreation(FrameGraphVisitor, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render17FrameGraphVisitorC1EPKNS0_17FrameGra'
        'phManagerE',
        self._addressOf(nodeManager),
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

  @overload(WAIT['Qt3DRender.Render.FrameGraphNode'])
  @overload(NoneType)
  def visit(self, node: Optional[Qt3DRender.Render.FrameGraphNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameGraphVisitor::visit(Render::FrameGraphNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphvisitor.html#visit

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrameGraphVisitor::visit(Render::
    #      FrameGraphNode *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrameGraphVisitor5visitEPNS0_14Frame'
        'GraphNodeE',
        self._addressOf(node),
    )

  @staticmethod
  def takeEnablersToDisable(*__, **_) -> Never:
    """
    Qt's 'std::vector<FrameGraphNode *>
    &&Qt3DRender::Render::FrameGraphVisitor::takeEnablersToDisable()': takes
    or gives a type that cannot be passed yet:
    std::vector<Qt3DRender::Render::FrameGraphNode *> &&.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FrameGraphVisitor.takeEnablersToDisable' has no "
        "cute function yet. Qt's 'std::vector<FrameGraphNode *> "
        "&&Qt3DRender::Render::FrameGraphVisitor::takeEnablersToDisable()': "
        "takes or gives a type that cannot be passed yet: "
        "std::vector<Qt3DRender::Render::FrameGraphNode *> &&.")

  @staticmethod
  def traverse(*__, **_) -> Never:
    """
    Qt's 'std::vector<FrameGraphNode *>
    &&Qt3DRender::Render::FrameGraphVisitor::traverse(FrameGraphNode *root)':
    takes or gives a type that cannot be passed yet:
    std::vector<Qt3DRender::Render::FrameGraphNode *> &&.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FrameGraphVisitor.traverse' has no cute "
        "function yet. Qt's 'std::vector<FrameGraphNode *> "
        "&&Qt3DRender::Render::FrameGraphVisitor::traverse(FrameGraphNode "
        "*root)': takes or gives a type that cannot be passed yet: "
        "std::vector<Qt3DRender::Render::FrameGraphNode *> &&.")
