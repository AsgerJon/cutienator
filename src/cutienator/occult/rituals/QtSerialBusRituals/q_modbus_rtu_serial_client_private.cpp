//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSerialBus/qtserialbusglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(modbus_serialport)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbusrtuserialclient.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbuspdu.h>
#include <QtSerialBus/qmodbusdataunit.h>
#include <cstring>

//  A QModbusRtuSerialClientPrivate that Python can take functions over in. Every QModbusRtuSerialClientPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusRtuSerialClientPrivateCall0)(const void *, const QModbusRequest *, int, const QModbusDataUnit *, int, int *);
typedef bool (*CuteQModbusRtuSerialClientPrivateCall1)(const void *, int *);
typedef void * (*CuteQModbusRtuSerialClientPrivateCall2)(const void *, int *);
class CuteQModbusRtuSerialClientPrivate : public QModbusRtuSerialClientPrivate {
public:
  using QModbusRtuSerialClientPrivate::QModbusRtuSerialClientPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QModbusClientPrivate6isOpenEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QModbusDevicePrivate6deviceEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QModbusReply *QModbusRtuSerialClientPrivate::enqueueRequest(const
  //      QModbusRequest &request, int serverAddress, const QModbusDataUnit
  //      &unit, QModbusReply::ReplyType type)
  QModbusReply *enqueueRequest(
      const QModbusRequest &request,
      int serverAddress,
      const QModbusDataUnit &unit,
      QModbusReply::ReplyType type) override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusRtuSerialClientPrivateCall0 call = reinterpret_cast<CuteQModbusRtuSerialClientPrivateCall0>(taken[0]);
      void * given = call(this, &request, serverAddress, &unit, static_cast<int>(type), &handled);
      if (handled) return static_cast<QModbusReply *>(given);
    }
    return QModbusRtuSerialClientPrivate::enqueueRequest(request, serverAddress, unit, type);
  }

  //  bool QModbusRtuSerialClientPrivate::isOpen() const
  bool isOpen() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusRtuSerialClientPrivateCall1 call = reinterpret_cast<CuteQModbusRtuSerialClientPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusRtuSerialClientPrivate::isOpen();
  }

  //  QIODevice *QModbusRtuSerialClientPrivate::device() const
  QIODevice *device() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusRtuSerialClientPrivateCall2 call = reinterpret_cast<CuteQModbusRtuSerialClientPrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusRtuSerialClientPrivate::device();
  }
};

//  QModbusRtuSerialClient *QModbusRtuSerialClientPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusRtuSerialClient *ritual_ZN29QModbusRtuSerialClientPrivate6q_funcEv(
    QModbusRtuSerialClientPrivate *self) {
  return self->q_func();
}

//  const QModbusRtuSerialClient *QModbusRtuSerialClientPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QModbusRtuSerialClient *ritual_ZNK29QModbusRtuSerialClientPrivate6q_funcEv(
    const QModbusRtuSerialClientPrivate *self) {
  return self->q_func();
}

//  void QModbusRtuSerialClientPrivate::onAboutToClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QModbusRtuSerialClientPrivate14onAboutToCloseEv(
    QModbusRtuSerialClientPrivate *self) {
  self->onAboutToClose();
}

//  void QModbusRtuSerialClientPrivate::setupEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QModbusRtuSerialClientPrivate16setupEnvironmentEv(
    QModbusRtuSerialClientPrivate *self) {
  self->setupEnvironment();
}

//  QModbusReply *QModbusRtuSerialClientPrivate::enqueueRequest(const
//      QModbusRequest &request, int serverAddress, const QModbusDataUnit
//      &unit, QModbusReply::ReplyType type)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN29QModbusRtuSerialClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE(
    QModbusRtuSerialClientPrivate *self,
    const QModbusRequest *request,
    int serverAddress,
    const QModbusDataUnit *unit,
    QModbusReply::ReplyType type) {
  return self->enqueueRequest(*request, serverAddress, *unit, type);
}

//  bool QModbusRtuSerialClientPrivate::canMatchRequestAndResponse(const
//      QModbusResponse &response, int sendingServer) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QModbusRtuSerialClientPrivate26canMatchRequestAndResponseERK15QModbusResponsei(
    const QModbusRtuSerialClientPrivate *self,
    const QModbusResponse *response,
    int sendingServer) {
  return self->canMatchRequestAndResponse(*response, sendingServer);
}

//  bool QModbusRtuSerialClientPrivate::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QModbusRtuSerialClientPrivate6isOpenEv(
    const QModbusRtuSerialClientPrivate *self) {
  return self->isOpen();
}

//  QIODevice *QModbusRtuSerialClientPrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK29QModbusRtuSerialClientPrivate6deviceEv(
    const QModbusRtuSerialClientPrivate *self) {
  return self->device();
}

//  a Python function taken by a CuteQModbusRtuSerialClientPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusRtuSerialClientPrivate(
    QModbusRtuSerialClientPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusRtuSerialClientPrivate *>(self)->take(key, call);
}

//  bool QModbusRtuSerialClientPrivate::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QModbusRtuSerialClientPrivate6isOpenEv(
    const QModbusRtuSerialClientPrivate *self) {
  return self->QModbusRtuSerialClientPrivate::isOpen();
}

//  QIODevice *QModbusRtuSerialClientPrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZNK29QModbusRtuSerialClientPrivate6deviceEv(
    const QModbusRtuSerialClientPrivate *self) {
  return self->QModbusRtuSerialClientPrivate::device();
}

#endif  // QT_CONFIG(modbus_serialport)
