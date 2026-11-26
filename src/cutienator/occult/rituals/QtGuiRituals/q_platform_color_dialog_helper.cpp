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

//  void *QPlatformColorDialogHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QPlatformColorDialogHelper11qt_metacastEPKc(
    QPlatformColorDialogHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformColorDialogHelper::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QPlatformColorDialogHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformColorDialogHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  const QSharedPointer<QColorDialogOptions>
//      &QPlatformColorDialogHelper::options() const
extern "C" Q_DECL_EXPORT
const QSharedPointer<QColorDialogOptions> *ritual_ZNK26QPlatformColorDialogHelper7optionsEv(
    const QPlatformColorDialogHelper *self) {
  return &(self->options());
}

//  void QPlatformColorDialogHelper::setOptions(const
//      QSharedPointer<QColorDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformColorDialogHelper10setOptionsERK14QSharedPointerI19QColorDialogOptionsE(
    QPlatformColorDialogHelper *self,
    const QSharedPointer<QColorDialogOptions> *options) {
  self->setOptions(*options);
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

//  void QPlatformColorDialogHelper::currentColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformColorDialogHelper19currentColorChangedERK6QColor(
    QPlatformColorDialogHelper *self,
    const QColor *color) {
  self->currentColorChanged(*color);
}

//  void QPlatformColorDialogHelper::colorSelected(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformColorDialogHelper13colorSelectedERK6QColor(
    QPlatformColorDialogHelper *self,
    const QColor *color) {
  self->colorSelected(*color);
}
