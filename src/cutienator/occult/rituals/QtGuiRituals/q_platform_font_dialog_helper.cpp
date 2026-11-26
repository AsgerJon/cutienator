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

//  void *QPlatformFontDialogHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QPlatformFontDialogHelper11qt_metacastEPKc(
    QPlatformFontDialogHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformFontDialogHelper::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QPlatformFontDialogHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformFontDialogHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  const QSharedPointer<QFontDialogOptions>
//      &QPlatformFontDialogHelper::options() const
extern "C" Q_DECL_EXPORT
const QSharedPointer<QFontDialogOptions> *ritual_ZNK25QPlatformFontDialogHelper7optionsEv(
    const QPlatformFontDialogHelper *self) {
  return &(self->options());
}

//  void QPlatformFontDialogHelper::setOptions(const
//      QSharedPointer<QFontDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFontDialogHelper10setOptionsERK14QSharedPointerI18QFontDialogOptionsE(
    QPlatformFontDialogHelper *self,
    const QSharedPointer<QFontDialogOptions> *options) {
  self->setOptions(*options);
}

//  void QPlatformFontDialogHelper::currentFontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFontDialogHelper18currentFontChangedERK5QFont(
    QPlatformFontDialogHelper *self,
    const QFont *font) {
  self->currentFontChanged(*font);
}

//  void QPlatformFontDialogHelper::fontSelected(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFontDialogHelper12fontSelectedERK5QFont(
    QPlatformFontDialogHelper *self,
    const QFont *font) {
  self->fontSelected(*font);
}
