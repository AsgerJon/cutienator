//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QModbusRequest that Python can take functions over in. Every QModbusRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQModbusRequestCall0)(const void *, int, int *);
class CuteQModbusRequest : public QModbusRequest {
public:
  using QModbusRequest::QModbusRequest;
  CuteQModbusRequest(const QModbusRequest & other) : QModbusRequest(other) {}
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
      CuteQModbusRequestCall0 call = reinterpret_cast<CuteQModbusRequestCall0>(taken[0]);
      call(this, static_cast<int>(code), &handled);
      if (handled) return;
    }
    QModbusPdu::setFunctionCode(code);
  }
};

//  QModbusRequest::QModbusRequest()
extern "C" Q_DECL_EXPORT
QModbusRequest *ritual_ZN14QModbusRequestC1Ev() {
  return new CuteQModbusRequest();
}

//  QModbusRequest::QModbusRequest(const QModbusPdu &pdu)
extern "C" Q_DECL_EXPORT
QModbusRequest *ritual_ZN14QModbusRequestC1ERK10QModbusPdu(
    const QModbusPdu *pdu) {
  return new CuteQModbusRequest(*pdu);
}

//  QModbusRequest::QModbusRequest(FunctionCode code, const QByteArray
//      &newData)
extern "C" Q_DECL_EXPORT
QModbusRequest *ritual_ZN14QModbusRequestC1EN10QModbusPdu12FunctionCodeERK10QByteArray(
    QModbusPdu::FunctionCode code,
    const QByteArray *newData) {
  return new CuteQModbusRequest(code, *newData);
}

//  QModbusRequest::~QModbusRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModbusRequestD1Ev(QModbusRequest *self) {
  delete self;
}

//  int QModbusRequest::minimumDataSize(const QModbusRequest &pdu)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QModbusRequest15minimumDataSizeERKS_(
    const QModbusRequest *pdu) {
  return QModbusRequest::minimumDataSize(*pdu);
}

//  int QModbusRequest::calculateDataSize(const QModbusRequest &pdu)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QModbusRequest17calculateDataSizeERKS_(
    const QModbusRequest *pdu) {
  return QModbusRequest::calculateDataSize(*pdu);
}

//  void QModbusRequest::registerDataSizeCalculator(FunctionCode fc,
//      CalcFuncPtr func)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QModbusRequest26registerDataSizeCalculatorEN10QModbusPdu12FunctionCodeEPFiRKS_E(
    QModbusPdu::FunctionCode fc,
    void *func) {
  QModbusRequest::registerDataSizeCalculator(
      fc,
      reinterpret_cast<QModbusRequest::CalcFuncPtr>(func));
}

//  a Python function taken by a CuteQModbusRequest, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusRequest(
    QModbusRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusRequest *>(self)->take(key, call);
}
