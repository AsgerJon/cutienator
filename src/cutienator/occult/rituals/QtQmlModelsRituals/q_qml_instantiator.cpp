//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlInstantiator that Python can take functions over in. Every QQmlInstantiator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlInstantiatorCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlInstantiatorCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlInstantiatorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlInstantiatorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInstantiatorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInstantiatorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInstantiatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInstantiatorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInstantiatorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlInstantiator : public QQmlInstantiator {
public:
  using QQmlInstantiator::QQmlInstantiator;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlInstantiator::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlInstantiatorCall0 call = reinterpret_cast<CuteQQmlInstantiatorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlInstantiator::classBegin();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlInstantiator::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlInstantiatorCall1 call = reinterpret_cast<CuteQQmlInstantiatorCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlInstantiator::componentComplete();
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlInstantiatorCall2 call = reinterpret_cast<CuteQQmlInstantiatorCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlInstantiatorCall3 call = reinterpret_cast<CuteQQmlInstantiatorCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlInstantiatorCall4 call = reinterpret_cast<CuteQQmlInstantiatorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlInstantiatorCall5 call = reinterpret_cast<CuteQQmlInstantiatorCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlInstantiatorCall6 call = reinterpret_cast<CuteQQmlInstantiatorCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlInstantiatorCall7 call = reinterpret_cast<CuteQQmlInstantiatorCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlInstantiatorCall8 call = reinterpret_cast<CuteQQmlInstantiatorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlInstantiator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlInstantiator10metaObjectEv(
    const QQmlInstantiator *self) {
  return self->metaObject();
}

//  QString QQmlInstantiator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlInstantiator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlInstantiator::tr(s, c, n));
}

//  QQmlInstantiator::QQmlInstantiator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlInstantiator *ritual_ZN16QQmlInstantiatorC1EP7QObject(QObject *parent) {
  return new CuteQQmlInstantiator(parent);
}

//  QQmlInstantiator::~QQmlInstantiator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiatorD1Ev(QQmlInstantiator *self) {
  delete self;
}

//  bool QQmlInstantiator::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlInstantiator8isActiveEv(const QQmlInstantiator *self) {
  return self->isActive();
}

//  void QQmlInstantiator::setActive(bool newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator9setActiveEb(
    QQmlInstantiator *self,
    bool newVal) {
  self->setActive(newVal);
}

//  bool QQmlInstantiator::isAsync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlInstantiator7isAsyncEv(const QQmlInstantiator *self) {
  return self->isAsync();
}

//  void QQmlInstantiator::setAsync(bool newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator8setAsyncEb(
    QQmlInstantiator *self,
    bool newVal) {
  self->setAsync(newVal);
}

//  int QQmlInstantiator::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlInstantiator5countEv(const QQmlInstantiator *self) {
  return self->count();
}

//  QQmlComponent *QQmlInstantiator::delegate()
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN16QQmlInstantiator8delegateEv(
    QQmlInstantiator *self) {
  return self->delegate();
}

//  void QQmlInstantiator::setDelegate(QQmlComponent *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator11setDelegateEP13QQmlComponent(
    QQmlInstantiator *self,
    QQmlComponent *c) {
  self->setDelegate(c);
}

//  QVariant QQmlInstantiator::model() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlInstantiator5modelEv(
    const QQmlInstantiator *self) {
  return new QVariant(self->model());
}

//  void QQmlInstantiator::setModel(const QVariant &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator8setModelERK8QVariant(
    QQmlInstantiator *self,
    const QVariant *v) {
  self->setModel(*v);
}

//  QQmlDelegateModel::DelegateModelAccess
//      QQmlInstantiator::delegateModelAccess() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel::DelegateModelAccess ritual_ZNK16QQmlInstantiator19delegateModelAccessEv(
    const QQmlInstantiator *self) {
  return self->delegateModelAccess();
}

//  void QQmlInstantiator::setDelegateModelAccess(QQmlDelegateModel::Delegate
//      ModelAccess delegateModelAccess)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator22setDelegateModelAccessEN17QQmlDelegateModel19DelegateModelAccessE(
    QQmlInstantiator *self,
    QQmlDelegateModel::DelegateModelAccess delegateModelAccess) {
  self->setDelegateModelAccess(delegateModelAccess);
}

//  QObject *QQmlInstantiator::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQmlInstantiator6objectEv(
    const QQmlInstantiator *self) {
  return self->object();
}

//  QObject *QQmlInstantiator::objectAt(int index) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQmlInstantiator8objectAtEi(
    const QQmlInstantiator *self,
    int index) {
  return self->objectAt(index);
}

//  void QQmlInstantiator::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator10classBeginEv(QQmlInstantiator *self) {
  self->classBegin();
}

//  void QQmlInstantiator::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlInstantiator17componentCompleteEv(
    QQmlInstantiator *self) {
  self->componentComplete();
}

//  QQmlInstantiatorPrivate *QQmlInstantiator::d_func()
extern "C" Q_DECL_EXPORT
QQmlInstantiatorPrivate *ritual_ZN16QQmlInstantiator6d_funcEv(
    QQmlInstantiator *self) {
  return self->d_func();
}

//  const QQmlInstantiatorPrivate *QQmlInstantiator::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlInstantiatorPrivate *ritual_ZNK16QQmlInstantiator6d_funcEv(
    const QQmlInstantiator *self) {
  return self->d_func();
}

//  QQmlInstantiator as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlInstantiator_QQmlParserStatus(
    QQmlInstantiator *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlInstantiator, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlInstantiator(
    QQmlInstantiator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlInstantiator *>(self)->take(key, call);
}

//  void QQmlInstantiator::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlInstantiator10classBeginEv(QQmlInstantiator *self) {
  self->QQmlInstantiator::classBegin();
}

//  void QQmlInstantiator::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlInstantiator17componentCompleteEv(
    QQmlInstantiator *self) {
  self->QQmlInstantiator::componentComplete();
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
