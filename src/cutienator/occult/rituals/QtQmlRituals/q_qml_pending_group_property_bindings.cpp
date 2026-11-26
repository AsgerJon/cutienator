//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycachecreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycachecreator.cpp, line 123, as _ZNK32QQmlPendingGroupPropertyBindings28resolveMissingPropertyCachesEP23QQmlPropertyCacheVector
inline void QQmlPendingGroupPropertyBindings::resolveMissingPropertyCaches(
        QQmlPropertyCacheVector *propertyCaches) const
{
    for (QQmlBindingInstantiationContext pendingBinding: *this) {
        const int groupPropertyObjectIndex = pendingBinding.instantiatingBinding->value.objectIndex;

        if (propertyCaches->at(groupPropertyObjectIndex))
            continue;

        Q_ASSERT(!pendingBinding.instantiatingPropertyName.isEmpty());

        if (!pendingBinding.referencingObjectPropertyCache) {
            pendingBinding.referencingObjectPropertyCache
                    = propertyCaches->at(pendingBinding.referencingObjectIndex);
        }

        if (!pendingBinding.resolveInstantiatingProperty())
            continue;
        if (auto cache = pendingBinding.instantiatingPropertyCache())
            propertyCaches->set(groupPropertyObjectIndex, cache);
    }
}
//  -----------------------------------------------------------------------

//  void QQmlPendingGroupPropertyBindings::resolveMissingPropertyCaches(QQmlP
//      ropertyCacheVector *propertyCaches) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK32QQmlPendingGroupPropertyBindings28resolveMissingPropertyCachesEP23QQmlPropertyCacheVector(
    const QQmlPendingGroupPropertyBindings *self,
    QQmlPropertyCacheVector *propertyCaches) {
  self->resolveMissingPropertyCaches(propertyCaches);
}

//  QQmlPendingGroupPropertyBindings::~QQmlPendingGroupPropertyBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQmlPendingGroupPropertyBindingsD1Ev(
    QQmlPendingGroupPropertyBindings *self) {
  delete self;
}
