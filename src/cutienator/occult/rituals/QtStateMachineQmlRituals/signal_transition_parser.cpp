//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/signaltransition_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/signaltransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/private/signaltransition_p.h>
#include <QtStateMachine/QStateMachine>
#include <QtCore/QMetaProperty>
#include <QtQml/QQmlInfo>
#include <QtQml/QQmlEngine>
#include <QtQml/QQmlContext>
#include <QtQml/QQmlExpression>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/statemachineqml/signaltransition.cpp, line 190, as _ZN22SignalTransitionParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE
inline void SignalTransitionParser::verifyBindings(
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
        const QList<const QV4::CompiledData::Binding *> &props)
{
    for (int ii = 0; ii < props.size(); ++ii) {
        const QV4::CompiledData::Binding *binding = props.at(ii);

        QString propName = compilationUnit->stringAt(binding->propertyNameIndex);

        if (propName != QLatin1String("onTriggered")) {
            error(props.at(ii), SignalTransition::tr("Cannot assign to non-existent property \"%1\"").arg(propName));
            return;
        }

        if (binding->type() != QV4::CompiledData::Binding::Type_Script) {
            error(binding, SignalTransition::tr("SignalTransition: script expected"));
            return;
        }
    }
}

//  from ../qtscxml/src/statemachineqml/signaltransition.cpp, line 211, as _ZN22SignalTransitionParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE
inline void SignalTransitionParser::applyBindings(
        QObject *object, const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
        const QList<const QV4::CompiledData::Binding *> &bindings)
{
    SignalTransition *st = qobject_cast<SignalTransition*>(object);
    st->m_compilationUnit = compilationUnit;
    st->m_bindings = bindings;
}
//  -----------------------------------------------------------------------

//  void SignalTransitionParser::verifyBindings(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &props)
extern "C" Q_DECL_EXPORT
void ritual_ZN22SignalTransitionParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE(
    SignalTransitionParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *props) {
  self->verifyBindings(*compilationUnit, *props);
}

//  void SignalTransitionParser::applyBindings(QObject *object, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN22SignalTransitionParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE(
    SignalTransitionParser *self,
    QObject *object,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *bindings) {
  self->applyBindings(object, *compilationUnit, *bindings);
}

//  SignalTransitionParser::~SignalTransitionParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN22SignalTransitionParserD1Ev(SignalTransitionParser *self) {
  delete self;
}
