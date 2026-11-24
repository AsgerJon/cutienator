//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/csshighlighter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/csshighlighter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on qdesigner_internal::CssHighlighter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_CssHighlighter : qdesigner_internal::CssHighlighter {
  using qdesigner_internal::CssHighlighter::highlightBlock;
};

//  const QMetaObject *qdesigner_internal::CssHighlighter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14CssHighlighter10metaObjectEv(
    const qdesigner_internal::CssHighlighter *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::CssHighlighter::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14CssHighlighter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::CssHighlighter::tr(s, c, n));
}

//  void qdesigner_internal::CssHighlighter::highlightBlock(const QString
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14CssHighlighter14highlightBlockERK7QString(
    qdesigner_internal::CssHighlighter *self,
    const QString *a0) {
  static_cast<Ownqdesigner_internal_CssHighlighter *>(self)->Ownqdesigner_internal_CssHighlighter::highlightBlock(
      *a0);
}
