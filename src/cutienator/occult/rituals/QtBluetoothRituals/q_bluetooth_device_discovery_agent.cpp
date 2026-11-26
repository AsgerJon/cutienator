//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothdevicediscoveryagent.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtBluetooth/qbluetoothdevicediscoveryagent.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBluetoothDeviceDiscoveryAgent that Python can take functions over in. Every QBluetoothDeviceDiscoveryAgent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothDeviceDiscoveryAgentCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothDeviceDiscoveryAgentCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothDeviceDiscoveryAgentCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothDeviceDiscoveryAgentCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothDeviceDiscoveryAgentCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothDeviceDiscoveryAgentCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothDeviceDiscoveryAgentCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothDeviceDiscoveryAgent : public QBluetoothDeviceDiscoveryAgent {
public:
  using QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent;
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
      CuteQBluetoothDeviceDiscoveryAgentCall0 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall0>(taken[0]);
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
      CuteQBluetoothDeviceDiscoveryAgentCall1 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall1>(taken[1]);
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
      CuteQBluetoothDeviceDiscoveryAgentCall2 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall2>(taken[2]);
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
      CuteQBluetoothDeviceDiscoveryAgentCall3 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall3>(taken[3]);
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
      CuteQBluetoothDeviceDiscoveryAgentCall4 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall4>(taken[4]);
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
      CuteQBluetoothDeviceDiscoveryAgentCall5 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall5>(taken[5]);
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
      CuteQBluetoothDeviceDiscoveryAgentCall6 call = reinterpret_cast<CuteQBluetoothDeviceDiscoveryAgentCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothDeviceDiscoveryAgent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QBluetoothDeviceDiscoveryAgent10metaObjectEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return self->metaObject();
}

//  void *QBluetoothDeviceDiscoveryAgent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QBluetoothDeviceDiscoveryAgent11qt_metacastEPKc(
    QBluetoothDeviceDiscoveryAgent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBluetoothDeviceDiscoveryAgent::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QBluetoothDeviceDiscoveryAgent11qt_metacallEN11QMetaObject4CallEiPPv(
    QBluetoothDeviceDiscoveryAgent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBluetoothDeviceDiscoveryAgent::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QBluetoothDeviceDiscoveryAgent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBluetoothDeviceDiscoveryAgent::tr(s, c, n));
}

//  QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QBluetoothDeviceDiscoveryAgent *ritual_ZN30QBluetoothDeviceDiscoveryAgentC1EP7QObject(
    QObject *parent) {
  return new CuteQBluetoothDeviceDiscoveryAgent(parent);
}

//  QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent(const
//      QBluetoothAddress &deviceAdapter, QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothDeviceDiscoveryAgent *ritual_ZN30QBluetoothDeviceDiscoveryAgentC1ERK17QBluetoothAddressP7QObject(
    const QBluetoothAddress *deviceAdapter,
    QObject *parent) {
  return new CuteQBluetoothDeviceDiscoveryAgent(*deviceAdapter, parent);
}

//  QBluetoothDeviceDiscoveryAgent::~QBluetoothDeviceDiscoveryAgent()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgentD1Ev(
    QBluetoothDeviceDiscoveryAgent *self) {
  delete self;
}

//  bool QBluetoothDeviceDiscoveryAgent::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QBluetoothDeviceDiscoveryAgent8isActiveEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return self->isActive();
}

//  Error QBluetoothDeviceDiscoveryAgent::error() const
extern "C" Q_DECL_EXPORT
QBluetoothDeviceDiscoveryAgent::Error ritual_ZNK30QBluetoothDeviceDiscoveryAgent5errorEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return self->error();
}

//  QString QBluetoothDeviceDiscoveryAgent::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QBluetoothDeviceDiscoveryAgent11errorStringEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return new QString(self->errorString());
}

//  QList<QBluetoothDeviceInfo>
//      QBluetoothDeviceDiscoveryAgent::discoveredDevices() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothDeviceInfo> *ritual_ZNK30QBluetoothDeviceDiscoveryAgent17discoveredDevicesEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return new QList<QBluetoothDeviceInfo>(self->discoveredDevices());
}

