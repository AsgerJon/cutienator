"""
QSvgStructureNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgStructureNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgStructureNode(QSvgNode):
  """
  The cute side of Qt's QSvgStructureNode: a plain Python object standing in
  front of one C++ QSvgStructureNode.

  It is built on the cute 'QSvgNode', as Qt's QSvgStructureNode is built on
  Qt's QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgStructureNode that has a ritual and that Python
  can call so far, 2 names in all: 'previousSiblingNode',
  'releaseDescendants'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgStructureNode::~QSvgStructureNode()': the destructor: Python
    never removes a C++ QSvgStructureNode.
  - Qt's 'QRectF QSvgStructureNode::internalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QRectF QSvgStructureNode::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'const std::list<std::unique_ptr<QSvgNode>>
    &QSvgStructureNode::renderers() const': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open; 1 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QSvgStructureNode is created at the first use, not by
    'QSvgStructureNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgStructureNode.
  - Each name of Qt's QSvgStructureNode that has no cute function yet,
    '__init__', 'addChild', 'renderers', holds a function that raises
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
  __qt_class__ = 'QSvgStructureNode'

  #  A C++ QSvgStructureNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgStructureNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSvgNode)
  @overload(NoneType)
  def previousSiblingNode(self, n: Optional[QSvgNode]) -> Optional[QSvgNode]:
    """
    Calls Qt's 'QSvgNode *QSvgStructureNode::previousSiblingNode(QSvgNode *n)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstructurenode.html#previousSiblingNode

    Parameters
    ----------

    n : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSvgNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgNode *QSvgStructureNode::previousSiblingNode(QSvgNode *n) const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgStructureNode19previousSiblingNodeEP8QSvgNode',
        self._addressOf(n),
    )
    return QSvgNode._cuteAt(address)

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
    Qt's 'QSvgStructureNode::QSvgStructureNode(QSvgNode *parent)': the class
    is abstract, so C++ cannot make one, and the C++ class of ours does not
    fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSvgStructureNode.__init__' has no cute function yet. Qt's "
        "'QSvgStructureNode::QSvgStructureNode(QSvgNode *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def releaseDescendants(self) -> None:
    """
    Calls Qt's 'void QSvgStructureNode::releaseDescendants()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstructurenode.html#releaseDescendants
    """
    #  void QSvgStructureNode::releaseDescendants()
    self.uglySide.call('ritual_ZN17QSvgStructureNode18releaseDescendantsEv')

  @staticmethod
  def addChild(*__, **_) -> Never:
    """
    Qt's 'void QSvgStructureNode::addChild(QSvgDocument *doc,
    std::unique_ptr<QSvgNode> child, const QString &id)': the compiler
    refuses its ritual as it would be written here: call to deleted
    constructor of 'std::unique_ptr<QSvgNode>'.
    """
    raise NotImplementedError(
        "'QSvgStructureNode.addChild' has no cute function yet. Qt's 'void "
        "QSvgStructureNode::addChild(QSvgDocument *doc, "
        "std::unique_ptr<QSvgNode> child, const QString &id)': the compiler "
        "refuses its ritual as it would be written here: call to deleted "
        "constructor of 'std::unique_ptr<QSvgNode>'.")

  @staticmethod
  def renderers(*__, **_) -> Never:
    """
    Qt's 'const std::list<std::unique_ptr<QSvgNode>>
    &QSvgStructureNode::renderers() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QSvgStructureNode.renderers' has no cute function yet. Qt's "
        "'const std::list<std::unique_ptr<QSvgNode>> "
        "&QSvgStructureNode::renderers() const': gives a type Python has no "
        "way to take yet.")
