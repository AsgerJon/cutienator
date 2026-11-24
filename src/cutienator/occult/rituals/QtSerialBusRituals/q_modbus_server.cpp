//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbusserver.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtSerialBus/qmodbusdataunit.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QModbusServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQModbusServer : QModbusServer {
  using QModbusServer::writeData;
  using QModbusServer::readData;
};

//  A QModbusServer that Python can take functions over in. Every QModbusServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusServerCall0)(const void *, int *);
typedef const QVariant * (*CuteQModbusServerCall1)(const void *, int, int *);
typedef bool (*CuteQModbusServerCall2)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQModbusServerCall3)(const void *, const QModbusDataUnit *, int *);
typedef bool (*CuteQModbusServerCall4)(const void *, QModbusDataUnit *, int *);
typedef bool (*CuteQModbusServerCall5)(const void *, int *);
typedef void (*CuteQModbusServerCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusServerCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusServerCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusServerCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusServerCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusServerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusServerCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusServer : public QModbusServer {
public:
  using QModbusServer::QModbusServer;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QModbusServer18processesBroadcastEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QModbusServer5valueEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusServer8setValueEiRK8QVariant")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusServer9writeDataERK15QModbusDataUnit")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QModbusServer8readDataEP15QModbusDataUnit")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
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

  //  bool QModbusServer::processesBroadcast() const
  bool processesBroadcast() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusServerCall0 call = reinterpret_cast<CuteQModbusServerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusServer::processesBroadcast();
  }

  //  QVariant QModbusServer::value(int option) const
  QVariant value(int option) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusServerCall1 call = reinterpret_cast<CuteQModbusServerCall1>(taken[1]);
      const QVariant * given = call(this, option, &handled);
      if (handled && given) return *given;
    }
    return QModbusServer::value(option);
  }

  //  bool QModbusServer::setValue(int option, const QVariant &value)
  bool setValue(int option, const QVariant &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusServerCall2 call = reinterpret_cast<CuteQModbusServerCall2>(taken[2]);
      bool given = call(this, option, &value, &handled);
      if (handled) return given;
    }
    return QModbusServer::setValue(option, value);
  }

  //  bool QModbusServer::writeData(const QModbusDataUnit &unit)
  bool writeData(const QModbusDataUnit &unit) override {
    if (taken[3]) {
      int handled = 0;
      CuteQModbusServerCall3 call = reinterpret_cast<CuteQModbusServerCall3>(taken[3]);
      bool given = call(this, &unit, &handled);
      if (handled) return given;
    }
    return QModbusServer::writeData(unit);
  }

  //  bool QModbusServer::readData(QModbusDataUnit *newData) const
  bool readData(QModbusDataUnit *newData) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQModbusServerCall4 call = reinterpret_cast<CuteQModbusServerCall4>(taken[4]);
      bool given = call(this, newData, &handled);
      if (handled) return given;
    }
    return QModbusServer::readData(newData);
  }

  //  bool QModbusDevice::open()
  bool open() override {
    if (taken[5]) {
      int handled = 0;
      CuteQModbusServerCall5 call = reinterpret_cast<CuteQModbusServerCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QModbusDevice::close()
  void close() override {
    if (taken[6]) {
      int handled = 0;
      CuteQModbusServerCall6 call = reinterpret_cast<CuteQModbusServerCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQModbusServerCall7 call = reinterpret_cast<CuteQModbusServerCall7>(taken[7]);
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
      CuteQModbusServerCall8 call = reinterpret_cast<CuteQModbusServerCall8>(taken[8]);
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
      CuteQModbusServerCall9 call = reinterpret_cast<CuteQModbusServerCall9>(taken[9]);
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
      CuteQModbusServerCall10 call = reinterpret_cast<CuteQModbusServerCall10>(taken[10]);
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
      CuteQModbusServerCall11 call = reinterpret_cast<CuteQModbusServerCall11>(taken[11]);
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
      CuteQModbusServerCall12 call = reinterpret_cast<CuteQModbusServerCall12>(taken[12]);
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
      CuteQModbusServerCall13 call = reinterpret_cast<CuteQModbusServerCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QModbusServer10metaObjectEv(
    const QModbusServer *self) {
  return self->metaObject();
}

//  QString QModbusServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QModbusServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusServer::tr(s, c, n));
}

//  QModbusServerPrivate *QModbusServer::d_func()
extern "C" Q_DECL_EXPORT
QModbusServerPrivate *ritual_ZN13QModbusServer6d_funcEv(
    QModbusServer *self) {
  return self->d_func();
}

//  const QModbusServerPrivate *QModbusServer::d_func() const
extern "C" Q_DECL_EXPORT
const QModbusServerPrivate *ritual_ZNK13QModbusServer6d_funcEv(
    const QModbusServer *self) {
  return self->d_func();
}

//  QModbusServer::~QModbusServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusServerD1Ev(QModbusServer *self) {
  delete self;
}

//  int QModbusServer::serverAddress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QModbusServer13serverAddressEv(const QModbusServer *self) {
  return self->serverAddress();
}

//  void QModbusServer::setServerAddress(int serverAddress)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusServer16setServerAddressEi(
    QModbusServer *self,
    int serverAddress) {
  self->setServerAddress(serverAddress);
}