//  void QBluetoothDeviceDiscoveryAgent::setLowEnergyDiscoveryTimeout(int
//      msTimeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent28setLowEnergyDiscoveryTimeoutEi(
    QBluetoothDeviceDiscoveryAgent *self,
    int msTimeout) {
  self->setLowEnergyDiscoveryTimeout(msTimeout);
}

//  int QBluetoothDeviceDiscoveryAgent::lowEnergyDiscoveryTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QBluetoothDeviceDiscoveryAgent25lowEnergyDiscoveryTimeoutEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return self->lowEnergyDiscoveryTimeout();
}

//  DiscoveryMethods
//      QBluetoothDeviceDiscoveryAgent::supportedDiscoveryMethods()
extern "C" Q_DECL_EXPORT
int ritual_ZN30QBluetoothDeviceDiscoveryAgent25supportedDiscoveryMethodsEv() {
  return static_cast<int>(
      QBluetoothDeviceDiscoveryAgent::supportedDiscoveryMethods().toInt());
}

//  void QBluetoothDeviceDiscoveryAgent::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent5startEv(
    QBluetoothDeviceDiscoveryAgent *self) {
  self->start();
}

//  void QBluetoothDeviceDiscoveryAgent::start(DiscoveryMethods method)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent5startE6QFlagsINS_15DiscoveryMethodEE(
    QBluetoothDeviceDiscoveryAgent *self,
    int method) {
  self->start(
      QFlags<QBluetoothDeviceDiscoveryAgent::DiscoveryMethod>::fromInt(method));
}

//  void QBluetoothDeviceDiscoveryAgent::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent4stopEv(
    QBluetoothDeviceDiscoveryAgent *self) {
  self->stop();
}

//  void QBluetoothDeviceDiscoveryAgent::deviceDiscovered(const
//      QBluetoothDeviceInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent16deviceDiscoveredERK20QBluetoothDeviceInfo(
    QBluetoothDeviceDiscoveryAgent *self,
    const QBluetoothDeviceInfo *info) {
  self->deviceDiscovered(*info);
}

//  void QBluetoothDeviceDiscoveryAgent::deviceUpdated(const
//      QBluetoothDeviceInfo &info, QBluetoothDeviceInfo::Fields
//      updatedFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent13deviceUpdatedERK20QBluetoothDeviceInfo6QFlagsINS0_5FieldEE(
    QBluetoothDeviceDiscoveryAgent *self,
    const QBluetoothDeviceInfo *info,
    int updatedFields) {
  self->deviceUpdated(
      *info,
      QFlags<QBluetoothDeviceInfo::Field>::fromInt(updatedFields));
}

//  void QBluetoothDeviceDiscoveryAgent::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent8finishedEv(
    QBluetoothDeviceDiscoveryAgent *self) {
  self->finished();
}

//  void QBluetoothDeviceDiscoveryAgent::errorOccurred(QBluetoothDeviceDiscov
//      eryAgent::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent13errorOccurredENS_5ErrorE(
    QBluetoothDeviceDiscoveryAgent *self,
    QBluetoothDeviceDiscoveryAgent::Error error) {
  self->errorOccurred(error);
}

//  void QBluetoothDeviceDiscoveryAgent::canceled()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QBluetoothDeviceDiscoveryAgent8canceledEv(
    QBluetoothDeviceDiscoveryAgent *self) {
  self->canceled();
}

//  QBluetoothDeviceDiscoveryAgentPrivate
//      *QBluetoothDeviceDiscoveryAgent::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothDeviceDiscoveryAgentPrivate *ritual_ZN30QBluetoothDeviceDiscoveryAgent6d_funcEv(
    QBluetoothDeviceDiscoveryAgent *self) {
  return self->d_func();
}

//  const QBluetoothDeviceDiscoveryAgentPrivate
//      *QBluetoothDeviceDiscoveryAgent::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothDeviceDiscoveryAgentPrivate *ritual_ZNK30QBluetoothDeviceDiscoveryAgent6d_funcEv(
    const QBluetoothDeviceDiscoveryAgent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBluetoothDeviceDiscoveryAgent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothDeviceDiscoveryAgent(
    QBluetoothDeviceDiscoveryAgent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothDeviceDiscoveryAgent *>(self)->take(key, call);
}
