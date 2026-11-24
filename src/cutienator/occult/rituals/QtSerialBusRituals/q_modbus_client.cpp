//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusclient.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbusclient.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qmodbusdataunit.h>
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QModbusClient may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQModbusClient : QModbusClient {
  using QModbusClient::processResponse;
  using QModbusClient::processPrivateResponse;
};

//  A QModbusClient that Python can take functions over in. Every QModbusClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusClientCall0)(const void *, const QModbusResponse *, QModbusDataUnit *, int *);
typedef bool (*CuteQModbusClientCall1)(const void *, const QModbusResponse *, QModbusDataUnit *, int *);
typedef bool (*CuteQModbusClientCall2)(const void *, int *);
typedef void (*CuteQModbusClientCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusClientCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusClientCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusClientCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusClientCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusClientCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusClientCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusClient : public QModbusClient {
public:
  using QModbusClient::QModbusClient;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QModbusClient15processResponseERK15QModbusResponseP15QModbusDataUnit")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusClient22processPrivateResponseERK15QModbusResponseP15QModbusDataUnit")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
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

  //  bool QModbusClient::processResponse(const QModbusResponse &response,
  //      QModbusDataUnit *data)
  bool processResponse(
      const QModbusResponse &response,
      QModbusDataUnit *data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusClientCall0 call = reinterpret_cast<CuteQModbusClientCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQModbusClientCall1 call = reinterpret_cast<CuteQModbusClientCall1>(taken[1]);
      bool given = call(this, &response, data, &handled);
      if (handled) return given;
    }
    return QModbusClient::processPrivateResponse(response, data);
  }

  //  bool QModbusDevice::open()
  bool open() override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusClientCall2 call = reinterpret_cast<CuteQModbusClientCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QModbusDevice::close()
  void close() override {
    if (taken[3]) {
      int handled = 0;
      CuteQModbusClientCall3 call = reinterpret_cast<CuteQModbusClientCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQModbusClientCall4 call = reinterpret_cast<CuteQModbusClientCall4>(taken[4]);
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
      CuteQModbusClientCall5 call = reinterpret_cast<CuteQModbusClientCall5>(taken[5]);
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
      CuteQModbusClientCall6 call = reinterpret_cast<CuteQModbusClientCall6>(taken[6]);
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
      CuteQModbusClientCall7 call = reinterpret_cast<CuteQModbusClientCall7>(taken[7]);
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
      CuteQModbusClientCall8 call = reinterpret_cast<CuteQModbusClientCall8>(taken[8]);
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
      CuteQModbusClientCall9 call = reinterpret_cast<CuteQModbusClientCall9>(taken[9]);
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
      CuteQModbusClientCall10 call = reinterpret_cast<CuteQModbusClientCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QModbusClient10metaObjectEv(
    const QModbusClient *self) {
  return self->metaObject();
}

//  QString QModbusClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QModbusClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusClient::tr(s, c, n));
}

//  QModbusClientPrivate *QModbusClient::d_func()
extern "C" Q_DECL_EXPORT
QModbusClientPrivate *ritual_ZN13QModbusClient6d_funcEv(
    QModbusClient *self) {
  return self->d_func();
}

//  const QModbusClientPrivate *QModbusClient::d_func() const
extern "C" Q_DECL_EXPORT
const QModbusClientPrivate *ritual_ZNK13QModbusClient6d_funcEv(
    const QModbusClient *self) {
  return self->d_func();
}

//  QModbusClient::~QModbusClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusClientD1Ev(QModbusClient *self) {
  delete self;
}

//  QModbusReply *QModbusClient::sendReadRequest(const QModbusDataUnit &read,
//      int serverAddress)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN13QModbusClient15sendReadRequestERK15QModbusDataUniti(
    QModbusClient *self,
    const QModbusDataUnit *read,
    int serverAddress) {
  return self->sendReadRequest(*read, serverAddress);
}

//  QModbusReply *QModbusClient::sendWriteRequest(const QModbusDataUnit
//      &write, int serverAddress)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN13QModbusClient16sendWriteRequestERK15QModbusDataUniti(
    QModbusClient *self,
    const QModbusDataUnit *write,
    int serverAddress) {
  return self->sendWriteRequest(*write, serverAddress);
}

//  QModbusReply *QModbusClient::sendReadWriteRequest(const QModbusDataUnit
//      &read, const QModbusDataUnit &write, int serverAddress)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN13QModbusClient20sendReadWriteRequestERK15QModbusDataUnitS2_i(
    QModbusClient *self,
    const QModbusDataUnit *read,
    const QModbusDataUnit *write,
    int serverAddress) {
  return self->sendReadWriteRequest(*read, *write, serverAddress);
}

//  QModbusReply *QModbusClient::sendRawRequest(const QModbusRequest
//      &request, int serverAddress)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN13QModbusClient14sendRawRequestERK14QModbusRequesti(
    QModbusClient *self,
    const QModbusRequest *request,
    int serverAddress) {
  return self->sendRawRequest(*request, serverAddress);
}

//  int QModbusClient::timeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QModbusClient7timeoutEv(const QModbusClient *self) {
  return self->timeout();
}

//  void QModbusClient::setTimeout(int newTimeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusClient10setTimeoutEi(
    QModbusClient *self,
    int newTimeout) {
  self->setTimeout(newTimeout);
}

//  int QModbusClient::numberOfRetries() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QModbusClient15numberOfRetriesEv(const QModbusClient *self) {
  return self->numberOfRetries();
}

//  void QModbusClient::setNumberOfRetries(int number)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusClient18setNumberOfRetriesEi(
    QModbusClient *self,
    int number) {
  self->setNumberOfRetries(number);
}

//  bool QModbusClient::processResponse(const QModbusResponse &response,
//      QModbusDataUnit *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusClient15processResponseERK15QModbusResponseP15QModbusDataUnit(
    QModbusClient *self,
    const QModbusResponse *response,
    QModbusDataUnit *data) {
  return self->processResponse(*response, data);
}

//  bool QModbusClient::processPrivateResponse(const QModbusResponse
//      &response, QModbusDataUnit *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusClient22processPrivateResponseERK15QModbusResponseP15QModbusDataUnit(
    QModbusClient *self,
    const QModbusResponse *response,
    QModbusDataUnit *data) {
  return self->processPrivateResponse(*response, data);
}

//  a Python function taken by a CuteQModbusClient, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusClient(
    QModbusClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusClient *>(self)->take(key, call);
}

//  bool QModbusClient::processResponse(const QModbusResponse &response,
//      QModbusDataUnit *data)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QModbusClient15processResponseERK15QModbusResponseP15QModbusDataUnit(
    QModbusClient *self,
    const QModbusResponse *response,
    QModbusDataUnit *data) {
  return static_cast<OwnQModbusClient *>(self)->OwnQModbusClient::processResponse(
      *response,
      data);
}

//  bool QModbusClient::processPrivateResponse(const QModbusResponse
//      &response, QModbusDataUnit *data)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QModbusClient22processPrivateResponseERK15QModbusResponseP15QModbusDataUnit(
    QModbusClient *self,
    const QModbusResponse *response,
    QModbusDataUnit *data) {
  return static_cast<OwnQModbusClient *>(self)->OwnQModbusClient::processPrivateResponse(
      *response,
      data);
}
