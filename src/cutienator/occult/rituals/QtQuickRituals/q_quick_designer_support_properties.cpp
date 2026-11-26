//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportproperties_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupportproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/QtQml>
#include <QtQml/qqmllist.h>
#include <QtCore/qlist.h>

//  void QQuickDesignerSupportProperties::createNewDynamicProperty(QObject
//      *object, QQmlEngine *engine, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties24createNewDynamicPropertyEP7QObjectP10QQmlEngineRK7QString(
    QObject *object,
    QQmlEngine *engine,
    const QString *name) {
  QQuickDesignerSupportProperties::createNewDynamicProperty(
      object,
      engine,
      *name);
}

//  void
//      QQuickDesignerSupportProperties::registerNodeInstanceMetaObject(QObje
//      ct *object, QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties30registerNodeInstanceMetaObjectEP7QObjectP10QQmlEngine(
    QObject *object,
    QQmlEngine *engine) {
  QQuickDesignerSupportProperties::registerNodeInstanceMetaObject(
      object,
      engine);
}

//  void QQuickDesignerSupportProperties::registerCustomData(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties18registerCustomDataEP7QObject(
    QObject *object) {
  QQuickDesignerSupportProperties::registerCustomData(object);
}

//  QVariant QQuickDesignerSupportProperties::getResetValue(QObject *object,
//      const QQuickDesignerSupport::PropertyName &propertyName)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN31QQuickDesignerSupportProperties13getResetValueEP7QObjectRK10QByteArray(
    QObject *object,
    const QByteArray *propertyName) {
  return new QVariant(
      QQuickDesignerSupportProperties::getResetValue(
          object,
          *propertyName));
}

//  void QQuickDesignerSupportProperties::doResetProperty(QObject *object,
//      QQmlContext *context, const QQuickDesignerSupport::PropertyName
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties15doResetPropertyEP7QObjectP11QQmlContextRK10QByteArray(
    QObject *object,
    QQmlContext *context,
    const QByteArray *propertyName) {
  QQuickDesignerSupportProperties::doResetProperty(
      object,
      context,
      *propertyName);
}

//  bool QQuickDesignerSupportProperties::hasValidResetBinding(QObject
//      *object, const QQuickDesignerSupport::PropertyName &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickDesignerSupportProperties20hasValidResetBindingEP7QObjectRK10QByteArray(
    QObject *object,
    const QByteArray *propertyName) {
  return QQuickDesignerSupportProperties::hasValidResetBinding(
      object,
      *propertyName);
}

//  bool QQuickDesignerSupportProperties::hasBindingForProperty(QObject
//      *object, QQmlContext *context, const
//      QQuickDesignerSupport::PropertyName &propertyName, bool *hasChanged)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickDesignerSupportProperties21hasBindingForPropertyEP7QObjectP11QQmlContextRK10QByteArrayPb(
    QObject *object,
    QQmlContext *context,
    const QByteArray *propertyName,
    bool *hasChanged) {
  return QQuickDesignerSupportProperties::hasBindingForProperty(
      object,
      context,
      *propertyName,
      hasChanged);
}

//  void QQuickDesignerSupportProperties::setPropertyBinding(QObject *object,
//      QQmlContext *context, const QQuickDesignerSupport::PropertyName
//      &propertyName, const QString &expression)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties18setPropertyBindingEP7QObjectP11QQmlContextRK10QByteArrayRK7QString(
    QObject *object,
    QQmlContext *context,
    const QByteArray *propertyName,
    const QString *expression) {
  QQuickDesignerSupportProperties::setPropertyBinding(
      object,
      context,
      *propertyName,
      *expression);
}

//  void
//      QQuickDesignerSupportProperties::keepBindingFromGettingDeleted(QObjec
//      t *object, QQmlContext *context, const
//      QQuickDesignerSupport::PropertyName &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties29keepBindingFromGettingDeletedEP7QObjectP11QQmlContextRK10QByteArray(
    QObject *object,
    QQmlContext *context,
    const QByteArray *propertyName) {
  QQuickDesignerSupportProperties::keepBindingFromGettingDeleted(
      object,
      context,
      *propertyName);
}

//  bool QQuickDesignerSupportProperties::isPropertyQObject(const
//      QMetaProperty &metaProperty)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickDesignerSupportProperties17isPropertyQObjectERK13QMetaProperty(
    const QMetaProperty *metaProperty) {
  return QQuickDesignerSupportProperties::isPropertyQObject(*metaProperty);
}

//  QObject *QQuickDesignerSupportProperties::readQObjectProperty(const
//      QMetaProperty &metaProperty, QObject *object)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN31QQuickDesignerSupportProperties19readQObjectPropertyERK13QMetaPropertyP7QObject(
    const QMetaProperty *metaProperty,
    QObject *object) {
  return QQuickDesignerSupportProperties::readQObjectProperty(
      *metaProperty,
      object);
}

//  void QQuickDesignerSupportProperties::getPropertyCache(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportProperties16getPropertyCacheEP7QObject(
    QObject *object) {
  QQuickDesignerSupportProperties::getPropertyCache(object);
}

//  bool QQuickDesignerSupportProperties::isPropertyBlackListed(const
//      QQuickDesignerSupport::PropertyName &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickDesignerSupportProperties21isPropertyBlackListedERK10QByteArray(
    const QByteArray *propertyName) {
  return QQuickDesignerSupportProperties::isPropertyBlackListed(
      *propertyName);
}

//  QQuickDesignerSupport::PropertyNameList QQuickDesignerSupportProperties::
//      propertyNameListForWritableProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN31QQuickDesignerSupportProperties37propertyNameListForWritablePropertiesEP7QObject(
    QObject *object) {
  return new QList<QByteArray>(
      QQuickDesignerSupportProperties::propertyNameListForWritableProperties(
          object));
}

//  QQuickDesignerSupport::PropertyNameList
//      QQuickDesignerSupportProperties::allPropertyNames(QObject *object,
//      const QQuickDesignerSupport::PropertyName &baseName, QObjectList
//      *inspectedObjects, int depth)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN31QQuickDesignerSupportProperties16allPropertyNamesEP7QObjectRK10QByteArrayP5QListIS1_Ei(
    QObject *object,
    const QByteArray *baseName,
    QObjectList *inspectedObjects,
    int depth) {
  return new QList<QByteArray>(
      QQuickDesignerSupportProperties::allPropertyNames(
          object,
          *baseName,
          inspectedObjects,
          depth));
}

//  bool
//      QQuickDesignerSupportProperties::hasFullImplementedListInterface(cons
//      t QQmlListReference &list)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickDesignerSupportProperties31hasFullImplementedListInterfaceERK17QQmlListReference(
    const QQmlListReference *list) {
  return QQuickDesignerSupportProperties::hasFullImplementedListInterface(
      *list);
}

//  QQuickDesignerSupportProperties::~QQuickDesignerSupportProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickDesignerSupportPropertiesD1Ev(
    QQuickDesignerSupportProperties *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
