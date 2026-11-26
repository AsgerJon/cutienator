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

//  QString QCss::Scanner::preprocess(const QString &input, bool
//      *hasEscapeSequences)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN4QCss7Scanner10preprocessERK7QStringPb(
    const QString *input,
    bool *hasEscapeSequences) {
  return new QString(QCss::Scanner::preprocess(*input, hasEscapeSequences));
}

//  void QCss::Scanner::scan(const QString &preprocessedInput, QList<Symbol>
//      *symbols)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss7Scanner4scanERK7QStringP5QListINS_6SymbolEE(
    const QString *preprocessedInput,
    QList<QCss::Symbol> *symbols) {
  QCss::Scanner::scan(*preprocessedInput, symbols);
}

//  QCss::Scanner::~Scanner()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss7ScannerD1Ev(QCss::Scanner *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
