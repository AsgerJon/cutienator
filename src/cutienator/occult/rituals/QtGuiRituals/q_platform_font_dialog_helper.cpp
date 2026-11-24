//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QPlatformFontDialogHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QPlatformFontDialogHelper10metaObjectEv(
    const QPlatformFontDialogHelper *self) {
  return self->metaObject();
}

//  QString QPlatformFontDialogHelper::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QPlatformFontDialogHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformFontDialogHelper::tr(s, c, n));
}

//  void QPlatformFontDialogHelper::setCurrentFont(const QFont &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFontDialogHelper14setCurrentFontERK5QFont(
    QPlatformFontDialogHelper *self,
    const QFont *a0) {
  self->setCurrentFont(*a0);
}

//  QFont QPlatformFontDialogHelper::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK25QPlatformFontDialogHelper11currentFontEv(
    const QPlatformFontDialogHelper *self) {
  return new QFont(self->currentFont());
}
