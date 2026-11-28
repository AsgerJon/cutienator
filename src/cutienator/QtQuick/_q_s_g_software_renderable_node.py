"""
QSGSoftwareRenderableNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareRenderableNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from ..QtGui import QPainter, QRegion, QTransform
  from . import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRegion = WAIT['QRegion']
  QSGNode = WAIT['QSGNode']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareRenderableNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGSoftwareRenderableNode: a plain Python object
  standing in front of one C++ QSGSoftwareRenderableNode.

  C++ hands a QSGSoftwareRenderableNode around as a copy, so every C++
  QSGSoftwareRenderableNode behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGSoftwareRenderableNode that has a ritual and that
  Python can call so far, 21 names in all: 'update', 'renderNode',
  'boundingRectMin', 'boundingRectMax', 'type', 'isOpaque', 'isDirty',
  'isDirtyRegionEmpty', 'handle', 'setTransform', 'setClipRegion',
  'setOpacity', 'transform', 'clipRegion', 'opacity', 'markGeometryDirty',
  'markMaterialDirty', 'addDirtyRegion', 'subtractDirtyRegion',
  'previousDirtyRegion', 'dirtyRegion'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwareRenderableNode::~QSGSoftwareRenderableNode()': the
    destructor: Python removes its C++ QSGSoftwareRenderableNode by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSGSoftwareRenderableNode is created at the first use, not by
    'QSGSoftwareRenderableNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGSoftwareRenderableNode back gives a copy the
    ritual made for Python, in a new cute QSGSoftwareRenderableNode.
  """

  #  The enums Qt writes inside QSGSoftwareRenderableNode, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class NodeType(CuteNum):
    """
    The enum 'QSGSoftwareRenderableNode::NodeType' of Qt, with the 12 names
    Qt gives in it.
    """

    Invalid = Kee[int](-1)
    SimpleRect = Kee[int](0)
    SimpleTexture = Kee[int](1)
    Image = Kee[int](2)
    Painter = Kee[int](3)
    Rectangle = Kee[int](4)
    Glyph = Kee[int](5)
    NinePatch = Kee[int](6)
    SimpleRectangle = Kee[int](7)
    SimpleImage = Kee[int](8)
    SpriteNode = Kee[int](9)
    RenderNode = Kee[int](10)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareRenderableNode'

  #  Qt's '~QSGSoftwareRenderableNode()'. Naming it makes this a value class:
  #  Python owns every C++ QSGSoftwareRenderableNode behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QSGSoftwareRenderableNodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def boundingRectMin(self) -> QRect:
    """
    Calls Qt's 'QRect QSGSoftwareRenderableNode::boundingRectMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#boundingRectMin

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGSoftwareRenderableNode::boundingRectMin() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode15boundingRectMinEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def boundingRectMax(self) -> QRect:
    """
    Calls Qt's 'QRect QSGSoftwareRenderableNode::boundingRectMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#boundingRectMax

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGSoftwareRenderableNode::boundingRectMax() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode15boundingRectMaxEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def type(self) -> NodeType:
    """
    Calls Qt's 'NodeType QSGSoftwareRenderableNode::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#type

    Returns
    -------

    NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NodeType(number)' gives.
    """
    #  NodeType QSGSoftwareRenderableNode::type() const
    return QSGSoftwareRenderableNode.NodeType(self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode4typeEv',
    ))

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNode::isOpaque() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#isOpaque
    """
    #  bool QSGSoftwareRenderableNode::isOpaque() const
    return self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode8isOpaqueEv',
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNode::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#isDirty
    """
    #  bool QSGSoftwareRenderableNode::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode7isDirtyEv',
    )

  def isDirtyRegionEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareRenderableNode::isDirtyRegionEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#isDirtyRegionEmpty
    """
    #  bool QSGSoftwareRenderableNode::isDirtyRegionEmpty() const
    return self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode18isDirtyRegionEmptyEv',
    )

  def handle(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QSGSoftwareRenderableNode::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#handle

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QSGSoftwareRenderableNode::handle() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode6handleEv',
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def transform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QSGSoftwareRenderableNode::transform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QSGSoftwareRenderableNode::transform() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode9transformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def clipRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QSGSoftwareRenderableNode::clipRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#clipRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGSoftwareRenderableNode::clipRegion() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode10clipRegionEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'float QSGSoftwareRenderableNode::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#opacity
    """
    #  float QSGSoftwareRenderableNode::opacity() const
    return self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode7opacityEv',
    )

  @overload()
  @overload(bool)
  def previousDirtyRegion(self, wasRemoved: bool = False) -> QRegion:
    """
    Calls Qt's 'QRegion QSGSoftwareRenderableNode::previousDirtyRegion(bool
    wasRemoved) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#previousDirtyRegion

    Parameters
    ----------

    wasRemoved : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGSoftwareRenderableNode::previousDirtyRegion(bool
    #      wasRemoved) const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode19previousDirtyRegionEb',
        wasRemoved,
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def dirtyRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QSGSoftwareRenderableNode::dirtyRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#dirtyRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGSoftwareRenderableNode::dirtyRegion() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGSoftwareRenderableNode11dirtyRegionEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTransform)
  def setTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::setTransform(const QTransform
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#setTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QSGSoftwareRenderableNode::setTransform(const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode12setTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(QRegion)
  @overload(QRegion, bool)
  def setClipRegion(
      self,
      clipRegion: QRegion,
      hasClipRegion: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::setClipRegion(const QRegion
    &clipRegion, bool hasClipRegion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#setClipRegion

    Parameters
    ----------

    clipRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    hasClipRegion : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSGSoftwareRenderableNode::setClipRegion(const QRegion
    #      &clipRegion, bool hasClipRegion)
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode13setClipRegionERK7QRegionb',
        self._valueOf(clipRegion), hasClipRegion,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::setOpacity(float opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QSGSoftwareRenderableNode::setOpacity(float opacity)
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode10setOpacityEf', opacity,
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

  @overload(NodeType, QSGNode)
  @overload(NodeType, NoneType)
  def __init__(self, type: NodeType, node: Optional[QSGNode]) -> None:
    """
    Notes what was given, for Qt's
    'QSGSoftwareRenderableNode::QSGSoftwareRenderableNode(NodeType type,
    QSGNode *node)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html

    Parameters
    ----------

    type : NodeType
      Passed on as its number.

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGSoftwareRenderableNode::QSGSoftwareRenderableNode(NodeType type,
    #      QSGNode *node)
    self._noteCreation(QSGSoftwareRenderableNode, lambda: Rituals.call(
        'ritual_ZN25QSGSoftwareRenderableNodeC1ENS_8NodeTypeEP7QSGNode',
        type.value, self._addressOf(node, 'QSGNode'),
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

  def update(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#update
    """
    #  void QSGSoftwareRenderableNode::update()
    self.uglySide.call('ritual_ZN25QSGSoftwareRenderableNode6updateEv')

  @overload(QPainter)
  @overload(NoneType)
  @overload(QPainter, bool)
  @overload(NoneType, bool)
  def renderNode(
      self,
      painter: Optional[QPainter],
      forceOpaquePainting: bool = False,
  ) -> QRegion:
    """
    Calls Qt's 'QRegion QSGSoftwareRenderableNode::renderNode(QPainter
    *painter, bool forceOpaquePainting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#renderNode

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    forceOpaquePainting : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGSoftwareRenderableNode::renderNode(QPainter *painter, bool
    #      forceOpaquePainting)
    address = self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode10renderNodeEP8QPainterb',
        self._addressOf(painter), forceOpaquePainting,
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def markGeometryDirty(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::markGeometryDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#markGeometryDirty
    """
    #  void QSGSoftwareRenderableNode::markGeometryDirty()
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode17markGeometryDirtyEv',
    )

  def markMaterialDirty(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::markMaterialDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#markMaterialDirty
    """
    #  void QSGSoftwareRenderableNode::markMaterialDirty()
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode17markMaterialDirtyEv',
    )

  @overload(QRegion)
  @overload(QRegion, bool)
  def addDirtyRegion(
      self,
      dirtyRegion: QRegion,
      forceDirty: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::addDirtyRegion(const QRegion
    &dirtyRegion, bool forceDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#addDirtyRegion

    Parameters
    ----------

    dirtyRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    forceDirty : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSGSoftwareRenderableNode::addDirtyRegion(const QRegion
    #      &dirtyRegion, bool forceDirty)
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode14addDirtyRegionERK7QRegionb',
        self._valueOf(dirtyRegion), forceDirty,
    )

  @overload(QRegion)
  def subtractDirtyRegion(self, dirtyRegion: QRegion) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderableNode::subtractDirtyRegion(const
    QRegion &dirtyRegion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderablenode.html#subtractDirtyRegion

    Parameters
    ----------

    dirtyRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QSGSoftwareRenderableNode::subtractDirtyRegion(const QRegion
    #      &dirtyRegion)
    self.uglySide.call(
        'ritual_ZN25QSGSoftwareRenderableNode19subtractDirtyRegionERK7QRegi'
        'on',
        self._valueOf(dirtyRegion),
    )


#  Qt's 'QList<QSGSoftwareRenderableNode *>': the list of
#  QSGSoftwareRenderableNode, which 'QList[QSGSoftwareRenderableNode]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QSGSoftwareRenderableNode.
QList.createKind(
    QSGSoftwareRenderableNode, 'address',
    make='ritual_list_make_QSGSoftwareRenderableNode_ptr',
    add='ritual_list_add_QSGSoftwareRenderableNode_ptr',
    size='ritual_list_size_QSGSoftwareRenderableNode_ptr',
    at='ritual_list_at_QSGSoftwareRenderableNode_ptr',
    drop='ritual_list_drop_QSGSoftwareRenderableNode_ptr',
)
