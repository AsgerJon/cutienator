//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlproperty.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmlpropertytopropertybinding_p.h"
#include <private/qqmlanybinding_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmlproperty_p.h>
#include <private/qqmlvmemetaobject_p.h>
#include <private/qv4alloca_p.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 52, as _ZN29QQmlPropertyToPropertyBindingC1EP10QQmlEngineRK12QQmlProperty
inline QQmlPropertyToPropertyBinding::QQmlPropertyToPropertyBinding(
        QQmlEngine *engine, const QQmlProperty &source)
    : engine(engine)
    , sourceObject(source.object())
    , sourcePropertyIndex(QQmlPropertyPrivate::get(source)->encodedIndex())
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 193, as _ZN37QQmlPropertyToBindablePropertyBindingC1EP10QQmlEngineRK12QQmlPropertyS4_PKN9QtPrivate21BindingFunctionVTableE
inline QQmlPropertyToBindablePropertyBinding::QQmlPropertyToBindablePropertyBinding(
        QQmlEngine *engine, const QQmlProperty &source, const QQmlProperty &target,
        const QtPrivate::BindingFunctionVTable *vtable)
    : QQmlPropertyBindingBase(target.object(), QQmlPropertyPrivate::propertyIndex(target),
                              target.propertyMetaType(), vtable, BindingKind::PropertyToProperty),
      m_binding(engine, source)
{
    errorCallBack = [](QPropertyBindingPrivate *that) {
        auto self = static_cast<QQmlPropertyToBindablePropertyBinding *>(that);
        if (self->m_binding.engine) {
            const auto error = self->bindingError();
            if (error.type() == QPropertyBindingError::BindingLoop) {
                qmlWarning(self->m_binding.sourceObject)
                        << QStringLiteral("Binding loop detected for property bound to ")
                        << self->propertyDataPtr;
            }
        }
    };
}
//  -----------------------------------------------------------------------

//  QQmlPropertyToBindablePropertyBinding::QQmlPropertyToBindablePropertyBind
//      ing(QQmlEngine *engine, const QQmlProperty &source, const
//      QQmlProperty &target, const QtPrivate::BindingFunctionVTable *vtable)
extern "C" Q_DECL_EXPORT
QQmlPropertyToBindablePropertyBinding *ritual_ZN37QQmlPropertyToBindablePropertyBindingC1EP10QQmlEngineRK12QQmlPropertyS4_PKN9QtPrivate21BindingFunctionVTableE(
    QQmlEngine *engine,
    const QQmlProperty *source,
    const QQmlProperty *target,
    const QtPrivate::BindingFunctionVTable *vtable) {
  return new QQmlPropertyToBindablePropertyBinding(
      engine,
      *source,
      *target,
      vtable);
}

//  QObject *QQmlPropertyToBindablePropertyBinding::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK37QQmlPropertyToBindablePropertyBinding6sourceEv(
    const QQmlPropertyToBindablePropertyBinding *self) {
  return self->source();
}