//  bool QModbusServer::processesBroadcast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QModbusServer18processesBroadcastEv(
    const QModbusServer *self) {
  return self->processesBroadcast();
}

//  QVariant QModbusServer::value(int option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QModbusServer5valueEi(
    const QModbusServer *self,
    int option) {
  return new QVariant(self->value(option));
}

//  bool QModbusServer::setValue(int option, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusServer8setValueEiRK8QVariant(
    QModbusServer *self,
    int option,
    const QVariant *value) {
  return self->setValue(option, *value);
}

//  bool QModbusServer::data(QModbusDataUnit *newData) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QModbusServer4dataEP15QModbusDataUnit(
    const QModbusServer *self,
    QModbusDataUnit *newData) {
  return self->data(newData);
}

//  bool QModbusServer::setData(const QModbusDataUnit &unit)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusServer7setDataERK15QModbusDataUnit(
    QModbusServer *self,
    const QModbusDataUnit *unit) {
  return self->setData(*unit);
}

//  bool QModbusServer::setData(QModbusDataUnit::RegisterType table, quint16
//      address, quint16 data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusServer7setDataEN15QModbusDataUnit12RegisterTypeEtt(
    QModbusServer *self,
    QModbusDataUnit::RegisterType table,
    quint16 address,
    quint16 data) {
  return self->setData(table, address, data);
}

//  bool QModbusServer::data(QModbusDataUnit::RegisterType table, quint16
//      address, quint16 *data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QModbusServer4dataEN15QModbusDataUnit12RegisterTypeEtPt(
    const QModbusServer *self,
    QModbusDataUnit::RegisterType table,
    quint16 address,
    quint16 *data) {
  return self->data(table, address, data);
}

//  bool QModbusServer::writeData(const QModbusDataUnit &unit)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusServer9writeDataERK15QModbusDataUnit(
    QModbusServer *self,
    const QModbusDataUnit *unit) {
  return self->writeData(*unit);
}

//  bool QModbusServer::readData(QModbusDataUnit *newData) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QModbusServer8readDataEP15QModbusDataUnit(
    const QModbusServer *self,
    QModbusDataUnit *newData) {
  return self->readData(newData);
}

//  a Python function taken by a CuteQModbusServer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusServer(
    QModbusServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusServer *>(self)->take(key, call);
}

//  bool QModbusServer::processesBroadcast() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QModbusServer18processesBroadcastEv(
    const QModbusServer *self) {
  return self->QModbusServer::processesBroadcast();
}

//  QVariant QModbusServer::value(int option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13QModbusServer5valueEi(
    const QModbusServer *self,
    int option) {
  return new QVariant(self->QModbusServer::value(option));
}

//  bool QModbusServer::setValue(int option, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QModbusServer8setValueEiRK8QVariant(
    QModbusServer *self,
    int option,
    const QVariant *value) {
  return self->QModbusServer::setValue(option, *value);
}

//  bool QModbusServer::writeData(const QModbusDataUnit &unit)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QModbusServer9writeDataERK15QModbusDataUnit(
    QModbusServer *self,
    const QModbusDataUnit *unit) {
  return static_cast<OwnQModbusServer *>(self)->OwnQModbusServer::writeData(
      *unit);
}

//  bool QModbusServer::readData(QModbusDataUnit *newData) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QModbusServer8readDataEP15QModbusDataUnit(
    const QModbusServer *self,
    QModbusDataUnit *newData) {
  return static_cast<const OwnQModbusServer *>(self)->OwnQModbusServer::readData(
      newData);
}
