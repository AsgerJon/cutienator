"""
QSGAbstractSoftwareRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgabstractsoftwarerenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGAbstractSoftwareRenderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSGNode, QSGRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from ..QtGui import QColor, QPainter, QRegion
  from . import QSGRenderContext, QSGSoftwareRenderableNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSGRenderContext = WAIT['QSGRenderContext']
  QSGSoftwareRenderableNode = WAIT['QSGSoftwareRenderableNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGAbstractSoftwareRenderer(QSGRenderer):
  """
  The cute side of Qt's QSGAbstractSoftwareRenderer: a plain Python object
  standing in front of one C++ QSGAbstractSoftwareRenderer.

  It is built on the cute 'QSGRenderer', as Qt's QSGAbstractSoftwareRenderer
  is built on Qt's QSGRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGAbstractSoftwareRenderer that has a ritual and
  that Python can call so far, 22 names in all: 'renderableNode',
  'addNodeMapping', 'appendRenderableNode', 'nodeChanged', 'markDirty',
  'setClearColorEnabled', 'clearColorEnabled', 'renderNodes',
  'buildRenderList', 'optimizeRenderList', 'setBackgroundColor',
  'setBackgroundRect', 'backgroundColor', 'backgroundRect', 'isOpaque',
  'renderableNodes', 'nodeAdded', 'nodeRemoved', 'nodeGeometryUpdated',
  'nodeMaterialUpdated', 'nodeMatrixUpdated', 'nodeOpacityUpdated'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGAbstractSoftwareRenderer::~QSGAbstractSoftwareRenderer()': the
    destructor: Python never removes a C++ QSGAbstractSoftwareRenderer.

  What to expect
  --------------

  - The C++ QSGAbstractSoftwareRenderer is created at the first use, not by
    'QSGAbstractSoftwareRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGAbstractSoftwareRenderer.
  - Qt tells when it has removed the C++ QSGAbstractSoftwareRenderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGAbstractSoftwareRenderer'

  #  A C++ QSGAbstractSoftwareRenderer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGAbstractSoftwareRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGNode)
  @overload(NoneType)
  def renderableNode(
      self,
      node: Optional[QSGNode],
  ) -> Optional[QSGSoftwareRenderableNode]:
    """
    Calls Qt's 'QSGSoftwareRenderableNode
    *QSGAbstractSoftwareRenderer::renderableNode(QSGNode *node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#renderableNode

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGSoftwareRenderableNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGSoftwareRenderableNode
    #      *QSGAbstractSoftwareRenderer::renderableNode(QSGNode *node) const
    address = self.uglySide.call(
        'ritual_ZNK27QSGAbstractSoftwareRenderer14renderableNodeEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )
    from . import QSGSoftwareRenderableNode
    return QSGSoftwareRenderableNode._cuteAt(address)

  def clearColorEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSGAbstractSoftwareRenderer::clearColorEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#clearColorEnabled
    """
    #  bool QSGAbstractSoftwareRenderer::clearColorEnabled() const
    return self.uglySide.call(
        'ritual_ZNK27QSGAbstractSoftwareRenderer17clearColorEnabledEv',
    )

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QSGAbstractSoftwareRenderer::isOpaque() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#isOpaque
    """
    #  bool QSGAbstractSoftwareRenderer::isOpaque() const
    return self.uglySide.call(
        'ritual_ZNK27QSGAbstractSoftwareRenderer8isOpaqueEv',
    )

  def renderableNodes(self) -> QList[QSGSoftwareRenderableNode]:
    """
    Calls Qt's 'const QList<QSGSoftwareRenderableNode *>
    &QSGAbstractSoftwareRenderer::renderableNodes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#renderableNodes

    Returns
    -------

    QList[QSGSoftwareRenderableNode]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QSGSoftwareRenderableNode *>
    #      &QSGAbstractSoftwareRenderer::renderableNodes() const
    address = self.uglySide.call(
        'ritual_ZNK27QSGAbstractSoftwareRenderer15renderableNodesEv',
    )
    from . import QSGSoftwareRenderableNode
    return QList[QSGSoftwareRenderableNode]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setClearColorEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::setClearColorEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSGAbstractSoftwareRenderer::setClearColorEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer20setClearColorEnabledEb',
        enable,
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::setBackgroundColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGAbstractSoftwareRenderer::setBackgroundColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer18setBackgroundColorERK6QCol'
        'or',
        self._valueOf(color),
    )

  @overload(QRect, float)
  def setBackgroundRect(self, rect: QRect, devicePixelRatio: float) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::setBackgroundRect(const
    QRect &rect, qreal devicePixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#setBackgroundRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    devicePixelRatio : float
      Passed on as it is.
    """
    #  void QSGAbstractSoftwareRenderer::setBackgroundRect(const QRect &rect,
    #      qreal devicePixelRatio)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer17setBackgroundRectERK5QRect'
        'd',
        self._valueOf(rect), devicePixelRatio,
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

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGAbstractSoftwareRenderer::QSGAbstractSoftwareRenderer(
    QSGRenderContext *context)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    context : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGAbstractSoftwareRenderer::QSGAbstractSoftwareRenderer(
    #      QSGRenderContext *context)
    self._noteCreation(QSGAbstractSoftwareRenderer, lambda: Rituals.call(
        'ritual_ZN27QSGAbstractSoftwareRendererC1EP16QSGRenderContext',
        self._addressOf(context),
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

  @overload(QSGNode, QSGSoftwareRenderableNode)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QSGSoftwareRenderableNode)
  @overload(NoneType, NoneType)
  def addNodeMapping(
      self,
      node: Optional[QSGNode],
      renderableNode: Optional[QSGSoftwareRenderableNode],
  ) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::addNodeMapping(QSGNode
    *node, QSGSoftwareRenderableNode *renderableNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#addNodeMapping

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderableNode : Optional[QSGSoftwareRenderableNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::addNodeMapping(QSGNode *node,
    #      QSGSoftwareRenderableNode *renderableNode)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer14addNodeMappingEP7QSGNodeP2'
        '5QSGSoftwareRenderableNode',
        self._addressOf(node, 'QSGNode'), self._addressOf(renderableNode),
    )

  @overload(QSGSoftwareRenderableNode)
  @overload(NoneType)
  def appendRenderableNode(
      self,
      node: Optional[QSGSoftwareRenderableNode],
  ) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::appendRenderableNode(
    QSGSoftwareRenderableNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    node : Optional[QSGSoftwareRenderableNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::appendRenderableNode(
    #      QSGSoftwareRenderableNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer20appendRenderableNodeEP25QS'
        'GSoftwareRenderableNode',
        self._addressOf(node),
    )

  @overload(QSGNode, QSGNode.DirtyState)
  @overload(NoneType, QSGNode.DirtyState)
  def nodeChanged(
      self,
      node: Optional[QSGNode],
      state: QSGNode.DirtyState,
  ) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeChanged(QSGNode *node,
    QSGNode::DirtyState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#nodeChanged

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QSGNode.DirtyState
      Passed on as its number.
    """
    #  void QSGAbstractSoftwareRenderer::nodeChanged(QSGNode *node,
    #      QSGNode::DirtyState state)
    ritual = (
        'ritual_ZN27QSGAbstractSoftwareRenderer11nodeChangedEP7QSGNode6QFla'
        'gsINS0_13DirtyStateBitEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QSGAbstractSoftwareRenderer11nodeChangedEP7QSGNod'
          'e6QFlagsINS0_13DirtyStateBitEE')
    self.uglySide.call(ritual, self._addressOf(node, 'QSGNode'), state.value)

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::markDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#markDirty
    """
    #  void QSGAbstractSoftwareRenderer::markDirty()
    self.uglySide.call('ritual_ZN27QSGAbstractSoftwareRenderer9markDirtyEv')

  @overload(QPainter)
  @overload(NoneType)
  def renderNodes(self, painter: Optional[QPainter]) -> QRegion:
    """
    Calls Qt's 'QRegion QSGAbstractSoftwareRenderer::renderNodes(QPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#renderNodes

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGAbstractSoftwareRenderer::renderNodes(QPainter *painter)
    address = self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer11renderNodesEP8QPainter',
        self._addressOf(painter),
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def buildRenderList(self) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::buildRenderList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#buildRenderList
    """
    #  void QSGAbstractSoftwareRenderer::buildRenderList()
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer15buildRenderListEv',
    )

  def optimizeRenderList(self) -> QRegion:
    """
    Calls Qt's 'QRegion QSGAbstractSoftwareRenderer::optimizeRenderList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGAbstractSoftwareRenderer::optimizeRenderList()
    address = self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer18optimizeRenderListEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGAbstractSoftwareRenderer::backgroundColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGAbstractSoftwareRenderer::backgroundColor()
    address = self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def backgroundRect(self) -> QRect:
    """
    Calls Qt's 'QRect QSGAbstractSoftwareRenderer::backgroundRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#backgroundRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGAbstractSoftwareRenderer::backgroundRect()
    address = self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer14backgroundRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QSGNode)
  @overload(NoneType)
  def nodeAdded(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeAdded(QSGNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#nodeAdded

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::nodeAdded(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer9nodeAddedEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def nodeRemoved(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeRemoved(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#nodeRemoved

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::nodeRemoved(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer11nodeRemovedEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def nodeGeometryUpdated(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeGeometryUpdated(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::nodeGeometryUpdated(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer19nodeGeometryUpdatedEP7QSGN'
        'ode',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def nodeMaterialUpdated(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeMaterialUpdated(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::nodeMaterialUpdated(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer19nodeMaterialUpdatedEP7QSGN'
        'ode',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def nodeMatrixUpdated(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeMatrixUpdated(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html#nodeMatrixUpdated

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::nodeMatrixUpdated(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer17nodeMatrixUpdatedEP7QSGNod'
        'e',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def nodeOpacityUpdated(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGAbstractSoftwareRenderer::nodeOpacityUpdated(QSGNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgabstractsoftwarerenderer.html

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGAbstractSoftwareRenderer::nodeOpacityUpdated(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN27QSGAbstractSoftwareRenderer18nodeOpacityUpdatedEP7QSGNo'
        'de',
        self._addressOf(node, 'QSGNode'),
    )
