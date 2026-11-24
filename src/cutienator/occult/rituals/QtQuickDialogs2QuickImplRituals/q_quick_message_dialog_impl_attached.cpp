//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimp
//  l_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickMessageDialogImplAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickMessageDialogImplAttached10metaObjectEv(
    const QQuickMessageDialogImplAttached *self) {
  return self->metaObject();
}

//  QString QQuickMessageDialogImplAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickMessageDialogImplAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMessageDialogImplAttached::tr(s, c, n));
}

//  QQuickMessageDialogImplAttached::QQuickMessageDialogImplAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplAttached *ritual_ZN31QQuickMessageDialogImplAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickMessageDialogImplAttached(parent);
}

//  QQuickDialogButtonBox *QQuickMessageDialogImplAttached::buttonBox() const
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBox *ritual_ZNK31QQuickMessageDialogImplAttached9buttonBoxEv(
    const QQuickMessageDialogImplAttached *self) {
  return self->buttonBox();
}

//  void QQuickMessageDialogImplAttached::setButtonBox(QQuickDialogButtonBox
//      *buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickMessageDialogImplAttached12setButtonBoxEP21QQuickDialogButtonBox(
    QQuickMessageDialogImplAttached *self,
    QQuickDialogButtonBox *buttons) {
  self->setButtonBox(buttons);
}

//  QQuickButton *QQuickMessageDialogImplAttached::detailedTextButton() const
extern "C" Q_DECL_EXPORT
QQuickButton *ritual_ZNK31QQuickMessageDialogImplAttached18detailedTextButtonEv(
    const QQuickMessageDialogImplAttached *self) {
  return self->detailedTextButton();
}

//  void QQuickMessageDialogImplAttached::setDetailedTextButton(QQuickButton
//      *detailedTextButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickMessageDialogImplAttached21setDetailedTextButtonEP12QQuickButton(
    QQuickMessageDialogImplAttached *self,
    QQuickButton *detailedTextButton) {
  self->setDetailedTextButton(detailedTextButton);
}

//  QQuickMessageDialogImplAttachedPrivate
//      *QQuickMessageDialogImplAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplAttachedPrivate *ritual_ZN31QQuickMessageDialogImplAttached6d_funcEv(
    QQuickMessageDialogImplAttached *self) {
  return self->d_func();
}

//  const QQuickMessageDialogImplAttachedPrivate
//      *QQuickMessageDialogImplAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMessageDialogImplAttachedPrivate *ritual_ZNK31QQuickMessageDialogImplAttached6d_funcEv(
    const QQuickMessageDialogImplAttached *self) {
  return self->d_func();
}
