//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QModbusPdu that Python can take functions over in. Every QModbusPdu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQModbusPduCall0)(const void *, int, int *);
class CuteQModbusPdu : public QModbusPdu {
public:
  using QModbusPdu::QModbusPdu;
  CuteQModbusPdu(const QModbusPdu & other) : QModbusPdu(other) {}
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
      CuteQModbusPduCall0 call = reinterpret_cast<CuteQModbusPduCall0>(taken[0]);
      call(this, static_cast<int>(code), &handled);
      if (handled) return;
    }
    QModbusPdu::setFunctionCode(code);
  }
};

//  QModbusPdu::QModbusPdu()
extern "C" Q_DECL_EXPORT
QModbusPdu *ritual_ZN10QModbusPduC1Ev() {
  return new CuteQModbusPdu();
}

//  QModbusPdu::~QModbusPdu()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QModbusPduD1Ev(QModbusPdu *self) {
  delete self;
}

//  bool QModbusPdu::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QModbusPdu7isValidEv(const QModbusPdu *self) {
  return self->isValid();
}

//  ExceptionCode QModbusPdu::exceptionCode() const
extern "C" Q_DECL_EXPORT
QModbusPdu::ExceptionCode ritual_ZNK10QModbusPdu13exceptionCodeEv(
    const QModbusPdu *self) {
  return self->exceptionCode();
}

//  bool QModbusPdu::isException() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QModbusPdu11isExceptionEv(const QModbusPdu *self) {
  return self->isException();
}

//  qint16 QModbusPdu::size() const
extern "C" Q_DECL_EXPORT
qint16 ritual_ZNK10QModbusPdu4sizeEv(const QModbusPdu *self) {
  return self->size();
}

//  qint16 QModbusPdu::dataSize() const
extern "C" Q_DECL_EXPORT
qint16 ritual_ZNK10QModbusPdu8dataSizeEv(const QModbusPdu *self) {
  return self->dataSize();
}

//  FunctionCode QModbusPdu::functionCode() const
extern "C" Q_DECL_EXPORT
QModbusPdu::FunctionCode ritual_ZNK10QModbusPdu12functionCodeEv(
    const QModbusPdu *self) {
  return self->functionCode();
}

//  void QModbusPdu::setFunctionCode(FunctionCode code)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE(
    QModbusPdu *self,
    QModbusPdu::FunctionCode code) {
  self->setFunctionCode(code);
}

//  QByteArray QModbusPdu::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QModbusPdu4dataEv(const QModbusPdu *self) {
  return new QByteArray(self->data());
}

//  void QModbusPdu::setData(const QByteArray &newData)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QModbusPdu7setDataERK10QByteArray(
    QModbusPdu *self,
    const QByteArray *newData) {
  self->setData(*newData);
}

//  QModbusPdu::QModbusPdu(FunctionCode code, const QByteArray &newData)
extern "C" Q_DECL_EXPORT
QModbusPdu *ritual_ZN10QModbusPduC1ENS_12FunctionCodeERK10QByteArray(
    QModbusPdu::FunctionCode code,
    const QByteArray *newData) {
  return new CuteQModbusPdu(code, *newData);
}

//  QModbusPdu::QModbusPdu(const QModbusPdu &a0)
extern "C" Q_DECL_EXPORT
QModbusPdu *ritual_ZN10QModbusPduC1ERKS_(const QModbusPdu *a0) {
  return new CuteQModbusPdu(*a0);
}

//  QModbusPdu &QModbusPdu::operator=(const QModbusPdu &a0)
extern "C" Q_DECL_EXPORT
QModbusPdu *ritual_ZN10QModbusPduaSERKS_(
    QModbusPdu *self,
    const QModbusPdu *a0) {
  return &(self->operator=(*a0));
}

//  a Python function taken by a CuteQModbusPdu, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusPdu(QModbusPdu *self, const char *key, void *call) {
  return static_cast<CuteQModbusPdu *>(self)->take(key, call);
}

//  void QModbusPdu::setFunctionCode(FunctionCode code)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QModbusPdu15setFunctionCodeENS_12FunctionCodeE(
    QModbusPdu *self,
    QModbusPdu::FunctionCode code) {
  self->QModbusPdu::setFunctionCode(code);
}
