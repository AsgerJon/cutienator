//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbustcpclient.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbustcpclient.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QModbusTcpClient may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQModbusTcpClient : QModbusTcpClient {
  using QModbusTcpClient::open;
  using QModbusTcpClient::close;
};

//  A QModbusTcpClient that Python can take functions over in. Every QModbusTcpClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusTcpClientCall0)(const void *, int *);
typedef void (*CuteQModbusTcpClientCall1)(const void *, int *);
typedef bool (*CuteQModbusTcpClientCall2)(const void *, const QModbusResponse *, QModbusDataUnit *, int *);
typedef bool (*CuteQModbusTcpClientCall3)(const void *, const QModbusResponse *, QModbusDataUnit *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusTcpClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusTcpClientCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpClientCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpClientCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpClientCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpClientCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusTcpClientCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusTcpClient : public QModbusTcpClient {
public:
  using QModbusTcpClient::QModbusTcpClient;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
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

  //  bool QModbusTcpClient::open()
  bool open() override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusTcpClientCall0 call = reinterpret_cast<CuteQModbusTcpClientCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusTcpClient::open();
  }

  //  void QModbusTcpClient::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusTcpClientCall1 call = reinterpret_cast<CuteQModbusTcpClientCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QModbusTcpClient::close();
  }

  //  bool QModbusClient::processResponse(const QModbusResponse &response,
  //      QModbusDataUnit *data)
  bool processResponse(
      const QModbusResponse &response,
      QModbusDataUnit *data) override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusTcpClientCall2 call = reinterpret_cast<CuteQModbusTcpClientCall2>(taken[2]);
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
      CuteQModbusTcpClientCall3 call = reinterpret_cast<CuteQModbusTcpClientCall3>(taken[3]);
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
      CuteQModbusTcpClientCall4 call = reinterpret_cast<CuteQModbusTcpClientCall4>(taken[4]);
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
      CuteQModbusTcpClientCall5 call = reinterpret_cast<CuteQModbusTcpClientCall5>(taken[5]);
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
      CuteQModbusTcpClientCall6 call = reinterpret_cast<CuteQModbusTcpClientCall6>(taken[6]);
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
      CuteQModbusTcpClientCall7 call = reinterpret_cast<CuteQModbusTcpClientCall7>(taken[7]);
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
      CuteQModbusTcpClientCall8 call = reinterpret_cast<CuteQModbusTcpClientCall8>(taken[8]);
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
      CuteQModbusTcpClientCall9 call = reinterpret_cast<CuteQModbusTcpClientCall9>(taken[9]);
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
      CuteQModbusTcpClientCall10 call = reinterpret_cast<CuteQModbusTcpClientCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusTcpClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QModbusTcpClient10metaObjectEv(
    const QModbusTcpClient *self) {
  return self->metaObject();
}

//  void *QModbusTcpClient::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QModbusTcpClient11qt_metacastEPKc(
    QModbusTcpClient *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QModbusTcpClient::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QModbusTcpClient11qt_metacallEN11QMetaObject4CallEiPPv(
    QModbusTcpClient *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QModbusTcpClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QModbusTcpClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusTcpClient::tr(s, c, n));
}

//  QModbusTcpClientPrivate *QModbusTcpClient::d_func()
extern "C" Q_DECL_EXPORT
QModbusTcpClientPrivate *ritual_ZN16QModbusTcpClient6d_funcEv(
    QModbusTcpClient *self) {
  return self->d_func();
}

//  const QModbusTcpClientPrivate *QModbusTcpClient::d_func() const
extern "C" Q_DECL_EXPORT
const QModbusTcpClientPrivate *ritual_ZNK16QModbusTcpClient6d_funcEv(
    const QModbusTcpClient *self) {
  return self->d_func();
}

//  QModbusTcpClient::QModbusTcpClient(QObject *parent)
extern "C" Q_DECL_EXPORT
QModbusTcpClient *ritual_ZN16QModbusTcpClientC1EP7QObject(QObject *parent) {
  return new CuteQModbusTcpClient(parent);
}

//  QModbusTcpClient::~QModbusTcpClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusTcpClientD1Ev(QModbusTcpClient *self) {
  delete self;
}

//  QModbusTcpClient::QModbusTcpClient(QModbusTcpClientPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QModbusTcpClient *ritual_ZN16QModbusTcpClientC1ER23QModbusTcpClientPrivateP7QObject(
    QModbusTcpClientPrivate *dd,
    QObject *parent) {
  return new CuteQModbusTcpClient(*dd, parent);
}

//  bool QModbusTcpClient::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QModbusTcpClient4openEv(QModbusTcpClient *self) {
  return self->open();
}

//  void QModbusTcpClient::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusTcpClient5closeEv(QModbusTcpClient *self) {
  self->close();
}

//  a Python function taken by a CuteQModbusTcpClient, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusTcpClient(
    QModbusTcpClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusTcpClient *>(self)->take(key, call);
}

//  bool QModbusTcpClient::open()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QModbusTcpClient4openEv(QModbusTcpClient *self) {
  return static_cast<OwnQModbusTcpClient *>(self)->OwnQModbusTcpClient::open();
}

//  void QModbusTcpClient::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QModbusTcpClient5closeEv(QModbusTcpClient *self) {
  static_cast<OwnQModbusTcpClient *>(self)->OwnQModbusTcpClient::close();
}
