//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *qdesigner_internal::DesignerIconCache::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17DesignerIconCache10metaObjectEv(
    const qdesigner_internal::DesignerIconCache *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::DesignerIconCache::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17DesignerIconCache2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::DesignerIconCache::tr(s, c, n));
}
