//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QModbusResponse that Python can take functions over in. Every QModbusResponse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQModbusResponseCall0)(const void *, int, int *);
class CuteQModbusResponse : public QModbusResponse {
public:
  using QModbusResponse::QModbusResponse;
  CuteQModbusResponse(const QModbusResponse &other) : QModbusResponse(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QModbusPdu::setFunctionCode(FunctionCode code)
  void setFunctionCode(QModbusPdu::FunctionCode code) override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusResponseCall0 call = reinterpret_cast<CuteQModbusResponseCall0>(taken[0]);
      call(this, static_cast<int>(code), &handled);
      if (handled) return;
    }
    QModbusPdu::setFunctionCode(code);
  }
};

//  QModbusResponse::QModbusResponse()
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN15QModbusResponseC1Ev() {
  return new CuteQModbusResponse();
}

//  QModbusResponse::QModbusResponse(FunctionCode code, const QByteArray
//      &newData)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN15QModbusResponseC1EN10QModbusPdu12FunctionCodeERK10QByteArray(
    QModbusPdu::FunctionCode code,
    const QByteArray *newData) {
  return new CuteQModbusResponse(code, *newData);
}

//  QModbusResponse::~QModbusResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QModbusResponseD1Ev(QModbusResponse *self) {
  delete self;
}

//  int QModbusResponse::minimumDataSize(const QModbusResponse &pdu)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QModbusResponse15minimumDataSizeERKS_(
    const QModbusResponse *pdu) {
  return QModbusResponse::minimumDataSize(*pdu);
}

//  int QModbusResponse::calculateDataSize(const QModbusResponse &pdu)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QModbusResponse17calculateDataSizeERKS_(
    const QModbusResponse *pdu) {
  return QModbusResponse::calculateDataSize(*pdu);
}

//  a Python function taken by a CuteQModbusResponse, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusResponse(
    QModbusResponse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusResponse *>(self)->take(key, call);
}
