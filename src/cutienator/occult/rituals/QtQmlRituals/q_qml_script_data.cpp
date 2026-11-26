//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlscriptdata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlscriptdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qv4module_p.h>
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlscriptdata.cpp, line 17, as _ZN14QQmlScriptData24qmlContextDataForContextERK14QQmlRefPointerI15QQmlContextDataE
inline QQmlRefPointer<QQmlContextData> QQmlScriptData::qmlContextDataForContext(
        const QQmlRefPointer<QQmlContextData> &parentQmlContextData)
{
    Q_ASSERT(parentQmlContextData && parentQmlContextData->engine());

    if (!m_precompiledScript || m_precompiledScript->isESModule())
        return nullptr;

    QQmlRefPointer<QQmlContextData> qmlContextData = m_precompiledScript->isSharedLibrary()
            ? QQmlContextData::createRefCounted(QQmlRefPointer<QQmlContextData>())
            : QQmlContextData::createRefCounted(parentQmlContextData);

    qmlContextData->setInternal(true);
    qmlContextData->setJSContext(true);
    if (m_precompiledScript->isSharedLibrary())
        qmlContextData->setPragmaLibraryContext(true);
    else
        qmlContextData->setPragmaLibraryContext(parentQmlContextData->isPragmaLibraryContext());
    qmlContextData->setBaseUrl(url);
    qmlContextData->setBaseUrlString(urlString);
    QV4::ExecutionEngine *v4 = parentQmlContextData->engine()->handle();

    // For backward compatibility, if there are no imports, we need to use the
    // imports from the parent context.  See QTBUG-17518.
    if (!typeNameCache->isEmpty()) {
        qmlContextData->setImports(typeNameCache);
    } else if (!m_precompiledScript->isSharedLibrary()) {
        qmlContextData->setImports(parentQmlContextData->imports());
        qmlContextData->setImportedScripts(v4,  parentQmlContextData->importedScripts());
    }

    if (m_precompiledScript->isSharedLibrary())
        qmlContextData->setEngine(parentQmlContextData->engine()); // Fix for QTBUG-21620

    QV4::Scope scope(v4);
    QV4::ScopedObject scriptsArray(scope);
    if (QV4::Value::fromReturnedValue(qmlContextData->importedScripts()).isNullOrUndefined()) {
        scriptsArray = v4->newArrayObject(scripts.size());
        qmlContextData->setImportedScripts(v4, scriptsArray);
    } else {
        scriptsArray = qmlContextData->importedScripts();
    }
    QV4::ScopedValue v(scope);
    for (int ii = 0; ii < scripts.size(); ++ii) {
        v = scripts.at(ii)->scriptValueForContext(qmlContextData);
        scriptsArray->put(ii, v);
    }

    return qmlContextData;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}

//  from ../qtdeclarative/src/qml/qml/qqmlscriptdata.cpp, line 68, as _ZN14QQmlScriptData21scriptValueForContextERK14QQmlRefPointerI15QQmlContextDataE
inline QV4::ReturnedValue QQmlScriptData::scriptValueForContext(
        const QQmlRefPointer<QQmlContextData> &parentQmlContextData)
{
    QV4::ExecutionEngine *v4 = parentQmlContextData->engine()->handle();
    return handleOwnScriptValueOrExecutableCU(
            v4, [&](const QQmlRefPointer<QV4::ExecutableCompilationUnit> &executableCU) {
        QV4::Scope scope(v4);
        QV4::ScopedValue value(scope, executableCU->value());
        if (!value->isEmpty())
            return value->asReturnedValue();

        QV4::Scoped<QV4::QmlContext> qmlExecutionContext(scope);
        if (auto qmlContextData = qmlContextDataForContext(parentQmlContextData)) {
            qmlExecutionContext = QV4::QmlContext::create(
                    v4->rootContext(), std::move(qmlContextData), /* scopeObject: */ nullptr);
        }

        QV4::Scoped<QV4::Module> module(scope, executableCU->instantiate());
        if (module) {
            if (qmlExecutionContext) {
                module->d()->scope->outer.set(v4, qmlExecutionContext->d());
                qmlExecutionContext->d()->qml()->module.set(v4, module->d());
            }

            module->evaluate();
        }

        if (v4->hasException) {
            QQmlError error = v4->catchExceptionAsQmlError();
            if (error.isValid())
                QQmlEnginePrivate::get(v4)->warning(error);
        }

        if (qmlExecutionContext)
            value = qmlExecutionContext->d()->qml();
        else if (module)
            value = module->d();

        if (m_precompiledScript->isSharedLibrary() || m_precompiledScript->isESModule())
            executableCU->setValue(value);

        return value->asReturnedValue();
    });
}
//  -----------------------------------------------------------------------

//  QQmlScriptData::QQmlScriptData()
extern "C" Q_DECL_EXPORT
QQmlScriptData *ritual_ZN14QQmlScriptDataC1Ev() {
  return new QQmlScriptData();
}

//  QV4::ReturnedValue QQmlScriptData::scriptValueForContext(const
//      QQmlRefPointer<QQmlContextData> &parentCtxt)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN14QQmlScriptData21scriptValueForContextERK14QQmlRefPointerI15QQmlContextDataE(
    QQmlScriptData *self,
    const QQmlRefPointer<QQmlContextData> *parentCtxt) {
  return self->scriptValueForContext(*parentCtxt);
}

//  QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      QQmlScriptData::compilationUnit() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZNK14QQmlScriptData15compilationUnitEv(
    const QQmlScriptData *self) {
  return new QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
      self->compilationUnit());
}

//  a QQmlRefPointer<QV4::CompiledData::CompilationUnit> a ritual of
//      QQmlScriptData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlScriptData__QQmlRefPointer_QV4_CompiledData_CompilationUnit(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *self) {
  delete self;
}
