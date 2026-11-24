//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportstates_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupportstates_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  bool QQuickDesignerSupportStates::isStateActive(QObject *object,
//      QQmlContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickDesignerSupportStates13isStateActiveEP7QObjectP11QQmlContext(
    QObject *object,
    QQmlContext *context) {
  return QQuickDesignerSupportStates::isStateActive(object, context);
}

//  void QQuickDesignerSupportStates::activateState(QObject *object,
//      QQmlContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickDesignerSupportStates13activateStateEP7QObjectP11QQmlContext(
    QObject *object,
    QQmlContext *context) {
  QQuickDesignerSupportStates::activateState(object, context);
}

//  void QQuickDesignerSupportStates::deactivateState(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickDesignerSupportStates15deactivateStateEP7QObject(
    QObject *object) {
  QQuickDesignerSupportStates::deactivateState(object);
}

//  bool QQuickDesignerSupportStates::changeValueInRevertList(QObject *state,
//      QObject *target, const QQuickDesignerSupport::PropertyName
//      &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickDesignerSupportStates23changeValueInRevertListEP7QObjectS1_RK10QByteArrayRK8QVariant(
    QObject *state,
    QObject *target,
    const QByteArray *propertyName,
    const QVariant *value) {
  return QQuickDesignerSupportStates::changeValueInRevertList(
      state,
      target,
      *propertyName,
      *value);
}

//  bool QQuickDesignerSupportStates::updateStateBinding(QObject *state,
//      QObject *target, const QQuickDesignerSupport::PropertyName
//      &propertyName, const QString &expression)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickDesignerSupportStates18updateStateBindingEP7QObjectS1_RK10QByteArrayRK7QString(
    QObject *state,
    QObject *target,
    const QByteArray *propertyName,
    const QString *expression) {
  return QQuickDesignerSupportStates::updateStateBinding(
      state,
      target,
      *propertyName,
      *expression);
}

//  bool QQuickDesignerSupportStates::resetStateProperty(QObject *state,
//      QObject *target, const QQuickDesignerSupport::PropertyName
//      &propertyName, const QVariant &a3)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQuickDesignerSupportStates18resetStatePropertyEP7QObjectS1_RK10QByteArrayRK8QVariant(
    QObject *state,
    QObject *target,
    const QByteArray *propertyName,
    const QVariant *a3) {
  return QQuickDesignerSupportStates::resetStateProperty(
      state,
      target,
      *propertyName,
      *a3);
}

//  QQuickDesignerSupportStates::~QQuickDesignerSupportStates()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickDesignerSupportStatesD1Ev(
    QQuickDesignerSupportStates *self) {
  delete self;
}
