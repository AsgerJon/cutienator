//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertyvalidator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyvalidator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlpropertymap.h>
#include <QtCore/qcryptographichash.h>
#include <QtQml/private/qqmlpropertyvalidator_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/qdatetime.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 19, as local:qqmlpropertyvalidator.cpp:isPrimitiveType
static bool isPrimitiveType(QMetaType metaType)
{
    switch (metaType.id()) {
#define HANDLE_PRIMITIVE(Type, id, T) \
    case QMetaType::Type:
QT_FOR_EACH_STATIC_PRIMITIVE_TYPE(HANDLE_PRIMITIVE);
#undef HANDLE_PRIMITIVE
        return true;
    default:
        return false;
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 50, as local:qqmlpropertyvalidator.cpp:GroupPropertyVector
typedef QVarLengthArray<const QV4::CompiledData::Binding *, 8> GroupPropertyVector;

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 52, as local:qqmlpropertyvalidator.cpp:BindingFinder
struct BindingFinder
{
    bool operator()(quint32 name, const QV4::CompiledData::Binding *binding) const
    {
        return name < binding->propertyNameIndex;
    }
    bool operator()(const QV4::CompiledData::Binding *binding, quint32 name) const
    {
        return binding->propertyNameIndex < name;
    }
    bool operator()(const QV4::CompiledData::Binding *lhs, const QV4::CompiledData::Binding *rhs) const
    {
        return lhs->propertyNameIndex < rhs->propertyNameIndex;
    }
};

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 40, as _ZN3QV421ResolvedTypeReference19createPropertyCacheEv
namespace QV4 {
inline QQmlPropertyCache::ConstPtr ResolvedTypeReference::createPropertyCache()
{
    if (!m_typePropertyCache && m_type.isValid()) {
        const QMetaObject *metaObject = m_type.metaObject();
        if (!metaObject) // value type of non-Q_GADGET base with extension
            metaObject = m_type.extensionMetaObject();
        if (metaObject)
            m_typePropertyCache = QQmlMetaType::propertyCache(metaObject, m_version);
    }

    return m_typePropertyCache;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 32, as _ZN21QQmlPropertyValidatorC1EP14QQmlTypeLoaderPK11QQmlImportsRK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEE
inline QQmlPropertyValidator::QQmlPropertyValidator(
        QQmlTypeLoader *typeLoader, const QQmlImports *imports,
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)
    : m_typeLoader(typeLoader)
    , compilationUnit(compilationUnit)
    , imports(imports)
    , qmlUnit(compilationUnit->unitData())
    , propertyCaches(compilationUnit->propertyCaches)
    , bindingPropertyDataPerObject(&compilationUnit->bindingPropertyDataPerObject)
{
    bindingPropertyDataPerObject->resize(compilationUnit->objectCount());
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 695, as _ZNK21QQmlPropertyValidator21validateObjectBindingEPK16QQmlPropertyDataRK7QStringPKN3QV412CompiledData7BindingE
inline QQmlError QQmlPropertyValidator::validateObjectBinding(const QQmlPropertyData *property, const QString &propertyName, const QV4::CompiledData::Binding *binding) const
{
    QQmlError noError;

    if (binding->hasFlag(QV4::CompiledData::Binding::IsOnAssignment)) {
        Q_ASSERT(binding->type() == QV4::CompiledData::Binding::Type_Object);

        bool isValueSource = false;
        bool isPropertyInterceptor = false;

        const QV4::CompiledData::Object *targetObject = compilationUnit->objectAt(binding->value.objectIndex);
        if (auto *typeRef = resolvedType(targetObject->inheritedTypeNameIndex)) {
            QQmlPropertyCache::ConstPtr cache = typeRef->createPropertyCache();
            const QMetaObject *mo = cache ? cache->firstCppMetaObject() : nullptr;
            QQmlType qmlType;
            while (mo && !qmlType.isValid()) {
                qmlType = QQmlMetaType::qmlType(mo);
                mo = mo->superClass();
            }

            isValueSource = qmlType.propertyValueSourceCast() != -1;
            isPropertyInterceptor = qmlType.propertyValueInterceptorCast() != -1;
        }

        if (!isValueSource && !isPropertyInterceptor) {
            return qQmlCompileError(
                    binding->valueLocation,
                    tr("\"%1\" cannot operate on \"%2\"")
                            .arg(stringAt(targetObject->inheritedTypeNameIndex), propertyName));
        }

        return noError;
    }

    const QMetaType propType = property->propType();
    const auto rhsType = [&]() {
        return stringAt(compilationUnit->objectAt(binding->value.objectIndex)
                        ->inheritedTypeNameIndex);
    };

    if (QQmlMetaType::isInterface(propType)) {
        // Can only check at instantiation time if the created sub-object successfully casts to the
        // target interface.
        return noError;
    } else if (propType == QMetaType::fromType<QVariant>()
               || propType == QMetaType::fromType<QJSValue>()) {
        // We can convert everything to QVariant :)
        return noError;
    } else if (property->isQList()) {
        const QMetaType listType = QQmlMetaType::listValueType(property->propType());
        if (!QQmlMetaType::isInterface(listType)) {
            QQmlPropertyCache::ConstPtr source = propertyCaches.at(binding->value.objectIndex);

            if (const int wrapper = compilationUnit->implicitComponentForObject(
                        binding->value.objectIndex); wrapper != -1) {
                // If the child is wrapped in an implicit component, use the wrapper for coercion.
                source = propertyCaches.at(wrapper);
            }

            if (!canCoerce(listType, source)) {
                const QString expectedTypeName = QString::fromUtf8(listType.name()).remove(QLatin1Char('*'));
                return qQmlCompileError(binding->valueLocation,
                    tr("Cannot assign object of type \"%1\" to list property \"%2\"; expected \"%3\"")
                        .arg(source->className(), propertyName, expectedTypeName));
            }
        }
        return noError;
    } else if (binding->hasFlag(QV4::CompiledData::Binding::IsSignalHandlerObject)
               && property->isFunction()) {
        return noError;
    } else if (isPrimitiveType(propType)) {
        auto typeName = QString::fromUtf8(QMetaType(propType).name());
        return qQmlCompileError(
                binding->location,
                tr("Cannot assign value of type \"%1\" to property \"%2\", expecting \"%3\"")
                        .arg(rhsType(), propertyName, typeName));
    } else if (propType == QMetaType::fromType<QQmlScriptString>()) {
        return qQmlCompileError(binding->valueLocation, tr("Invalid property assignment: script expected"));
    } else if (!QQmlMetaType::isValueType(property->propType())) {
        QQmlPropertyCache::ConstPtr propertyMetaObject;

        // if we have an inline component from the current file,
        // it is not properly registered at this point, as registration
        // only occurs after the whole file has been validated
        // Therefore we need to check the ICs here
        for (const auto &icDatum: std::as_const(compilationUnit->inlineComponentData)) {
            if (icDatum.qmlType.typeId() == property->propType()) {
                propertyMetaObject = compilationUnit->propertyCaches.at(icDatum.objectIndex);
                break;
            }
        }

        if (!propertyMetaObject) {
            // We want to use the raw metaObject here as the raw metaobject is the
            // actual property type before we applied any extensions that might
            // effect the properties on the type, but don't effect assignability
            // Not passing a version ensures that we get the raw metaObject.
            propertyMetaObject = QQmlMetaType::rawPropertyCacheForType(propType);
        }

        if (propertyMetaObject) {
            // Will be true if the assigned type inherits propertyMetaObject
            // Determine isAssignable value
            bool isAssignable = false;
            QQmlPropertyCache::ConstPtr c = propertyCaches.at(binding->value.objectIndex);

            if (const int wrapper = compilationUnit->implicitComponentForObject(
                        binding->value.objectIndex); wrapper != -1) {
                // If the child is wrapped in an implicit component, use the wrapper.
                c = propertyCaches.at(wrapper);
            }

            while (c && !isAssignable) {
                isAssignable |= c == propertyMetaObject;
                c = c->parent();
            }

            if (!isAssignable) {
                return qQmlCompileError(binding->valueLocation, tr("Cannot assign object of type \"%1\" to property of type \"%2\" as the former is neither the same as the latter nor a sub-class of it.")
                        .arg(rhsType()).arg(QLatin1String(property->propType().name())));
            }
        } else {
            return qQmlCompileError(binding->valueLocation, tr("Cannot assign to property of unknown type \"%1\".")
                        .arg(QLatin1String(property->propType().name())));
        }

    }
    return noError;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 657, as _ZNK21QQmlPropertyValidator9canCoerceE9QMetaTypeN17QQmlPropertyCache8ConstPtrE
inline bool QQmlPropertyValidator::canCoerce(QMetaType to, QQmlPropertyCache::ConstPtr fromMo) const
{
    if (QQmlMetaType::canConvert(fromMo, to))
        return true;

    // if we have an inline component from the current file,
    // it is not properly registered at this point, as registration
    // only occurs after the whole file has been validated
    // Therefore we need to check the ICs here
    for (const auto &icDatum : std::as_const(compilationUnit->inlineComponentData)) {
        if (icDatum.qmlType.typeId() != to)
            continue;

        const auto toMo = compilationUnit->propertyCaches.at(icDatum.objectIndex);
        for (QQmlPropertyCache::ConstPtr parent = fromMo; parent; parent = parent->parent()) {
            if (parent == toMo)
                return true;
        }
        return false;
    }

    return false;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 681, as _ZNK21QQmlPropertyValidator11recordErrorERKN3QV412CompiledData8LocationERK7QString
inline QList<QQmlError> QQmlPropertyValidator::recordError(const QV4::CompiledData::Location &location, const QString &description) const
{
    QList<QQmlError> errors;
    errors.append(qQmlCompileError(location, description));
    return errors;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertyvalidator.cpp, line 688, as _ZNK21QQmlPropertyValidator11recordErrorERK9QQmlError
inline QList<QQmlError> QQmlPropertyValidator::recordError(const QQmlError &error) const
{
    QList<QQmlError> errors;
    errors.append(error);
    return errors;
}
//  -----------------------------------------------------------------------

//  QString QQmlPropertyValidator::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlPropertyValidator2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlPropertyValidator::tr(
          sourceText,
          disambiguation,
          n));
}

//  QQmlPropertyValidator::QQmlPropertyValidator(QQmlTypeLoader *typeLoader,
//      const QQmlImports *imports, const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)
extern "C" Q_DECL_EXPORT
QQmlPropertyValidator *ritual_ZN21QQmlPropertyValidatorC1EP14QQmlTypeLoaderPK11QQmlImportsRK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEE(
    QQmlTypeLoader *typeLoader,
    const QQmlImports *imports,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit) {
  return new QQmlPropertyValidator(typeLoader, imports, *compilationUnit);
}

//  QQmlPropertyCache::ConstPtr QQmlPropertyValidator::rootPropertyCache()
//      const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK21QQmlPropertyValidator17rootPropertyCacheEv(
    const QQmlPropertyValidator *self) {
  return new QQmlPropertyCache::ConstPtr(self->rootPropertyCache());
}

//  QUrl QQmlPropertyValidator::documentSourceUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QQmlPropertyValidator17documentSourceUrlEv(
    const QQmlPropertyValidator *self) {
  return new QUrl(self->documentSourceUrl());
}

//  QQmlTypeLoader *QQmlPropertyValidator::typeLoader() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZNK21QQmlPropertyValidator10typeLoaderEv(
    const QQmlPropertyValidator *self) {
  return self->typeLoader();
}

//  QQmlError QQmlPropertyValidator::validateObjectBinding(const
//      QQmlPropertyData *property, const QString &propertyName, const
//      QV4::CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZNK21QQmlPropertyValidator21validateObjectBindingEPK16QQmlPropertyDataRK7QStringPKN3QV412CompiledData7BindingE(
    const QQmlPropertyValidator *self,
    const QQmlPropertyData *property,
    const QString *propertyName,
    const QV4::CompiledData::Binding *binding) {
  return new QQmlError(
      self->validateObjectBinding(
          property,
          *propertyName,
          binding));
}

//  bool QQmlPropertyValidator::canCoerce(QMetaType to,
//      QQmlPropertyCache::ConstPtr fromMo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQmlPropertyValidator9canCoerceE9QMetaTypeN17QQmlPropertyCache8ConstPtrE(
    const QQmlPropertyValidator *self,
    const QMetaType *to,
    const QQmlPropertyCache::ConstPtr *fromMo) {
  return self->canCoerce(*to, *fromMo);
}

