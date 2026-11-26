//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertytopropertybinding_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 183, as local:qqmlpropertytopropertybinding.cpp:bindingFunctionVTableForQQmlPropertyToBindablePropertyBinding
namespace QtPrivate {
template<typename Binding>
inline constexpr BindingFunctionVTable
    bindingFunctionVTableForQQmlPropertyToBindablePropertyBinding = {
        &QQmlPropertyToBindablePropertyBinding::update<Binding>,
        [](void *qpropertyBinding) { delete reinterpret_cast<Binding *>(qpropertyBinding); },
        [](void *, void *){},
        0
    };
}  // namespace QtPrivate

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 223, as _ZN39QQmlUnbindableToBindablePropertyBinding6updateEv
inline void QQmlUnbindableToBindablePropertyBinding::update()
{
    PendingBindingObserverList bindingObservers;
    evaluateRecursive(bindingObservers);

    if (const QPropertyBindingError error = bindingError();
            Q_UNLIKELY(error.type() == QPropertyBindingError::BindingLoop)) {
        return;
    }

    notifyNonRecursive(bindingObservers);
}
//  -----------------------------------------------------------------------

//  void QQmlUnbindableToBindablePropertyBinding::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlUnbindableToBindablePropertyBinding6updateEv(
    QQmlUnbindableToBindablePropertyBinding *self) {
  self->update();
}

//  void QQmlUnbindableToBindablePropertyBinding::captureProperty(const
//      QMetaObject *a0, const QMetaProperty &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlUnbindableToBindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty(
    QQmlUnbindableToBindablePropertyBinding *self,
    const QMetaObject *a0,
    const QMetaProperty *property) {
  self->captureProperty(a0, *property);
}

//  QQmlUnbindableToBindablePropertyBinding as the QQmlNotifierEndpoint it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlNotifierEndpoint *ritual_cast_QQmlUnbindableToBindablePropertyBinding_QQmlNotifierEndpoint(
    QQmlUnbindableToBindablePropertyBinding *self) {
  return static_cast<QQmlNotifierEndpoint *>(self);
}
