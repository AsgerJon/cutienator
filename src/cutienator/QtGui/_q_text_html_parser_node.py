"""
QTextHtmlParserNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtexthtmlparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextHtmlParserNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTextDocument, QTextHtmlParser
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']
  QTextHtmlParser = WAIT['QTextHtmlParser']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextHtmlParserNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextHtmlParserNode: a plain Python object standing
  in front of one C++ QTextHtmlParserNode.

  C++ hands a QTextHtmlParserNode around as a copy, so every C++
  QTextHtmlParserNode behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextHtmlParserNode that has a ritual and that
  Python can call so far, 13 names in all: 'isListStart', 'isTableCell',
  'isBlock', 'isNotSelfNesting', 'allowedInContext', 'mayNotHaveChildren',
  'initializeProperties', 'uncollapsedMargin', 'isNestedList',
  'parseStyleAttribute', 'applyForegroundImage', 'applyBackgroundImage',
  'hasOnlyWhitespace'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QTextHtmlParserNode::applyCssDeclarations(const
    QList<QCss::Declaration> &declarations, const QTextDocument
    *resourceProvider)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTextHtmlParserNode::setListStyle(const QList<QCss::Value>
    &cssValues)': takes a type Python has no way to hand over yet.
  - Qt's 'QTextHtmlParserNode::~QTextHtmlParserNode()': the destructor:
    Python removes its C++ QTextHtmlParserNode by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTextHtmlParserNode is created at the first use, not by
    'QTextHtmlParserNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextHtmlParserNode back gives a copy the ritual made
    for Python, in a new cute QTextHtmlParserNode.
  - Each name of Qt's QTextHtmlParserNode that has no cute function yet,
    'applyCssDeclarations', 'setListStyle', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextHtmlParserNode, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class WhiteSpaceMode(CuteNum):
    """
    The enum 'QTextHtmlParserNode::WhiteSpaceMode' of Qt, with the 6 names Qt
    gives in it.
    """

    WhiteSpaceNormal = Kee[int](0)
    WhiteSpacePre = Kee[int](1)
    WhiteSpaceNoWrap = Kee[int](2)
    WhiteSpacePreWrap = Kee[int](3)
    WhiteSpacePreLine = Kee[int](4)
    WhiteSpaceModeUndefined = Kee[int](-1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextHtmlParserNode'

  #  Qt's '~QTextHtmlParserNode()'. Naming it makes this a value class:
  #  Python owns every C++ QTextHtmlParserNode behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QTextHtmlParserNodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isListStart(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::isListStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#isListStart
    """
    #  bool QTextHtmlParserNode::isListStart() const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode11isListStartEv',
    )

  def isTableCell(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::isTableCell() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#isTableCell
    """
    #  bool QTextHtmlParserNode::isTableCell() const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode11isTableCellEv',
    )

  def isBlock(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::isBlock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparsernode.html#isBlock
    """
    #  bool QTextHtmlParserNode::isBlock() const
    return self.uglySide.call('ritual_ZNK19QTextHtmlParserNode7isBlockEv')

  def isNotSelfNesting(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::isNotSelfNesting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#isNotSelfNesting
    """
    #  bool QTextHtmlParserNode::isNotSelfNesting() const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode16isNotSelfNestingEv',
    )

  @overload(int)
  def allowedInContext(self, parentId: int) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::allowedInContext(int parentId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#allowedInContext

    Parameters
    ----------

    parentId : int
      Passed on as it is.
    """
    #  bool QTextHtmlParserNode::allowedInContext(int parentId) const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode16allowedInContextEi', parentId,
    )

  def mayNotHaveChildren(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::mayNotHaveChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#mayNotHaveChildren
    """
    #  bool QTextHtmlParserNode::mayNotHaveChildren() const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode18mayNotHaveChildrenEv',
    )

  @overload(int)
  def uncollapsedMargin(self, mar: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParserNode::uncollapsedMargin(int mar) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#uncollapsedMargin

    Parameters
    ----------

    mar : int
      Passed on as it is.
    """
    #  int QTextHtmlParserNode::uncollapsedMargin(int mar) const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode17uncollapsedMarginEi', mar,
    )

  @overload(QTextHtmlParser)
  @overload(NoneType)
  def isNestedList(self, parser: Optional[QTextHtmlParser]) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::isNestedList(const QTextHtmlParser
    *parser) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#isNestedList

    Parameters
    ----------

    parser : Optional[QTextHtmlParser]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTextHtmlParserNode::isNestedList(const QTextHtmlParser *parser)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode12isNestedListEPK15QTextHtmlParser',
        self._addressOf(parser),
    )

  def hasOnlyWhitespace(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParserNode::hasOnlyWhitespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#hasOnlyWhitespace
    """
    #  bool QTextHtmlParserNode::hasOnlyWhitespace() const
    return self.uglySide.call(
        'ritual_ZNK19QTextHtmlParserNode17hasOnlyWhitespaceEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QTextHtmlParserNode::QTextHtmlParserNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#QTextHtmlParserNode
    """
    #  QTextHtmlParserNode::QTextHtmlParserNode()
    self._noteCreation(QTextHtmlParserNode, lambda: Rituals.call(
        'ritual_ZN19QTextHtmlParserNodeC1Ev',
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

  @overload(THIS, QTextHtmlParser)
  @overload(THIS, NoneType)
  @overload(NoneType, QTextHtmlParser)
  @overload(NoneType, NoneType)
  def initializeProperties(
      self,
      parent: Optional[QTextHtmlParserNode],
      parser: Optional[QTextHtmlParser],
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlParserNode::initializeProperties(const
    QTextHtmlParserNode *parent, const QTextHtmlParser *parser)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#initializeProperties

    Parameters
    ----------

    parent : Optional[QTextHtmlParserNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parser : Optional[QTextHtmlParser]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextHtmlParserNode::initializeProperties(const
    #      QTextHtmlParserNode *parent, const QTextHtmlParser *parser)
    self.uglySide.call(
        'ritual_ZN19QTextHtmlParserNode20initializePropertiesEPKS_PK15QText'
        'HtmlParser',
        self._addressOf(parent), self._addressOf(parser),
    )

  @overload(str, QTextDocument)
  @overload(str, NoneType)
  def parseStyleAttribute(
      self,
      value: str,
      resourceProvider: Optional[QTextDocument],
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlParserNode::parseStyleAttribute(const QString
    &value, const QTextDocument *resourceProvider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#parseStyleAttribute

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.

    resourceProvider : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextHtmlParserNode::parseStyleAttribute(const QString &value,
    #      const QTextDocument *resourceProvider)
    self.uglySide.call(
        'ritual_ZN19QTextHtmlParserNode19parseStyleAttributeERK7QStringPK13'
        'QTextDocument',
        value, self._addressOf(resourceProvider),
    )

  @overload(int, QTextDocument)
  @overload(int, NoneType)
  def applyForegroundImage(
      self,
      cacheKey: int,
      resourceProvider: Optional[QTextDocument],
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlParserNode::applyForegroundImage(qint64
    cacheKey, const QTextDocument *resourceProvider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#applyForegroundImage

    Parameters
    ----------

    cacheKey : int
      Passed on as it is.

    resourceProvider : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextHtmlParserNode::applyForegroundImage(qint64 cacheKey, const
    #      QTextDocument *resourceProvider)
    self.uglySide.call(
        'ritual_ZN19QTextHtmlParserNode20applyForegroundImageExPK13QTextDoc'
        'ument',
        cacheKey, self._addressOf(resourceProvider),
    )

  @overload(str, QTextDocument)
  @overload(str, NoneType)
  def applyBackgroundImage(
      self,
      url: str,
      resourceProvider: Optional[QTextDocument],
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlParserNode::applyBackgroundImage(const QString
    &url, const QTextDocument *resourceProvider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparsernode.html#applyBackgroundImage

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.

    resourceProvider : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextHtmlParserNode::applyBackgroundImage(const QString &url,
    #      const QTextDocument *resourceProvider)
    self.uglySide.call(
        'ritual_ZN19QTextHtmlParserNode20applyBackgroundImageERK7QStringPK1'
        '3QTextDocument',
        url, self._addressOf(resourceProvider),
    )

  @staticmethod
  def applyCssDeclarations(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlParserNode::applyCssDeclarations(const
    QList<QCss::Declaration> &declarations, const QTextDocument
    *resourceProvider)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextHtmlParserNode.applyCssDeclarations' has no cute function "
        "yet. Qt's 'void QTextHtmlParserNode::applyCssDeclarations(const "
        "QList<QCss::Declaration> &declarations, const QTextDocument "
        "*resourceProvider)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setListStyle(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlParserNode::setListStyle(const QList<QCss::Value>
    &cssValues)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextHtmlParserNode.setListStyle' has no cute function yet. Qt's "
        "'void QTextHtmlParserNode::setListStyle(const QList<QCss::Value> "
        "&cssValues)': takes a type Python has no way to hand over yet.")
