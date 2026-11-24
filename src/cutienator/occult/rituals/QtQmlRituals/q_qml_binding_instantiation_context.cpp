//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 65, as _ZN31QQmlBindingInstantiationContextC1EiPKN3QV412CompiledData7BindingERK7QStringRKN17QQmlPropertyCache8ConstPtrE
inline QQmlBindingInstantiationContext::QQmlBindingInstantiationContext(
        int referencingObjectIndex,
        const QV4::CompiledData::Binding *instantiatingBinding,
        const QString &instantiatingPropertyName,
        const QQmlPropertyCache::ConstPtr &referencingObjectPropertyCache)
    : referencingObjectIndex(referencingObjectIndex)
    , instantiatingBinding(instantiatingBinding)
    , instantiatingPropertyName(instantiatingPropertyName)
    , referencingObjectPropertyCache(referencingObjectPropertyCache)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 77, as _ZN31QQmlBindingInstantiationContext28resolveInstantiatingPropertyEv
inline bool QQmlBindingInstantiationContext::resolveInstantiatingProperty()
{
    if (!instantiatingBinding
           || instantiatingBinding->type() != QV4::CompiledData::Binding::Type_GroupProperty) {
        return true;
    }

    if (!referencingObjectPropertyCache)
        return false;

    Q_ASSERT(referencingObjectIndex >= 0);
    Q_ASSERT(instantiatingBinding->propertyNameIndex != 0);

    bool notInRevision = false;
    instantiatingProperty = QQmlPropertyResolver(referencingObjectPropertyCache)
                                    .property(instantiatingPropertyName, &notInRevision,
                                              QQmlPropertyResolver::IgnoreRevision);
    return instantiatingProperty != nullptr;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 97, as _ZNK31QQmlBindingInstantiationContext26instantiatingPropertyCacheEv
inline QQmlPropertyCache::ConstPtr QQmlBindingInstantiationContext::instantiatingPropertyCache() const
{
    if (instantiatingProperty) {
        if (instantiatingProperty->isQObject()) {
            // rawPropertyCacheForType assumes a given unspecified version means "any version".
            // There is another overload that takes no version, which we shall not use here.
            auto result = QQmlMetaType::rawPropertyCacheForType(instantiatingProperty->propType(),
                                                         instantiatingProperty->typeVersion());
            if (result)
                return result;
            /* We might end up here if there's a grouped property, and the type hasn't been registered.
               Still try to get a property cache, as long as the type of the property is well-behaved
               (i.e., not dynamic)*/
            if (auto metaObject = instantiatingProperty->propType().metaObject(); metaObject) {
                // we'll warn about dynamic meta-object later in the property validator
                if (!(QMetaObjectPrivate::get(metaObject)->flags & DynamicMetaObject))
                    return QQmlMetaType::propertyCache(metaObject);
            }
            // fall through intentional
        } else if (const QMetaObject *vtmo = QQmlMetaType::metaObjectForValueType(instantiatingProperty->propType())) {
            return QQmlMetaType::propertyCache(vtmo, instantiatingProperty->typeVersion());
        }
    }
    return QQmlPropertyCache::ConstPtr();
}
//  -----------------------------------------------------------------------

//  QQmlBindingInstantiationContext::QQmlBindingInstantiationContext()
extern "C" Q_DECL_EXPORT
QQmlBindingInstantiationContext *ritual_ZN31QQmlBindingInstantiationContextC1Ev() {
  return new QQmlBindingInstantiationContext();
}

//  QQmlBindingInstantiationContext::QQmlBindingInstantiationContext(int
//      referencingObjectIndex, const QV4::CompiledData::Binding
//      *instantiatingBinding, const QString &instantiatingPropertyName,
//      const QQmlPropertyCache::ConstPtr &referencingObjectPropertyCache)
extern "C" Q_DECL_EXPORT
QQmlBindingInstantiationContext *ritual_ZN31QQmlBindingInstantiationContextC1EiPKN3QV412CompiledData7BindingERK7QStringRKN17QQmlPropertyCache8ConstPtrE(
    int referencingObjectIndex,
    const QV4::CompiledData::Binding *instantiatingBinding,
    const QString *instantiatingPropertyName,
    const QQmlPropertyCache::ConstPtr *referencingObjectPropertyCache) {
  return new QQmlBindingInstantiationContext(
      referencingObjectIndex,
      instantiatingBinding,
      *instantiatingPropertyName,
      *referencingObjectPropertyCache);
}

//  bool QQmlBindingInstantiationContext::resolveInstantiatingProperty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQmlBindingInstantiationContext28resolveInstantiatingPropertyEv(
    QQmlBindingInstantiationContext *self) {
  return self->resolveInstantiatingProperty();
}

//  QQmlPropertyCache::ConstPtr
//      QQmlBindingInstantiationContext::instantiatingPropertyCache() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK31QQmlBindingInstantiationContext26instantiatingPropertyCacheEv(
    const QQmlBindingInstantiationContext *self) {
  return new QQmlPropertyCache::ConstPtr(self->instantiatingPropertyCache());
}

//  QQmlBindingInstantiationContext::~QQmlBindingInstantiationContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlBindingInstantiationContextD1Ev(
    QQmlBindingInstantiationContext *self) {
  delete self;
}
