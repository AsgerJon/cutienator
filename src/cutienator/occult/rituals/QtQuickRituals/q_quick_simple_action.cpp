//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQuickSimpleAction::QQuickSimpleAction(const QQuickStateAction &a, State
//      state)
extern "C" Q_DECL_EXPORT
QQuickSimpleAction *ritual_ZN18QQuickSimpleActionC1ERK17QQuickStateActionNS_5StateE(
    const QQuickStateAction *a,
    QQuickSimpleAction::State state) {
  return new QQuickSimpleAction(*a, state);
}

//  QQuickSimpleAction::~QQuickSimpleAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSimpleActionD1Ev(QQuickSimpleAction *self) {
  delete self;
}

//  QQuickSimpleAction::QQuickSimpleAction(const QQuickSimpleAction &other)
extern "C" Q_DECL_EXPORT
QQuickSimpleAction *ritual_ZN18QQuickSimpleActionC1ERKS_(
    const QQuickSimpleAction *other) {
  return new QQuickSimpleAction(*other);
}

//  void QQuickSimpleAction::setProperty(const QQmlProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSimpleAction11setPropertyERK12QQmlProperty(
    QQuickSimpleAction *self,
    const QQmlProperty *property) {
  self->setProperty(*property);
}

//  const QQmlProperty &QQuickSimpleAction::property() const
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZNK18QQuickSimpleAction8propertyEv(
    const QQuickSimpleAction *self) {
  return new QQmlProperty(self->property());
}

//  void QQuickSimpleAction::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSimpleAction8setValueERK8QVariant(
    QQuickSimpleAction *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  const QVariant &QQuickSimpleAction::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQuickSimpleAction5valueEv(
    const QQuickSimpleAction *self) {
  return new QVariant(self->value());
}

//  void QQuickSimpleAction::setBinding(QQmlAnyBinding binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickSimpleAction10setBindingE14QQmlAnyBinding(
    QQuickSimpleAction *self,
    const QQmlAnyBinding *binding) {
  self->setBinding(*binding);
}

//  QQmlAnyBinding QQuickSimpleAction::binding() const
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZNK18QQuickSimpleAction7bindingEv(
    const QQuickSimpleAction *self) {
  return new QQmlAnyBinding(self->binding());
}

//  QObject *QQuickSimpleAction::specifiedObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQuickSimpleAction15specifiedObjectEv(
    const QQuickSimpleAction *self) {
  return self->specifiedObject();
}

//  const QString &QQuickSimpleAction::specifiedProperty() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickSimpleAction17specifiedPropertyEv(
    const QQuickSimpleAction *self) {
  return new QString(self->specifiedProperty());
}

//  QQuickStateActionEvent *QQuickSimpleAction::event() const
extern "C" Q_DECL_EXPORT
QQuickStateActionEvent *ritual_ZNK18QQuickSimpleAction5eventEv(
    const QQuickSimpleAction *self) {
  return self->event();
}

//  bool QQuickSimpleAction::reverseEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickSimpleAction12reverseEventEv(
    const QQuickSimpleAction *self) {
  return self->reverseEvent();
}
