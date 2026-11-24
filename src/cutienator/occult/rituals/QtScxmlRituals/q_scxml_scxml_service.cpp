//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlinvokableservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScxmlScxmlService that Python can take functions over in. Every QScxmlScxmlService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQScxmlScxmlServiceCall0)(const void *, int *);
typedef QString * (*CuteQScxmlScxmlServiceCall1)(const void *, int *);
typedef QString * (*CuteQScxmlScxmlServiceCall2)(const void *, int *);
typedef void (*CuteQScxmlScxmlServiceCall3)(const void *, QScxmlEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlScxmlServiceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlScxmlServiceCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlScxmlServiceCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlScxmlServiceCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlScxmlServiceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlScxmlServiceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlScxmlServiceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlScxmlService : public QScxmlScxmlService {
public:
  using QScxmlScxmlService::QScxmlScxmlService;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QScxmlInvokableService5startEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QScxmlInvokableService2idEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QScxmlInvokableService4nameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QScxmlInvokableService9postEventEP11QScxmlEvent")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QScxmlScxmlService::start()
  bool start() override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall0 call = reinterpret_cast<CuteQScxmlScxmlServiceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QScxmlScxmlService::start();
  }

  //  QString QScxmlScxmlService::id() const
  QString id() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall1 call = reinterpret_cast<CuteQScxmlScxmlServiceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QScxmlScxmlService::id();
  }

  //  QString QScxmlScxmlService::name() const
  QString name() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall2 call = reinterpret_cast<CuteQScxmlScxmlServiceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QScxmlScxmlService::name();
  }

  //  void QScxmlScxmlService::postEvent(QScxmlEvent *event)
  void postEvent(QScxmlEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall3 call = reinterpret_cast<CuteQScxmlScxmlServiceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QScxmlScxmlService::postEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall4 call = reinterpret_cast<CuteQScxmlScxmlServiceCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall5 call = reinterpret_cast<CuteQScxmlScxmlServiceCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall6 call = reinterpret_cast<CuteQScxmlScxmlServiceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall7 call = reinterpret_cast<CuteQScxmlScxmlServiceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall8 call = reinterpret_cast<CuteQScxmlScxmlServiceCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall9 call = reinterpret_cast<CuteQScxmlScxmlServiceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQScxmlScxmlServiceCall10 call = reinterpret_cast<CuteQScxmlScxmlServiceCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlScxmlService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QScxmlScxmlService10metaObjectEv(
    const QScxmlScxmlService *self) {
  return self->metaObject();
}

//  QString QScxmlScxmlService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QScxmlScxmlService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlScxmlService::tr(s, c, n));
}

//  QScxmlInvokableServicePrivate *QScxmlScxmlService::d_func()
extern "C" Q_DECL_EXPORT
QScxmlInvokableServicePrivate *ritual_ZN18QScxmlScxmlService6d_funcEv(
    QScxmlScxmlService *self) {
  return self->d_func();
}

//  const QScxmlInvokableServicePrivate *QScxmlScxmlService::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlInvokableServicePrivate *ritual_ZNK18QScxmlScxmlService6d_funcEv(
    const QScxmlScxmlService *self) {
  return self->d_func();
}

//  QScxmlScxmlService::QScxmlScxmlService(QScxmlStateMachine *stateMachine,
//      QScxmlStateMachine *parentStateMachine, QScxmlInvokableServiceFactory
//      *parent)
extern "C" Q_DECL_EXPORT
QScxmlScxmlService *ritual_ZN18QScxmlScxmlServiceC1EP18QScxmlStateMachineS1_P29QScxmlInvokableServiceFactory(
    QScxmlStateMachine *stateMachine,
    QScxmlStateMachine *parentStateMachine,
    QScxmlInvokableServiceFactory *parent) {
  return new CuteQScxmlScxmlService(
      stateMachine,
      parentStateMachine,
      parent);
}

//  QScxmlScxmlService::~QScxmlScxmlService()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlScxmlServiceD1Ev(QScxmlScxmlService *self) {
  delete self;
}

//  bool QScxmlScxmlService::start()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QScxmlScxmlService5startEv(QScxmlScxmlService *self) {
  return self->start();
}

//  QString QScxmlScxmlService::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QScxmlScxmlService2idEv(
    const QScxmlScxmlService *self) {
  return new QString(self->id());
}

//  QString QScxmlScxmlService::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QScxmlScxmlService4nameEv(
    const QScxmlScxmlService *self) {
  return new QString(self->name());
}

//  void QScxmlScxmlService::postEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QScxmlScxmlService9postEventEP11QScxmlEvent(
    QScxmlScxmlService *self,
    QScxmlEvent *event) {
  self->postEvent(event);
}

//  QScxmlStateMachine *QScxmlScxmlService::stateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK18QScxmlScxmlService12stateMachineEv(
    const QScxmlScxmlService *self) {
  return self->stateMachine();
}

//  a Python function taken by a CuteQScxmlScxmlService, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlScxmlService(
    QScxmlScxmlService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlScxmlService *>(self)->take(key, call);
}

//  bool QScxmlScxmlService::start()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QScxmlScxmlService5startEv(QScxmlScxmlService *self) {
  return self->QScxmlScxmlService::start();
}

//  QString QScxmlScxmlService::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QScxmlScxmlService2idEv(
    const QScxmlScxmlService *self) {
  return new QString(self->QScxmlScxmlService::id());
}

//  QString QScxmlScxmlService::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QScxmlScxmlService4nameEv(
    const QScxmlScxmlService *self) {
  return new QString(self->QScxmlScxmlService::name());
}

//  void QScxmlScxmlService::postEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QScxmlScxmlService9postEventEP11QScxmlEvent(
    QScxmlScxmlService *self,
    QScxmlEvent *event) {
  self->QScxmlScxmlService::postEvent(event);
}
