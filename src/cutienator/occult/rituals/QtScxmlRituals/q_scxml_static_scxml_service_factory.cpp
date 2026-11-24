//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlinvokableservice.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScxmlStaticScxmlServiceFactory that Python can take functions over in. Every QScxmlStaticScxmlServiceFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScxmlStaticScxmlServiceFactoryCall0)(const void *, QScxmlStateMachine *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlStaticScxmlServiceFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlStaticScxmlServiceFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlStaticScxmlServiceFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlStaticScxmlServiceFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlStaticScxmlServiceFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlStaticScxmlServiceFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlStaticScxmlServiceFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlStaticScxmlServiceFactory : public QScxmlStaticScxmlServiceFactory {
public:
  using QScxmlStaticScxmlServiceFactory::QScxmlStaticScxmlServiceFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN29QScxmlInvokableServiceFactory6invokeEP18QScxmlStateMachine")) {
      taken[0] = call;
      return true;
    }
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

  //  QScxmlInvokableService
  //      *QScxmlStaticScxmlServiceFactory::invoke(QScxmlStateMachine
  //      *parentStateMachine)
  QScxmlInvokableService *invoke(
      QScxmlStateMachine *parentStateMachine) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlStaticScxmlServiceFactoryCall0 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall0>(taken[0]);
      void * given = call(this, parentStateMachine, &handled);
      if (handled) return static_cast<QScxmlInvokableService *>(given);
    }
    return QScxmlStaticScxmlServiceFactory::invoke(parentStateMachine);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlStaticScxmlServiceFactoryCall1 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall1>(taken[1]);
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
      CuteQScxmlStaticScxmlServiceFactoryCall2 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall2>(taken[2]);
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
      CuteQScxmlStaticScxmlServiceFactoryCall3 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall3>(taken[3]);
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
      CuteQScxmlStaticScxmlServiceFactoryCall4 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall4>(taken[4]);
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
      CuteQScxmlStaticScxmlServiceFactoryCall5 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall5>(taken[5]);
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
      CuteQScxmlStaticScxmlServiceFactoryCall6 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall6>(taken[6]);
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
      CuteQScxmlStaticScxmlServiceFactoryCall7 call = reinterpret_cast<CuteQScxmlStaticScxmlServiceFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlStaticScxmlServiceFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QScxmlStaticScxmlServiceFactory10metaObjectEv(
    const QScxmlStaticScxmlServiceFactory *self) {
  return self->metaObject();
}

//  QString QScxmlStaticScxmlServiceFactory::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QScxmlStaticScxmlServiceFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlStaticScxmlServiceFactory::tr(s, c, n));
}

//  QScxmlStaticScxmlServiceFactoryPrivate
//      *QScxmlStaticScxmlServiceFactory::d_func()
extern "C" Q_DECL_EXPORT
QScxmlStaticScxmlServiceFactoryPrivate *ritual_ZN31QScxmlStaticScxmlServiceFactory6d_funcEv(
    QScxmlStaticScxmlServiceFactory *self) {
  return self->d_func();
}

//  const QScxmlStaticScxmlServiceFactoryPrivate
//      *QScxmlStaticScxmlServiceFactory::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlStaticScxmlServiceFactoryPrivate *ritual_ZNK31QScxmlStaticScxmlServiceFactory6d_funcEv(
    const QScxmlStaticScxmlServiceFactory *self) {
  return self->d_func();
}

//  QScxmlInvokableService
//      *QScxmlStaticScxmlServiceFactory::invoke(QScxmlStateMachine
//      *parentStateMachine)
extern "C" Q_DECL_EXPORT
QScxmlInvokableService *ritual_ZN31QScxmlStaticScxmlServiceFactory6invokeEP18QScxmlStateMachine(
    QScxmlStaticScxmlServiceFactory *self,
    QScxmlStateMachine *parentStateMachine) {
  return self->invoke(parentStateMachine);
}

//  a Python function taken by a CuteQScxmlStaticScxmlServiceFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlStaticScxmlServiceFactory(
    QScxmlStaticScxmlServiceFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlStaticScxmlServiceFactory *>(self)->take(key, call);
}

//  QScxmlInvokableService
//      *QScxmlStaticScxmlServiceFactory::invoke(QScxmlStateMachine
//      *parentStateMachine)
extern "C" Q_DECL_EXPORT
QScxmlInvokableService *ritual_own_ZN31QScxmlStaticScxmlServiceFactory6invokeEP18QScxmlStateMachine(
    QScxmlStaticScxmlServiceFactory *self,
    QScxmlStateMachine *parentStateMachine) {
  return self->QScxmlStaticScxmlServiceFactory::invoke(parentStateMachine);
}
