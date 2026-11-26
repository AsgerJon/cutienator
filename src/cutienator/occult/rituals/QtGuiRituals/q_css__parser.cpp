//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(cssparser)
#if !defined(QT_NO_CSSPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>

//  QCss::Parser::Parser()
extern "C" Q_DECL_EXPORT
QCss::Parser *ritual_ZN4QCss6ParserC1Ev() {
  return new QCss::Parser();
}

//  QCss::Parser::Parser(const QString &css, bool file)
extern "C" Q_DECL_EXPORT
QCss::Parser *ritual_ZN4QCss6ParserC1ERK7QStringb(
    const QString *css,
    bool file) {
  return new QCss::Parser(*css, file);
}

//  void QCss::Parser::init(const QString &css, bool file)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss6Parser4initERK7QStringb(
    QCss::Parser *self,
    const QString *css,
    bool file) {
  self->init(*css, file);
}

//  bool QCss::Parser::parse(StyleSheet *styleSheet, Qt::CaseSensitivity
//      nameCaseSensitivity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser5parseEPNS_10StyleSheetEN2Qt15CaseSensitivityE(
    QCss::Parser *self,
    QCss::StyleSheet *styleSheet,
    Qt::CaseSensitivity nameCaseSensitivity) {
  return self->parse(styleSheet, nameCaseSensitivity);
}

//  Symbol QCss::Parser::errorSymbol()
extern "C" Q_DECL_EXPORT
QCss::Symbol *ritual_ZN4QCss6Parser11errorSymbolEv(QCss::Parser *self) {
  return new QCss::Symbol(self->errorSymbol());
}

//  bool QCss::Parser::parseImport(ImportRule *importRule)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser11parseImportEPNS_10ImportRuleE(
    QCss::Parser *self,
    QCss::ImportRule *importRule) {
  return self->parseImport(importRule);
}

//  bool QCss::Parser::parseMedia(MediaRule *mediaRule)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser10parseMediaEPNS_9MediaRuleE(
    QCss::Parser *self,
    QCss::MediaRule *mediaRule) {
  return self->parseMedia(mediaRule);
}

//  bool QCss::Parser::parseMedium(QStringList *media)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser11parseMediumEP5QListI7QStringE(
    QCss::Parser *self,
    QStringList *media) {
  return self->parseMedium(media);
}

//  bool QCss::Parser::parsePage(PageRule *pageRule)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser9parsePageEPNS_8PageRuleE(
    QCss::Parser *self,
    QCss::PageRule *pageRule) {
  return self->parsePage(pageRule);
}

//  bool QCss::Parser::parsePseudoPage(QString *selector)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser15parsePseudoPageEP7QString(
    QCss::Parser *self,
    QString *selector) {
  return self->parsePseudoPage(selector);
}

//  bool QCss::Parser::parseNextOperator(Value *value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser17parseNextOperatorEPNS_5ValueE(
    QCss::Parser *self,
    QCss::Value *value) {
  return self->parseNextOperator(value);
}

//  bool QCss::Parser::parseAnimation(AnimationRule *animationRule)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser14parseAnimationEPNS_13AnimationRuleE(
    QCss::Parser *self,
    QCss::AnimationRule *animationRule) {
  return self->parseAnimation(animationRule);
}

//  bool QCss::Parser::parseCombinator(BasicSelector::Relation *relation)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser15parseCombinatorEPNS_13BasicSelector8RelationE(
    QCss::Parser *self,
    QCss::BasicSelector::Relation *relation) {
  return self->parseCombinator(relation);
}

//  bool QCss::Parser::parseProperty(Declaration *decl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser13parsePropertyEPNS_11DeclarationE(
    QCss::Parser *self,
    QCss::Declaration *decl) {
  return self->parseProperty(decl);
}

//  bool QCss::Parser::parseRuleset(StyleRule *styleRule)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser12parseRulesetEPNS_9StyleRuleE(
    QCss::Parser *self,
    QCss::StyleRule *styleRule) {
  return self->parseRuleset(styleRule);
}

//  bool QCss::Parser::parseSelector(Selector *sel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser13parseSelectorEPNS_8SelectorE(
    QCss::Parser *self,
    QCss::Selector *sel) {
  return self->parseSelector(sel);
}

//  bool QCss::Parser::parseSimpleSelector(BasicSelector *basicSel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser19parseSimpleSelectorEPNS_13BasicSelectorE(
    QCss::Parser *self,
    QCss::BasicSelector *basicSel) {
  return self->parseSimpleSelector(basicSel);
}

//  bool QCss::Parser::parseClass(QString *name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser10parseClassEP7QString(
    QCss::Parser *self,
    QString *name) {
  return self->parseClass(name);
}

