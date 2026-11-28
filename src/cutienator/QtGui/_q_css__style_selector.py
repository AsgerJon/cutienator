"""
QCss::StyleSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::StyleSelector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QStringList
from . import QCss

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class StyleSelector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::StyleSelector: a plain Python object standing
  in front of one C++ QCss::StyleSelector.

  What exists
  -----------

  Every function of Qt's QCss::StyleSelector that has a ritual and that
  Python can call so far, 12 names in all: 'nodeNameEquals',
  'attributeValue', 'hasAttributes', 'nodeIds', 'nodeNames', 'isNullNode',
  'parentNode', 'previousSiblingNode', 'duplicateNode', 'freeNode',
  'selectorMatches', 'basicSelectorMatches'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCss::StyleSelector::~StyleSelector()': the destructor: Python
    never removes a C++ QCss::StyleSelector.
  - Qt's 'QList<StyleRule> QCss::StyleSelector::styleRulesForNode(NodePtr
    node)': gives a type Python has no way to take yet.
  - Qt's 'QList<Declaration> QCss::StyleSelector::declarationsForNode(NodePtr
    node, const char *extraPseudo)': gives a type Python has no way to take
    yet.
  - Qt's 'void QCss::StyleSelector::matchRule(NodePtr node, const StyleRule
    &rules, StyleSheetOrigin origin, int depth, std::multimap<uint64_t,
    StyleRule> *weightedRules) const': names 'std::multimap<uint64_t,
    QCss::StyleRule>', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QCss::StyleSelector is created at the first use, not by
    'QCss::StyleSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCss::StyleSelector.
  - Each name of Qt's QCss::StyleSelector that has no cute function yet,
    '__init__', 'declarationsForNode', 'matchRule', 'styleRulesForNode',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QCss::StyleSelector, each a class in here
  #  as in C++.

  class NodePtr(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCss::StyleSelector::NodePtr: a plain Python object
    standing in front of one C++ QCss::StyleSelector::NodePtr.

    C++ hands a QCss::StyleSelector::NodePtr around as a copy, so every C++
    QCss::StyleSelector::NodePtr behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QCss::StyleSelector::NodePtr yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCss::StyleSelector::NodePtr::~NodePtr()': the destructor: Python
      removes its C++ QCss::StyleSelector::NodePtr by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QCss::StyleSelector::NodePtr is created at the first use, not
      by 'QCss::StyleSelector::NodePtr(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCss::StyleSelector::NodePtr back gives a copy the
      ritual made for Python, in a new cute QCss::StyleSelector::NodePtr.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCss::StyleSelector::NodePtr'

    #  Qt's '~QCss::StyleSelector::NodePtr()'. Naming it makes this a value
    #  class: Python owns every C++ QCss::StyleSelector::NodePtr behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN4QCss13StyleSelector7NodePtrD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCss::StyleSelector'

  #  A C++ QCss::StyleSelector Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCss_StyleSelector'

  #  The functions Qt calls itself that QCss::StyleSelector is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nodeIds': (
          'QStringList QCss::StyleSelector::nodeIds(NodePtr) const',
      ),
      'nodeNames': (
          'QStringList QCss::StyleSelector::nodeNames(NodePtr) const',
      ),
  }

  #  The functions Qt calls itself that QCss::StyleSelector is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'nodeNameEquals': (
          ('_ZNK4QCss13StyleSelector14nodeNameEqualsENS0_7NodePtrERK7QStrin'
           'g',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
               ('address', 'text', ''),
           )),
      ),
      'attributeValue': (
          ('_ZNK4QCss13StyleSelector14attributeValueENS0_7NodePtrERKNS_17At'
           'tributeSelectorE',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
               ('address', 'value', 'QtGui:QCss.AttributeSelector'),
           )),
      ),
      'hasAttributes': (
          ('_ZNK4QCss13StyleSelector13hasAttributesENS0_7NodePtrE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           )),
      ),
      'isNullNode': (
          ('_ZNK4QCss13StyleSelector10isNullNodeENS0_7NodePtrE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           )),
      ),
      'parentNode': (
          ('_ZNK4QCss13StyleSelector10parentNodeENS0_7NodePtrE',
           ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           )),
      ),
      'previousSiblingNode': (
          ('_ZNK4QCss13StyleSelector19previousSiblingNodeENS0_7NodePtrE',
           ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           )),
      ),
      'duplicateNode': (
          ('_ZNK4QCss13StyleSelector13duplicateNodeENS0_7NodePtrE',
           ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           )),
      ),
      'freeNode': (
          ('_ZNK4QCss13StyleSelector8freeNodeENS0_7NodePtrE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QCss.StyleSelector.NodePtr'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(NodePtr, str)
  def nodeNameEquals(self, node: NodePtr, nodeName: str) -> bool:
    """
    Calls Qt's 'bool QCss::StyleSelector::nodeNameEquals(NodePtr node, const
    QString &nodeName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#nodeNameEquals

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    nodeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCss::StyleSelector::nodeNameEquals(NodePtr node, const QString
    #      &nodeName) const
    ritual = (
        'ritual_ZNK4QCss13StyleSelector14nodeNameEqualsENS0_7NodePtrERK7QSt'
        'ring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK4QCss13StyleSelector14nodeNameEqualsENS0_7NodePtrE'
          'RK7QString')
    return self.uglySide.call(ritual, self._valueOf(node), nodeName)

  @overload(NodePtr, WAIT['QCss.AttributeSelector'])
  def attributeValue(
      self,
      node: NodePtr,
      aSelector: QCss.AttributeSelector,
  ) -> str:
    """
    Calls Qt's 'QString QCss::StyleSelector::attributeValue(NodePtr node,
    const QCss::AttributeSelector &aSelector) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#attributeValue

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    aSelector : QCss.AttributeSelector
      Passed on as a value: Qt reads the C++ QCss::AttributeSelector, which
      stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCss::StyleSelector::attributeValue(NodePtr node, const
    #      QCss::AttributeSelector &aSelector) const
    return self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector14attributeValueENS0_7NodePtrERKNS_1'
        '7AttributeSelectorE',
        self._valueOf(node), self._valueOf(aSelector),
    )

  @overload(NodePtr)
  def hasAttributes(self, node: NodePtr) -> bool:
    """
    Calls Qt's 'bool QCss::StyleSelector::hasAttributes(NodePtr node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#hasAttributes

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  bool QCss::StyleSelector::hasAttributes(NodePtr node) const
    return self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector13hasAttributesENS0_7NodePtrE',
        self._valueOf(node),
    )

  @overload(NodePtr)
  def nodeIds(self, node: NodePtr) -> QStringList:
    """
    Calls Qt's 'QStringList QCss::StyleSelector::nodeIds(NodePtr node)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-styleselector.html#nodeIds

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCss::StyleSelector::nodeIds(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector7nodeIdsENS0_7NodePtrE',
        self._valueOf(node),
    )
    return QStringList._cuteOwning(address)

  @overload(NodePtr)
  def nodeNames(self, node: NodePtr) -> QStringList:
    """
    Calls Qt's 'QStringList QCss::StyleSelector::nodeNames(NodePtr node)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-styleselector.html#nodeNames

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCss::StyleSelector::nodeNames(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector9nodeNamesENS0_7NodePtrE',
        self._valueOf(node),
    )
    return QStringList._cuteOwning(address)

  @overload(NodePtr)
  def isNullNode(self, node: NodePtr) -> bool:
    """
    Calls Qt's 'bool QCss::StyleSelector::isNullNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-styleselector.html#isNullNode

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  bool QCss::StyleSelector::isNullNode(NodePtr node) const
    return self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector10isNullNodeENS0_7NodePtrE',
        self._valueOf(node),
    )

  @overload(NodePtr)
  def parentNode(self, node: NodePtr) -> NodePtr:
    """
    Calls Qt's 'NodePtr QCss::StyleSelector::parentNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-styleselector.html#parentNode

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    NodePtr
      A new cute QCss::StyleSelector::NodePtr around the copy Qt gave back.
      Python owns it.
    """
    #  NodePtr QCss::StyleSelector::parentNode(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector10parentNodeENS0_7NodePtrE',
        self._valueOf(node),
    )
    return QCss.StyleSelector.NodePtr._cuteOwning(address)

  @overload(NodePtr)
  def previousSiblingNode(self, node: NodePtr) -> NodePtr:
    """
    Calls Qt's 'NodePtr QCss::StyleSelector::previousSiblingNode(NodePtr
    node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#previousSiblingNode

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    NodePtr
      A new cute QCss::StyleSelector::NodePtr around the copy Qt gave back.
      Python owns it.
    """
    #  NodePtr QCss::StyleSelector::previousSiblingNode(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector19previousSiblingNodeENS0_7NodePtrE',
        self._valueOf(node),
    )
    return QCss.StyleSelector.NodePtr._cuteOwning(address)

  @overload(NodePtr)
  def duplicateNode(self, node: NodePtr) -> NodePtr:
    """
    Calls Qt's 'NodePtr QCss::StyleSelector::duplicateNode(NodePtr node)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#duplicateNode

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.

    Returns
    -------

    NodePtr
      A new cute QCss::StyleSelector::NodePtr around the copy Qt gave back.
      Python owns it.
    """
    #  NodePtr QCss::StyleSelector::duplicateNode(NodePtr node) const
    address = self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector13duplicateNodeENS0_7NodePtrE',
        self._valueOf(node),
    )
    return QCss.StyleSelector.NodePtr._cuteOwning(address)

  @overload(WAIT['QCss.Selector'], NodePtr)
  def selectorMatches(self, rule: QCss.Selector, node: NodePtr) -> bool:
    """
    Calls Qt's 'bool QCss::StyleSelector::selectorMatches(const Selector
    &rule, NodePtr node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#selectorMatches

    Parameters
    ----------

    rule : QCss.Selector
      Passed on as a value: Qt reads the C++ QCss::Selector, which stays
      Python's own.

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  bool QCss::StyleSelector::selectorMatches(const Selector &rule,
    #      NodePtr node) const
    return self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector15selectorMatchesERKNS_8SelectorENS0'
        '_7NodePtrE',
        self._valueOf(rule), self._valueOf(node),
    )

  @overload(WAIT['QCss.BasicSelector'], NodePtr)
  def basicSelectorMatches(
      self,
      rule: QCss.BasicSelector,
      node: NodePtr,
  ) -> bool:
    """
    Calls Qt's 'bool QCss::StyleSelector::basicSelectorMatches(const
    BasicSelector &rule, NodePtr node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-styleselector.html#basicSelectorMatches

    Parameters
    ----------

    rule : QCss.BasicSelector
      Passed on as a value: Qt reads the C++ QCss::BasicSelector, which stays
      Python's own.

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  bool QCss::StyleSelector::basicSelectorMatches(const BasicSelector
    #      &rule, NodePtr node) const
    return self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector20basicSelectorMatchesERKNS_13BasicS'
        'electorENS0_7NodePtrE',
        self._valueOf(rule), self._valueOf(node),
    )

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
    Qt's 'QCss::StyleSelector::StyleSelector()': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QCss.StyleSelector.__init__' has no cute function yet. Qt's "
        "'QCss::StyleSelector::StyleSelector()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  @overload(NodePtr)
  def freeNode(self, node: NodePtr) -> None:
    """
    Calls Qt's 'void QCss::StyleSelector::freeNode(NodePtr node) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-styleselector.html#freeNode

    Parameters
    ----------

    node : NodePtr
      Passed on as a value: Qt reads the C++ QCss::StyleSelector::NodePtr,
      which stays Python's own.
    """
    #  void QCss::StyleSelector::freeNode(NodePtr node) const
    self.uglySide.call(
        'ritual_ZNK4QCss13StyleSelector8freeNodeENS0_7NodePtrE',
        self._valueOf(node),
    )

  @staticmethod
  def declarationsForNode(*__, **_) -> Never:
    """
    Qt's 'QList<Declaration> QCss::StyleSelector::declarationsForNode(NodePtr
    node, const char *extraPseudo)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QCss.StyleSelector.declarationsForNode' has no cute function yet. "
        "Qt's 'QList<Declaration> "
        "QCss::StyleSelector::declarationsForNode(NodePtr node, const char "
        "*extraPseudo)': gives a type Python has no way to take yet.")

  @staticmethod
  def matchRule(*__, **_) -> Never:
    """
    Qt's 'void QCss::StyleSelector::matchRule(NodePtr node, const StyleRule
    &rules, StyleSheetOrigin origin, int depth, std::multimap<uint64_t,
    StyleRule> *weightedRules) const': names 'std::multimap<uint64_t,
    QCss::StyleRule>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCss.StyleSelector.matchRule' has no cute function yet. Qt's "
        "'void QCss::StyleSelector::matchRule(NodePtr node, const StyleRule "
        "&rules, StyleSheetOrigin origin, int depth, "
        "std::multimap<uint64_t, StyleRule> *weightedRules) const': names "
        "'std::multimap<uint64_t, QCss::StyleRule>', which has no cute "
        "class yet.")

  @staticmethod
  def styleRulesForNode(*__, **_) -> Never:
    """
    Qt's 'QList<StyleRule> QCss::StyleSelector::styleRulesForNode(NodePtr
    node)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCss.StyleSelector.styleRulesForNode' has no cute function yet. "
        "Qt's 'QList<StyleRule> "
        "QCss::StyleSelector::styleRulesForNode(NodePtr node)': gives a "
        "type Python has no way to take yet.")
