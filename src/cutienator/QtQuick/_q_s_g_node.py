"""
QSGNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGNode: a plain Python object standing in front of
  one C++ QSGNode.

  What exists
  -----------

  Every function of Qt's QSGNode that has a ritual and that Python can call
  so far, 25 names in all: 'parent', 'removeChildNode',
  'removeAllChildNodes', 'prependChildNode', 'appendChildNode',
  'insertChildNodeBefore', 'insertChildNodeAfter', 'reparentChildNodesTo',
  'childCount', 'childAtIndex', 'firstChild', 'lastChild', 'nextSibling',
  'previousSibling', 'type', 'clearDirty', 'markDirty', 'dirtyState',
  'isSubtreeBlocked', 'flags', 'setFlag', 'setFlags', 'preprocess', 'init',
  'destroy'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGNode::~QSGNode()': the destructor: Python never removes a C++
    QSGNode.
  - Qt's 'QSGNode::QSGNode(QSGNodePrivate &dd, NodeType type)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSGNode is created at the first use, not by 'QSGNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGNode.
  """

  #  The enums Qt writes inside QSGNode, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class DirtyStateBit(CuteFlags):
    """
    The flags enum 'QSGNode::DirtyStateBit' of Qt, with the 10 names Qt gives
    in it. Qt names the type of its combinations 'QSGNode::DirtyState'.
    """

    DirtySubtreeBlocked = 0x80
    DirtyMatrix = 0x100
    DirtyNodeAdded = 0x400
    DirtyNodeRemoved = 0x800
    DirtyGeometry = 0x1000
    DirtyMaterial = 0x2000
    DirtyOpacity = 0x4000
    DirtyForceUpdate = 0x8000
    DirtyUsePreprocess = 0x2
    DirtyPropagationMask = 0xc500

  DirtyState = DirtyStateBit

  class Flag(CuteFlags):
    """
    The flags enum 'QSGNode::Flag' of Qt, with the 6 names Qt gives in it. Qt
    names the type of its combinations 'QSGNode::Flags'.
    """

    OwnedByParent = 0x1
    UsePreprocess = 0x2
    OwnsGeometry = 0x10000
    OwnsMaterial = 0x20000
    OwnsOpaqueMaterial = 0x40000
    IsVisitableNode = 0x1000000

  Flags = Flag

  class NodeType(CuteNum):
    """
    The enum 'QSGNode::NodeType' of Qt, with the 7 names Qt gives in it.
    """

    BasicNodeType = Kee[int](0)
    GeometryNodeType = Kee[int](1)
    TransformNodeType = Kee[int](2)
    ClipNodeType = Kee[int](3)
    OpacityNodeType = Kee[int](4)
    RootNodeType = Kee[int](5)
    RenderNodeType = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGNode'

  #  A C++ QSGNode Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGNode'

  #  The functions Qt calls itself that QSGNode is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'isSubtreeBlocked': (
          ('_ZNK7QSGNode16isSubtreeBlockedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'preprocess': (
          ('_ZN7QSGNode10preprocessEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parent(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGNode::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#parent

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGNode::parent() const
    address = self._callAs('QSGNode', 'ritual_ZNK7QSGNode6parentEv')
    return QSGNode._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QSGNode::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#childCount
    """
    #  int QSGNode::childCount() const
    return self._callAs('QSGNode', 'ritual_ZNK7QSGNode10childCountEv')

  @overload(int)
  def childAtIndex(self, i: int) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGNode::childAtIndex(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#childAtIndex

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGNode::childAtIndex(int i) const
    address = self._callAs(
        'QSGNode', 'ritual_ZNK7QSGNode12childAtIndexEi', i,
    )
    return QSGNode._cuteAt(address)

  def firstChild(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGNode::firstChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#firstChild

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGNode::firstChild() const
    address = self._callAs('QSGNode', 'ritual_ZNK7QSGNode10firstChildEv')
    return QSGNode._cuteAt(address)

  def lastChild(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGNode::lastChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#lastChild

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGNode::lastChild() const
    address = self._callAs('QSGNode', 'ritual_ZNK7QSGNode9lastChildEv')
    return QSGNode._cuteAt(address)

  def nextSibling(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGNode::nextSibling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#nextSibling

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGNode::nextSibling() const
    address = self._callAs('QSGNode', 'ritual_ZNK7QSGNode11nextSiblingEv')
    return QSGNode._cuteAt(address)

  def previousSibling(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGNode::previousSibling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#previousSibling

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGNode::previousSibling() const
    address = self._callAs(
        'QSGNode', 'ritual_ZNK7QSGNode15previousSiblingEv',
    )
    return QSGNode._cuteAt(address)

  def type(self) -> NodeType:
    """
    Calls Qt's 'NodeType QSGNode::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#type

    Returns
    -------

    NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NodeType(number)' gives.
    """
    #  NodeType QSGNode::type() const
    return QSGNode.NodeType(self._callAs(
        'QSGNode', 'ritual_ZNK7QSGNode4typeEv',
    ))

  def dirtyState(self) -> DirtyState:
    """
    Calls Qt's 'DirtyState QSGNode::dirtyState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#dirtyState

    Returns
    -------

    DirtyState
      The value standing for the combination Qt gave back.
    """
    #  DirtyState QSGNode::dirtyState() const
    return QSGNode.DirtyState(self._callAs(
        'QSGNode', 'ritual_ZNK7QSGNode10dirtyStateEv',
    ))

  def isSubtreeBlocked(self) -> bool:
    """
    Calls Qt's 'bool QSGNode::isSubtreeBlocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#isSubtreeBlocked
    """
    #  bool QSGNode::isSubtreeBlocked() const
    ritual = 'ritual_ZNK7QSGNode16isSubtreeBlockedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QSGNode16isSubtreeBlockedEv'
    return self._callAs('QSGNode', ritual)

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QSGNode::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QSGNode::flags() const
    return QSGNode.Flags(self._callAs(
        'QSGNode', 'ritual_ZNK7QSGNode5flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flag)
  @overload(Flag, bool)
  def setFlag(self, a0: Flag, a1: bool = True) -> None:
    """
    Calls Qt's 'void QSGNode::setFlag(Flag a0, bool a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#setFlag

    Parameters
    ----------

    a0 : Flag
      Passed on as its number.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSGNode::setFlag(Flag a0, bool a1)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode7setFlagENS_4FlagEb', a0.value, a1,
    )

  @overload(Flags)
  @overload(Flags, bool)
  def setFlags(self, a0: Flags, a1: bool = True) -> None:
    """
    Calls Qt's 'void QSGNode::setFlags(Flags a0, bool a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#setFlags

    Parameters
    ----------

    a0 : Flags
      Passed on as its number.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSGNode::setFlags(Flags a0, bool a1)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode8setFlagsE6QFlagsINS_4FlagEEb',
        a0.value, a1,
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
    Notes what was given, for Qt's 'QSGNode::QSGNode()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#QSGNode
    """
    #  QSGNode::QSGNode()
    self._noteCreation(QSGNode, lambda: Rituals.call(
        'ritual_ZN7QSGNodeC1Ev',
    ))

  @overload(NodeType)
  def __init__(self, type: NodeType) -> None:
    """
    Notes what was given, for Qt's 'QSGNode::QSGNode(NodeType type)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#QSGNode

    Parameters
    ----------

    type : NodeType
      Passed on as its number.
    """
    #  QSGNode::QSGNode(NodeType type)
    self._noteCreation(QSGNode, lambda: Rituals.call(
        'ritual_ZN7QSGNodeC1ENS_8NodeTypeE', type.value,
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

  @overload(THIS)
  @overload(NoneType)
  def removeChildNode(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNode::removeChildNode(QSGNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#removeChildNode

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNode::removeChildNode(QSGNode *node)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode15removeChildNodeEPS_',
        self._addressOf(node, 'QSGNode'),
    )

  def removeAllChildNodes(self) -> None:
    """
    Calls Qt's 'void QSGNode::removeAllChildNodes()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#removeAllChildNodes
    """
    #  void QSGNode::removeAllChildNodes()
    self._callAs('QSGNode', 'ritual_ZN7QSGNode19removeAllChildNodesEv')

  @overload(THIS)
  @overload(NoneType)
  def prependChildNode(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNode::prependChildNode(QSGNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#prependChildNode

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNode::prependChildNode(QSGNode *node)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode16prependChildNodeEPS_',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(THIS)
  @overload(NoneType)
  def appendChildNode(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNode::appendChildNode(QSGNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#appendChildNode

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNode::appendChildNode(QSGNode *node)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode15appendChildNodeEPS_',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def insertChildNodeBefore(
      self,
      node: Optional[QSGNode],
      before: Optional[QSGNode],
  ) -> None:
    """
    Calls Qt's 'void QSGNode::insertChildNodeBefore(QSGNode *node, QSGNode
    *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#insertChildNodeBefore

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNode::insertChildNodeBefore(QSGNode *node, QSGNode *before)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode21insertChildNodeBeforeEPS_S0_',
        self._addressOf(node, 'QSGNode'), self._addressOf(before, 'QSGNode'),
    )

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def insertChildNodeAfter(
      self,
      node: Optional[QSGNode],
      after: Optional[QSGNode],
  ) -> None:
    """
    Calls Qt's 'void QSGNode::insertChildNodeAfter(QSGNode *node, QSGNode
    *after)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#insertChildNodeAfter

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    after : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNode::insertChildNodeAfter(QSGNode *node, QSGNode *after)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode20insertChildNodeAfterEPS_S0_',
        self._addressOf(node, 'QSGNode'), self._addressOf(after, 'QSGNode'),
    )

  @overload(THIS)
  @overload(NoneType)
  def reparentChildNodesTo(self, newParent: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGNode::reparentChildNodesTo(QSGNode *newParent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#reparentChildNodesTo

    Parameters
    ----------

    newParent : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNode::reparentChildNodesTo(QSGNode *newParent)
    self._callAs(
        'QSGNode', 'ritual_ZN7QSGNode20reparentChildNodesToEPS_',
        self._addressOf(newParent, 'QSGNode'),
    )

  def clearDirty(self) -> None:
    """
    Calls Qt's 'void QSGNode::clearDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#clearDirty
    """
    #  void QSGNode::clearDirty()
    self._callAs('QSGNode', 'ritual_ZN7QSGNode10clearDirtyEv')

  @overload(DirtyState)
  def markDirty(self, bits: DirtyState) -> None:
    """
    Calls Qt's 'void QSGNode::markDirty(DirtyState bits)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#markDirty

    Parameters
    ----------

    bits : DirtyState
      Passed on as its number.
    """
    #  void QSGNode::markDirty(DirtyState bits)
    self._callAs(
        'QSGNode',
        'ritual_ZN7QSGNode9markDirtyE6QFlagsINS_13DirtyStateBitEE',
        bits.value,
    )

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGNode::preprocess()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#preprocess
    """
    #  void QSGNode::preprocess()
    ritual = 'ritual_ZN7QSGNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QSGNode10preprocessEv'
    self._callAs('QSGNode', ritual)

  def init(self) -> None:
    """
    Calls Qt's 'void QSGNode::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#init
    """
    #  void QSGNode::init()
    self._callAs('QSGNode', 'ritual_ZN7QSGNode4initEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QSGNode::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnode.html#destroy
    """
    #  void QSGNode::destroy()
    self._callAs('QSGNode', 'ritual_ZN7QSGNode7destroyEv')
