//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothservicediscoveryagent.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtBluetooth/qbluetoothservicediscoveryagent.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBluetoothServiceDiscoveryAgent that Python can take functions over in. Every QBluetoothServiceDiscoveryAgent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothServiceDiscoveryAgentCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothServiceDiscoveryAgentCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceDiscoveryAgentCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceDiscoveryAgentCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceDiscoveryAgentCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceDiscoveryAgentCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServiceDiscoveryAgentCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothServiceDiscoveryAgent : public QBluetoothServiceDiscoveryAgent {
public:
  using QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent;
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
      CuteQBluetoothServiceDiscoveryAgentCall0 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall0>(taken[0]);
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
      CuteQBluetoothServiceDiscoveryAgentCall1 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall1>(taken[1]);
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
      CuteQBluetoothServiceDiscoveryAgentCall2 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall2>(taken[2]);
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
      CuteQBluetoothServiceDiscoveryAgentCall3 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall3>(taken[3]);
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
      CuteQBluetoothServiceDiscoveryAgentCall4 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall4>(taken[4]);
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
      CuteQBluetoothServiceDiscoveryAgentCall5 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall5>(taken[5]);
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
      CuteQBluetoothServiceDiscoveryAgentCall6 call = reinterpret_cast<CuteQBluetoothServiceDiscoveryAgentCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothServiceDiscoveryAgent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QBluetoothServiceDiscoveryAgent10metaObjectEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return self->metaObject();
}

//  QString QBluetoothServiceDiscoveryAgent::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QBluetoothServiceDiscoveryAgent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBluetoothServiceDiscoveryAgent::tr(s, c, n));
}

//  QBluetoothServiceDiscoveryAgentPrivate
//      *QBluetoothServiceDiscoveryAgent::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgentPrivate *ritual_ZN31QBluetoothServiceDiscoveryAgent6d_funcEv(
    QBluetoothServiceDiscoveryAgent *self) {
  return self->d_func();
}

//  const QBluetoothServiceDiscoveryAgentPrivate
//      *QBluetoothServiceDiscoveryAgent::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothServiceDiscoveryAgentPrivate *ritual_ZNK31QBluetoothServiceDiscoveryAgent6d_funcEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return self->d_func();
}

//  QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgent *ritual_ZN31QBluetoothServiceDiscoveryAgentC1EP7QObject(
    QObject *parent) {
  return new CuteQBluetoothServiceDiscoveryAgent(parent);
}

//  QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent(const
//      QBluetoothAddress &deviceAdapter, QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgent *ritual_ZN31QBluetoothServiceDiscoveryAgentC1ERK17QBluetoothAddressP7QObject(
    const QBluetoothAddress *deviceAdapter,
    QObject *parent) {
  return new CuteQBluetoothServiceDiscoveryAgent(*deviceAdapter, parent);
}

//  QBluetoothServiceDiscoveryAgent::~QBluetoothServiceDiscoveryAgent()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QBluetoothServiceDiscoveryAgentD1Ev(
    QBluetoothServiceDiscoveryAgent *self) {
  delete self;
}

//  bool QBluetoothServiceDiscoveryAgent::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QBluetoothServiceDiscoveryAgent8isActiveEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return self->isActive();
}

//  Error QBluetoothServiceDiscoveryAgent::error() const
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgent::Error ritual_ZNK31QBluetoothServiceDiscoveryAgent5errorEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return self->error();
}

//  QString QBluetoothServiceDiscoveryAgent::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QBluetoothServiceDiscoveryAgent11errorStringEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return new QString(self->errorString());
}

//  QList<QBluetoothServiceInfo>
//      QBluetoothServiceDiscoveryAgent::discoveredServices() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothServiceInfo> *ritual_ZNK31QBluetoothServiceDiscoveryAgent18discoveredServicesEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return new QList<QBluetoothServiceInfo>(self->discoveredServices());
}

//  void QBluetoothServiceDiscoveryAgent::setUuidFilter(const
//      QList<QBluetoothUuid> &uuids)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QBluetoothServiceDiscoveryAgent13setUuidFilterERK5QListI14QBluetoothUuidE(
    QBluetoothServiceDiscoveryAgent *self,
    const QList<QBluetoothUuid> *uuids) {
  self->setUuidFilter(*uuids);
}

//  void QBluetoothServiceDiscoveryAgent::setUuidFilter(const QBluetoothUuid
//      &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QBluetoothServiceDiscoveryAgent13setUuidFilterERK14QBluetoothUuid(
    QBluetoothServiceDiscoveryAgent *self,
    const QBluetoothUuid *uuid) {
  self->setUuidFilter(*uuid);
}

//  QList<QBluetoothUuid> QBluetoothServiceDiscoveryAgent::uuidFilter() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK31QBluetoothServiceDiscoveryAgent10uuidFilterEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return new QList<QBluetoothUuid>(self->uuidFilter());
}

//  bool QBluetoothServiceDiscoveryAgent::setRemoteAddress(const
//      QBluetoothAddress &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QBluetoothServiceDiscoveryAgent16setRemoteAddressERK17QBluetoothAddress(
    QBluetoothServiceDiscoveryAgent *self,
    const QBluetoothAddress *address) {
  return self->setRemoteAddress(*address);
}

//  QBluetoothAddress QBluetoothServiceDiscoveryAgent::remoteAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK31QBluetoothServiceDiscoveryAgent13remoteAddressEv(
    const QBluetoothServiceDiscoveryAgent *self) {
  return new QBluetoothAddress(self->remoteAddress());
}

//  void QBluetoothServiceDiscoveryAgent::start(DiscoveryMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QBluetoothServiceDiscoveryAgent5startENS_13DiscoveryModeE(
    QBluetoothServiceDiscoveryAgent *self,
    QBluetoothServiceDiscoveryAgent::DiscoveryMode mode) {
  self->start(mode);
}

//  void QBluetoothServiceDiscoveryAgent::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QBluetoothServiceDiscoveryAgent4stopEv(
    QBluetoothServiceDiscoveryAgent *self) {
  self->stop();
}

//  void QBluetoothServiceDiscoveryAgent::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QBluetoothServiceDiscoveryAgent5clearEv(
    QBluetoothServiceDiscoveryAgent *self) {
  self->clear();
}

//  a Python function taken by a CuteQBluetoothServiceDiscoveryAgent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothServiceDiscoveryAgent(
    QBluetoothServiceDiscoveryAgent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothServiceDiscoveryAgent *>(self)->take(key, call);
}
