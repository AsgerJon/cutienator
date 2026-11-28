"""
QSGBatchRenderer::Node binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Node to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QSGBatchRenderer, QSGNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Node(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::Node: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Node.

  C++ hands a QSGBatchRenderer::Node around as a copy, so every C++
  QSGBatchRenderer::Node behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Node that has a ritual and that
  Python can call so far, 12 names in all: 'parent', 'append', 'remove',
  'firstChild', 'sibling', 'setParent', 'hasChild', 'type', 'element',
  'renderNodeElement', 'clipInfo', 'rootInfo'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::Node::~Node()': the destructor: Python removes
    its C++ QSGBatchRenderer::Node by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Node is created at the first use, not by
    'QSGBatchRenderer::Node(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::Node back gives a copy the ritual
    made for Python, in a new cute QSGBatchRenderer::Node.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Node'

  #  Qt's '~QSGBatchRenderer::Node()'. Naming it makes this a value class:
  #  Python owns every C++ QSGBatchRenderer::Node behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN16QSGBatchRenderer4NodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parent(self) -> Optional[Node]:
    """
    Calls Qt's 'Node *QSGBatchRenderer::Node::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#parent

    Returns
    -------

    Optional[Node]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Node *QSGBatchRenderer::Node::parent() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node6parentEv',
    )
    return Node._cuteAt(address)

  def firstChild(self) -> Optional[Node]:
    """
    Calls Qt's 'Node *QSGBatchRenderer::Node::firstChild() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#firstChild

    Returns
    -------

    Optional[Node]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Node *QSGBatchRenderer::Node::firstChild() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node10firstChildEv',
    )
    return Node._cuteAt(address)

  def sibling(self) -> Optional[Node]:
    """
    Calls Qt's 'Node *QSGBatchRenderer::Node::sibling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#sibling

    Returns
    -------

    Optional[Node]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Node *QSGBatchRenderer::Node::sibling() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node7siblingEv',
    )
    return Node._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def hasChild(self, child: Optional[Node]) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Node::hasChild(Node *child) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#hasChild

    Parameters
    ----------

    child : Optional[Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGBatchRenderer::Node::hasChild(Node *child) const
    return self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node8hasChildEPS0_',
        self._addressOf(child),
    )

  def type(self) -> QSGNode.NodeType:
    """
    Calls Qt's 'QSGNode::NodeType QSGBatchRenderer::Node::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#type

    Returns
    -------

    QSGNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSGNode.NodeType(number)'
      gives.
    """
    #  QSGNode::NodeType QSGBatchRenderer::Node::type() const
    return QSGNode.NodeType(self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node4typeEv',
    ))

  def element(self) -> Optional[QSGBatchRenderer.Element]:
    """
    Calls Qt's 'Element *QSGBatchRenderer::Node::element() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#element

    Returns
    -------

    Optional[QSGBatchRenderer.Element]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Element *QSGBatchRenderer::Node::element() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node7elementEv',
    )
    return QSGBatchRenderer.Element._cuteAt(address)

  def renderNodeElement(
      self,
  ) -> Optional[QSGBatchRenderer.RenderNodeElement]:
    """
    Calls Qt's 'RenderNodeElement
    *QSGBatchRenderer::Node::renderNodeElement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#renderNodeElement

    Returns
    -------

    Optional[QSGBatchRenderer.RenderNodeElement]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderNodeElement *QSGBatchRenderer::Node::renderNodeElement() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node17renderNodeElementEv',
    )
    return QSGBatchRenderer.RenderNodeElement._cuteAt(address)

  def clipInfo(self) -> Optional[QSGBatchRenderer.ClipBatchRootInfo]:
    """
    Calls Qt's 'ClipBatchRootInfo *QSGBatchRenderer::Node::clipInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#clipInfo

    Returns
    -------

    Optional[QSGBatchRenderer.ClipBatchRootInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClipBatchRootInfo *QSGBatchRenderer::Node::clipInfo() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node8clipInfoEv',
    )
    return QSGBatchRenderer.ClipBatchRootInfo._cuteAt(address)

  def rootInfo(self) -> Optional[QSGBatchRenderer.BatchRootInfo]:
    """
    Calls Qt's 'BatchRootInfo *QSGBatchRenderer::Node::rootInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#rootInfo

    Returns
    -------

    Optional[QSGBatchRenderer.BatchRootInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  BatchRootInfo *QSGBatchRenderer::Node::rootInfo() const
    address = self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer4Node8rootInfoEv',
    )
    return QSGBatchRenderer.BatchRootInfo._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, p: Optional[Node]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Node::setParent(Node *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#setParent

    Parameters
    ----------

    p : Optional[Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Node::setParent(Node *p)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer4Node9setParentEPS0_',
        self._addressOf(p),
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
  def append(self, child: Optional[Node]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Node::append(Node *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#append

    Parameters
    ----------

    child : Optional[Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Node::append(Node *child)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer4Node6appendEPS0_',
        self._addressOf(child),
    )

  @overload(THIS)
  @overload(NoneType)
  def remove(self, child: Optional[Node]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Node::remove(Node *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-node.html#remove

    Parameters
    ----------

    child : Optional[Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Node::remove(Node *child)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer4Node6removeEPS0_',
        self._addressOf(child),
    )
