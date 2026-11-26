//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistmodel_p_p.h>
#include <QtQmlModels/private/qqmllistmodelworkeragent_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/private/qqmlnotifier_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstack.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/qdatetime.h>
#include <QtCore/QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 2990, as _ZN19QQmlListModelParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE
inline void QQmlListModelParser::verifyBindings(
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
        const QList<const QV4::CompiledData::Binding *> &bindings)
{
    listElementTypeName = QString(); // unknown

    for (const QV4::CompiledData::Binding *binding : bindings) {
        QString propName = compilationUnit->stringAt(binding->propertyNameIndex);
        if (!propName.isEmpty()) { // isn't default property
            error(binding, QQmlListModel::tr("ListModel: undefined property '%1'").arg(propName));
            return;
        }
        if (!verifyProperty(compilationUnit, binding))
            return;
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 3007, as _ZN19QQmlListModelParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE
inline void QQmlListModelParser::applyBindings(
        QObject *obj, const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
        const QList<const QV4::CompiledData::Binding *> &bindings)
{
    QQmlListModel *rv = static_cast<QQmlListModel *>(obj);

    rv->m_engine = qmlEngine(rv)->handle();
    rv->m_compilationUnit = compilationUnit;

    bool setRoles = false;

    for (const QV4::CompiledData::Binding *binding : bindings) {
        if (binding->type() != QV4::CompiledData::Binding::Type_Object)
            continue;
        setRoles |= applyProperty(
                compilationUnit, binding, rv->m_listModel, rv, /*outter element index*/-1);
    }

    if (setRoles == false)
        qmlWarning(obj) << "All ListElement declarations are empty, no roles can be created unless dynamicRoles is set.";
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 2888, as _ZN19QQmlListModelParser13applyPropertyERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEEPKNS1_12CompiledData7BindingEP9ListModelP13QQmlListModeli
inline bool QQmlListModelParser::applyProperty(
        const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
        const QV4::CompiledData::Binding *binding, ListModel *model, QQmlListModel *owner,
        int outterElementIndex)
{
    const QString elementName = compilationUnit->stringAt(binding->propertyNameIndex);

    bool roleSet = false;
    const QV4::CompiledData::Binding::Type bindingType = binding->type();
    if (bindingType >= QV4::CompiledData::Binding::Type_Object) {
        const quint32 targetObjectIndex = binding->value.objectIndex;
        const QV4::CompiledData::Object *target = compilationUnit->objectAt(targetObjectIndex);

        ListModel *subModel = nullptr;
        if (outterElementIndex == -1) {
            subModel = model;
        } else {
            const ListLayout::Role &role = model->getOrCreateListRole(elementName);
            if (role.type == ListLayout::Role::List) {
                subModel = model->getListProperty(outterElementIndex, role);
                if (subModel == nullptr) {
                    subModel = new ListModel(role.subLayout, nullptr);
                    model->setOrCreateProperty(
                            outterElementIndex, elementName,
                            QVariant::fromValue(subModel));
                }
            }
        }

        int elementIndex = subModel ? subModel->appendElement() : -1;

        const QV4::CompiledData::Binding *subBinding = target->bindingTable();
        for (quint32 i = 0; i < target->nBindings; ++i, ++subBinding) {
            roleSet |= applyProperty(compilationUnit, subBinding, subModel, owner, elementIndex);
        }
    } else if (!model) {
        return false;
    } else {
        QVariant value;

        const bool isTranslationBinding = binding->isTranslationBinding();
        if (isTranslationBinding) {
            value = QVariant::fromValue<const QV4::CompiledData::Binding*>(binding);
        } else if (binding->evaluatesToString()) {
            value = compilationUnit->bindingValueAsString(binding);
        } else if (bindingType == QV4::CompiledData::Binding::Type_Number) {
            value = compilationUnit->bindingValueAsNumber(binding);
        } else if (bindingType == QV4::CompiledData::Binding::Type_Boolean) {
            value = binding->valueAsBoolean();
        } else if (bindingType == QV4::CompiledData::Binding::Type_Null) {
            value = QVariant::fromValue(nullptr);
        } else if (bindingType == QV4::CompiledData::Binding::Type_Script) {
            QString scriptStr = compilationUnit->bindingValueAsScriptString(binding);
            if (definesEmptyList(scriptStr)) {
                value = QVariant::fromValue(
                        new ListModel(model->getOrCreateListRole(elementName).subLayout, nullptr));
            } else if (binding->isFunctionExpression()) {
                QQmlBinding::Identifier id = binding->value.compiledScriptIndex;
                Q_ASSERT(id != QQmlBinding::Invalid);

                auto v4 = compilationUnit->engine;
                QV4::Scope scope(v4);

                if (model->m_modelCache == nullptr) {
                    model->m_modelCache = new QQmlListModel(owner, model, v4);
                    QQmlEngine::setContextForObject(
                            model->m_modelCache, QQmlEngine::contextForObject(owner));
                }

                // for now we do not provide a context object; data from the ListElement must be passed to the function
                QV4::ScopedContext context(scope, QV4::QmlContext::create(v4->rootContext(), QQmlContextData::get(qmlContext(model->m_modelCache)), nullptr));
                QV4::ScopedFunctionObject function(scope, QV4::FunctionObject::createScriptFunction(context, compilationUnit->runtimeFunctions[id]));

                QJSValue v;
                QV4::ScopedValue result(scope, function->call(v4->globalObject, nullptr, 0));
                if (v4->hasException)
                    v4->catchException();
                else
                    QJSValuePrivate::setValue(&v, result);
                value.setValue(v);
            } else {
                bool ok;
                value = evaluateEnum(scriptStr, &ok);
            }
        } else {
            Q_UNREACHABLE();
        }

        model->setOrCreateProperty(outterElementIndex, elementName, value);
        auto listModel = model->m_modelCache;
        if (isTranslationBinding && listModel) {
            if (!listModel->translationChangeHandler) {
                auto ep = QQmlEnginePrivate::get(compilationUnit->engine);
                model->m_modelCache->translationChangeHandler = std::make_unique<QPropertyNotifier>(
                            ep->translationLanguage.addNotifier([listModel](){ listModel->updateTranslations(); }));
            }
        }
        roleSet = true;
    }
    return roleSet;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 2841, as _ZN19QQmlListModelParser14verifyPropertyERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEEPKNS2_7BindingE
inline bool QQmlListModelParser::verifyProperty(
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
        const QV4::CompiledData::Binding *binding)
{
    if (binding->type() >= QV4::CompiledData::Binding::Type_Object) {
        const quint32 targetObjectIndex = binding->value.objectIndex;
        const QV4::CompiledData::Object *target = compilationUnit->objectAt(targetObjectIndex);
        QString objName = compilationUnit->stringAt(target->inheritedTypeNameIndex);
        if (objName != listElementTypeName) {
            const QMetaObject *mo = resolveType(objName);
            if (mo != &QQmlListElement::staticMetaObject) {
                error(target, QQmlListModel::tr("ListElement: cannot contain nested elements"));
                return false;
            }
            listElementTypeName = objName; // cache right name for next time
        }

        if (!compilationUnit->stringAt(target->idNameIndex).isEmpty()) {
            error(target->locationOfIdProperty, QQmlListModel::tr("ListElement: cannot use reserved \"id\" property"));
            return false;
        }

        const QV4::CompiledData::Binding *binding = target->bindingTable();
        for (quint32 i = 0; i < target->nBindings; ++i, ++binding) {
            QString propName = compilationUnit->stringAt(binding->propertyNameIndex);
            if (propName.isEmpty()) {
                error(binding, QQmlListModel::tr("ListElement: cannot contain nested elements"));
                return false;
            }
            if (!verifyProperty(compilationUnit, binding))
                return false;
        }
    } else if (binding->type() == QV4::CompiledData::Binding::Type_Script) {
        QString scriptStr = compilationUnit->bindingValueAsScriptString(binding);
        if (!binding->isFunctionExpression() && !definesEmptyList(scriptStr)) {
            bool ok;
            evaluateEnum(scriptStr, &ok);
            if (!ok) {
                error(binding, QQmlListModel::tr("ListElement: cannot use script for property value"));
                return false;
            }
        }
    }

    return true;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 3029, as _ZN19QQmlListModelParser16definesEmptyListE11QStringView
inline bool QQmlListModelParser::definesEmptyList(QStringView s)
{
    if (s.startsWith(QLatin1Char('[')) && s.endsWith(QLatin1Char(']'))) {
        for (auto c : s.sliced(1).chopped(1)) {
            if (!c.isSpace())
                return false;
        }
        return true;
    }
    return false;
}
//  -----------------------------------------------------------------------

//  void QQmlListModelParser::verifyBindings(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlListModelParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE(
    QQmlListModelParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *bindings) {
  self->verifyBindings(*compilationUnit, *bindings);
}

//  void QQmlListModelParser::applyBindings(QObject *obj, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlListModelParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE(
    QQmlListModelParser *self,
    QObject *obj,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *bindings) {
  self->applyBindings(obj, *compilationUnit, *bindings);
}

//  bool QQmlListModelParser::definesEmptyList(QStringView s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlListModelParser16definesEmptyListE11QStringView(
    const QString *s) {
  return QQmlListModelParser::definesEmptyList(QStringView(*s));
}

//  QQmlListModelParser::~QQmlListModelParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlListModelParserD1Ev(QQmlListModelParser *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
