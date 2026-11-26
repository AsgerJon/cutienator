//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpropertychanges_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpropertychanges_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickpropertychanges_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/qqmlexpression.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQuick/private/qquickstate_p_p.h>
#include <QtQml/private/qqmlboundsignal_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qqmlpropertybinding_p.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtCore/qdebug.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickpropertychanges.cpp, line 339, as _ZN27QQuickPropertyChangesParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE
inline void QQuickPropertyChangesParser::verifyBindings(
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
        const QList<const QV4::CompiledData::Binding *> &props)
{
    for (int ii = 0; ii < props.size(); ++ii)
        verifyList(compilationUnit, props.at(ii));
}

//  from ../qtdeclarative/src/quick/util/qquickpropertychanges.cpp, line 218, as _ZN27QQuickPropertyChangesParser10verifyListERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEEPKNS2_7BindingE
inline void QQuickPropertyChangesParser::verifyList(
        const QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
        const QV4::CompiledData::Binding *binding)
{
    switch (binding->type()) {
    case QV4::CompiledData::Binding::Type_Object:
        error(compilationUnit->objectAt(binding->value.objectIndex),
              QQuickPropertyChanges::tr(
                      "PropertyChanges does not support creating state-specific objects."));
        break;
    case QV4::CompiledData::Binding::Type_GroupProperty:
    case QV4::CompiledData::Binding::Type_AttachedProperty: {
        const QV4::CompiledData::Object *subObj = compilationUnit->objectAt(binding->value.objectIndex);
        const QV4::CompiledData::Binding *subBinding = subObj->bindingTable();
        for (quint32 i = 0; i < subObj->nBindings; ++i, ++subBinding)
            verifyList(compilationUnit, subBinding);
        break;
    }
    default:
        break;
    }
}
//  -----------------------------------------------------------------------

//  void QQuickPropertyChangesParser::verifyList(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
//      const QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPropertyChangesParser10verifyListERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEEPKNS2_7BindingE(
    QQuickPropertyChangesParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    const QV4::CompiledData::Binding *binding) {
  self->verifyList(*compilationUnit, binding);
}

//  void QQuickPropertyChangesParser::verifyBindings(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &props)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPropertyChangesParser14verifyBindingsERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK5QListIPKNS2_7BindingEE(
    QQuickPropertyChangesParser *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *props) {
  self->verifyBindings(*compilationUnit, *props);
}

//  void QQuickPropertyChangesParser::applyBindings(QObject *obj, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QList<const QV4::CompiledData::Binding *> &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPropertyChangesParser13applyBindingsEP7QObjectRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERK5QListIPKNS3_12CompiledData7BindingEE(
    QQuickPropertyChangesParser *self,
    QObject *obj,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QList<const QV4::CompiledData::Binding *> *bindings) {
  self->applyBindings(obj, *compilationUnit, *bindings);
}

//  QQuickPropertyChangesParser::~QQuickPropertyChangesParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPropertyChangesParserD1Ev(
    QQuickPropertyChangesParser *self) {
  delete self;
}
