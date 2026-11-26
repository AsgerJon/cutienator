//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qdeclarativepluginparameter_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativepluginparameter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDeclarativePluginParameter that Python can take functions over in. Every QDeclarativePluginParameter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePluginParameterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePluginParameterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePluginParameterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePluginParameterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePluginParameterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePluginParameterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePluginParameterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativePluginParameter : public QDeclarativePluginParameter {
public:
  using QDeclarativePluginParameter::QDeclarativePluginParameter;
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
      CuteQDeclarativePluginParameterCall0 call = reinterpret_cast<CuteQDeclarativePluginParameterCall0>(taken[0]);
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
      CuteQDeclarativePluginParameterCall1 call = reinterpret_cast<CuteQDeclarativePluginParameterCall1>(taken[1]);
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
      CuteQDeclarativePluginParameterCall2 call = reinterpret_cast<CuteQDeclarativePluginParameterCall2>(taken[2]);
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
      CuteQDeclarativePluginParameterCall3 call = reinterpret_cast<CuteQDeclarativePluginParameterCall3>(taken[3]);
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
      CuteQDeclarativePluginParameterCall4 call = reinterpret_cast<CuteQDeclarativePluginParameterCall4>(taken[4]);
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
      CuteQDeclarativePluginParameterCall5 call = reinterpret_cast<CuteQDeclarativePluginParameterCall5>(taken[5]);
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
      CuteQDeclarativePluginParameterCall6 call = reinterpret_cast<CuteQDeclarativePluginParameterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativePluginParameter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDeclarativePluginParameter10metaObjectEv(
    const QDeclarativePluginParameter *self) {
  return self->metaObject();
}

//  void *QDeclarativePluginParameter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QDeclarativePluginParameter11qt_metacastEPKc(
    QDeclarativePluginParameter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativePluginParameter::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDeclarativePluginParameter11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativePluginParameter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativePluginParameter::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDeclarativePluginParameter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativePluginParameter::tr(s, c, n));
}

//  QDeclarativePluginParameter::QDeclarativePluginParameter(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativePluginParameter *ritual_ZN27QDeclarativePluginParameterC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativePluginParameter(parent);
}

//  QDeclarativePluginParameter::~QDeclarativePluginParameter()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePluginParameterD1Ev(
    QDeclarativePluginParameter *self) {
  delete self;
}

//  void QDeclarativePluginParameter::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePluginParameter7setNameERK7QString(
    QDeclarativePluginParameter *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QDeclarativePluginParameter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDeclarativePluginParameter4nameEv(
    const QDeclarativePluginParameter *self) {
  return new QString(self->name());
}

//  void QDeclarativePluginParameter::setValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePluginParameter8setValueERK8QVariant(
    QDeclarativePluginParameter *self,
    const QVariant *value) {
  self->setValue(*value);
}

//  QVariant QDeclarativePluginParameter::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QDeclarativePluginParameter5valueEv(
    const QDeclarativePluginParameter *self) {
  return new QVariant(self->value());
}

//  bool QDeclarativePluginParameter::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativePluginParameter13isInitializedEv(
    const QDeclarativePluginParameter *self) {
  return self->isInitialized();
}

//  void QDeclarativePluginParameter::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePluginParameter11nameChangedERK7QString(
    QDeclarativePluginParameter *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  void QDeclarativePluginParameter::valueChanged(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePluginParameter12valueChangedERK8QVariant(
    QDeclarativePluginParameter *self,
    const QVariant *value) {
  self->valueChanged(*value);
}

//  void QDeclarativePluginParameter::initialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativePluginParameter11initializedEv(
    QDeclarativePluginParameter *self) {
  self->initialized();
}

//  a Python function taken by a CuteQDeclarativePluginParameter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePluginParameter(
    QDeclarativePluginParameter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePluginParameter *>(self)->take(key, call);
}
