//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbustcpserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbustcpserver.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtSerialBus/qmodbusdataunit.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QModbusTcpServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQModbusTcpServer : QModbusTcpServer {
  using QModbusTcpServer::open;
  using QModbusTcpServer::close;
};

//  A QModbusTcpServer that Python can take functions over in. Every QModbusTcpServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusTcpServerCall0)(const void *, int *);
typedef void (*CuteQModbusTcpServerCall1)(const void *, int *);
typedef bool (*CuteQModbusTcpServerCall2)(const void *, int *);
typedef const QVariant * (*CuteQModbusTcpServerCall3)(const void *, int, int *);
typedef bool (*CuteQModbusTcpServerCall4)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQModbusTcpServerCall5)(const void *, const QModbusDataUnit *, int *);
typedef bool (*CuteQModbusTcpServerCall6)(const void *, QModbusDataUnit *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusTcpServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusTcpServerCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpServerCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpServerCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpServerCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpServerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpServerCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusTcpServer : public QModbusTcpServer {
public:
  using QModbusTcpServer::QModbusTcpServer;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QModbusServer18processesBroadcastEv")) {
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

  //  bool QModbusTcpServer::open()
  bool open() override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusTcpServerCall0 call = reinterpret_cast<CuteQModbusTcpServerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusTcpServer::open();
  }

  //  void QModbusTcpServer::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusTcpServerCall1 call = reinterpret_cast<CuteQModbusTcpServerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QModbusTcpServer::close();
  }

  //  bool QModbusServer::processesBroadcast() const
  bool processesBroadcast() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusTcpServerCall2 call = reinterpret_cast<CuteQModbusTcpServerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusServer::processesBroadcast();
  }

  //  QVariant QModbusServer::value(int option) const
  QVariant value(int option) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQModbusTcpServerCall3 call = reinterpret_cast<CuteQModbusTcpServerCall3>(taken[3]);
      const QVariant * given = call(this, option, &handled);
      if (handled && given) return *given;
    }
    return QModbusServer::value(option);
  }

  //  bool QModbusServer::setValue(int option, const QVariant &value)
  bool setValue(int option, const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQModbusTcpServerCall4 call = reinterpret_cast<CuteQModbusTcpServerCall4>(taken[4]);
      bool given = call(this, option, &value, &handled);
      if (handled) return given;
    }
    return QModbusServer::setValue(option, value);
  }

  //  bool QModbusServer::writeData(const QModbusDataUnit &unit)
  bool writeData(const QModbusDataUnit &unit) override {
    if (taken[5]) {
      int handled = 0;
      CuteQModbusTcpServerCall5 call = reinterpret_cast<CuteQModbusTcpServerCall5>(taken[5]);
      bool given = call(this, &unit, &handled);
      if (handled) return given;
    }
    return QModbusServer::writeData(unit);
  }

  //  bool QModbusServer::readData(QModbusDataUnit *newData) const
  bool readData(QModbusDataUnit *newData) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQModbusTcpServerCall6 call = reinterpret_cast<CuteQModbusTcpServerCall6>(taken[6]);
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
      CuteQModbusTcpServerCall7 call = reinterpret_cast<CuteQModbusTcpServerCall7>(taken[7]);
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
      CuteQModbusTcpServerCall8 call = reinterpret_cast<CuteQModbusTcpServerCall8>(taken[8]);
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
      CuteQModbusTcpServerCall9 call = reinterpret_cast<CuteQModbusTcpServerCall9>(taken[9]);
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
      CuteQModbusTcpServerCall10 call = reinterpret_cast<CuteQModbusTcpServerCall10>(taken[10]);
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
      CuteQModbusTcpServerCall11 call = reinterpret_cast<CuteQModbusTcpServerCall11>(taken[11]);
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
      CuteQModbusTcpServerCall12 call = reinterpret_cast<CuteQModbusTcpServerCall12>(taken[12]);
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
      CuteQModbusTcpServerCall13 call = reinterpret_cast<CuteQModbusTcpServerCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusTcpServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QModbusTcpServer10metaObjectEv(
    const QModbusTcpServer *self) {
  return self->metaObject();
}

//  QString QModbusTcpServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QModbusTcpServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusTcpServer::tr(s, c, n));
}

//  QModbusTcpServerPrivate *QModbusTcpServer::d_func()
extern "C" Q_DECL_EXPORT
QModbusTcpServerPrivate *ritual_ZN16QModbusTcpServer6d_funcEv(
    QModbusTcpServer *self) {
  return self->d_func();
}

//  const QModbusTcpServerPrivate *QModbusTcpServer::d_func() const
extern "C" Q_DECL_EXPORT
const QModbusTcpServerPrivate *ritual_ZNK16QModbusTcpServer6d_funcEv(
    const QModbusTcpServer *self) {
  return self->d_func();
}

//  QModbusTcpServer::QModbusTcpServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QModbusTcpServer *ritual_ZN16QModbusTcpServerC1EP7QObject(QObject *parent) {
  return new CuteQModbusTcpServer(parent);
}

//  QModbusTcpServer::~QModbusTcpServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusTcpServerD1Ev(QModbusTcpServer *self) {
  delete self;
}

//  void
//      QModbusTcpServer::installConnectionObserver(QModbusTcpConnectionObser
//      ver *observer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusTcpServer25installConnectionObserverEP28QModbusTcpConnectionObserver(
    QModbusTcpServer *self,
    QModbusTcpConnectionObserver *observer) {
  self->installConnectionObserver(observer);
}

//  bool QModbusTcpServer::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QModbusTcpServer4openEv(QModbusTcpServer *self) {
  return self->open();
}

//  void QModbusTcpServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusTcpServer5closeEv(QModbusTcpServer *self) {
  self->close();
}

//  a Python function taken by a CuteQModbusTcpServer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusTcpServer(
    QModbusTcpServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusTcpServer *>(self)->take(key, call);
}

//  bool QModbusTcpServer::open()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QModbusTcpServer4openEv(QModbusTcpServer *self) {
  return static_cast<OwnQModbusTcpServer *>(self)->OwnQModbusTcpServer::open();
}

//  void QModbusTcpServer::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QModbusTcpServer5closeEv(QModbusTcpServer *self) {
  static_cast<OwnQModbusTcpServer *>(self)->OwnQModbusTcpServer::close();
}
