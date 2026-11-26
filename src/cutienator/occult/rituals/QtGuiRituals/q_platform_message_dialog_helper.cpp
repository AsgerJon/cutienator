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

//  void *QPlatformMessageDialogHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QPlatformMessageDialogHelper11qt_metacastEPKc(
    QPlatformMessageDialogHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformMessageDialogHelper::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QPlatformMessageDialogHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformMessageDialogHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  const QSharedPointer<QMessageDialogOptions>
//      &QPlatformMessageDialogHelper::options() const
extern "C" Q_DECL_EXPORT
const QSharedPointer<QMessageDialogOptions> *ritual_ZNK28QPlatformMessageDialogHelper7optionsEv(
    const QPlatformMessageDialogHelper *self) {
  return &(self->options());
}

//  void QPlatformMessageDialogHelper::setOptions(const
//      QSharedPointer<QMessageDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMessageDialogHelper10setOptionsERK14QSharedPointerI21QMessageDialogOptionsE(
    QPlatformMessageDialogHelper *self,
    const QSharedPointer<QMessageDialogOptions> *options) {
  self->setOptions(*options);
}

//  void QPlatformMessageDialogHelper::clicked(QPlatformDialogHelper::Standar
//      dButton button, QPlatformDialogHelper::ButtonRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMessageDialogHelper7clickedEN21QPlatformDialogHelper14StandardButtonENS0_10ButtonRoleE(
    QPlatformMessageDialogHelper *self,
    QPlatformDialogHelper::StandardButton button,
    QPlatformDialogHelper::ButtonRole role) {
  self->clicked(button, role);
}

//  void QPlatformMessageDialogHelper::checkBoxStateChanged(Qt::CheckState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformMessageDialogHelper20checkBoxStateChangedEN2Qt10CheckStateE(
    QPlatformMessageDialogHelper *self,
    Qt::CheckState state) {
  self->checkBoxStateChanged(state);
}
