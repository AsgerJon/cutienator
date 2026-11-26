//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlinvokableservice.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtCore/qstring.h>
#include <QtScxml/qscxmlexecutablecontent.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScxmlDynamicScxmlServiceFactory that Python can take functions over in. Every QScxmlDynamicScxmlServiceFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScxmlDynamicScxmlServiceFactoryCall0)(const void *, QScxmlStateMachine *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlDynamicScxmlServiceFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlDynamicScxmlServiceFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDynamicScxmlServiceFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDynamicScxmlServiceFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDynamicScxmlServiceFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDynamicScxmlServiceFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDynamicScxmlServiceFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlDynamicScxmlServiceFactory : public QScxmlDynamicScxmlServiceFactory {
public:
  using QScxmlDynamicScxmlServiceFactory::QScxmlDynamicScxmlServiceFactory;
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
  //      *QScxmlDynamicScxmlServiceFactory::invoke(QScxmlStateMachine
  //      *parentStateMachine)
  QScxmlInvokableService *invoke(
      QScxmlStateMachine *parentStateMachine) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlDynamicScxmlServiceFactoryCall0 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall0>(taken[0]);
      void * given = call(this, parentStateMachine, &handled);
      if (handled) return static_cast<QScxmlInvokableService *>(given);
    }
    return QScxmlDynamicScxmlServiceFactory::invoke(parentStateMachine);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlDynamicScxmlServiceFactoryCall1 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall1>(taken[1]);
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
      CuteQScxmlDynamicScxmlServiceFactoryCall2 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall2>(taken[2]);
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
      CuteQScxmlDynamicScxmlServiceFactoryCall3 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall3>(taken[3]);
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
      CuteQScxmlDynamicScxmlServiceFactoryCall4 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall4>(taken[4]);
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
      CuteQScxmlDynamicScxmlServiceFactoryCall5 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall5>(taken[5]);
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
      CuteQScxmlDynamicScxmlServiceFactoryCall6 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall6>(taken[6]);
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
      CuteQScxmlDynamicScxmlServiceFactoryCall7 call = reinterpret_cast<CuteQScxmlDynamicScxmlServiceFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlDynamicScxmlServiceFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QScxmlDynamicScxmlServiceFactory10metaObjectEv(
    const QScxmlDynamicScxmlServiceFactory *self) {
  return self->metaObject();
}

//  void *QScxmlDynamicScxmlServiceFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QScxmlDynamicScxmlServiceFactory11qt_metacastEPKc(
    QScxmlDynamicScxmlServiceFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlDynamicScxmlServiceFactory::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QScxmlDynamicScxmlServiceFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlDynamicScxmlServiceFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlDynamicScxmlServiceFactory::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QScxmlDynamicScxmlServiceFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlDynamicScxmlServiceFactory::tr(s, c, n));
}

//  QScxmlDynamicScxmlServiceFactory::QScxmlDynamicScxmlServiceFactory(const
//      QScxmlExecutableContent::InvokeInfo &invokeInfo, const
//      QList<QScxmlExecutableContent::StringId> &names, const
//      QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QScxmlDynamicScxmlServiceFactory *ritual_ZN32QScxmlDynamicScxmlServiceFactoryC1ERKN23QScxmlExecutableContent10InvokeInfoERK5QListIiERKS4_INS0_13ParameterInfoEEP7QObject(
    const QScxmlExecutableContent::InvokeInfo *invokeInfo,
    const QList<QScxmlExecutableContent::StringId> *names,
    const QList<QScxmlExecutableContent::ParameterInfo> *parameters,
    QObject *parent) {
  return new CuteQScxmlDynamicScxmlServiceFactory(
      *invokeInfo,
      *names,
      *parameters,
      parent);
}

//  QScxmlInvokableService
//      *QScxmlDynamicScxmlServiceFactory::invoke(QScxmlStateMachine
//      *parentStateMachine)
extern "C" Q_DECL_EXPORT
QScxmlInvokableService *ritual_ZN32QScxmlDynamicScxmlServiceFactory6invokeEP18QScxmlStateMachine(
    QScxmlDynamicScxmlServiceFactory *self,
    QScxmlStateMachine *parentStateMachine) {
  return self->invoke(parentStateMachine);
}

//  a Python function taken by a CuteQScxmlDynamicScxmlServiceFactory, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlDynamicScxmlServiceFactory(
    QScxmlDynamicScxmlServiceFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlDynamicScxmlServiceFactory *>(self)->take(key, call);
}

//  QScxmlInvokableService
//      *QScxmlDynamicScxmlServiceFactory::invoke(QScxmlStateMachine
//      *parentStateMachine)
extern "C" Q_DECL_EXPORT
QScxmlInvokableService *ritual_own_ZN32QScxmlDynamicScxmlServiceFactory6invokeEP18QScxmlStateMachine(
    QScxmlDynamicScxmlServiceFactory *self,
    QScxmlStateMachine *parentStateMachine) {
  return self->QScxmlDynamicScxmlServiceFactory::invoke(parentStateMachine);
}
