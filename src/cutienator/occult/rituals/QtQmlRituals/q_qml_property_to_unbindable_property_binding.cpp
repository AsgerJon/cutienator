//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlproperty.h>
#include <cstring>
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

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 67, as _ZNK39QQmlPropertyToUnbindablePropertyBinding4kindEv
inline QQmlAbstractBinding::Kind QQmlPropertyToUnbindablePropertyBinding::kind() const
{
    return PropertyToPropertyBinding;
}

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
//  -----------------------------------------------------------------------

//  A QQmlPropertyToUnbindablePropertyBinding that Python can take functions over in. Every QQmlPropertyToUnbindablePropertyBinding
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlPropertyToUnbindablePropertyBindingCall0)(const void *, const QMetaObject *, const QMetaProperty *, int *);
typedef QString * (*CuteQQmlPropertyToUnbindablePropertyBindingCall1)(const void *, int *);
typedef void (*CuteQQmlPropertyToUnbindablePropertyBindingCall2)(const void *, const QQmlProperty *, int *);
class CuteQQmlPropertyToUnbindablePropertyBinding : public QQmlPropertyToUnbindablePropertyBinding {
public:
  using QQmlPropertyToUnbindablePropertyBinding::QQmlPropertyToUnbindablePropertyBinding;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN39QQmlPropertyToUnbindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QQmlAbstractBinding10expressionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProperty")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QQmlPropertyToUnbindablePropertyBinding::captureProperty(const
  //      QMetaObject *sourceMetaObject, const QMetaProperty
  //      &sourceProperty)
  void captureProperty(
      const QMetaObject *sourceMetaObject,
      const QMetaProperty &sourceProperty) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPropertyToUnbindablePropertyBindingCall0 call = reinterpret_cast<CuteQQmlPropertyToUnbindablePropertyBindingCall0>(taken[0]);
      call(this, sourceMetaObject, &sourceProperty, &handled);
      if (handled) return;
    }
  }

  //  QString QQmlAbstractBinding::expression() const
  QString expression() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlPropertyToUnbindablePropertyBindingCall1 call = reinterpret_cast<CuteQQmlPropertyToUnbindablePropertyBindingCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlAbstractBinding::expression();
  }

  //  void QQmlAbstractBinding::printBindingLoopError(const QQmlProperty
  //      &prop)
  void printBindingLoopError(const QQmlProperty &prop) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlPropertyToUnbindablePropertyBindingCall2 call = reinterpret_cast<CuteQQmlPropertyToUnbindablePropertyBindingCall2>(taken[2]);
      call(this, &prop, &handled);
      if (handled) return;
    }
    QQmlAbstractBinding::printBindingLoopError(prop);
  }
};

//  Kind QQmlPropertyToUnbindablePropertyBinding::kind() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding::Kind ritual_ZNK39QQmlPropertyToUnbindablePropertyBinding4kindEv(
    const QQmlPropertyToUnbindablePropertyBinding *self) {
  return self->kind();
}

//  void QQmlPropertyToUnbindablePropertyBinding::setEnabled(bool e,
//      QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlPropertyToUnbindablePropertyBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlPropertyToUnbindablePropertyBinding *self,
    bool e,
    int flags) {
  self->setEnabled(e, QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  void QQmlPropertyToUnbindablePropertyBinding::update(QQmlPropertyData::Wr
//      iteFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlPropertyToUnbindablePropertyBinding6updateE6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlPropertyToUnbindablePropertyBinding *self,
    int flags) {
  self->update(QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  QObject *QQmlPropertyToUnbindablePropertyBinding::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK39QQmlPropertyToUnbindablePropertyBinding6sourceEv(
    const QQmlPropertyToUnbindablePropertyBinding *self) {
  return self->source();
}

//  void QQmlPropertyToUnbindablePropertyBinding::captureProperty(const
//      QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QQmlPropertyToUnbindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty(
    QQmlPropertyToUnbindablePropertyBinding *self,
    const QMetaObject *sourceMetaObject,
    const QMetaProperty *sourceProperty) {
  self->captureProperty(sourceMetaObject, *sourceProperty);
}

//  a Python function taken by a CuteQQmlPropertyToUnbindablePropertyBinding,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPropertyToUnbindablePropertyBinding(
    QQmlPropertyToUnbindablePropertyBinding *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPropertyToUnbindablePropertyBinding *>(self)->take(key, call);
}
