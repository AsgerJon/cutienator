//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QPlatformMessageDialogHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QPlatformMessageDialogHelper10metaObjectEv(
    const QPlatformMessageDialogHelper *self) {
  return self->metaObject();
}

//  QString QPlatformMessageDialogHelper::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QPlatformMessageDialogHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMessageDialogHelper::tr(s, c, n));
}
