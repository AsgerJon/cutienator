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

//  void *qdesigner_internal::CssHighlighter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14CssHighlighter11qt_metacastEPKc(
    qdesigner_internal::CssHighlighter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::CssHighlighter::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14CssHighlighter11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::CssHighlighter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  qdesigner_internal::CssHighlighter::CssHighlighter(const
//      CssHighlightColors &colors, QTextDocument *document)
extern "C" Q_DECL_EXPORT
qdesigner_internal::CssHighlighter *ritual_ZN18qdesigner_internal14CssHighlighterC1ERKNS_18CssHighlightColorsEP13QTextDocument(
    const qdesigner_internal::CssHighlightColors *colors,
    QTextDocument *document) {
  return new qdesigner_internal::CssHighlighter(*colors, document);
}

//  void qdesigner_internal::CssHighlighter::highlightBlock(const QString
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14CssHighlighter14highlightBlockERK7QString(
    qdesigner_internal::CssHighlighter *self,
    const QString *a0) {
  self->highlightBlock(*a0);
}

//  void qdesigner_internal::CssHighlighter::highlight(const QString &a0, int
//      a1, int a2, int a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14CssHighlighter9highlightERK7QStringiii(
    qdesigner_internal::CssHighlighter *self,
    const QString *a0,
    int a1,
    int a2,
    int a3) {
  self->highlight(*a0, a1, a2, a3);
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
