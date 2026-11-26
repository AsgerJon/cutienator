//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlabstractprofileradapter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlabstractprofileradapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlAbstractProfilerAdapterFactory that Python can take functions over in. Every QQmlAbstractProfilerAdapterFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_debug)
typedef void * (*CuteQQmlAbstractProfilerAdapterFactoryCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractProfilerAdapterFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractProfilerAdapterFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlAbstractProfilerAdapterFactory : public QQmlAbstractProfilerAdapterFactory {
public:
  using QQmlAbstractProfilerAdapterFactory::QQmlAbstractProfilerAdapterFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN34QQmlAbstractProfilerAdapterFactory6createERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_debug)
  //  QQmlAbstractProfilerAdapter
  //      *QQmlAbstractProfilerAdapterFactory::create(const QString &key)
  QQmlAbstractProfilerAdapter *create(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall0 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QQmlAbstractProfilerAdapter *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(qml_debug)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall1 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall2 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall3 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall4 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall5 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall6 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterFactoryCall7 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlAbstractProfilerAdapterFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK34QQmlAbstractProfilerAdapterFactory10metaObjectEv(
    const QQmlAbstractProfilerAdapterFactory *self) {
  return self->metaObject();
}

//  void *QQmlAbstractProfilerAdapterFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN34QQmlAbstractProfilerAdapterFactory11qt_metacastEPKc(
    QQmlAbstractProfilerAdapterFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlAbstractProfilerAdapterFactory::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN34QQmlAbstractProfilerAdapterFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlAbstractProfilerAdapterFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlAbstractProfilerAdapterFactory::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN34QQmlAbstractProfilerAdapterFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAbstractProfilerAdapterFactory::tr(s, c, n));
}

//  QQmlAbstractProfilerAdapter
//      *QQmlAbstractProfilerAdapterFactory::create(const QString &key)
extern "C" Q_DECL_EXPORT
QQmlAbstractProfilerAdapter *ritual_ZN34QQmlAbstractProfilerAdapterFactory6createERK7QString(
    QQmlAbstractProfilerAdapterFactory *self,
    const QString *key) {
  return self->create(*key);
}

//  a Python function taken by a CuteQQmlAbstractProfilerAdapterFactory, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractProfilerAdapterFactory(
    QQmlAbstractProfilerAdapterFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractProfilerAdapterFactory *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_debug)
#endif  // QT_CONFIG(qml_debug)
