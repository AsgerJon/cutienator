//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/htmlhighlighter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/htmlhighlighter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>

//  const QMetaObject *qdesigner_internal::HtmlHighlighter::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal15HtmlHighlighter10metaObjectEv(
    const qdesigner_internal::HtmlHighlighter *self) {
  return self->metaObject();
}

//  QTextCharFormat qdesigner_internal::HtmlHighlighter::formatFor(Construct
//      construct) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK18qdesigner_internal15HtmlHighlighter9formatForENS0_9ConstructE(
    const qdesigner_internal::HtmlHighlighter *self,
    qdesigner_internal::HtmlHighlighter::Construct construct) {
  return new QTextCharFormat(self->formatFor(construct));
}
