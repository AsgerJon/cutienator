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

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 72, as _ZN39QQmlPropertyToUnbindablePropertyBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE
inline void QQmlPropertyToUnbindablePropertyBinding::setEnabled(
        bool e, QQmlPropertyData::WriteFlags flags)
{
    const bool wasEnabled = enabledFlag();
    setEnabledFlag(e);
    updateCanUseAccessor();
    if (e && !wasEnabled)
        update(flags);
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 82, as _ZN39QQmlPropertyToUnbindablePropertyBinding6updateE6QFlagsIN16QQmlPropertyData9WriteFlagEE
inline void QQmlPropertyToUnbindablePropertyBinding::update(QQmlPropertyData::WriteFlags flags)
{
    if (!enabledFlag())
        return;

    // Check that the target has not been deleted
    QObject *target = targetObject();
    if (QQmlData::wasDeleted(target))
        return;

    const QQmlPropertyData *d = nullptr;
    QQmlPropertyData vtd;
    getPropertyData(&d, &vtd);
    Q_ASSERT(d);

    // Check for a binding update loop
    if (Q_UNLIKELY(updatingFlag()))
        return;

    setUpdatingFlag(true);

    if (canUseAccessor())
        flags.setFlag(QQmlPropertyData::BypassInterceptor);

    QVariant value = m_binding.readSourceValue(
            [&](const QMetaObject *sourceMetaObject, const QMetaProperty &property) {
        captureProperty(sourceMetaObject, property);
    });

    QV4::ExecutionEngine *v4 = m_binding.engine->handle();
    Q_ASSERT(v4);

    const QMetaType targetMetaType = vtd.isValid() ? vtd.propType() : d->propType();
    const QMetaType valueMetaType = value.metaType();

    if (valueMetaType != targetMetaType && targetMetaType != QMetaType::fromType<QVariant>()) {
        // Coerce the value to the target type using JavaScript semantics.
        // Don't use QQmlProperty's internal coercion. It's not the same.
        QVariant coerced(targetMetaType);
        QV4::Scope scope(v4);
        QV4::ScopedValue jsValue(
                scope, value.isValid()
                        ? v4->metaTypeToJS(valueMetaType, value.constData())
                        : QV4::Encode::undefined());

        // If the coercion fails, let writeValueProperty() do its thing after all.
        if (QV4::ExecutionEngine::metaTypeFromJS(jsValue, targetMetaType, coerced.data()))
            value = std::move(coerced);
    }

    QQmlPropertyPrivate::writeValueProperty(target, *d, vtd, value, {}, flags);
    setUpdatingFlag(false);
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 136, as _ZN39QQmlPropertyToUnbindablePropertyBindingC2EP10QQmlEngineRK12QQmlPropertyS4_
inline QQmlPropertyToUnbindablePropertyBinding::QQmlPropertyToUnbindablePropertyBinding(
        QQmlEngine *engine, const QQmlProperty &source, const QQmlProperty &target)
    : m_binding(engine, source)
{
    setTarget(target);
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 67, as _ZNK39QQmlPropertyToUnbindablePropertyBinding4kindEv
inline QQmlAbstractBinding::Kind QQmlPropertyToUnbindablePropertyBinding::kind() const
{
    return PropertyToPropertyBinding;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 150, as _ZN39QQmlBindableToUnbindablePropertyBinding6updateEP17QPropertyObserverP20QUntypedPropertyData
inline void QQmlBindableToUnbindablePropertyBinding::update(
        QPropertyObserver *observer, QUntypedPropertyData *)
{
    static_cast<QQmlBindableToUnbindablePropertyBinding *>(observer)
            ->QQmlPropertyToUnbindablePropertyBinding::update();
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 164, as _ZN39QQmlBindableToUnbindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty
inline void QQmlBindableToUnbindablePropertyBinding::captureProperty(
        const QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)
{
    Q_UNUSED(sourceProperty);

    // We have already captured.
    if (m_isObserving)
        return;

    QUntypedBindable bindable;
    void *argv[] = { &bindable };
    sourceMetaObject->metacall(
            m_binding.sourceObject, QMetaObject::BindableProperty,
            m_binding.sourcePropertyIndex.coreIndex(), argv);
    bindable.observe(this);
    m_isObserving = true;
}
//  -----------------------------------------------------------------------

//  void QQmlBindableToUnbindablePropertyBinding::update(QPropertyObserver
//      *observer, QUntypedPropertyData *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlBindableToUnbindablePropertyBinding6updateEP17QPropertyObserverP20QUntypedPropertyData(
    QPropertyObserver *observer,
    QUntypedPropertyData *a1) {
  QQmlBindableToUnbindablePropertyBinding::update(observer, a1);
}

//  void QQmlBindableToUnbindablePropertyBinding::captureProperty(const
//      QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlBindableToUnbindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty(
    QQmlBindableToUnbindablePropertyBinding *self,
    const QMetaObject *sourceMetaObject,
    const QMetaProperty *sourceProperty) {
  self->captureProperty(sourceMetaObject, *sourceProperty);
}

//  QQmlBindableToUnbindablePropertyBinding as the
//      QQmlPropertyToUnbindablePropertyBinding it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyToUnbindablePropertyBinding *ritual_cast_QQmlBindableToUnbindablePropertyBinding_QQmlPropertyToUnbindablePropertyBinding(
    QQmlBindableToUnbindablePropertyBinding *self) {
  return static_cast<QQmlPropertyToUnbindablePropertyBinding *>(self);
}
