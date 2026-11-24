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

//  from ../qtdeclarative/src/qml/qml/qqmlpropertytopropertybinding.cpp, line 157, as _ZN41QQmlUnbindableToUnbindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty
inline void QQmlUnbindableToUnbindablePropertyBinding::captureProperty(
        const QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)
{
    Q_UNUSED(sourceMetaObject);
    m_binding.doConnectNotify(this, sourceProperty);
}
//  -----------------------------------------------------------------------

//  A QQmlUnbindableToUnbindablePropertyBinding that Python can take functions over in. Every QQmlUnbindableToUnbindablePropertyBinding
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQQmlUnbindableToUnbindablePropertyBindingCall0)(const void *, int *);
typedef void (*CuteQQmlUnbindableToUnbindablePropertyBindingCall1)(const void *, const QQmlProperty *, int *);
class CuteQQmlUnbindableToUnbindablePropertyBinding : public QQmlUnbindableToUnbindablePropertyBinding {
public:
  using QQmlUnbindableToUnbindablePropertyBinding::QQmlUnbindableToUnbindablePropertyBinding;
  CuteQQmlUnbindableToUnbindablePropertyBinding(const QQmlUnbindableToUnbindablePropertyBinding &other) : QQmlUnbindableToUnbindablePropertyBinding(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QQmlAbstractBinding10expressionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProperty")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QString QQmlAbstractBinding::expression() const
  QString expression() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlUnbindableToUnbindablePropertyBindingCall0 call = reinterpret_cast<CuteQQmlUnbindableToUnbindablePropertyBindingCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQQmlUnbindableToUnbindablePropertyBindingCall1 call = reinterpret_cast<CuteQQmlUnbindableToUnbindablePropertyBindingCall1>(taken[1]);
      call(this, &prop, &handled);
      if (handled) return;
    }
    QQmlAbstractBinding::printBindingLoopError(prop);
  }
};

//  void QQmlUnbindableToUnbindablePropertyBinding::captureProperty(const
//      QMetaObject *sourceMetaObject, const QMetaProperty &sourceProperty)
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQmlUnbindableToUnbindablePropertyBinding15capturePropertyEPK11QMetaObjectRK13QMetaProperty(
    QQmlUnbindableToUnbindablePropertyBinding *self,
    const QMetaObject *sourceMetaObject,
    const QMetaProperty *sourceProperty) {
  self->captureProperty(sourceMetaObject, *sourceProperty);
}

//  QQmlUnbindableToUnbindablePropertyBinding::~QQmlUnbindableToUnbindablePro
//      pertyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN41QQmlUnbindableToUnbindablePropertyBindingD1Ev(
    QQmlUnbindableToUnbindablePropertyBinding *self) {
  delete self;
}

//  QQmlUnbindableToUnbindablePropertyBinding as the
//      QQmlPropertyToUnbindablePropertyBinding it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyToUnbindablePropertyBinding *ritual_cast_QQmlUnbindableToUnbindablePropertyBinding_QQmlPropertyToUnbindablePropertyBinding(
    QQmlUnbindableToUnbindablePropertyBinding *self) {
  return static_cast<QQmlPropertyToUnbindablePropertyBinding *>(self);
}

//  a Python function taken by a
//      CuteQQmlUnbindableToUnbindablePropertyBinding, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlUnbindableToUnbindablePropertyBinding(
    QQmlUnbindableToUnbindablePropertyBinding *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlUnbindableToUnbindablePropertyBinding *>(self)->take(key, call);
}
