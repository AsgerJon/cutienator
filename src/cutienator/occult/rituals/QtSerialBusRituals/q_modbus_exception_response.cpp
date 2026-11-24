//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbuspdu.h>
#include <cstring>

//  A QModbusExceptionResponse that Python can take functions over in. Every QModbusExceptionResponse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQModbusExceptionResponseCall0)(const void *, int, int *);
class CuteQModbusExceptionResponse : public QModbusExceptionResponse {
public:
  using QModbusExceptionResponse::QModbusExceptionResponse;
  CuteQModbusExceptionResponse(const QModbusExceptionResponse &other) : QModbusExceptionResponse(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QModbusExceptionResponse::setFunctionCode(FunctionCode c)
  void setFunctionCode(QModbusPdu::FunctionCode c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusExceptionResponseCall0 call = reinterpret_cast<CuteQModbusExceptionResponseCall0>(taken[0]);
      call(this, static_cast<int>(c), &handled);
      if (handled) return;
    }
    QModbusExceptionResponse::setFunctionCode(c);
  }
};

//  QModbusExceptionResponse::QModbusExceptionResponse()
extern "C" Q_DECL_EXPORT
QModbusExceptionResponse *ritual_ZN24QModbusExceptionResponseC1Ev() {
  return new CuteQModbusExceptionResponse();
}

//  QModbusExceptionResponse::QModbusExceptionResponse(FunctionCode fc,
//      ExceptionCode ec)
extern "C" Q_DECL_EXPORT
QModbusExceptionResponse *ritual_ZN24QModbusExceptionResponseC1EN10QModbusPdu12FunctionCodeENS0_13ExceptionCodeE(
    QModbusPdu::FunctionCode fc,
    QModbusPdu::ExceptionCode ec) {
  return new CuteQModbusExceptionResponse(fc, ec);
}

//  QModbusExceptionResponse::~QModbusExceptionResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QModbusExceptionResponseD1Ev(
    QModbusExceptionResponse *self) {
  delete self;
}

//  void QModbusExceptionResponse::setFunctionCode(FunctionCode c)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QModbusExceptionResponse15setFunctionCodeEN10QModbusPdu12FunctionCodeE(
    QModbusExceptionResponse *self,
    QModbusPdu::FunctionCode c) {
  self->setFunctionCode(c);
}

//  void QModbusExceptionResponse::setExceptionCode(ExceptionCode ec)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QModbusExceptionResponse16setExceptionCodeEN10QModbusPdu13ExceptionCodeE(
    QModbusExceptionResponse *self,
    QModbusPdu::ExceptionCode ec) {
  self->setExceptionCode(ec);
}

//  a Python function taken by a CuteQModbusExceptionResponse, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusExceptionResponse(
    QModbusExceptionResponse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusExceptionResponse *>(self)->take(key, call);
}

//  void QModbusExceptionResponse::setFunctionCode(FunctionCode c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QModbusExceptionResponse15setFunctionCodeEN10QModbusPdu12FunctionCodeE(
    QModbusExceptionResponse *self,
    QModbusPdu::FunctionCode c) {
  self->QModbusExceptionResponse::setFunctionCode(c);
}