//  bool QCss::Parser::parseElementName(QString *name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser16parseElementNameEP7QString(
    QCss::Parser *self,
    QString *name) {
  return self->parseElementName(name);
}

//  bool QCss::Parser::parseAttrib(AttributeSelector *attr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser11parseAttribEPNS_17AttributeSelectorE(
    QCss::Parser *self,
    QCss::AttributeSelector *attr) {
  return self->parseAttrib(attr);
}

//  bool QCss::Parser::parsePseudo(Pseudo *pseudo)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser11parsePseudoEPNS_6PseudoE(
    QCss::Parser *self,
    QCss::Pseudo *pseudo) {
  return self->parsePseudo(pseudo);
}

//  bool QCss::Parser::parseNextDeclaration(Declaration *declaration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser20parseNextDeclarationEPNS_11DeclarationE(
    QCss::Parser *self,
    QCss::Declaration *declaration) {
  return self->parseNextDeclaration(declaration);
}

//  bool QCss::Parser::parsePrio(Declaration *declaration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser9parsePrioEPNS_11DeclarationE(
    QCss::Parser *self,
    QCss::Declaration *declaration) {
  return self->parsePrio(declaration);
}

//  bool QCss::Parser::parseExpr(QList<Value> *values)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser9parseExprEP5QListINS_5ValueEE(
    QCss::Parser *self,
    QList<QCss::Value> *values) {
  return self->parseExpr(values);
}

//  bool QCss::Parser::parseTerm(Value *value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser9parseTermEPNS_5ValueE(
    QCss::Parser *self,
    QCss::Value *value) {
  return self->parseTerm(value);
}

//  bool QCss::Parser::parseFunction(QString *name, QString *args)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser13parseFunctionEP7QStringS2_(
    QCss::Parser *self,
    QString *name,
    QString *args) {
  return self->parseFunction(name, args);
}

//  bool QCss::Parser::parseHexColor(QColor *col)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser13parseHexColorEP6QColor(
    QCss::Parser *self,
    QColor *col) {
  return self->parseHexColor(col);
}

//  bool QCss::Parser::testAndParseUri(QString *uri)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser15testAndParseUriEP7QString(
    QCss::Parser *self,
    QString *uri) {
  return self->testAndParseUri(uri);
}

//  bool QCss::Parser::testRuleset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser11testRulesetEv(QCss::Parser *self) {
  return self->testRuleset();
}

//  bool QCss::Parser::testSelector()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser12testSelectorEv(QCss::Parser *self) {
  return self->testSelector();
}

//  bool QCss::Parser::parseNextSelector(Selector *sel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser17parseNextSelectorEPNS_8SelectorE(
    QCss::Parser *self,
    QCss::Selector *sel) {
  return self->parseNextSelector(sel);
}

//  bool QCss::Parser::testSimpleSelector()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser18testSimpleSelectorEv(QCss::Parser *self) {
  return self->testSimpleSelector();
}

//  bool QCss::Parser::parseNextSimpleSelector(BasicSelector *basicSel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser23parseNextSimpleSelectorEPNS_13BasicSelectorE(
    QCss::Parser *self,
    QCss::BasicSelector *basicSel) {
  return self->parseNextSimpleSelector(basicSel);
}

//  bool QCss::Parser::testElementName()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser15testElementNameEv(QCss::Parser *self) {
  return self->testElementName();
}

//  bool QCss::Parser::testClass()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser9testClassEv(QCss::Parser *self) {
  return self->testClass();
}

//  bool QCss::Parser::testAttrib()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser10testAttribEv(QCss::Parser *self) {
  return self->testAttrib();
}

//  bool QCss::Parser::testPseudo()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser10testPseudoEv(QCss::Parser *self) {
  return self->testPseudo();
}

//  bool QCss::Parser::testMedium()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser10testMediumEv(QCss::Parser *self) {
  return self->testMedium();
}

//  bool QCss::Parser::parseNextMedium(QStringList *media)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser15parseNextMediumEP5QListI7QStringE(
    QCss::Parser *self,
    QStringList *media) {
  return self->parseNextMedium(media);
}

//  bool QCss::Parser::testPseudoPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser14testPseudoPageEv(QCss::Parser *self) {
  return self->testPseudoPage();
}

//  bool QCss::Parser::testImport()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser10testImportEv(QCss::Parser *self) {
  return self->testImport();
}

//  bool QCss::Parser::testMedia()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser9testMediaEv(QCss::Parser *self) {
  return self->testMedia();
}

