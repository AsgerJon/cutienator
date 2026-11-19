//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsyntaxhighlighter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qsyntaxhighlighter.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextobject.h>

//  const QMetaObject *QSyntaxHighlighter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSyntaxHighlighter10metaObjectEv(
    const QSyntaxHighlighter *self) {
  return self->metaObject();
}

//  QString QSyntaxHighlighter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSyntaxHighlighter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSyntaxHighlighter::tr(s, c, n));
}

//  QSyntaxHighlighter::~QSyntaxHighlighter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighterD1Ev(QSyntaxHighlighter *self) {
  delete self;
}

//  void QSyntaxHighlighter::setDocument(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter11setDocumentEP13QTextDocument(
    QSyntaxHighlighter *self,
    QTextDocument *doc) {
  self->setDocument(doc);
}

//  QTextDocument *QSyntaxHighlighter::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK18QSyntaxHighlighter8documentEv(
    const QSyntaxHighlighter *self) {
  return self->document();
}

//  void QSyntaxHighlighter::rehighlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter11rehighlightEv(QSyntaxHighlighter *self) {
  self->rehighlight();
}

//  void QSyntaxHighlighter::rehighlightBlock(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSyntaxHighlighter16rehighlightBlockERK10QTextBlock(
    QSyntaxHighlighter *self,
    const QTextBlock *block) {
  self->rehighlightBlock(*block);
}
