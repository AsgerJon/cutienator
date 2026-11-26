//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugconnector_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugconnector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlDebugConnectorFactory that Python can take functions over in. Every QQmlDebugConnectorFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(!QT_CONFIG(qml_debug))
typedef void * (*CuteQQmlDebugConnectorFactoryCall0)(const void *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugConnectorFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugConnectorFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugConnectorFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDebugConnectorFactory : public QQmlDebugConnectorFactory {
public:
  using QQmlDebugConnectorFactory::QQmlDebugConnectorFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN25QQmlDebugConnectorFactory6createERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
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

#if !(!QT_CONFIG(qml_debug))
  //  QQmlDebugConnector *QQmlDebugConnectorFactory::create(const QString
  //      &key)
  QQmlDebugConnector *create(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDebugConnectorFactoryCall0 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QQmlDebugConnector *>(given);
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDebugConnectorFactoryCall1 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall1>(taken[1]);
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
      CuteQQmlDebugConnectorFactoryCall2 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall2>(taken[2]);
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
      CuteQQmlDebugConnectorFactoryCall3 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall3>(taken[3]);
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
      CuteQQmlDebugConnectorFactoryCall4 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall4>(taken[4]);
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
      CuteQQmlDebugConnectorFactoryCall5 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall5>(taken[5]);
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
      CuteQQmlDebugConnectorFactoryCall6 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall6>(taken[6]);
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
      CuteQQmlDebugConnectorFactoryCall7 call = reinterpret_cast<CuteQQmlDebugConnectorFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDebugConnectorFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQmlDebugConnectorFactory10metaObjectEv(
    const QQmlDebugConnectorFactory *self) {
  return self->metaObject();
}

//  void *QQmlDebugConnectorFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQmlDebugConnectorFactory11qt_metacastEPKc(
    QQmlDebugConnectorFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDebugConnectorFactory::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQmlDebugConnectorFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDebugConnectorFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlDebugConnectorFactory::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQmlDebugConnectorFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDebugConnectorFactory::tr(s, c, n));
}

//  QQmlDebugConnector *QQmlDebugConnectorFactory::create(const QString &key)
extern "C" Q_DECL_EXPORT
QQmlDebugConnector *ritual_ZN25QQmlDebugConnectorFactory6createERK7QString(
    QQmlDebugConnectorFactory *self,
    const QString *key) {
  return self->create(*key);
}

//  QQmlDebugConnectorFactory::~QQmlDebugConnectorFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlDebugConnectorFactoryD1Ev(
    QQmlDebugConnectorFactory *self) {
  delete self;
}

//  a Python function taken by a CuteQQmlDebugConnectorFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDebugConnectorFactory(
    QQmlDebugConnectorFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDebugConnectorFactory *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
