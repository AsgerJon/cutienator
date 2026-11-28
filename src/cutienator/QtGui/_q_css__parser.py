"""
QCss::Parser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCss::Parser to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QCss

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String, QString
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QLatin1String = WAIT['QLatin1String']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Parser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCss::Parser: a plain Python object standing in front
  of one C++ QCss::Parser.

  C++ hands a QCss::Parser around as a copy, so every C++ QCss::Parser behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCss::Parser that has a ritual and that Python can
  call so far, 60 names in all: 'init', 'parse', 'errorSymbol',
  'parseImport', 'parseMedia', 'parsePage', 'parsePseudoPage',
  'parseNextOperator', 'parseAnimation', 'parseProperty', 'parseRuleset',
  'parseSelector', 'parseSimpleSelector', 'parseClass', 'parseElementName',
  'parseAttrib', 'parsePseudo', 'parseNextDeclaration', 'parsePrio',
  'parseTerm', 'parseFunction', 'parseHexColor', 'testAndParseUri',
  'testRuleset', 'testSelector', 'parseNextSelector', 'testSimpleSelector',
  'parseNextSimpleSelector', 'testElementName', 'testClass', 'testAttrib',
  'testPseudo', 'testMedium', 'testPseudoPage', 'testImport', 'testMedia',
  'testPage', 'testAnimation', 'testCombinator', 'testProperty', 'testTerm',
  'testExpr', 'testPrio', 'testHexColor', 'testFunction',
  'parseNextFunction', 'lookupElementName', 'skipSpace', 'hasNext', 'next',
  'test', 'prev', 'symbol', 'lexem', 'unquotedLexem', 'lexemUntil', 'until',
  'lookup', 'testTokenAndEndsWith', 'recordError'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCss::Parser::parseMedium(QStringList *media)': names
    'QStringList', which has no cute class yet.
  - Qt's 'bool QCss::Parser::parseCombinator(BasicSelector::Relation
    *relation)': names 'QCss::BasicSelector::Relation', which has no cute
    class yet.
  - Qt's 'bool QCss::Parser::parseExpr(QList<Value> *values)': names
    'QList<QCss::Value>', which has no cute class yet.
  - Qt's 'bool QCss::Parser::parseNextMedium(QStringList *media)': names
    'QStringList', which has no cute class yet.
  - Qt's 'bool QCss::Parser::parseNextExpr(QList<Value> *values)': names
    'QList<QCss::Value>', which has no cute class yet.
  - Qt's 'QCss::Parser::~Parser()': the destructor: Python removes its C++
    QCss::Parser by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCss::Parser is created at the first use, not by
    'QCss::Parser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCss::Parser back gives a copy the ritual made for
    Python, in a new cute QCss::Parser.
  - Each name of Qt's QCss::Parser that has no cute function yet,
    'parseCombinator', 'parseExpr', 'parseMedium', 'parseNextExpr',
    'parseNextMedium', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCss::Parser'

  #  Qt's '~QCss::Parser()'. Naming it makes this a value class: Python owns
  #  every C++ QCss::Parser behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QCss6ParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lookupElementName(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::lookupElementName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#lookupElementName
    """
    #  bool QCss::Parser::lookupElementName() const
    return self.uglySide.call('ritual_ZNK4QCss6Parser17lookupElementNameEv')

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::hasNext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#hasNext
    """
    #  bool QCss::Parser::hasNext() const
    return self.uglySide.call('ritual_ZNK4QCss6Parser7hasNextEv')

  def symbol(self) -> QCss.Symbol:
    """
    Calls Qt's 'const Symbol &QCss::Parser::symbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#symbol

    Returns
    -------

    QCss.Symbol
      A new cute QCss::Symbol around the copy Qt gave back. Python owns it.
    """
    #  const Symbol &QCss::Parser::symbol() const
    address = self.uglySide.call('ritual_ZNK4QCss6Parser6symbolEv')
    return QCss.Symbol._cuteOwning(address)

  def lexem(self) -> str:
    """
    Calls Qt's 'QString QCss::Parser::lexem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#lexem

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCss::Parser::lexem() const
    return self.uglySide.call('ritual_ZNK4QCss6Parser5lexemEv')

  def unquotedLexem(self) -> str:
    """
    Calls Qt's 'QString QCss::Parser::unquotedLexem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#unquotedLexem

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCss::Parser::unquotedLexem() const
    return self.uglySide.call('ritual_ZNK4QCss6Parser13unquotedLexemEv')

  def lookup(self) -> QCss.TokenType:
    """
    Calls Qt's 'TokenType QCss::Parser::lookup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#lookup

    Returns
    -------

    QCss.TokenType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCss.TokenType(number)'
      gives.
    """
    #  TokenType QCss::Parser::lookup() const
    return QCss.TokenType(self.uglySide.call(
        'ritual_ZNK4QCss6Parser6lookupEv',
    ))

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
    Notes what was given, for Qt's 'QCss::Parser::Parser()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#Parser
    """
    #  QCss::Parser::Parser()
    self._noteCreation(Parser, lambda: Rituals.call(
        'ritual_ZN4QCss6ParserC1Ev',
    ))

  @overload(str)
  @overload(str, bool)
  def __init__(self, css: str, file: bool = False) -> None:
    """
    Notes what was given, for Qt's 'QCss::Parser::Parser(const QString &css,
    bool file)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#Parser

    Parameters
    ----------

    css : str
      Passed on as it is: a QString is made of it for the call.

    file : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QCss::Parser::Parser(const QString &css, bool file)
    self._noteCreation(Parser, lambda: Rituals.call(
        'ritual_ZN4QCss6ParserC1ERK7QStringb', css, file,
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

  @overload(str)
  @overload(str, bool)
  def init(self, css: str, file: bool = False) -> None:
    """
    Calls Qt's 'void QCss::Parser::init(const QString &css, bool file)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#init

    Parameters
    ----------

    css : str
      Passed on as it is: a QString is made of it for the call.

    file : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QCss::Parser::init(const QString &css, bool file)
    self.uglySide.call('ritual_ZN4QCss6Parser4initERK7QStringb', css, file)

  @overload(WAIT['QCss.StyleSheet'])
  @overload(NoneType)
  @overload(WAIT['QCss.StyleSheet'], Qt.CaseSensitivity)
  @overload(NoneType, Qt.CaseSensitivity)
  def parse(
      self,
      styleSheet: Optional[QCss.StyleSheet],
      nameCaseSensitivity: Qt.CaseSensitivity = (
          Qt.CaseSensitivity.CaseSensitive),
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parse(StyleSheet *styleSheet,
    Qt::CaseSensitivity nameCaseSensitivity)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parse

    Parameters
    ----------

    styleSheet : Optional[QCss.StyleSheet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nameCaseSensitivity : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QCss::Parser::parse(StyleSheet *styleSheet, Qt::CaseSensitivity
    #      nameCaseSensitivity)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser5parseEPNS_10StyleSheetEN2Qt15CaseSensitivity'
        'E',
        self._addressOf(styleSheet), nameCaseSensitivity.value,
    )

  def errorSymbol(self) -> QCss.Symbol:
    """
    Calls Qt's 'Symbol QCss::Parser::errorSymbol()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#errorSymbol

    Returns
    -------

    QCss.Symbol
      A new cute QCss::Symbol around the copy Qt gave back. Python owns it.
    """
    #  Symbol QCss::Parser::errorSymbol()
    address = self.uglySide.call('ritual_ZN4QCss6Parser11errorSymbolEv')
    return QCss.Symbol._cuteOwning(address)

  @overload(WAIT['QCss.ImportRule'])
  @overload(NoneType)
  def parseImport(self, importRule: Optional[QCss.ImportRule]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseImport(ImportRule *importRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseImport

    Parameters
    ----------

    importRule : Optional[QCss.ImportRule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseImport(ImportRule *importRule)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser11parseImportEPNS_10ImportRuleE',
        self._addressOf(importRule),
    )

  @overload(WAIT['QCss.MediaRule'])
  @overload(NoneType)
  def parseMedia(self, mediaRule: Optional[QCss.MediaRule]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseMedia(MediaRule *mediaRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseMedia

    Parameters
    ----------

    mediaRule : Optional[QCss.MediaRule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseMedia(MediaRule *mediaRule)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser10parseMediaEPNS_9MediaRuleE',
        self._addressOf(mediaRule),
    )

  @overload(WAIT['QCss.PageRule'])
  @overload(NoneType)
  def parsePage(self, pageRule: Optional[QCss.PageRule]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parsePage(PageRule *pageRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parsePage

    Parameters
    ----------

    pageRule : Optional[QCss.PageRule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parsePage(PageRule *pageRule)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser9parsePageEPNS_8PageRuleE',
        self._addressOf(pageRule),
    )

  @overload(QString)
  @overload(NoneType)
  def parsePseudoPage(self, selector: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parsePseudoPage(QString *selector)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parsePseudoPage

    Parameters
    ----------

    selector : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parsePseudoPage(QString *selector)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser15parsePseudoPageEP7QString',
        self._addressOf(selector),
    )

  @overload(WAIT['QCss.Value'])
  @overload(NoneType)
  def parseNextOperator(self, value: Optional[QCss.Value]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseNextOperator(Value *value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseNextOperator

    Parameters
    ----------

    value : Optional[QCss.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseNextOperator(Value *value)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser17parseNextOperatorEPNS_5ValueE',
        self._addressOf(value),
    )

  @overload(WAIT['QCss.AnimationRule'])
  @overload(NoneType)
  def parseAnimation(
      self,
      animationRule: Optional[QCss.AnimationRule],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseAnimation(AnimationRule
    *animationRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseAnimation

    Parameters
    ----------

    animationRule : Optional[QCss.AnimationRule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseAnimation(AnimationRule *animationRule)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser14parseAnimationEPNS_13AnimationRuleE',
        self._addressOf(animationRule),
    )

  @overload(WAIT['QCss.Declaration'])
  @overload(NoneType)
  def parseProperty(self, decl: Optional[QCss.Declaration]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseProperty(Declaration *decl)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseProperty

    Parameters
    ----------

    decl : Optional[QCss.Declaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseProperty(Declaration *decl)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser13parsePropertyEPNS_11DeclarationE',
        self._addressOf(decl),
    )

  @overload(WAIT['QCss.StyleRule'])
  @overload(NoneType)
  def parseRuleset(self, styleRule: Optional[QCss.StyleRule]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseRuleset(StyleRule *styleRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseRuleset

    Parameters
    ----------

    styleRule : Optional[QCss.StyleRule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseRuleset(StyleRule *styleRule)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser12parseRulesetEPNS_9StyleRuleE',
        self._addressOf(styleRule),
    )

  @overload(WAIT['QCss.Selector'])
  @overload(NoneType)
  def parseSelector(self, sel: Optional[QCss.Selector]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseSelector(Selector *sel)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseSelector

    Parameters
    ----------

    sel : Optional[QCss.Selector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseSelector(Selector *sel)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser13parseSelectorEPNS_8SelectorE',
        self._addressOf(sel),
    )

  @overload(WAIT['QCss.BasicSelector'])
  @overload(NoneType)
  def parseSimpleSelector(
      self,
      basicSel: Optional[QCss.BasicSelector],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseSimpleSelector(BasicSelector
    *basicSel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-parser.html#parseSimpleSelector

    Parameters
    ----------

    basicSel : Optional[QCss.BasicSelector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseSimpleSelector(BasicSelector *basicSel)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser19parseSimpleSelectorEPNS_13BasicSelectorE',
        self._addressOf(basicSel),
    )

  @overload(QString)
  @overload(NoneType)
  def parseClass(self, name: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseClass(QString *name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseClass

    Parameters
    ----------

    name : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseClass(QString *name)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser10parseClassEP7QString', self._addressOf(name),
    )

  @overload(QString)
  @overload(NoneType)
  def parseElementName(self, name: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseElementName(QString *name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseElementName

    Parameters
    ----------

    name : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseElementName(QString *name)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser16parseElementNameEP7QString',
        self._addressOf(name),
    )

  @overload(WAIT['QCss.AttributeSelector'])
  @overload(NoneType)
  def parseAttrib(self, attr: Optional[QCss.AttributeSelector]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseAttrib(AttributeSelector *attr)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseAttrib

    Parameters
    ----------

    attr : Optional[QCss.AttributeSelector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseAttrib(AttributeSelector *attr)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser11parseAttribEPNS_17AttributeSelectorE',
        self._addressOf(attr),
    )

  @overload(WAIT['QCss.Pseudo'])
  @overload(NoneType)
  def parsePseudo(self, pseudo: Optional[QCss.Pseudo]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parsePseudo(Pseudo *pseudo)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parsePseudo

    Parameters
    ----------

    pseudo : Optional[QCss.Pseudo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parsePseudo(Pseudo *pseudo)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser11parsePseudoEPNS_6PseudoE',
        self._addressOf(pseudo),
    )

  @overload(WAIT['QCss.Declaration'])
  @overload(NoneType)
  def parseNextDeclaration(
      self,
      declaration: Optional[QCss.Declaration],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseNextDeclaration(Declaration
    *declaration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-parser.html#parseNextDeclaration

    Parameters
    ----------

    declaration : Optional[QCss.Declaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseNextDeclaration(Declaration *declaration)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser20parseNextDeclarationEPNS_11DeclarationE',
        self._addressOf(declaration),
    )

  @overload(WAIT['QCss.Declaration'])
  @overload(NoneType)
  def parsePrio(self, declaration: Optional[QCss.Declaration]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parsePrio(Declaration *declaration)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parsePrio

    Parameters
    ----------

    declaration : Optional[QCss.Declaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parsePrio(Declaration *declaration)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser9parsePrioEPNS_11DeclarationE',
        self._addressOf(declaration),
    )

  @overload(WAIT['QCss.Value'])
  @overload(NoneType)
  def parseTerm(self, value: Optional[QCss.Value]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseTerm(Value *value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseTerm

    Parameters
    ----------

    value : Optional[QCss.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseTerm(Value *value)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser9parseTermEPNS_5ValueE',
        self._addressOf(value),
    )

  @overload(QString, QString)
  @overload(QString, NoneType)
  @overload(NoneType, QString)
  @overload(NoneType, NoneType)
  def parseFunction(
      self,
      name: Optional[QString],
      args: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseFunction(QString *name, QString
    *args)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseFunction

    Parameters
    ----------

    name : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseFunction(QString *name, QString *args)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser13parseFunctionEP7QStringS2_',
        self._addressOf(name), self._addressOf(args),
    )

  @overload(QColor)
  @overload(NoneType)
  def parseHexColor(self, col: Optional[QColor]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseHexColor(QColor *col)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseHexColor

    Parameters
    ----------

    col : Optional[QColor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseHexColor(QColor *col)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser13parseHexColorEP6QColor',
        self._addressOf(col),
    )

  @overload(QString)
  @overload(NoneType)
  def testAndParseUri(self, uri: Optional[QString]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testAndParseUri(QString *uri)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testAndParseUri

    Parameters
    ----------

    uri : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::testAndParseUri(QString *uri)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser15testAndParseUriEP7QString',
        self._addressOf(uri),
    )

  def testRuleset(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testRuleset()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testRuleset
    """
    #  bool QCss::Parser::testRuleset()
    return self.uglySide.call('ritual_ZN4QCss6Parser11testRulesetEv')

  def testSelector(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testSelector()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testSelector
    """
    #  bool QCss::Parser::testSelector()
    return self.uglySide.call('ritual_ZN4QCss6Parser12testSelectorEv')

  @overload(WAIT['QCss.Selector'])
  @overload(NoneType)
  def parseNextSelector(self, sel: Optional[QCss.Selector]) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseNextSelector(Selector *sel)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseNextSelector

    Parameters
    ----------

    sel : Optional[QCss.Selector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseNextSelector(Selector *sel)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser17parseNextSelectorEPNS_8SelectorE',
        self._addressOf(sel),
    )

  def testSimpleSelector(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testSimpleSelector()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-parser.html#testSimpleSelector
    """
    #  bool QCss::Parser::testSimpleSelector()
    return self.uglySide.call('ritual_ZN4QCss6Parser18testSimpleSelectorEv')

  @overload(WAIT['QCss.BasicSelector'])
  @overload(NoneType)
  def parseNextSimpleSelector(
      self,
      basicSel: Optional[QCss.BasicSelector],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseNextSimpleSelector(BasicSelector
    *basicSel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-parser.html#parseNextSimpleSelector

    Parameters
    ----------

    basicSel : Optional[QCss.BasicSelector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseNextSimpleSelector(BasicSelector *basicSel)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser23parseNextSimpleSelectorEPNS_13BasicSelector'
        'E',
        self._addressOf(basicSel),
    )

  def testElementName(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testElementName()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testElementName
    """
    #  bool QCss::Parser::testElementName()
    return self.uglySide.call('ritual_ZN4QCss6Parser15testElementNameEv')

  def testClass(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testClass()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testClass
    """
    #  bool QCss::Parser::testClass()
    return self.uglySide.call('ritual_ZN4QCss6Parser9testClassEv')

  def testAttrib(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testAttrib()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testAttrib
    """
    #  bool QCss::Parser::testAttrib()
    return self.uglySide.call('ritual_ZN4QCss6Parser10testAttribEv')

  def testPseudo(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testPseudo()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testPseudo
    """
    #  bool QCss::Parser::testPseudo()
    return self.uglySide.call('ritual_ZN4QCss6Parser10testPseudoEv')

  def testMedium(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testMedium()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testMedium
    """
    #  bool QCss::Parser::testMedium()
    return self.uglySide.call('ritual_ZN4QCss6Parser10testMediumEv')

  def testPseudoPage(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testPseudoPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testPseudoPage
    """
    #  bool QCss::Parser::testPseudoPage()
    return self.uglySide.call('ritual_ZN4QCss6Parser14testPseudoPageEv')

  def testImport(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testImport()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testImport
    """
    #  bool QCss::Parser::testImport()
    return self.uglySide.call('ritual_ZN4QCss6Parser10testImportEv')

  def testMedia(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testMedia()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testMedia
    """
    #  bool QCss::Parser::testMedia()
    return self.uglySide.call('ritual_ZN4QCss6Parser9testMediaEv')

  def testPage(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testPage
    """
    #  bool QCss::Parser::testPage()
    return self.uglySide.call('ritual_ZN4QCss6Parser8testPageEv')

  def testAnimation(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testAnimation()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testAnimation
    """
    #  bool QCss::Parser::testAnimation()
    return self.uglySide.call('ritual_ZN4QCss6Parser13testAnimationEv')

  def testCombinator(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testCombinator()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testCombinator
    """
    #  bool QCss::Parser::testCombinator()
    return self.uglySide.call('ritual_ZN4QCss6Parser14testCombinatorEv')

  def testProperty(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testProperty()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testProperty
    """
    #  bool QCss::Parser::testProperty()
    return self.uglySide.call('ritual_ZN4QCss6Parser12testPropertyEv')

  def testTerm(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testTerm()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testTerm
    """
    #  bool QCss::Parser::testTerm()
    return self.uglySide.call('ritual_ZN4QCss6Parser8testTermEv')

  def testExpr(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testExpr()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testExpr
    """
    #  bool QCss::Parser::testExpr()
    return self.uglySide.call('ritual_ZN4QCss6Parser8testExprEv')

  def testPrio(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testPrio()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testPrio
    """
    #  bool QCss::Parser::testPrio()
    return self.uglySide.call('ritual_ZN4QCss6Parser8testPrioEv')

  def testHexColor(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testHexColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testHexColor
    """
    #  bool QCss::Parser::testHexColor()
    return self.uglySide.call('ritual_ZN4QCss6Parser12testHexColorEv')

  def testFunction(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testFunction()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#testFunction
    """
    #  bool QCss::Parser::testFunction()
    return self.uglySide.call('ritual_ZN4QCss6Parser12testFunctionEv')

  @overload(QString, QString)
  @overload(QString, NoneType)
  @overload(NoneType, QString)
  @overload(NoneType, NoneType)
  def parseNextFunction(
      self,
      name: Optional[QString],
      args: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::parseNextFunction(QString *name, QString
    *args)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#parseNextFunction

    Parameters
    ----------

    name : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCss::Parser::parseNextFunction(QString *name, QString *args)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser17parseNextFunctionEP7QStringS2_',
        self._addressOf(name), self._addressOf(args),
    )

  def skipSpace(self) -> None:
    """
    Calls Qt's 'void QCss::Parser::skipSpace()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#skipSpace
    """
    #  void QCss::Parser::skipSpace()
    self.uglySide.call('ritual_ZN4QCss6Parser9skipSpaceEv')

  @overload()
  def next(self) -> QCss.TokenType:
    """
    Calls Qt's 'TokenType QCss::Parser::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#next

    Returns
    -------

    QCss.TokenType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCss.TokenType(number)'
      gives.
    """
    #  TokenType QCss::Parser::next()
    return QCss.TokenType(self.uglySide.call('ritual_ZN4QCss6Parser4nextEv'))

  @overload(QCss.TokenType)
  def next(self, t: QCss.TokenType) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::next(TokenType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#next

    Parameters
    ----------

    t : QCss.TokenType
      Passed on as its number.
    """
    #  bool QCss::Parser::next(TokenType t)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser4nextENS_9TokenTypeE', t.value,
    )

  @overload(QCss.TokenType)
  def test(self, t: QCss.TokenType) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::test(TokenType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#test

    Parameters
    ----------

    t : QCss.TokenType
      Passed on as its number.
    """
    #  bool QCss::Parser::test(TokenType t)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser4testENS_9TokenTypeE', t.value,
    )

  def prev(self) -> None:
    """
    Calls Qt's 'void QCss::Parser::prev()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#prev
    """
    #  void QCss::Parser::prev()
    self.uglySide.call('ritual_ZN4QCss6Parser4prevEv')

  @overload(QCss.TokenType)
  def lexemUntil(self, t: QCss.TokenType) -> str:
    """
    Calls Qt's 'QString QCss::Parser::lexemUntil(TokenType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#lexemUntil

    Parameters
    ----------

    t : QCss.TokenType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCss::Parser::lexemUntil(TokenType t)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser10lexemUntilENS_9TokenTypeE', t.value,
    )

  @overload(QCss.TokenType)
  @overload(QCss.TokenType, QCss.TokenType)
  def until(
      self,
      target: QCss.TokenType,
      target2: QCss.TokenType = QCss.TokenType.NONE,
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::until(TokenType target, TokenType
    target2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#until

    Parameters
    ----------

    target : QCss.TokenType
      Passed on as its number.

    target2 : QCss.TokenType
      Passed on as its number. May be left out, as in Qt: it is then
      QCss.TokenType.NONE.
    """
    #  bool QCss::Parser::until(TokenType target, TokenType target2)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser5untilENS_9TokenTypeES1_',
        target.value, target2.value,
    )

  @overload(QCss.TokenType, QLatin1String)
  def testTokenAndEndsWith(
      self,
      t: QCss.TokenType,
      str: QLatin1String,
  ) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::testTokenAndEndsWith(TokenType t,
    QLatin1StringView str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcss-parser.html#testTokenAndEndsWith

    Parameters
    ----------

    t : QCss.TokenType
      Passed on as its number.

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool QCss::Parser::testTokenAndEndsWith(TokenType t, QLatin1StringView
    #      str)
    return self.uglySide.call(
        'ritual_ZN4QCss6Parser20testTokenAndEndsWithENS_9TokenTypeE13QLatin'
        '1String',
        t.value, self._valueOf(str),
    )

  def recordError(self) -> bool:
    """
    Calls Qt's 'bool QCss::Parser::recordError()'.

    Qt's own words: https://doc.qt.io/qt-6/qcss-parser.html#recordError
    """
    #  bool QCss::Parser::recordError()
    return self.uglySide.call('ritual_ZN4QCss6Parser11recordErrorEv')

  @staticmethod
  def parseCombinator(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Parser::parseCombinator(BasicSelector::Relation
    *relation)': names 'QCss::BasicSelector::Relation', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QCss.Parser.parseCombinator' has no cute function yet. Qt's 'bool "
        "QCss::Parser::parseCombinator(BasicSelector::Relation *relation)': "
        "names 'QCss::BasicSelector::Relation', which has no cute class yet."
    )

  @staticmethod
  def parseExpr(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Parser::parseExpr(QList<Value> *values)': names
    'QList<QCss::Value>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCss.Parser.parseExpr' has no cute function yet. Qt's 'bool "
        "QCss::Parser::parseExpr(QList<Value> *values)': names "
        "'QList<QCss::Value>', which has no cute class yet.")

  @staticmethod
  def parseMedium(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Parser::parseMedium(QStringList *media)': names
    'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCss.Parser.parseMedium' has no cute function yet. Qt's 'bool "
        "QCss::Parser::parseMedium(QStringList *media)': names "
        "'QStringList', which has no cute class yet.")

  @staticmethod
  def parseNextExpr(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Parser::parseNextExpr(QList<Value> *values)': names
    'QList<QCss::Value>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCss.Parser.parseNextExpr' has no cute function yet. Qt's 'bool "
        "QCss::Parser::parseNextExpr(QList<Value> *values)': names "
        "'QList<QCss::Value>', which has no cute class yet.")

  @staticmethod
  def parseNextMedium(*__, **_) -> Never:
    """
    Qt's 'bool QCss::Parser::parseNextMedium(QStringList *media)': names
    'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCss.Parser.parseNextMedium' has no cute function yet. Qt's 'bool "
        "QCss::Parser::parseNextMedium(QStringList *media)': names "
        "'QStringList', which has no cute class yet.")
