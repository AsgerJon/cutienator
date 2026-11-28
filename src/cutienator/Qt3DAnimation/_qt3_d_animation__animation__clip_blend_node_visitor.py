"""
Qt3DAnimation::Animation::ClipBlendNodeVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnodevisitor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ClipBlendNodeVisitor to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ClipBlendNodeVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ClipBlendNodeVisitor: a
  plain Python object standing in front of one C++
  Qt3DAnimation::Animation::ClipBlendNodeVisitor.

  C++ hands a Qt3DAnimation::Animation::ClipBlendNodeVisitor around as a
  copy, so every C++ Qt3DAnimation::Animation::ClipBlendNodeVisitor behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's Qt3DAnimation::Animation::ClipBlendNodeVisitor yet. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::traverse(Qt3DCore::
    QNodeId rootId, const VisitFunction &visitFunction) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPreOrderAllNodes(
    ClipBlendNode *node, const VisitFunction &visitFunction) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPostOrderAllNodes(
    ClipBlendNode *node, const VisitFunction &visitFunction) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void Qt3DAnimation::Animation::ClipBlendNodeVisitor::
    visitPreOrderDependencyNodes(ClipBlendNode *node, const VisitFunction
    &visitFunction) const': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DAnimation::Animation::ClipBlendNodeVisitor::
    visitPostOrderDependencyNodes(ClipBlendNode *node, const VisitFunction
    &visitFunction) const': takes a type Python has no way to hand over yet.
  - Qt's
    'Qt3DAnimation::Animation::ClipBlendNodeVisitor::~ClipBlendNodeVisitor(
    )': the destructor: Python removes its C++
    Qt3DAnimation::Animation::ClipBlendNodeVisitor by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ClipBlendNodeVisitor is created at the
    first use, not by 'Qt3DAnimation::Animation::ClipBlendNodeVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::ClipBlendNodeVisitor back
    gives a copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::ClipBlendNodeVisitor.
  - Each name of Qt's Qt3DAnimation::Animation::ClipBlendNodeVisitor that has
    no cute function yet, 'traverse', 'visitPostOrderAllNodes',
    'visitPostOrderDependencyNodes', 'visitPreOrderAllNodes',
    'visitPreOrderDependencyNodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside
  #  Qt3DAnimation::Animation::ClipBlendNodeVisitor, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class NodeFilter(CuteNum):
    """
    The enum 'Qt3DAnimation::Animation::ClipBlendNodeVisitor::NodeFilter' of
    Qt, with the 2 names Qt gives in it.
    """

    VisitAllNodes = Kee[int](0)
    VisitOnlyDependencies = Kee[int](1)

  class TraversalOrder(CuteNum):
    """
    The enum 'Qt3DAnimation::Animation::ClipBlendNodeVisitor::TraversalOrder'
    of Qt, with the 2 names Qt gives in it.
    """

    PreOrder = Kee[int](0)
    PostOrder = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ClipBlendNodeVisitor'

  #  Qt's '~Qt3DAnimation::Animation::ClipBlendNodeVisitor()'. Naming it
  #  makes this a value class: Python owns every C++
  #  Qt3DAnimation::Animation::ClipBlendNodeVisitor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeVisitorD1Ev')

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

  @overload(WAIT['Qt3DAnimation.Animation.ClipBlendNodeManager'])
  @overload(NoneType)
  @overload(
      WAIT['Qt3DAnimation.Animation.ClipBlendNodeManager'], TraversalOrder,
  )
  @overload(NoneType, TraversalOrder)
  @overload(
      WAIT['Qt3DAnimation.Animation.ClipBlendNodeManager'], TraversalOrder,
      NodeFilter,
  )
  @overload(NoneType, TraversalOrder, NodeFilter)
  def __init__(
      self,
      manager: Optional[Qt3DAnimation.Animation.ClipBlendNodeManager],
      order: TraversalOrder = TraversalOrder.PostOrder,
      filter: NodeFilter = NodeFilter.VisitAllNodes,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::Animation::ClipBlendNodeVisitor::ClipBlendNodeVisitor(
    ClipBlendNodeManager *manager, TraversalOrder order, NodeFilter filter)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnodevisitor.html

    Parameters
    ----------

    manager : Optional[Qt3DAnimation.Animation.ClipBlendNodeManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    order : TraversalOrder
      Passed on as its number. May be left out, as in Qt: it is then
      TraversalOrder.PostOrder.

    filter : NodeFilter
      Passed on as its number. May be left out, as in Qt: it is then
      NodeFilter.VisitAllNodes.
    """
    #  Qt3DAnimation::Animation::ClipBlendNodeVisitor::
    #      ClipBlendNodeVisitor(ClipBlendNodeManager *manager, TraversalOrder
    #      order, NodeFilter filter)
    self._noteCreation(ClipBlendNodeVisitor, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeVisitorC1EPNS0_20'
        'ClipBlendNodeManagerENS1_14TraversalOrderENS1_10NodeFilterE',
        self._addressOf(manager), order.value, filter.value,
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
  def traverse(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::traverse(Qt3DCore::
    QNodeId rootId, const VisitFunction &visitFunction) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNodeVisitor.traverse' has no "
        "cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipBlendNodeVisitor::traverse(Qt3DCore::"
        "QNodeId rootId, const VisitFunction &visitFunction) const': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def visitPostOrderAllNodes(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPostOrderAllNodes(
    ClipBlendNode *node, const VisitFunction &visitFunction) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNodeVisitor.visitPostOrderAllNode"
        "s' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPostOrderAllNo"
        "des(ClipBlendNode *node, const VisitFunction &visitFunction) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def visitPostOrderDependencyNodes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::Animation::ClipBlendNodeVisitor::
    visitPostOrderDependencyNodes(ClipBlendNode *node, const VisitFunction
    &visitFunction) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNodeVisitor.visitPostOrderDepende"
        "ncyNodes' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPostOrderDepen"
        "dencyNodes(ClipBlendNode *node, const VisitFunction "
        "&visitFunction) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def visitPreOrderAllNodes(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPreOrderAllNodes(
    ClipBlendNode *node, const VisitFunction &visitFunction) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNodeVisitor.visitPreOrderAllNodes"
        "' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPreOrderAllNod"
        "es(ClipBlendNode *node, const VisitFunction &visitFunction) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def visitPreOrderDependencyNodes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::Animation::ClipBlendNodeVisitor::
    visitPreOrderDependencyNodes(ClipBlendNode *node, const VisitFunction
    &visitFunction) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNodeVisitor.visitPreOrderDependen"
        "cyNodes' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPreOrderDepend"
        "encyNodes(ClipBlendNode *node, const VisitFunction &visitFunction) "
        "const': takes a type Python has no way to hand over yet.")
