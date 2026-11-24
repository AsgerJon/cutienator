//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QPlatformColorDialogHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QPlatformColorDialogHelper10metaObjectEv(
    const QPlatformColorDialogHelper *self) {
  return self->metaObject();
}

//  QString QPlatformColorDialogHelper::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QPlatformColorDialogHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformColorDialogHelper::tr(s, c, n));
}

//  void QPlatformColorDialogHelper::setCurrentColor(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformColorDialogHelper15setCurrentColorERK6QColor(
    QPlatformColorDialogHelper *self,
    const QColor *a0) {
  self->setCurrentColor(*a0);
}

//  QColor QPlatformColorDialogHelper::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QPlatformColorDialogHelper12currentColorEv(
    const QPlatformColorDialogHelper *self) {
  return new QColor(self->currentColor());
}
