//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxmlQml/6.12.0/QtScxmlQml/private/eventconnection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/qscxmlqmlglobals_p.h>
#include <QtScxmlQml/QtScxmlQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/eventconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QScxmlEventConnection that Python can take functions over in. Every QScxmlEventConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScxmlEventConnectionCall0)(const void *, int *);
typedef void (*CuteQScxmlEventConnectionCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlEventConnectionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlEventConnectionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlEventConnectionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlEventConnectionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlEventConnectionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlEventConnectionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlEventConnectionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlEventConnection : public QScxmlEventConnection {
public:
  using QScxmlEventConnection::QScxmlEventConnection;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
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

  //  void QScxmlEventConnection::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlEventConnectionCall0 call = reinterpret_cast<CuteQScxmlEventConnectionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QScxmlEventConnection::classBegin();
  }

  //  void QScxmlEventConnection::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlEventConnectionCall1 call = reinterpret_cast<CuteQScxmlEventConnectionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QScxmlEventConnection::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlEventConnectionCall2 call = reinterpret_cast<CuteQScxmlEventConnectionCall2>(taken[2]);
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
      CuteQScxmlEventConnectionCall3 call = reinterpret_cast<CuteQScxmlEventConnectionCall3>(taken[3]);
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
      CuteQScxmlEventConnectionCall4 call = reinterpret_cast<CuteQScxmlEventConnectionCall4>(taken[4]);
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
      CuteQScxmlEventConnectionCall5 call = reinterpret_cast<CuteQScxmlEventConnectionCall5>(taken[5]);
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
      CuteQScxmlEventConnectionCall6 call = reinterpret_cast<CuteQScxmlEventConnectionCall6>(taken[6]);
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
      CuteQScxmlEventConnectionCall7 call = reinterpret_cast<CuteQScxmlEventConnectionCall7>(taken[7]);
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
      CuteQScxmlEventConnectionCall8 call = reinterpret_cast<CuteQScxmlEventConnectionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlEventConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QScxmlEventConnection10metaObjectEv(
    const QScxmlEventConnection *self) {
  return self->metaObject();
}

//  QString QScxmlEventConnection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QScxmlEventConnection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlEventConnection::tr(s, c, n));
}

//  QScxmlEventConnection::QScxmlEventConnection(QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlEventConnection *ritual_ZN21QScxmlEventConnectionC1EP7QObject(
    QObject *parent) {
  return new CuteQScxmlEventConnection(parent);
}

//  QScxmlEventConnection::~QScxmlEventConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlEventConnectionD1Ev(QScxmlEventConnection *self) {
  delete self;
}

//  QStringList QScxmlEventConnection::events() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QScxmlEventConnection6eventsEv(
    const QScxmlEventConnection *self) {
  return new QList<QString>(self->events());
}

//  void QScxmlEventConnection::setEvents(const QStringList &events)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlEventConnection9setEventsERK5QListI7QStringE(
    QScxmlEventConnection *self,
    const QList<QString> *events) {
  self->setEvents(*events);
}

//  QScxmlStateMachine *QScxmlEventConnection::stateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK21QScxmlEventConnection12stateMachineEv(
    const QScxmlEventConnection *self) {
  return self->stateMachine();
}

//  void QScxmlEventConnection::setStateMachine(QScxmlStateMachine
//      *stateMachine)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlEventConnection15setStateMachineEP18QScxmlStateMachine(
    QScxmlEventConnection *self,
    QScxmlStateMachine *stateMachine) {
  self->setStateMachine(stateMachine);
}

//  void QScxmlEventConnection::doConnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlEventConnection9doConnectEv(
    QScxmlEventConnection *self) {
  self->doConnect();
}

//  void QScxmlEventConnection::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlEventConnection10classBeginEv(
    QScxmlEventConnection *self) {
  self->classBegin();
}

//  void QScxmlEventConnection::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlEventConnection17componentCompleteEv(
    QScxmlEventConnection *self) {
  self->componentComplete();
}

//  QScxmlEventConnection as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QScxmlEventConnection_QQmlParserStatus(
    QScxmlEventConnection *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQScxmlEventConnection, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlEventConnection(
    QScxmlEventConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlEventConnection *>(self)->take(key, call);
}

//  void QScxmlEventConnection::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QScxmlEventConnection10classBeginEv(
    QScxmlEventConnection *self) {
  self->QScxmlEventConnection::classBegin();
}

//  void QScxmlEventConnection::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QScxmlEventConnection17componentCompleteEv(
    QScxmlEventConnection *self) {
  self->QScxmlEventConnection::componentComplete();
}
