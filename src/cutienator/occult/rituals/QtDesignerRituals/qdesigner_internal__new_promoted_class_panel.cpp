//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *qdesigner_internal::NewPromotedClassPanel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal21NewPromotedClassPanel10metaObjectEv(
    const qdesigner_internal::NewPromotedClassPanel *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::NewPromotedClassPanel::promotedHeaderSuffix()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal21NewPromotedClassPanel20promotedHeaderSuffixEv(
    const qdesigner_internal::NewPromotedClassPanel *self) {
  return new QString(self->promotedHeaderSuffix());
}

//  void
//      qdesigner_internal::NewPromotedClassPanel::setPromotedHeaderSuffix(co
//      nst QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel23setPromotedHeaderSuffixERK7QString(
    qdesigner_internal::NewPromotedClassPanel *self,
    const QString *s) {
  self->setPromotedHeaderSuffix(*s);
}

//  bool
//      qdesigner_internal::NewPromotedClassPanel::isPromotedHeaderLowerCase(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal21NewPromotedClassPanel25isPromotedHeaderLowerCaseEv(
    const qdesigner_internal::NewPromotedClassPanel *self) {
  return self->isPromotedHeaderLowerCase();
}

//  void qdesigner_internal::NewPromotedClassPanel::setPromotedHeaderLowerCas
//      e(bool l)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal21NewPromotedClassPanel26setPromotedHeaderLowerCaseEb(
    qdesigner_internal::NewPromotedClassPanel *self,
    bool l) {
  self->setPromotedHeaderLowerCase(l);
}
