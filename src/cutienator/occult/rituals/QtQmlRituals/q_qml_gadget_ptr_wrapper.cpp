//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlGadgetPtrWrapper that Python can take functions over in. Every QQmlGadgetPtrWrapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGadgetPtrWrapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGadgetPtrWrapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGadgetPtrWrapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGadgetPtrWrapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGadgetPtrWrapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGadgetPtrWrapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGadgetPtrWrapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlGadgetPtrWrapper : public QQmlGadgetPtrWrapper {
public:
  using QQmlGadgetPtrWrapper::QQmlGadgetPtrWrapper;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall0 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall1 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall2 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall3 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall4 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall5 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlGadgetPtrWrapperCall6 call = reinterpret_cast<CuteQQmlGadgetPtrWrapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlGadgetPtrWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlGadgetPtrWrapper10metaObjectEv(
    const QQmlGadgetPtrWrapper *self) {
  return self->metaObject();
}

//  QString QQmlGadgetPtrWrapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlGadgetPtrWrapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlGadgetPtrWrapper::tr(s, c, n));
}

//  QQmlGadgetPtrWrapper *QQmlGadgetPtrWrapper::instance(QQmlEngine *engine,
//      QMetaType type)
extern "C" Q_DECL_EXPORT
QQmlGadgetPtrWrapper *ritual_ZN20QQmlGadgetPtrWrapper8instanceEP10QQmlEngine9QMetaType(
    QQmlEngine *engine,
    const QMetaType *type) {
  return QQmlGadgetPtrWrapper::instance(engine, *type);
}

//  QQmlGadgetPtrWrapper::QQmlGadgetPtrWrapper(QQmlValueType *valueType,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlGadgetPtrWrapper *ritual_ZN20QQmlGadgetPtrWrapperC1EP13QQmlValueTypeP7QObject(
    QQmlValueType *valueType,
    QObject *parent) {
  return new CuteQQmlGadgetPtrWrapper(valueType, parent);
}

//  QQmlGadgetPtrWrapper::~QQmlGadgetPtrWrapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGadgetPtrWrapperD1Ev(QQmlGadgetPtrWrapper *self) {
  delete self;
}

//  void QQmlGadgetPtrWrapper::read(QObject *obj, int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGadgetPtrWrapper4readEP7QObjecti(
    QQmlGadgetPtrWrapper *self,
    QObject *obj,
    int idx) {
  self->read(obj, idx);
}

//  void QQmlGadgetPtrWrapper::write(QObject *obj, int idx,
//      QQmlPropertyData::WriteFlags flags, int internalIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QQmlGadgetPtrWrapper5writeEP7QObjecti6QFlagsIN16QQmlPropertyData9WriteFlagEEi(
    const QQmlGadgetPtrWrapper *self,
    QObject *obj,
    int idx,
    int flags,
    int internalIndex) {
  self->write(
      obj,
      idx,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags),
      internalIndex);
}

//  QVariant QQmlGadgetPtrWrapper::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQmlGadgetPtrWrapper5valueEv(
    const QQmlGadgetPtrWrapper *self) {
  return new QVariant(self->value());
}

//  void QQmlGadgetPtrWrapper::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGadgetPtrWrapper8setValueERK8QVariant(
    QQmlGadgetPtrWrapper *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  QMetaType QQmlGadgetPtrWrapper::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK20QQmlGadgetPtrWrapper8metaTypeEv(
    const QQmlGadgetPtrWrapper *self) {
  return new QMetaType(self->metaType());
}

//  QMetaProperty QQmlGadgetPtrWrapper::property(int index) const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK20QQmlGadgetPtrWrapper8propertyEi(
    const QQmlGadgetPtrWrapper *self,
    int index) {
  return new QMetaProperty(self->property(index));
}

//  QVariant QQmlGadgetPtrWrapper::readOnGadget(const QMetaProperty
//      &property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQmlGadgetPtrWrapper12readOnGadgetERK13QMetaProperty(
    const QQmlGadgetPtrWrapper *self,
    const QMetaProperty *property) {
  return new QVariant(self->readOnGadget(*property));
}

//  void QQmlGadgetPtrWrapper::writeOnGadget(const QMetaProperty &property,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlGadgetPtrWrapper13writeOnGadgetERK13QMetaPropertyRK8QVariant(
    QQmlGadgetPtrWrapper *self,
    const QMetaProperty *property,
    const QVariant *value) {
  self->writeOnGadget(*property, *value);
}

//  const QQmlValueType *QQmlGadgetPtrWrapper::valueType() const
extern "C" Q_DECL_EXPORT
const QQmlValueType *ritual_ZNK20QQmlGadgetPtrWrapper9valueTypeEv(
    const QQmlGadgetPtrWrapper *self) {
  return self->valueType();
}

//  a Python function taken by a CuteQQmlGadgetPtrWrapper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGadgetPtrWrapper(
    QQmlGadgetPtrWrapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGadgetPtrWrapper *>(self)->take(key, call);
}
