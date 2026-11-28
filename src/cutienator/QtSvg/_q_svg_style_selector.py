"""
QSvgStyleSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyleselector_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgStyleSelector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtGui import QCss

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSvgNode, QSvgStructureNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgNode = WAIT['QSvgNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgStyleSelector(QCss.StyleSelector):
  """
  The cute side of Qt's QSvgStyleSelector: a plain Python object standing in
  front of one C++ QSvgStyleSelector.

  It is built on the cute 'QCss::StyleSelector', as Qt's QSvgStyleSelector is
  built on Qt's QCss::StyleSelector, and has everything that class has.

  C++ hands a QSvgStyleSelector around as a copy, so every C++
  QSvgStyleSelector behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgStyleSelector that has a ritual and that Python
  can call so far, 13 names in all: 'svgNode', 'nodeToStructure',
  'svgStructure', 'nodeNameEquals', 'attributeValue', 'hasAttributes',
  'nodeIds', 'nodeNames', 'isNullNode', 'parentNode', 'previousSiblingNode',
  'duplicateNode', 'freeNode'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgStyleSelector::~QSvgStyleSelector()': the destructor: Python
    removes its C++ QSvgStyleSelector by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSvgStyleSelector is created at the first use, not by
    'QSvgStyleSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgStyleSelector back gives a copy the ritual made
    for Python, in a new cute QSvgStyleSelector.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgStyleSelector'

  #  A C++ QSvgStyleSelector Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgStyleSelector'

  #  Qt's '~QSvgStyleSelector()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgStyleSelector behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSvgStyleSelectorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCss.StyleSelector.NodePtr)
  def svgNode(self, node: QCss.StyleSelector.NodePtr) -> Optional[QSvgNode]:
    """
    Calls Qt's 'QSvgNode *QSvgStyleSelector::svgNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleselector.html#svgNode

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    Optional[QSvgNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgNode *QSvgStyleSelector::svgNode(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgStyleSelector7svgNodeEN4QCss13StyleSelector7NodePt'
        'rE',
        self._valueOf(node),
    )
    from . import QSvgNode
    return QSvgNode._cuteAt(address)

  @overload(QSvgNode)
  @overload(NoneType)
  def nodeToStructure(
      self,
      n: Optional[QSvgNode],
  ) -> Optional[QSvgStructureNode]:
    """
    Calls Qt's 'QSvgStructureNode
    *QSvgStyleSelector::nodeToStructure(QSvgNode *n) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#nodeToStructure

    Parameters
    ----------

    n : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSvgStructureNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgStructureNode *QSvgStyleSelector::nodeToStructure(QSvgNode *n)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgStyleSelector15nodeToStructureEP8QSvgNode',
        self._addressOf(n),
    )
    from . import QSvgStructureNode
    return QSvgStructureNode._cuteAt(address)

  @overload(QCss.StyleSelector.NodePtr)
  def svgStructure(
      self,
      node: QCss.StyleSelector.NodePtr,
  ) -> Optional[QSvgStructureNode]:
    """
    Calls Qt's 'QSvgStructureNode *QSvgStyleSelector::svgStructure(NodePtr
    node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#svgStructure

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    Optional[QSvgStructureNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgStructureNode *QSvgStyleSelector::svgStructure(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgStyleSelector12svgStructureEN4QCss13StyleSelector7'
        'NodePtrE',
        self._valueOf(node),
    )
    from . import QSvgStructureNode
    return QSvgStructureNode._cuteAt(address)

  @overload(QCss.StyleSelector.NodePtr, str)
  def nodeNameEquals(
      self,
      node: QCss.StyleSelector.NodePtr,
      nodeName: str,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgStyleSelector::nodeNameEquals(NodePtr node, const
    QString &nodeName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#nodeNameEquals

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    nodeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgStyleSelector::nodeNameEquals(NodePtr node, const QString
    #      &nodeName) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector14nodeNameEqualsEN4QCss13StyleSelecto'
        'r7NodePtrERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector14nodeNameEqualsEN4QCss13StyleS'
          'elector7NodePtrERK7QString')
    return self.uglySide.call(ritual, self._valueOf(node), nodeName)

  @overload(QCss.StyleSelector.NodePtr, WAIT['QCss.AttributeSelector'])
  def attributeValue(
      self,
      node: QCss.StyleSelector.NodePtr,
      asel: QCss.AttributeSelector,
  ) -> str:
    """
    Calls Qt's 'QString QSvgStyleSelector::attributeValue(NodePtr node, const
    QCss::AttributeSelector &asel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#attributeValue

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    asel : QCss.AttributeSelector
      Passed on as a value: Qt reads the C++ QCss::AttributeSelector, which
      stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgStyleSelector::attributeValue(NodePtr node, const
    #      QCss::AttributeSelector &asel) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector14attributeValueEN4QCss13StyleSelecto'
        'r7NodePtrERKNS0_17AttributeSelectorE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector14attributeValueEN4QCss13StyleS'
          'elector7NodePtrERKNS0_17AttributeSelectorE')
    return self.uglySide.call(
        ritual, self._valueOf(node), self._valueOf(asel),
    )

  @overload(QCss.StyleSelector.NodePtr)
  def hasAttributes(self, node: QCss.StyleSelector.NodePtr) -> bool:
    """
    Calls Qt's 'bool QSvgStyleSelector::hasAttributes(NodePtr node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#hasAttributes

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  bool QSvgStyleSelector::hasAttributes(NodePtr node) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector13hasAttributesEN4QCss13StyleSelector'
        '7NodePtrE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector13hasAttributesEN4QCss13StyleSe'
          'lector7NodePtrE')
    return self.uglySide.call(ritual, self._valueOf(node))

  @overload(QCss.StyleSelector.NodePtr)
  def nodeIds(self, node: QCss.StyleSelector.NodePtr) -> QStringList:
    """
    Calls Qt's 'QStringList QSvgStyleSelector::nodeIds(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleselector.html#nodeIds

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSvgStyleSelector::nodeIds(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgStyleSelector7nodeIdsEN4QCss13StyleSelector7NodePt'
        'rE',
        self._valueOf(node),
    )
    return QStringList._cuteOwning(address)

  @overload(QCss.StyleSelector.NodePtr)
  def nodeNames(self, node: QCss.StyleSelector.NodePtr) -> QStringList:
    """
    Calls Qt's 'QStringList QSvgStyleSelector::nodeNames(NodePtr node)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleselector.html#nodeNames

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSvgStyleSelector::nodeNames(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgStyleSelector9nodeNamesEN4QCss13StyleSelector7Node'
        'PtrE',
        self._valueOf(node),
    )
    return QStringList._cuteOwning(address)

  @overload(QCss.StyleSelector.NodePtr)
  def isNullNode(self, node: QCss.StyleSelector.NodePtr) -> bool:
    """
    Calls Qt's 'bool QSvgStyleSelector::isNullNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleselector.html#isNullNode

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  bool QSvgStyleSelector::isNullNode(NodePtr node) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector10isNullNodeEN4QCss13StyleSelector7No'
        'dePtrE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector10isNullNodeEN4QCss13StyleSelec'
          'tor7NodePtrE')
    return self.uglySide.call(ritual, self._valueOf(node))

  @overload(QCss.StyleSelector.NodePtr)
  def parentNode(
      self,
      node: QCss.StyleSelector.NodePtr,
  ) -> QCss.StyleSelector.NodePtr:
    """
    Calls Qt's 'NodePtr QSvgStyleSelector::parentNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleselector.html#parentNode

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QCss.StyleSelector.NodePtr
      A new cute QCss::StyleSelector::NodePtr around the copy Qt gave back.
      Python owns it.
    """
    #  NodePtr QSvgStyleSelector::parentNode(NodePtr node) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector10parentNodeEN4QCss13StyleSelector7No'
        'dePtrE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector10parentNodeEN4QCss13StyleSelec'
          'tor7NodePtrE')
    address = self.uglySide.call(ritual, self._valueOf(node))
    return QCss.StyleSelector.NodePtr._cuteOwning(address)

  @overload(QCss.StyleSelector.NodePtr)
  def previousSiblingNode(
      self,
      node: QCss.StyleSelector.NodePtr,
  ) -> QCss.StyleSelector.NodePtr:
    """
    Calls Qt's 'NodePtr QSvgStyleSelector::previousSiblingNode(NodePtr node)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#previousSiblingNode

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QCss.StyleSelector.NodePtr
      A new cute QCss::StyleSelector::NodePtr around the copy Qt gave back.
      Python owns it.
    """
    #  NodePtr QSvgStyleSelector::previousSiblingNode(NodePtr node) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector19previousSiblingNodeEN4QCss13StyleSe'
        'lector7NodePtrE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector19previousSiblingNodeEN4QCss13S'
          'tyleSelector7NodePtrE')
    address = self.uglySide.call(ritual, self._valueOf(node))
    return QCss.StyleSelector.NodePtr._cuteOwning(address)

  @overload(QCss.StyleSelector.NodePtr)
  def duplicateNode(
      self,
      node: QCss.StyleSelector.NodePtr,
  ) -> QCss.StyleSelector.NodePtr:
    """
    Calls Qt's 'NodePtr QSvgStyleSelector::duplicateNode(NodePtr node)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#duplicateNode

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QCss.StyleSelector.NodePtr
      A new cute QCss::StyleSelector::NodePtr around the copy Qt gave back.
      Python owns it.
    """
    #  NodePtr QSvgStyleSelector::duplicateNode(NodePtr node) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector13duplicateNodeEN4QCss13StyleSelector'
        '7NodePtrE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector13duplicateNodeEN4QCss13StyleSe'
          'lector7NodePtrE')
    address = self.uglySide.call(ritual, self._valueOf(node))
    return QCss.StyleSelector.NodePtr._cuteOwning(address)

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
    Notes what was given, for Qt's 'QSvgStyleSelector::QSvgStyleSelector()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgstyleselector.html#QSvgStyleSelector
    """
    #  QSvgStyleSelector::QSvgStyleSelector()
    self._noteCreation(QSvgStyleSelector, lambda: Rituals.call(
        'ritual_ZN17QSvgStyleSelectorC1Ev',
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

  @overload(QCss.StyleSelector.NodePtr)
  def freeNode(self, node: QCss.StyleSelector.NodePtr) -> None:
    """
    Calls Qt's 'void QSvgStyleSelector::freeNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgstyleselector.html#freeNode

    Parameters
    ----------

    node : QCss.StyleSelector.NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  void QSvgStyleSelector::freeNode(NodePtr node) const
    ritual = (
        'ritual_ZNK17QSvgStyleSelector8freeNodeEN4QCss13StyleSelector7NodeP'
        'trE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QSvgStyleSelector8freeNodeEN4QCss13StyleSelector'
          '7NodePtrE')
    self.uglySide.call(ritual, self._valueOf(node))
