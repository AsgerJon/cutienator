//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypecompiler_p.h>
#include <QtQml/private/qqmlobjectcreator_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/private/qqmlcomponentandaliasresolver_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/qtyperevision.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qv4staticvalue_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4compilerscanfunctions_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QCryptographicHash>
#include <QtCore/qtyperevision.h>
#include <cmath>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 17, as local:qqmltypecompiler.cpp:COMPILE_EXCEPTION
#define COMPILE_EXCEPTION(token, desc) \

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 280, as _ZN15QQmlCompilePassC2EP16QQmlTypeCompiler
inline QQmlCompilePass::QQmlCompilePass(QQmlTypeCompiler *typeCompiler)
    : compiler(typeCompiler)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 224, as _ZN16QQmlTypeCompiler14propertyCachesEv
inline QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
{
    return &m_propertyCaches;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 219, as _ZNK16QQmlTypeCompiler10qmlObjectsEv
inline QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const
{
    return &document->objects;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 214, as _ZNK16QQmlTypeCompiler7importsEv
inline const QQmlImports *QQmlTypeCompiler::imports() const
{
    return typeData->imports();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 313, as _ZN21SignalHandlerResolver31resolveSignalHandlerExpressionsEPKN5QmlIR6ObjectERK7QStringRKN17QQmlPropertyCache8ConstPtrEN20QQmlPropertyResolver13RevisionCheckE
inline bool SignalHandlerResolver::resolveSignalHandlerExpressions(
        const QmlIR::Object *obj, const QString &typeName,
        const QQmlPropertyCache::ConstPtr &propertyCache,
        QQmlPropertyResolver::RevisionCheck checkRevision)
{
    // map from signal name defined in qml itself to list of parameters
    QHash<QString, QStringList> customSignals;

    for (QmlIR::Binding *binding = obj->firstBinding(); binding; binding = binding->next) {
        const QString bindingPropertyName = stringAt(binding->propertyNameIndex);
        // Attached property?
        const QV4::CompiledData::Binding::Type bindingType = binding->type();
        if (bindingType == QV4::CompiledData::Binding::Type_AttachedProperty) {
            const QmlIR::Object *attachedObj = qmlObjects.at(binding->value.objectIndex);
            auto *typeRef = resolvedType(binding->propertyNameIndex);
            QQmlType type = typeRef ? typeRef->type() : QQmlType();
            if (!type.isValid())
                imports->resolveType(typeLoader, bindingPropertyName, &type, nullptr, nullptr);

            const QMetaObject *attachedType = type.attachedPropertiesType(typeLoader);
            if (!attachedType)
                COMPILE_EXCEPTION(binding, tr("Non-existent attached object"));
            QQmlPropertyCache::ConstPtr cache = QQmlMetaType::propertyCache(attachedType);

            // Ignore revisions of signals on attached objects. They are not unqualified.
            if (!resolveSignalHandlerExpressions(
                        attachedObj, bindingPropertyName, cache,
                        QQmlPropertyResolver::IgnoreRevision)) {
                return false;
            }

            continue;
        }

        QString qPropertyName;
        QString signalName;
        if (auto propertyName =
                    QQmlSignalNames::changedHandlerNameToPropertyName(bindingPropertyName)) {
            qPropertyName = *propertyName;
            signalName = *QQmlSignalNames::changedHandlerNameToSignalName(bindingPropertyName);
        } else {
            signalName = QQmlSignalNames::handlerNameToSignalName(bindingPropertyName)
                                 .value_or(QString());
        }
        if (signalName.isEmpty())
            continue;

        QQmlPropertyResolver resolver(propertyCache);

        bool notInRevision = false;
        const QQmlPropertyData *const signal
                = resolver.signal(signalName, &notInRevision, checkRevision);
        const QQmlPropertyData *const signalPropertyData
                = resolver.property(signalName, /*notInRevision ptr*/nullptr, checkRevision);
        const QQmlPropertyData *const qPropertyData = !qPropertyName.isEmpty()
                ? resolver.property(qPropertyName, nullptr, checkRevision)
                : nullptr;
        QString finalSignalHandlerPropertyName = signalName;
        QV4::CompiledData::Binding::Flag flag
                = QV4::CompiledData::Binding::IsSignalHandlerExpression;

        const bool isPropertyObserver
                = !signalPropertyData && qPropertyData && qPropertyData->notifiesViaBindable();
        if (signal && !(qPropertyData && qPropertyData->isAlias() && isPropertyObserver)) {
            int sigIndex = propertyCache->methodIndexToSignalIndex(signal->coreIndex());
            sigIndex = propertyCache->originalClone(sigIndex);

            bool unnamedParameter = false;

            QList<QByteArray> parameterNames = propertyCache->signalParameterNames(sigIndex);
            for (int i = 0; i < parameterNames.size(); ++i) {
                const QString param = QString::fromUtf8(parameterNames.at(i));
                if (param.isEmpty())
                    unnamedParameter = true;
                else if (unnamedParameter) {
                    COMPILE_EXCEPTION(binding, tr("Signal uses unnamed parameter followed by named parameter."));
                } else if (QV4::Compiler::Codegen::isNameGlobal(param)) {
                    COMPILE_EXCEPTION(binding, tr("Signal parameter \"%1\" hides global variable.").arg(param));
                }
            }
        } else if (isPropertyObserver) {
            finalSignalHandlerPropertyName = qPropertyName;
            flag = QV4::CompiledData::Binding::IsPropertyObserver;
        } else {
            if (notInRevision) {
                // Try assinging it as a property later
                if (signalPropertyData)
                    continue;

                const QString &originalPropertyName = stringAt(binding->propertyNameIndex);

                auto *typeRef = resolvedType(obj->inheritedTypeNameIndex);
                const QQmlType type = typeRef ? typeRef->type() : QQmlType();
                if (type.isValid()) {
                    COMPILE_EXCEPTION(binding, tr("\"%1.%2\" is not available in %3 %4.%5.")
                                      .arg(typeName, originalPropertyName, type.module())
                                      .arg(type.version().majorVersion())
                                      .arg(type.version().minorVersion()));
                } else {
                    COMPILE_EXCEPTION(
                            binding,
                            tr("\"%1.%2\" is not available due to component versioning.")
                                    .arg(typeName, originalPropertyName));
                }
            }

            // Try to look up the signal parameter names in the object itself

            // build cache if necessary
            if (customSignals.isEmpty()) {
                for (const QmlIR::Signal *signal = obj->firstSignal(); signal; signal = signal->next) {
                    const QString &signalName = stringAt(signal->nameIndex);
                    customSignals.insert(signalName, signal->parameterStringList(compiler->stringPool()));
                }

                for (const QmlIR::Property *property = obj->firstProperty(); property; property = property->next) {
                    const QString propName = stringAt(property->nameIndex());
                    customSignals.insert(propName, QStringList());
                }
            }

            QHash<QString, QStringList>::ConstIterator entry = customSignals.constFind(signalName);
            if (entry == customSignals.constEnd() && !qPropertyName.isEmpty())
                entry = customSignals.constFind(qPropertyName);

            if (entry == customSignals.constEnd()) {
                // Can't find even a custom signal, then just don't do anything and try
                // keeping the binding as a regular property assignment.
                continue;
            }
        }

        // Binding object to signal means connect the signal to the object's default method.
        if (bindingType == QV4::CompiledData::Binding::Type_Object) {
            binding->setFlag(QV4::CompiledData::Binding::IsSignalHandlerObject);
            continue;
        }

        if (bindingType != QV4::CompiledData::Binding::Type_Script) {
            if (bindingType < QV4::CompiledData::Binding::Type_Script) {
                COMPILE_EXCEPTION(binding, tr("Cannot assign a value to a signal (expecting a script to be run)"));
            } else {
                COMPILE_EXCEPTION(binding, tr("Incorrectly specified signal assignment"));
            }
        }

        binding->propertyNameIndex = compiler->registerString(finalSignalHandlerPropertyName);
        binding->setFlag(flag);
    }
    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 174, as _ZNK16QQmlTypeCompiler8stringAtEi
inline QString QQmlTypeCompiler::stringAt(int idx) const
{
    return document->stringAt(idx);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 179, as _ZN16QQmlTypeCompiler14registerStringERK7QString
inline int QQmlTypeCompiler::registerString(const QString &str)
{
    return document->jsGenerator.registerString(str);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 244, as _ZNK16QQmlTypeCompiler10stringPoolEv
inline const QV4::Compiler::StringTableGenerator *QQmlTypeCompiler::stringPool() const
{
    return &document->jsGenerator.stringTable;
}

//  from ../qtdeclarative/src/qml/compiler/qqmlirbuilder.cpp, line 421, as _ZNK5QmlIR6Signal19parameterStringListEPKN3QV48Compiler20StringTableGeneratorE
namespace QmlIR {
using namespace Qt::StringLiterals;
using namespace QQmlJS;
inline QStringList Signal::parameterStringList(const QV4::Compiler::StringTableGenerator *stringPool) const
{
    QStringList result;
    result.reserve(parameters->count);
    for (Parameter *param = parameters->first; param; param = param->next)
        result << stringPool->stringForIndex(param->nameIndex);
    return result;
}
}  // namespace QmlIR

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 285, as _ZN21SignalHandlerResolverC1EP16QQmlTypeCompiler
inline SignalHandlerResolver::SignalHandlerResolver(QQmlTypeCompiler *typeCompiler)
    : QQmlCompilePass(typeCompiler)
    , typeLoader(typeCompiler->typeLoader())
    , qmlObjects(*typeCompiler->qmlObjects())
    , imports(typeCompiler->imports())
    , customParsers(typeCompiler->customParserCache())
    , propertyCaches(typeCompiler->propertyCaches())
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 295, as _ZN21SignalHandlerResolver31resolveSignalHandlerExpressionsEv
inline bool SignalHandlerResolver::resolveSignalHandlerExpressions()
{
    for (int objectIndex = 0; objectIndex < qmlObjects.size(); ++objectIndex) {
        const QmlIR::Object * const obj = qmlObjects.at(objectIndex);
        QQmlPropertyCache::ConstPtr cache = propertyCaches->at(objectIndex);
        if (!cache)
            continue;
        if (QQmlCustomParser *customParser = customParsers.value(obj->inheritedTypeNameIndex)) {
            if (!(customParser->flags() & QQmlCustomParser::AcceptsSignalHandlers))
                continue;
        }
        const QString elementName = stringAt(obj->inheritedTypeNameIndex);
        if (!resolveSignalHandlerExpressions(obj, elementName, cache))
            return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  QString SignalHandlerResolver::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21SignalHandlerResolver2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      SignalHandlerResolver::tr(
          sourceText,
          disambiguation,
          n));
}

//  SignalHandlerResolver::SignalHandlerResolver(QQmlTypeCompiler
//      *typeCompiler)
extern "C" Q_DECL_EXPORT
SignalHandlerResolver *ritual_ZN21SignalHandlerResolverC1EP16QQmlTypeCompiler(
    QQmlTypeCompiler *typeCompiler) {
  return new SignalHandlerResolver(typeCompiler);
}

//  bool SignalHandlerResolver::resolveSignalHandlerExpressions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21SignalHandlerResolver31resolveSignalHandlerExpressionsEv(
    SignalHandlerResolver *self) {
  return self->resolveSignalHandlerExpressions();
}

//  SignalHandlerResolver::~SignalHandlerResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN21SignalHandlerResolverD1Ev(SignalHandlerResolver *self) {
  delete self;
}
