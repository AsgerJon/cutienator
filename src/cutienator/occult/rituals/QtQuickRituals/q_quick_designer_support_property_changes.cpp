//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportpropertychanges_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupportpropertychanges_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  void QQuickDesignerSupportPropertyChanges::detachFromState(QObject
//      *propertyChanges)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDesignerSupportPropertyChanges15detachFromStateEP7QObject(
    QObject *propertyChanges) {
  QQuickDesignerSupportPropertyChanges::detachFromState(propertyChanges);
}

//  void QQuickDesignerSupportPropertyChanges::attachToState(QObject
//      *propertyChanges)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDesignerSupportPropertyChanges13attachToStateEP7QObject(
    QObject *propertyChanges) {
  QQuickDesignerSupportPropertyChanges::attachToState(propertyChanges);
}

//  QObject *QQuickDesignerSupportPropertyChanges::targetObject(QObject
//      *propertyChanges)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN36QQuickDesignerSupportPropertyChanges12targetObjectEP7QObject(
    QObject *propertyChanges) {
  return QQuickDesignerSupportPropertyChanges::targetObject(propertyChanges);
}

//  void QQuickDesignerSupportPropertyChanges::removeProperty(QObject
//      *propertyChanges, const QQuickDesignerSupport::PropertyName
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDesignerSupportPropertyChanges14removePropertyEP7QObjectRK10QByteArray(
    QObject *propertyChanges,
    const QByteArray *propertyName) {
  QQuickDesignerSupportPropertyChanges::removeProperty(
      propertyChanges,
      *propertyName);
}

//  QVariant QQuickDesignerSupportPropertyChanges::getProperty(QObject
//      *propertyChanges, const QQuickDesignerSupport::PropertyName
//      &propertyName)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN36QQuickDesignerSupportPropertyChanges11getPropertyEP7QObjectRK10QByteArray(
    QObject *propertyChanges,
    const QByteArray *propertyName) {
  return new QVariant(
      QQuickDesignerSupportPropertyChanges::getProperty(
          propertyChanges,
          *propertyName));
}

//  void QQuickDesignerSupportPropertyChanges::changeValue(QObject
//      *propertyChanges, const QQuickDesignerSupport::PropertyName
//      &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDesignerSupportPropertyChanges11changeValueEP7QObjectRK10QByteArrayRK8QVariant(
    QObject *propertyChanges,
    const QByteArray *propertyName,
    const QVariant *value) {
  QQuickDesignerSupportPropertyChanges::changeValue(
      propertyChanges,
      *propertyName,
      *value);
}

//  void QQuickDesignerSupportPropertyChanges::changeExpression(QObject
//      *propertyChanges, const QQuickDesignerSupport::PropertyName
//      &propertyName, const QString &expression)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDesignerSupportPropertyChanges16changeExpressionEP7QObjectRK10QByteArrayRK7QString(
    QObject *propertyChanges,
    const QByteArray *propertyName,
    const QString *expression) {
  QQuickDesignerSupportPropertyChanges::changeExpression(
      propertyChanges,
      *propertyName,
      *expression);
}

//  QObject *QQuickDesignerSupportPropertyChanges::stateObject(QObject
//      *propertyChanges)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN36QQuickDesignerSupportPropertyChanges11stateObjectEP7QObject(
    QObject *propertyChanges) {
  return QQuickDesignerSupportPropertyChanges::stateObject(propertyChanges);
}

//  bool QQuickDesignerSupportPropertyChanges::isNormalProperty(const
//      QQuickDesignerSupport::PropertyName &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN36QQuickDesignerSupportPropertyChanges16isNormalPropertyERK10QByteArray(
    const QByteArray *propertyName) {
  return QQuickDesignerSupportPropertyChanges::isNormalProperty(
      *propertyName);
}

//  QQuickDesignerSupportPropertyChanges::~QQuickDesignerSupportPropertyChang
//      es()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDesignerSupportPropertyChangesD1Ev(
    QQuickDesignerSupportPropertyChanges *self) {
  delete self;
}
