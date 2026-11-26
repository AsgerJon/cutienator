//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttsubscription.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqttsubscription.h>
#include <QtCore/qstring.h>
#include <QtMqtt/qmqtttopicfilter.h>
#include <QtMqtt/qmqtttype.h>
#include <QtMqtt/qmqttmessage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMqttSubscription that Python can take functions over in. Every QMqttSubscription
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMqttSubscriptionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMqttSubscriptionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttSubscriptionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttSubscriptionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttSubscriptionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttSubscriptionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttSubscriptionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMqttSubscription : public QMqttSubscription {
public:
  using QMqttSubscription::QMqttSubscription;
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
      CuteQMqttSubscriptionCall0 call = reinterpret_cast<CuteQMqttSubscriptionCall0>(taken[0]);
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
      CuteQMqttSubscriptionCall1 call = reinterpret_cast<CuteQMqttSubscriptionCall1>(taken[1]);
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
      CuteQMqttSubscriptionCall2 call = reinterpret_cast<CuteQMqttSubscriptionCall2>(taken[2]);
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
      CuteQMqttSubscriptionCall3 call = reinterpret_cast<CuteQMqttSubscriptionCall3>(taken[3]);
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
      CuteQMqttSubscriptionCall4 call = reinterpret_cast<CuteQMqttSubscriptionCall4>(taken[4]);
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
      CuteQMqttSubscriptionCall5 call = reinterpret_cast<CuteQMqttSubscriptionCall5>(taken[5]);
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
      CuteQMqttSubscriptionCall6 call = reinterpret_cast<CuteQMqttSubscriptionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMqttSubscription::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QMqttSubscription10metaObjectEv(
    const QMqttSubscription *self) {
  return self->metaObject();
}

//  void *QMqttSubscription::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QMqttSubscription11qt_metacastEPKc(
    QMqttSubscription *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMqttSubscription::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QMqttSubscription11qt_metacallEN11QMetaObject4CallEiPPv(
    QMqttSubscription *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMqttSubscription::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QMqttSubscription2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMqttSubscription::tr(s, c, n));
}

//  QMqttSubscription::~QMqttSubscription()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscriptionD1Ev(QMqttSubscription *self) {
  delete self;
}

//  SubscriptionState QMqttSubscription::state() const
extern "C" Q_DECL_EXPORT
QMqttSubscription::SubscriptionState ritual_ZNK17QMqttSubscription5stateEv(
    const QMqttSubscription *self) {
  return self->state();
}

//  QMqttTopicFilter QMqttSubscription::topic() const
extern "C" Q_DECL_EXPORT
QMqttTopicFilter *ritual_ZNK17QMqttSubscription5topicEv(
    const QMqttSubscription *self) {
  return new QMqttTopicFilter(self->topic());
}

//  quint8 QMqttSubscription::qos() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK17QMqttSubscription3qosEv(const QMqttSubscription *self) {
  return self->qos();
}

//  QString QMqttSubscription::reason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QMqttSubscription6reasonEv(
    const QMqttSubscription *self) {
  return new QString(self->reason());
}

//  QMqtt::ReasonCode QMqttSubscription::reasonCode() const
extern "C" Q_DECL_EXPORT
QMqtt::ReasonCode ritual_ZNK17QMqttSubscription10reasonCodeEv(
    const QMqttSubscription *self) {
  return self->reasonCode();
}

//  QMqttUserProperties QMqttSubscription::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK17QMqttSubscription14userPropertiesEv(
    const QMqttSubscription *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  bool QMqttSubscription::isSharedSubscription() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QMqttSubscription20isSharedSubscriptionEv(
    const QMqttSubscription *self) {
  return self->isSharedSubscription();
}

//  QString QMqttSubscription::sharedSubscriptionName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QMqttSubscription22sharedSubscriptionNameEv(
    const QMqttSubscription *self) {
  return new QString(self->sharedSubscriptionName());
}

//  void QMqttSubscription::stateChanged(SubscriptionState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription12stateChangedENS_17SubscriptionStateE(
    QMqttSubscription *self,
    QMqttSubscription::SubscriptionState state) {
  self->stateChanged(state);
}

//  void QMqttSubscription::qosChanged(quint8 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription10qosChangedEh(
    QMqttSubscription *self,
    quint8 a0) {
  self->qosChanged(a0);
}

//  void QMqttSubscription::messageReceived(QMqttMessage msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription15messageReceivedE12QMqttMessage(
    QMqttSubscription *self,
    const QMqttMessage *msg) {
  self->messageReceived(*msg);
}

//  void QMqttSubscription::unsubscribe()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription11unsubscribeEv(QMqttSubscription *self) {
  self->unsubscribe();
}

//  QMqttSubscriptionPrivate *QMqttSubscription::d_func()
extern "C" Q_DECL_EXPORT
QMqttSubscriptionPrivate *ritual_ZN17QMqttSubscription6d_funcEv(
    QMqttSubscription *self) {
  return self->d_func();
}

//  const QMqttSubscriptionPrivate *QMqttSubscription::d_func() const
extern "C" Q_DECL_EXPORT
const QMqttSubscriptionPrivate *ritual_ZNK17QMqttSubscription6d_funcEv(
    const QMqttSubscription *self) {
  return self->d_func();
}

//  void QMqttSubscription::setState(SubscriptionState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription8setStateENS_17SubscriptionStateE(
    QMqttSubscription *self,
    QMqttSubscription::SubscriptionState state) {
  self->setState(state);
}

//  void QMqttSubscription::setTopic(const QMqttTopicFilter &topic)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription8setTopicERK16QMqttTopicFilter(
    QMqttSubscription *self,
    const QMqttTopicFilter *topic) {
  self->setTopic(*topic);
}

//  void QMqttSubscription::setClient(QMqttClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription9setClientEP11QMqttClient(
    QMqttSubscription *self,
    QMqttClient *client) {
  self->setClient(client);
}

//  void QMqttSubscription::setQos(quint8 qos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription6setQosEh(
    QMqttSubscription *self,
    quint8 qos) {
  self->setQos(qos);
}

//  void QMqttSubscription::setSharedSubscription(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription21setSharedSubscriptionEb(
    QMqttSubscription *self,
    bool s) {
  self->setSharedSubscription(s);
}

//  void QMqttSubscription::setSharedSubscriptionName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMqttSubscription25setSharedSubscriptionNameERK7QString(
    QMqttSubscription *self,
    const QString *name) {
  self->setSharedSubscriptionName(*name);
}

//  QMqttSubscription::QMqttSubscription(QObject *parent)
extern "C" Q_DECL_EXPORT
QMqttSubscription *ritual_ZN17QMqttSubscriptionC1EP7QObject(
    QObject *parent) {
  return new CuteQMqttSubscription(parent);
}

//  a Python function taken by a CuteQMqttSubscription, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMqttSubscription(
    QMqttSubscription *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMqttSubscription *>(self)->take(key, call);
}