//  QList<QQmlError> QQmlPropertyValidator::recordError(const
//      QV4::CompiledData::Location &location, const QString &description)
//      const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK21QQmlPropertyValidator11recordErrorERKN3QV412CompiledData8LocationERK7QString(
    const QQmlPropertyValidator *self,
    const QV4::CompiledData::Location *location,
    const QString *description) {
  return new QList<QQmlError>(self->recordError(*location, *description));
}

//  QList<QQmlError> QQmlPropertyValidator::recordError(const QQmlError
//      &error) const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK21QQmlPropertyValidator11recordErrorERK9QQmlError(
    const QQmlPropertyValidator *self,
    const QQmlError *error) {
  return new QList<QQmlError>(self->recordError(*error));
}

//  QString QQmlPropertyValidator::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQmlPropertyValidator8stringAtEi(
    const QQmlPropertyValidator *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  QV4::ResolvedTypeReference *QQmlPropertyValidator::resolvedType(int id)
//      const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK21QQmlPropertyValidator12resolvedTypeEi(
    const QQmlPropertyValidator *self,
    int id) {
  return self->resolvedType(id);
}

//  QQmlPropertyValidator::~QQmlPropertyValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlPropertyValidatorD1Ev(QQmlPropertyValidator *self) {
  delete self;
}
