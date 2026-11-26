//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusrtuserialserver.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSerialBus/qtserialbusglobal.h>
#if QT_CONFIG(modbus_serialport)
#include <QtSerialBus/qmodbusrtuserialserver.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qvariant.h>
#include <QtSerialBus/qmodbusdataunit.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QModbusRtuSerialServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQModbusRtuSerialServer : QModbusRtuSerialServer {
  using QModbusRtuSerialServer::open;
  using QModbusRtuSerialServer::close;
};

//  A QModbusRtuSerialServer that Python can take functions over in. Every QModbusRtuSerialServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusRtuSerialServerCall0)(const void *, int *);
typedef bool (*CuteQModbusRtuSerialServerCall1)(const void *, int *);
typedef void (*CuteQModbusRtuSerialServerCall2)(const void *, int *);
typedef const QVariant * (*CuteQModbusRtuSerialServerCall3)(const void *, int, int *);
typedef bool (*CuteQModbusRtuSerialServerCall4)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQModbusRtuSerialServerCall5)(const void *, const QModbusDataUnit *, int *);
typedef bool (*CuteQModbusRtuSerialServerCall6)(const void *, QModbusDataUnit *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusRtuSerialServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusRtuSerialServerCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialServerCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialServerCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialServerCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialServerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialServerCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusRtuSerialServer : public QModbusRtuSerialServer {
public:
  using QModbusRtuSerialServer::QModbusRtuSerialServer;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QModbusServer18processesBroadcastEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QModbusServer5valueEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusServer8setValueEiRK8QVariant")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusServer9writeDataERK15QModbusDataUnit")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QModbusServer8readDataEP15QModbusDataUnit")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QModbusRtuSerialServer::processesBroadcast() const
  bool processesBroadcast() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall0 call = reinterpret_cast<CuteQModbusRtuSerialServerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusRtuSerialServer::processesBroadcast();
  }

  //  bool QModbusRtuSerialServer::open()
  bool open() override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall1 call = reinterpret_cast<CuteQModbusRtuSerialServerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusRtuSerialServer::open();
  }

  //  void QModbusRtuSerialServer::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall2 call = reinterpret_cast<CuteQModbusRtuSerialServerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QModbusRtuSerialServer::close();
  }

  //  QVariant QModbusServer::value(int option) const
  QVariant value(int option) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall3 call = reinterpret_cast<CuteQModbusRtuSerialServerCall3>(taken[3]);
      const QVariant * given = call(this, option, &handled);
      if (handled && given) return *given;
    }
    return QModbusServer::value(option);
  }

  //  bool QModbusServer::setValue(int option, const QVariant &value)
  bool setValue(int option, const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall4 call = reinterpret_cast<CuteQModbusRtuSerialServerCall4>(taken[4]);
      bool given = call(this, option, &value, &handled);
      if (handled) return given;
    }
    return QModbusServer::setValue(option, value);
  }

  //  bool QModbusServer::writeData(const QModbusDataUnit &unit)
  bool writeData(const QModbusDataUnit &unit) override {
    if (taken[5]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall5 call = reinterpret_cast<CuteQModbusRtuSerialServerCall5>(taken[5]);
      bool given = call(this, &unit, &handled);
      if (handled) return given;
    }
    return QModbusServer::writeData(unit);
  }

  //  bool QModbusServer::readData(QModbusDataUnit *newData) const
  bool readData(QModbusDataUnit *newData) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall6 call = reinterpret_cast<CuteQModbusRtuSerialServerCall6>(taken[6]);
      bool given = call(this, newData, &handled);
      if (handled) return given;
    }
    return QModbusServer::readData(newData);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall7 call = reinterpret_cast<CuteQModbusRtuSerialServerCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall8 call = reinterpret_cast<CuteQModbusRtuSerialServerCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall9 call = reinterpret_cast<CuteQModbusRtuSerialServerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall10 call = reinterpret_cast<CuteQModbusRtuSerialServerCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall11 call = reinterpret_cast<CuteQModbusRtuSerialServerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall12 call = reinterpret_cast<CuteQModbusRtuSerialServerCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQModbusRtuSerialServerCall13 call = reinterpret_cast<CuteQModbusRtuSerialServerCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusRtuSerialServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QModbusRtuSerialServer10metaObjectEv(
    const QModbusRtuSerialServer *self) {
  return self->metaObject();
}

