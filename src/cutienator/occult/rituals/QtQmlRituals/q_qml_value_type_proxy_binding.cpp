//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetypeproxybinding_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetypeproxybinding_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/qqmlproperty.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlvaluetypeproxybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypeproxybinding.cpp, line 31, as _ZN25QQmlValueTypeProxyBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE
inline void QQmlValueTypeProxyBinding::setEnabled(bool e, QQmlPropertyData::WriteFlags flags)
{
    QQmlAbstractBinding *b = m_bindings.data();
    while (b) {
        b->setEnabled(e, flags);
        b = b->nextBinding();
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypeproxybinding.cpp, line 22, as _ZN25QQmlValueTypeProxyBindingD1Ev
inline QQmlValueTypeProxyBinding::~QQmlValueTypeProxyBinding()
{
    QQmlAbstractBinding *binding = m_bindings.data();
    while (binding) {
        binding->setAddedToObject(false);
        binding = binding->nextBinding();
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypeproxybinding.cpp, line 14, as _ZN25QQmlValueTypeProxyBindingC1EP7QObject17QQmlPropertyIndex
inline QQmlValueTypeProxyBinding::QQmlValueTypeProxyBinding(QObject *o, QQmlPropertyIndex index)
    : QQmlAbstractBinding(),
      m_bindings(nullptr)
{
    m_target = o;
    m_targetIndex = index;
}

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypeproxybinding.cpp, line 40, as _ZNK25QQmlValueTypeProxyBinding7bindingE17QQmlPropertyIndex
inline QQmlAbstractBinding *QQmlValueTypeProxyBinding::binding(QQmlPropertyIndex propertyIndex) const
{
    QQmlAbstractBinding *binding = m_bindings.data();

    while (binding && binding->targetPropertyIndex() != propertyIndex)
        binding = binding->nextBinding();

    return binding;
}

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypeproxybinding.cpp, line 55, as _ZN25QQmlValueTypeProxyBinding14removeBindingsEj
inline void QQmlValueTypeProxyBinding::removeBindings(quint32 mask)
{
    QQmlAbstractBinding *binding = m_bindings.data();
    QQmlAbstractBinding *lastBinding = nullptr;

    while (binding) {
        const int valueTypeIndex = binding->targetPropertyIndex().valueTypeIndex();
        if (valueTypeIndex != -1 && (mask & (1 << valueTypeIndex))) {
            QQmlAbstractBinding *remove = binding;
            remove->setAddedToObject(false);
            binding = remove->nextBinding();

            if (lastBinding == nullptr)
                m_bindings = remove->nextBinding();
            else
                lastBinding->setNextBinding(remove->nextBinding());
        } else {
            lastBinding = binding;
            binding = binding->nextBinding();
        }
    }
}
//  -----------------------------------------------------------------------

//  A QQmlValueTypeProxyBinding that Python can take functions over in. Every QQmlValueTypeProxyBinding
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlValueTypeProxyBindingCall0)(const void *, bool, int, int *);
typedef QString * (*CuteQQmlValueTypeProxyBindingCall1)(const void *, int *);
typedef void (*CuteQQmlValueTypeProxyBindingCall2)(const void *, const QQmlProperty *, int *);
class CuteQQmlValueTypeProxyBinding : public QQmlValueTypeProxyBinding {
public:
  using QQmlValueTypeProxyBinding::QQmlValueTypeProxyBinding;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQmlAbstractBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE")) {
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

  //  void QQmlValueTypeProxyBinding::setEnabled(bool a0,
  //      QQmlPropertyData::WriteFlags a1)
  void setEnabled(bool a0, QQmlPropertyData::WriteFlags a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlValueTypeProxyBindingCall0 call = reinterpret_cast<CuteQQmlValueTypeProxyBindingCall0>(taken[0]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QQmlValueTypeProxyBinding::setEnabled(a0, a1);
  }

  //  QString QQmlAbstractBinding::expression() const
  QString expression() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlValueTypeProxyBindingCall1 call = reinterpret_cast<CuteQQmlValueTypeProxyBindingCall1>(taken[1]);
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
      CuteQQmlValueTypeProxyBindingCall2 call = reinterpret_cast<CuteQQmlValueTypeProxyBindingCall2>(taken[2]);
      call(this, &prop, &handled);
      if (handled) return;
    }
    QQmlAbstractBinding::printBindingLoopError(prop);
  }
};

//  QQmlValueTypeProxyBinding::QQmlValueTypeProxyBinding(QObject *o,
//      QQmlPropertyIndex coreIndex)
extern "C" Q_DECL_EXPORT
QQmlValueTypeProxyBinding *ritual_ZN25QQmlValueTypeProxyBindingC1EP7QObject17QQmlPropertyIndex(
    QObject *o,
    const QQmlPropertyIndex *coreIndex) {
  return new CuteQQmlValueTypeProxyBinding(o, *coreIndex);
}

//  QQmlAbstractBinding *QQmlValueTypeProxyBinding::subBindings() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZNK25QQmlValueTypeProxyBinding11subBindingsEv(
    const QQmlValueTypeProxyBinding *self) {
  return self->subBindings();
}

//  QQmlAbstractBinding *QQmlValueTypeProxyBinding::binding(QQmlPropertyIndex
//      targetPropertyIndex) const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZNK25QQmlValueTypeProxyBinding7bindingE17QQmlPropertyIndex(
    const QQmlValueTypeProxyBinding *self,
    const QQmlPropertyIndex *targetPropertyIndex) {
  return self->binding(*targetPropertyIndex);
}

//  void QQmlValueTypeProxyBinding::removeBindings(quint32 mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlValueTypeProxyBinding14removeBindingsEj(
    QQmlValueTypeProxyBinding *self,
    quint32 mask) {
  self->removeBindings(mask);
}

//  void QQmlValueTypeProxyBinding::setEnabled(bool a0,
//      QQmlPropertyData::WriteFlags a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlValueTypeProxyBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlValueTypeProxyBinding *self,
    bool a0,
    int a1) {
  self->setEnabled(a0, QFlags<QQmlPropertyData::WriteFlag>::fromInt(a1));
}

//  Kind QQmlValueTypeProxyBinding::kind() const
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding::Kind ritual_ZNK25QQmlValueTypeProxyBinding4kindEv(
    const QQmlValueTypeProxyBinding *self) {
  return self->kind();
}

//  QQmlValueTypeProxyBinding::~QQmlValueTypeProxyBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlValueTypeProxyBindingD1Ev(
    QQmlValueTypeProxyBinding *self) {
  delete self;
}

//  a Python function taken by a CuteQQmlValueTypeProxyBinding, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlValueTypeProxyBinding(
    QQmlValueTypeProxyBinding *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlValueTypeProxyBinding *>(self)->take(key, call);
}

//  void QQmlValueTypeProxyBinding::setEnabled(bool a0,
//      QQmlPropertyData::WriteFlags a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQmlValueTypeProxyBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlValueTypeProxyBinding *self,
    bool a0,
    int a1) {
  self->QQmlValueTypeProxyBinding::setEnabled(
      a0,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(a1));
}
