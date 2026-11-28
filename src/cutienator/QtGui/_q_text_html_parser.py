"""
QTextHtmlParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtexthtmlparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextHtmlParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QCss, QTextFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
  from . import QBrush, QTextHtmlParserNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']


class QTextHtmlParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextHtmlParser: a plain Python object standing in
  front of one C++ QTextHtmlParser.

  C++ hands a QTextHtmlParser around as a copy, so every C++ QTextHtmlParser
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextHtmlParser that has a ritual and that Python
  can call so far, 30 names in all: 'at', 'count', 'last', 'depth',
  'topMargin', 'bottomMargin', 'leftMargin', 'rightMargin', 'topPadding',
  'bottomPadding', 'leftPadding', 'rightPadding', 'tableCellBorder',
  'tableCellBorderStyle', 'tableCellBorderBrush', 'dumpHtml',
  'lookupElement', 'parseEntity', 'newNode', 'parseCloseTag',
  'parseExclamationTag', 'parseWord', 'resolveParent', 'resolveNode',
  'parseAttributes', 'eatSpace', 'hasPrefix', 'margin',
  'resolveStyleSheetImports', 'importStyleSheet'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextHtmlParser::~QTextHtmlParser()': the destructor: Python
    removes its C++ QTextHtmlParser by it, and has no other use for it.
  - Qt's 'QTextHtmlParserNode &QTextHtmlParser::operator[](int i)': gives a
    type Python has no way to take yet.
  - Qt's 'bool QTextHtmlParser::nodeIsChildOf(int i, QTextHTMLElements id)
    const': names the enum 'QTextHTMLElements', whose class cannot be named
    here.
  - Qt's 'QList<QCss::Declaration> QTextHtmlParser::declarationsForNode(int
    node) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QTextHtmlParser.

  What to expect
  --------------

  - The C++ QTextHtmlParser is created at the first use, not by
    'QTextHtmlParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextHtmlParser back gives a copy the ritual made for
    Python, in a new cute QTextHtmlParser.
  - Each name of Qt's QTextHtmlParser that has no cute function yet,
    'applyAttributes', 'declarationsForNode', 'nodeIsChildOf', 'parse',
    'parseTag', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QTextHtmlParser, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Margin(CuteNum):
    """
    The enum 'QTextHtmlParser::Margin' of Qt, with the 4 names Qt gives in
    it.
    """

    MarginTop = Kee[int](0)
    MarginRight = Kee[int](1)
    MarginBottom = Kee[int](2)
    MarginLeft = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def lookupElement(element: str) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::lookupElement(QAnyStringView element)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#lookupElement

    Parameters
    ----------

    element : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTextHtmlParser::lookupElement(QAnyStringView element)
    return Rituals.call(
        'ritual_ZN15QTextHtmlParser13lookupElementE14QAnyStringView',
        element,
    )

  @staticmethod
  @overload(str)
  def parseEntity(entity: str) -> str:
    """
    Calls Qt's 'QString QTextHtmlParser::parseEntity(QStringView entity)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#parseEntity

    Parameters
    ----------

    entity : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextHtmlParser::parseEntity(QStringView entity)
    return Rituals.call(
        'ritual_ZN15QTextHtmlParser11parseEntityE11QStringView', entity,
    )

  @overload()
  def parseEntity(self) -> str:
    """
    Calls Qt's 'QString QTextHtmlParser::parseEntity()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#parseEntity

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextHtmlParser::parseEntity()
    return self.uglySide.call('ritual_ZN15QTextHtmlParser11parseEntityEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextHtmlParser'

  #  Qt's '~QTextHtmlParser()'. Naming it makes this a value class: Python
  #  owns every C++ QTextHtmlParser behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QTextHtmlParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def at(self, i: int) -> QTextHtmlParserNode:
    """
    Calls Qt's 'const QTextHtmlParserNode &QTextHtmlParser::at(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QTextHtmlParserNode
      A new cute QTextHtmlParserNode around the copy Qt gave back. Python
      owns it.
    """
    #  const QTextHtmlParserNode &QTextHtmlParser::at(int i) const
    address = self.uglySide.call('ritual_ZNK15QTextHtmlParser2atEi', i)
    from . import QTextHtmlParserNode
    return QTextHtmlParserNode._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#count
    """
    #  int QTextHtmlParser::count() const
    return self.uglySide.call('ritual_ZNK15QTextHtmlParser5countEv')

  def last(self) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#last
    """
    #  int QTextHtmlParser::last() const
    return self.uglySide.call('ritual_ZNK15QTextHtmlParser4lastEv')

  @overload(int)
  def depth(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::depth(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#depth

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::depth(int i) const
    return self.uglySide.call('ritual_ZNK15QTextHtmlParser5depthEi', i)

  @overload(int)
  def topMargin(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::topMargin(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#topMargin

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::topMargin(int i) const
    return self.uglySide.call('ritual_ZNK15QTextHtmlParser9topMarginEi', i)

  @overload(int)
  def bottomMargin(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::bottomMargin(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#bottomMargin

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::bottomMargin(int i) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser12bottomMarginEi', i,
    )

  @overload(int)
  def leftMargin(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::leftMargin(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#leftMargin

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::leftMargin(int i) const
    return self.uglySide.call('ritual_ZNK15QTextHtmlParser10leftMarginEi', i)

  @overload(int)
  def rightMargin(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::rightMargin(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#rightMargin

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::rightMargin(int i) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser11rightMarginEi', i,
    )

  @overload(int)
  def topPadding(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::topPadding(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#topPadding

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::topPadding(int i) const
    return self.uglySide.call('ritual_ZNK15QTextHtmlParser10topPaddingEi', i)

  @overload(int)
  def bottomPadding(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::bottomPadding(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#bottomPadding

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::bottomPadding(int i) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser13bottomPaddingEi', i,
    )

  @overload(int)
  def leftPadding(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::leftPadding(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#leftPadding

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::leftPadding(int i) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser11leftPaddingEi', i,
    )

  @overload(int)
  def rightPadding(self, i: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::rightPadding(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#rightPadding

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::rightPadding(int i) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser12rightPaddingEi', i,
    )

  @overload(int, int)
  def tableCellBorder(self, i: int, edge: int) -> float:
    """
    Calls Qt's 'qreal QTextHtmlParser::tableCellBorder(int i, int edge)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#tableCellBorder

    Parameters
    ----------

    i : int
      Passed on as it is.

    edge : int
      Passed on as it is.
    """
    #  qreal QTextHtmlParser::tableCellBorder(int i, int edge) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser15tableCellBorderEii', i, edge,
    )

  @overload(int, int)
  def tableCellBorderStyle(
      self,
      i: int,
      edge: int,
  ) -> QTextFrameFormat.BorderStyle:
    """
    Calls Qt's 'QTextFrameFormat::BorderStyle
    QTextHtmlParser::tableCellBorderStyle(int i, int edge) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#tableCellBorderStyle

    Parameters
    ----------

    i : int
      Passed on as it is.

    edge : int
      Passed on as it is.

    Returns
    -------

    QTextFrameFormat.BorderStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextFrameFormat.BorderStyle(number)' gives.
    """
    #  QTextFrameFormat::BorderStyle
    #      QTextHtmlParser::tableCellBorderStyle(int i, int edge) const
    return QTextFrameFormat.BorderStyle(self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser20tableCellBorderStyleEii', i, edge,
    ))

  @overload(int, int)
  def tableCellBorderBrush(self, i: int, edge: int) -> QBrush:
    """
    Calls Qt's 'QBrush QTextHtmlParser::tableCellBorderBrush(int i, int edge)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#tableCellBorderBrush

    Parameters
    ----------

    i : int
      Passed on as it is.

    edge : int
      Passed on as it is.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextHtmlParser::tableCellBorderBrush(int i, int edge) const
    address = self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser20tableCellBorderBrushEii', i, edge,
    )
    from . import QBrush
    return QBrush._cuteOwning(address)

  @overload(QChar)
  @overload(QChar, int)
  def hasPrefix(self, c: QChar, lookahead: int = 0) -> bool:
    """
    Calls Qt's 'bool QTextHtmlParser::hasPrefix(QChar c, int lookahead)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#hasPrefix

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    lookahead : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QTextHtmlParser::hasPrefix(QChar c, int lookahead) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser9hasPrefixE5QChari',
        self._valueOf(c), lookahead,
    )

  @overload(int, int)
  def margin(self, i: int, mar: int) -> int:
    """
    Calls Qt's 'int QTextHtmlParser::margin(int i, int mar) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#margin

    Parameters
    ----------

    i : int
      Passed on as it is.

    mar : int
      Passed on as it is.
    """
    #  int QTextHtmlParser::margin(int i, int mar) const
    return self.uglySide.call(
        'ritual_ZNK15QTextHtmlParser6marginEii', i, mar,
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

  def dumpHtml(self) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::dumpHtml()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#dumpHtml
    """
    #  void QTextHtmlParser::dumpHtml()
    self.uglySide.call('ritual_ZN15QTextHtmlParser8dumpHtmlEv')

  @overload(int)
  def newNode(self, parent: int) -> Optional[QTextHtmlParserNode]:
    """
    Calls Qt's 'QTextHtmlParserNode *QTextHtmlParser::newNode(int parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#newNode

    Parameters
    ----------

    parent : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextHtmlParserNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextHtmlParserNode *QTextHtmlParser::newNode(int parent)
    address = self.uglySide.call(
        'ritual_ZN15QTextHtmlParser7newNodeEi', parent,
    )
    from . import QTextHtmlParserNode
    return QTextHtmlParserNode._cuteAt(address)

  def parseCloseTag(self) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::parseCloseTag()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#parseCloseTag
    """
    #  void QTextHtmlParser::parseCloseTag()
    self.uglySide.call('ritual_ZN15QTextHtmlParser13parseCloseTagEv')

  def parseExclamationTag(self) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::parseExclamationTag()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#parseExclamationTag
    """
    #  void QTextHtmlParser::parseExclamationTag()
    self.uglySide.call('ritual_ZN15QTextHtmlParser19parseExclamationTagEv')

  def parseWord(self) -> str:
    """
    Calls Qt's 'QString QTextHtmlParser::parseWord()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#parseWord

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextHtmlParser::parseWord()
    return self.uglySide.call('ritual_ZN15QTextHtmlParser9parseWordEv')

  def resolveParent(self) -> Optional[QTextHtmlParserNode]:
    """
    Calls Qt's 'QTextHtmlParserNode *QTextHtmlParser::resolveParent()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#resolveParent

    Returns
    -------

    Optional[QTextHtmlParserNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextHtmlParserNode *QTextHtmlParser::resolveParent()
    address = self.uglySide.call(
        'ritual_ZN15QTextHtmlParser13resolveParentEv',
    )
    from . import QTextHtmlParserNode
    return QTextHtmlParserNode._cuteAt(address)

  def resolveNode(self) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::resolveNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#resolveNode
    """
    #  void QTextHtmlParser::resolveNode()
    self.uglySide.call('ritual_ZN15QTextHtmlParser11resolveNodeEv')

  def parseAttributes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QTextHtmlParser::parseAttributes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#parseAttributes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTextHtmlParser::parseAttributes()
    address = self.uglySide.call(
        'ritual_ZN15QTextHtmlParser15parseAttributesEv',
    )
    return QStringList._cuteOwning(address)

  def eatSpace(self) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::eatSpace()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlparser.html#eatSpace
    """
    #  void QTextHtmlParser::eatSpace()
    self.uglySide.call('ritual_ZN15QTextHtmlParser8eatSpaceEv')

  @overload(WAIT['QCss.StyleSheet'])
  def resolveStyleSheetImports(self, sheet: QCss.StyleSheet) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::resolveStyleSheetImports(const
    QCss::StyleSheet &sheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#resolveStyleSheetImports

    Parameters
    ----------

    sheet : QCss.StyleSheet
      Passed on as a value: Qt reads the C++ QCss::StyleSheet, which stays
      Python's own.
    """
    #  void QTextHtmlParser::resolveStyleSheetImports(const QCss::StyleSheet
    #      &sheet)
    self.uglySide.call(
        'ritual_ZN15QTextHtmlParser24resolveStyleSheetImportsERKN4QCss10Sty'
        'leSheetE',
        self._valueOf(sheet),
    )

  @overload(str)
  def importStyleSheet(self, href: str) -> None:
    """
    Calls Qt's 'void QTextHtmlParser::importStyleSheet(const QString &href)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlparser.html#importStyleSheet

    Parameters
    ----------

    href : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextHtmlParser::importStyleSheet(const QString &href)
    self.uglySide.call(
        'ritual_ZN15QTextHtmlParser16importStyleSheetERK7QString', href,
    )

  @staticmethod
  def applyAttributes(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlParser::applyAttributes(const QStringList
    &attributes)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'setFloatAttribute'.
    """
    raise NotImplementedError(
        "'QTextHtmlParser.applyAttributes' has no cute function yet. Qt's "
        "'void QTextHtmlParser::applyAttributes(const QStringList "
        "&attributes)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'setFloatAttribute'.")

  @staticmethod
  def declarationsForNode(*__, **_) -> Never:
    """
    Qt's 'QList<QCss::Declaration> QTextHtmlParser::declarationsForNode(int
    node) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextHtmlParser.declarationsForNode' has no cute function yet. "
        "Qt's 'QList<QCss::Declaration> "
        "QTextHtmlParser::declarationsForNode(int node) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def nodeIsChildOf(*__, **_) -> Never:
    """
    Qt's 'bool QTextHtmlParser::nodeIsChildOf(int i, QTextHTMLElements id)
    const': names the enum 'QTextHTMLElements', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QTextHtmlParser.nodeIsChildOf' has no cute function yet. Qt's "
        "'bool QTextHtmlParser::nodeIsChildOf(int i, QTextHTMLElements id) "
        "const': names the enum 'QTextHTMLElements', whose class cannot be "
        "named here.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    - Qt's 'void QTextHtmlParser::parse(const QString &text, const
      QTextDocument *resourceProvider)': leans on
      'QTextHtmlParser::parseTag()', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'void QTextHtmlParser::parse()': leans on
      'QTextHtmlParser::parseTag()', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTextHtmlParser.parse' has no cute function yet. Qt's 'void "
        "QTextHtmlParser::parse(const QString &text, const QTextDocument "
        "*resourceProvider)': leans on 'QTextHtmlParser::parseTag()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void QTextHtmlParser::parse()': "
        "leans on 'QTextHtmlParser::parseTag()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parseTag(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlParser::parseTag()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'lookupElementHelper'; did you mean
    'lookupElement'?.
    """
    raise NotImplementedError(
        "'QTextHtmlParser.parseTag' has no cute function yet. Qt's 'void "
        "QTextHtmlParser::parseTag()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'lookupElementHelper'; did you mean "
        "'lookupElement'?.")
