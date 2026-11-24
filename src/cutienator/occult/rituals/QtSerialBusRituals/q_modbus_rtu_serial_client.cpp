//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusrtuserialclient.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSerialBus/qtserialbusglobal.h>
#if QT_CONFIG(modbus_serialport)
#include <QtSerialBus/qmodbusrtuserialclient.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QModbusRtuSerialClient may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQModbusRtuSerialClient : QModbusRtuSerialClient {
  using QModbusRtuSerialClient::close;
  using QModbusRtuSerialClient::open;
};

//  A QModbusRtuSerialClient that Python can take functions over in. Every QModbusRtuSerialClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQModbusRtuSerialClientCall0)(const void *, int *);
typedef bool (*CuteQModbusRtuSerialClientCall1)(const void *, int *);
typedef bool (*CuteQModbusRtuSerialClientCall2)(const void *, const QModbusResponse *, QModbusDataUnit *, int *);
typedef bool (*CuteQModbusRtuSerialClientCall3)(const void *, const QModbusResponse *, QModbusDataUnit *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusRtuSerialClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusRtuSerialClientCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialClientCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialClientCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialClientCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialClientCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusRtuSerialClientCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusRtuSerialClient : public QModbusRtuSerialClient {
public:
  using QModbusRtuSerialClient::QModbusRtuSerialClient;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusClient15processResponseERK15QModbusResponseP15QModbusDataUnit")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusClient22processPrivateResponseERK15QModbusResponseP15QModbusDataUnit")) {
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

  //  void QModbusRtuSerialClient::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusRtuSerialClientCall0 call = reinterpret_cast<CuteQModbusRtuSerialClientCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QModbusRtuSerialClient::close();
  }

  //  bool QModbusRtuSerialClient::open()
  bool open() override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusRtuSerialClientCall1 call = reinterpret_cast<CuteQModbusRtuSerialClientCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusRtuSerialClient::open();
  }

  //  bool QModbusClient::processResponse(const QModbusResponse &response,
  //      QModbusDataUnit *data)
  bool processResponse(
      const QModbusResponse &response,
      QModbusDataUnit *data) override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusRtuSerialClientCall2 call = reinterpret_cast<CuteQModbusRtuSerialClientCall2>(taken[2]);
      bool given = call(this, &response, data, &handled);
      if (handled) return given;
    }
    return QModbusClient::processResponse(response, data);
  }

  //  bool QModbusClient::processPrivateResponse(const QModbusResponse
  //      &response, QModbusDataUnit *data)
  bool processPrivateResponse(
      const QModbusResponse &response,
      QModbusDataUnit *data) override {
    if (taken[3]) {
      int handled = 0;
      CuteQModbusRtuSerialClientCall3 call = reinterpret_cast<CuteQModbusRtuSerialClientCall3>(taken[3]);
      bool given = call(this, &response, data, &handled);
      if (handled) return given;
    }
    return QModbusClient::processPrivateResponse(response, data);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQModbusRtuSerialClientCall4 call = reinterpret_cast<CuteQModbusRtuSerialClientCall4>(taken[4]);
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
      CuteQModbusRtuSerialClientCall5 call = reinterpret_cast<CuteQModbusRtuSerialClientCall5>(taken[5]);
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
      CuteQModbusRtuSerialClientCall6 call = reinterpret_cast<CuteQModbusRtuSerialClientCall6>(taken[6]);
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
      CuteQModbusRtuSerialClientCall7 call = reinterpret_cast<CuteQModbusRtuSerialClientCall7>(taken[7]);
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
      CuteQModbusRtuSerialClientCall8 call = reinterpret_cast<CuteQModbusRtuSerialClientCall8>(taken[8]);
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
      CuteQModbusRtuSerialClientCall9 call = reinterpret_cast<CuteQModbusRtuSerialClientCall9>(taken[9]);
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
      CuteQModbusRtuSerialClientCall10 call = reinterpret_cast<CuteQModbusRtuSerialClientCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusRtuSerialClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QModbusRtuSerialClient10metaObjectEv(
    const QModbusRtuSerialClient *self) {
  return self->metaObject();
}

//  QString QModbusRtuSerialClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QModbusRtuSerialClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusRtuSerialClient::tr(s, c, n));
}

//  QModbusRtuSerialClientPrivate *QModbusRtuSerialClient::d_func()
extern "C" Q_DECL_EXPORT
QModbusRtuSerialClientPrivate *ritual_ZN22QModbusRtuSerialClient6d_funcEv(
    QModbusRtuSerialClient *self) {
  return self->d_func();
}

//  const QModbusRtuSerialClientPrivate *QModbusRtuSerialClient::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QModbusRtuSerialClientPrivate *ritual_ZNK22QModbusRtuSerialClient6d_funcEv(
    const QModbusRtuSerialClient *self) {
  return self->d_func();
}

//  QModbusRtuSerialClient::QModbusRtuSerialClient(QObject *parent)
extern "C" Q_DECL_EXPORT
QModbusRtuSerialClient *ritual_ZN22QModbusRtuSerialClientC1EP7QObject(
    QObject *parent) {
  return new CuteQModbusRtuSerialClient(parent);
}

//  QModbusRtuSerialClient::~QModbusRtuSerialClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialClientD1Ev(QModbusRtuSerialClient *self) {
  delete self;
}

//  int QModbusRtuSerialClient::interFrameDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QModbusRtuSerialClient15interFrameDelayEv(
    const QModbusRtuSerialClient *self) {
  return self->interFrameDelay();
}

//  void QModbusRtuSerialClient::setInterFrameDelay(int microseconds)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialClient18setInterFrameDelayEi(
    QModbusRtuSerialClient *self,
    int microseconds) {
  self->setInterFrameDelay(microseconds);
}

//  int QModbusRtuSerialClient::turnaroundDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QModbusRtuSerialClient15turnaroundDelayEv(
    const QModbusRtuSerialClient *self) {
  return self->turnaroundDelay();
}

//  void QModbusRtuSerialClient::setTurnaroundDelay(int turnaroundDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialClient18setTurnaroundDelayEi(
    QModbusRtuSerialClient *self,
    int turnaroundDelay) {
  self->setTurnaroundDelay(turnaroundDelay);
}

//  void QModbusRtuSerialClient::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QModbusRtuSerialClient5closeEv(
    QModbusRtuSerialClient *self) {
  self->close();
}

//  bool QModbusRtuSerialClient::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QModbusRtuSerialClient4openEv(QModbusRtuSerialClient *self) {
  return self->open();
}

//  a Python function taken by a CuteQModbusRtuSerialClient, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusRtuSerialClient(
    QModbusRtuSerialClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusRtuSerialClient *>(self)->take(key, call);
}

//  void QModbusRtuSerialClient::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QModbusRtuSerialClient5closeEv(
    QModbusRtuSerialClient *self) {
  static_cast<OwnQModbusRtuSerialClient *>(self)->OwnQModbusRtuSerialClient::close();
}

//  bool QModbusRtuSerialClient::open()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QModbusRtuSerialClient4openEv(
    QModbusRtuSerialClient *self) {
  return static_cast<OwnQModbusRtuSerialClient *>(self)->OwnQModbusRtuSerialClient::open();
}

#endif  // QT_CONFIG(modbus_serialport)