//  bool QCss::Parser::testPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser8testPageEv(QCss::Parser *self) {
  return self->testPage();
}

//  bool QCss::Parser::testAnimation()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser13testAnimationEv(QCss::Parser *self) {
  return self->testAnimation();
}

//  bool QCss::Parser::testCombinator()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser14testCombinatorEv(QCss::Parser *self) {
  return self->testCombinator();
}

//  bool QCss::Parser::testProperty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser12testPropertyEv(QCss::Parser *self) {
  return self->testProperty();
}

//  bool QCss::Parser::testTerm()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser8testTermEv(QCss::Parser *self) {
  return self->testTerm();
}

//  bool QCss::Parser::testExpr()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser8testExprEv(QCss::Parser *self) {
  return self->testExpr();
}

//  bool QCss::Parser::parseNextExpr(QList<Value> *values)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser13parseNextExprEP5QListINS_5ValueEE(
    QCss::Parser *self,
    QList<QCss::Value> *values) {
  return self->parseNextExpr(values);
}

//  bool QCss::Parser::testPrio()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser8testPrioEv(QCss::Parser *self) {
  return self->testPrio();
}

//  bool QCss::Parser::testHexColor()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser12testHexColorEv(QCss::Parser *self) {
  return self->testHexColor();
}

//  bool QCss::Parser::testFunction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser12testFunctionEv(QCss::Parser *self) {
  return self->testFunction();
}

//  bool QCss::Parser::parseNextFunction(QString *name, QString *args)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser17parseNextFunctionEP7QStringS2_(
    QCss::Parser *self,
    QString *name,
    QString *args) {
  return self->parseNextFunction(name, args);
}

//  bool QCss::Parser::lookupElementName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss6Parser17lookupElementNameEv(const QCss::Parser *self) {
  return self->lookupElementName();
}

//  void QCss::Parser::skipSpace()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss6Parser9skipSpaceEv(QCss::Parser *self) {
  self->skipSpace();
}

//  bool QCss::Parser::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss6Parser7hasNextEv(const QCss::Parser *self) {
  return self->hasNext();
}

//  TokenType QCss::Parser::next()
extern "C" Q_DECL_EXPORT
QCss::TokenType ritual_ZN4QCss6Parser4nextEv(QCss::Parser *self) {
  return self->next();
}

//  bool QCss::Parser::next(TokenType t)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser4nextENS_9TokenTypeE(
    QCss::Parser *self,
    QCss::TokenType t) {
  return self->next(t);
}

//  bool QCss::Parser::test(TokenType t)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser4testENS_9TokenTypeE(
    QCss::Parser *self,
    QCss::TokenType t) {
  return self->test(t);
}

//  void QCss::Parser::prev()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss6Parser4prevEv(QCss::Parser *self) {
  self->prev();
}

//  const Symbol &QCss::Parser::symbol() const
extern "C" Q_DECL_EXPORT
QCss::Symbol *ritual_ZNK4QCss6Parser6symbolEv(const QCss::Parser *self) {
  return new QCss::Symbol(self->symbol());
}

//  QString QCss::Parser::lexem() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QCss6Parser5lexemEv(const QCss::Parser *self) {
  return new QString(self->lexem());
}

//  QString QCss::Parser::unquotedLexem() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QCss6Parser13unquotedLexemEv(const QCss::Parser *self) {
  return new QString(self->unquotedLexem());
}

//  QString QCss::Parser::lexemUntil(TokenType t)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QCss6Parser10lexemUntilENS_9TokenTypeE(
    QCss::Parser *self,
    QCss::TokenType t) {
  return new QString(self->lexemUntil(t));
}

//  bool QCss::Parser::until(TokenType target, TokenType target2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser5untilENS_9TokenTypeES1_(
    QCss::Parser *self,
    QCss::TokenType target,
    QCss::TokenType target2) {
  return self->until(target, target2);
}

//  TokenType QCss::Parser::lookup() const
extern "C" Q_DECL_EXPORT
QCss::TokenType ritual_ZNK4QCss6Parser6lookupEv(const QCss::Parser *self) {
  return self->lookup();
}

//  bool QCss::Parser::testTokenAndEndsWith(TokenType t, QLatin1StringView
//      str)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser20testTokenAndEndsWithENS_9TokenTypeE13QLatin1String(
    QCss::Parser *self,
    QCss::TokenType t,
    const QLatin1String *str) {
  return self->testTokenAndEndsWith(t, *str);
}

//  bool QCss::Parser::recordError()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser11recordErrorEv(QCss::Parser *self) {
  return self->recordError();
}

//  QCss::Parser::~Parser()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss6ParserD1Ev(QCss::Parser *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
