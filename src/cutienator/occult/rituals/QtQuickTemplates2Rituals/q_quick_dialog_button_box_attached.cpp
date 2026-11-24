//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickDialogButtonBoxAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickDialogButtonBoxAttached10metaObjectEv(
    const QQuickDialogButtonBoxAttached *self) {
  return self->metaObject();
}

//  QString QQuickDialogButtonBoxAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickDialogButtonBoxAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDialogButtonBoxAttached::tr(s, c, n));
}

//  QQuickDialogButtonBoxAttached::QQuickDialogButtonBoxAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxAttached *ritual_ZN29QQuickDialogButtonBoxAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickDialogButtonBoxAttached(parent);
}

//  QQuickDialogButtonBox *QQuickDialogButtonBoxAttached::buttonBox() const
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox *ritual_ZNK29QQuickDialogButtonBoxAttached9buttonBoxEv(
    const QQuickDialogButtonBoxAttached *self) {
  return self->buttonBox();
}

//  QPlatformDialogHelper::ButtonRole
//      QQuickDialogButtonBoxAttached::buttonRole() const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper::ButtonRole ritual_ZNK29QQuickDialogButtonBoxAttached10buttonRoleEv(
    const QQuickDialogButtonBoxAttached *self) {
  return self->buttonRole();
}

//  void QQuickDialogButtonBoxAttached::setButtonRole(QPlatformDialogHelper::
//      ButtonRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickDialogButtonBoxAttached13setButtonRoleEN21QPlatformDialogHelper10ButtonRoleE(
    QQuickDialogButtonBoxAttached *self,
    QPlatformDialogHelper::ButtonRole role) {
  self->setButtonRole(role);
}

//  QQuickDialogButtonBoxAttachedPrivate
//      *QQuickDialogButtonBoxAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxAttachedPrivate *ritual_ZN29QQuickDialogButtonBoxAttached6d_funcEv(
    QQuickDialogButtonBoxAttached *self) {
  return self->d_func();
}

//  const QQuickDialogButtonBoxAttachedPrivate
//      *QQuickDialogButtonBoxAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialogButtonBoxAttachedPrivate *ritual_ZNK29QQuickDialogButtonBoxAttached6d_funcEv(
    const QQuickDialogButtonBoxAttached *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quicktemplates2_container)
#endif  // QT_CONFIG(quicktemplates2_container)