//  void *QModbusRtuSerialServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QModbusRtuSerialServer11qt_metacastEPKc(
    QModbusRtuSerialServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QModbusRtuSerialServer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QModbusRtuSerialServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QModbusRtuSerialServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QModbusRtuSerialServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QModbusRtuSerialServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusRtuSerialServer::tr(s, c, n));
}

//  QModbusRtuSerialServerPrivate *QModbusRtuSerialServer::d_func()
extern "C" Q_DECL_EXPORT
QModbusRtuSerialServerPrivate *ritual_ZN22QModbusRtuSerialServer6d_funcEv(
    QModbusRtuSerialServer *self) {
  return self->d_func();
}

//  const QModbusRtuSerialServerPrivate *QModbusRtuSerialServer::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QModbusRtuSerialServerPrivate *ritual_ZNK22QModbusRtuSerialServer6d_funcEv(
    const QModbusRtuSerialServer *self) {
  return self->d_func();
}

//  QModbusRtuSerialServer::QModbusRtuSerialServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QModbusRtuSerialServer *ritual_ZN22QModbusRtuSerialServerC1EP7QObject(
    QObject *parent) {
  return new CuteQModbusRtuSerialServer(parent);
}

//  QModbusRtuSerialServer::~QModbusRtuSerialServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialServerD1Ev(QModbusRtuSerialServer *self) {
  delete self;
}

//  bool QModbusRtuSerialServer::processesBroadcast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QModbusRtuSerialServer18processesBroadcastEv(
    const QModbusRtuSerialServer *self) {
  return self->processesBroadcast();
}

//  int QModbusRtuSerialServer::interFrameDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QModbusRtuSerialServer15interFrameDelayEv(
    const QModbusRtuSerialServer *self) {
  return self->interFrameDelay();
}

//  void QModbusRtuSerialServer::setInterFrameDelay(int microseconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialServer18setInterFrameDelayEi(
    QModbusRtuSerialServer *self,
    int microseconds) {
  self->setInterFrameDelay(microseconds);
}

//  QModbusRtuSerialServer::QModbusRtuSerialServer(QModbusRtuSerialServerPriv
//      ate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QModbusRtuSerialServer *ritual_ZN22QModbusRtuSerialServerC1ER29QModbusRtuSerialServerPrivateP7QObject(
    QModbusRtuSerialServerPrivate *dd,
    QObject *parent) {
  return new CuteQModbusRtuSerialServer(*dd, parent);
}

//  bool QModbusRtuSerialServer::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QModbusRtuSerialServer4openEv(QModbusRtuSerialServer *self) {
  return self->open();
}

//  void QModbusRtuSerialServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialServer5closeEv(
    QModbusRtuSerialServer *self) {
  self->close();
}

//  QModbusResponse QModbusRtuSerialServer::processRequest(const QModbusPdu
//      &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN22QModbusRtuSerialServer14processRequestERK10QModbusPdu(
    QModbusRtuSerialServer *self,
    const QModbusPdu *request) {
  return new QModbusResponse(self->processRequest(*request));
}

//  a Python function taken by a CuteQModbusRtuSerialServer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusRtuSerialServer(
    QModbusRtuSerialServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusRtuSerialServer *>(self)->take(key, call);
}

//  bool QModbusRtuSerialServer::processesBroadcast() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QModbusRtuSerialServer18processesBroadcastEv(
    const QModbusRtuSerialServer *self) {
  return self->QModbusRtuSerialServer::processesBroadcast();
}

//  bool QModbusRtuSerialServer::open()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QModbusRtuSerialServer4openEv(
    QModbusRtuSerialServer *self) {
  return static_cast<OwnQModbusRtuSerialServer *>(self)->OwnQModbusRtuSerialServer::open();
}

//  void QModbusRtuSerialServer::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QModbusRtuSerialServer5closeEv(
    QModbusRtuSerialServer *self) {
  static_cast<OwnQModbusRtuSerialServer *>(self)->OwnQModbusRtuSerialServer::close();
}

#endif  // QT_CONFIG(modbus_serialport)
