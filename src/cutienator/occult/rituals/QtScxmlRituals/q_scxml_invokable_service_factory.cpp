//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlinvokableservice.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtCore/qstring.h>
#include <QtScxml/qscxmlexecutablecontent.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScxmlInvokableServiceFactory that Python can take functions over in. Every QScxmlInvokableServiceFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScxmlInvokableServiceFactoryCall0)(const void *, QScxmlStateMachine *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInvokableServiceFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInvokableServiceFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInvokableServiceFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlInvokableServiceFactory : public QScxmlInvokableServiceFactory {
public:
  using QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory;
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
  //      *QScxmlInvokableServiceFactory::invoke(QScxmlStateMachine
  //      *parentStateMachine)
  QScxmlInvokableService *invoke(
      QScxmlStateMachine *parentStateMachine) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlInvokableServiceFactoryCall0 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall0>(taken[0]);
      void * given = call(this, parentStateMachine, &handled);
      if (handled) return static_cast<QScxmlInvokableService *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlInvokableServiceFactoryCall1 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall1>(taken[1]);
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
      CuteQScxmlInvokableServiceFactoryCall2 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall2>(taken[2]);
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
      CuteQScxmlInvokableServiceFactoryCall3 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall3>(taken[3]);
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
      CuteQScxmlInvokableServiceFactoryCall4 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall4>(taken[4]);
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
      CuteQScxmlInvokableServiceFactoryCall5 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall5>(taken[5]);
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
      CuteQScxmlInvokableServiceFactoryCall6 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall6>(taken[6]);
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
      CuteQScxmlInvokableServiceFactoryCall7 call = reinterpret_cast<CuteQScxmlInvokableServiceFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlInvokableServiceFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QScxmlInvokableServiceFactory10metaObjectEv(
    const QScxmlInvokableServiceFactory *self) {
  return self->metaObject();
}

//  void *QScxmlInvokableServiceFactory::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QScxmlInvokableServiceFactory11qt_metacastEPKc(
    QScxmlInvokableServiceFactory *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlInvokableServiceFactory::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QScxmlInvokableServiceFactory11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlInvokableServiceFactory *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlInvokableServiceFactory::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QScxmlInvokableServiceFactory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlInvokableServiceFactory::tr(s, c, n));
}

//  QScxmlInvokableServiceFactoryPrivate
//      *QScxmlInvokableServiceFactory::d_func()
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactoryPrivate *ritual_ZN29QScxmlInvokableServiceFactory6d_funcEv(
    QScxmlInvokableServiceFactory *self) {
  return self->d_func();
}

//  const QScxmlInvokableServiceFactoryPrivate
//      *QScxmlInvokableServiceFactory::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlInvokableServiceFactoryPrivate *ritual_ZNK29QScxmlInvokableServiceFactory6d_funcEv(
    const QScxmlInvokableServiceFactory *self) {
  return self->d_func();
}

//  QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(const
//      QScxmlExecutableContent::InvokeInfo &invokeInfo, const
//      QList<QScxmlExecutableContent::StringId> &names, const
//      QList<QScxmlExecutableContent::ParameterInfo> &parameters, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_ZN29QScxmlInvokableServiceFactoryC1ERKN23QScxmlExecutableContent10InvokeInfoERK5QListIiERKS4_INS0_13ParameterInfoEEP7QObject(
    const QScxmlExecutableContent::InvokeInfo *invokeInfo,
    const QList<QScxmlExecutableContent::StringId> *names,
    const QList<QScxmlExecutableContent::ParameterInfo> *parameters,
    QObject *parent) {
  return new CuteQScxmlInvokableServiceFactory(
      *invokeInfo,
      *names,
      *parameters,
      parent);
}

//  QScxmlInvokableService
//      *QScxmlInvokableServiceFactory::invoke(QScxmlStateMachine
//      *parentStateMachine)
extern "C" Q_DECL_EXPORT
QScxmlInvokableService *ritual_ZN29QScxmlInvokableServiceFactory6invokeEP18QScxmlStateMachine(
    QScxmlInvokableServiceFactory *self,
    QScxmlStateMachine *parentStateMachine) {
  return self->invoke(parentStateMachine);
}

//  const QScxmlExecutableContent::InvokeInfo
//      &QScxmlInvokableServiceFactory::invokeInfo() const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::InvokeInfo *ritual_ZNK29QScxmlInvokableServiceFactory10invokeInfoEv(
    const QScxmlInvokableServiceFactory *self) {
  return new QScxmlExecutableContent::InvokeInfo(self->invokeInfo());
}

//  const QList<QScxmlExecutableContent::ParameterInfo>
//      &QScxmlInvokableServiceFactory::parameters() const
extern "C" Q_DECL_EXPORT
const QList<QScxmlExecutableContent::ParameterInfo> *ritual_ZNK29QScxmlInvokableServiceFactory10parametersEv(
    const QScxmlInvokableServiceFactory *self) {
  return &(self->parameters());
}

//  const QList<QScxmlExecutableContent::StringId>
//      &QScxmlInvokableServiceFactory::names() const
extern "C" Q_DECL_EXPORT
const QList<QScxmlExecutableContent::StringId> *ritual_ZNK29QScxmlInvokableServiceFactory5namesEv(
    const QScxmlInvokableServiceFactory *self) {
  return &(self->names());
}

//  QScxmlInvokableServiceFactory::QScxmlInvokableServiceFactory(QScxmlInvoka
//      bleServiceFactoryPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_ZN29QScxmlInvokableServiceFactoryC1ER36QScxmlInvokableServiceFactoryPrivateP7QObject(
    QScxmlInvokableServiceFactoryPrivate *dd,
    QObject *parent) {
  return new CuteQScxmlInvokableServiceFactory(*dd, parent);
}

//  a Python function taken by a CuteQScxmlInvokableServiceFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlInvokableServiceFactory(
    QScxmlInvokableServiceFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlInvokableServiceFactory *>(self)->take(key, call);
}
