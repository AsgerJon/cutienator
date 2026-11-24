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

//  bool QCss::Parser::testExpr()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QCss6Parser8testExprEv(QCss::Parser *self) {
  return self->testExpr();
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

//  TokenType QCss::Parser::lookup() const
extern "C" Q_DECL_EXPORT
QCss::TokenType ritual_ZNK4QCss6Parser6lookupEv(const QCss::Parser *self) {
  return self->lookup();
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
