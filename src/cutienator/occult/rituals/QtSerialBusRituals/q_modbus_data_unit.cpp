//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusdataunit.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbusdataunit.h>

//  QModbusDataUnit::QModbusDataUnit()
extern "C" Q_DECL_EXPORT
QModbusDataUnit *ritual_ZN15QModbusDataUnitC1Ev() {
  return new QModbusDataUnit();
}

//  QModbusDataUnit::QModbusDataUnit(RegisterType type)
extern "C" Q_DECL_EXPORT
QModbusDataUnit *ritual_ZN15QModbusDataUnitC1ENS_12RegisterTypeE(
    QModbusDataUnit::RegisterType type) {
  return new QModbusDataUnit(type);
}

//  QModbusDataUnit::QModbusDataUnit(RegisterType type, int newStartAddress,
//      quint16 newValueCount)
extern "C" Q_DECL_EXPORT
QModbusDataUnit *ritual_ZN15QModbusDataUnitC1ENS_12RegisterTypeEit(
    QModbusDataUnit::RegisterType type,
    int newStartAddress,
    quint16 newValueCount) {
  return new QModbusDataUnit(type, newStartAddress, newValueCount);
}

//  RegisterType QModbusDataUnit::registerType() const
extern "C" Q_DECL_EXPORT
QModbusDataUnit::RegisterType ritual_ZNK15QModbusDataUnit12registerTypeEv(
    const QModbusDataUnit *self) {
  return self->registerType();
}

//  void QModbusDataUnit::setRegisterType(RegisterType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QModbusDataUnit15setRegisterTypeENS_12RegisterTypeE(
    QModbusDataUnit *self,
    QModbusDataUnit::RegisterType type) {
  self->setRegisterType(type);
}

//  int QModbusDataUnit::startAddress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QModbusDataUnit12startAddressEv(
    const QModbusDataUnit *self) {
  return self->startAddress();
}

//  void QModbusDataUnit::setStartAddress(int newAddress)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QModbusDataUnit15setStartAddressEi(
    QModbusDataUnit *self,
    int newAddress) {
  self->setStartAddress(newAddress);
}

//  qsizetype QModbusDataUnit::valueCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QModbusDataUnit10valueCountEv(
    const QModbusDataUnit *self) {
  return self->valueCount();
}

//  void QModbusDataUnit::setValueCount(qsizetype newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QModbusDataUnit13setValueCountEx(
    QModbusDataUnit *self,
    qsizetype newCount) {
  self->setValueCount(newCount);
}

//  void QModbusDataUnit::setValue(qsizetype index, quint16 newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QModbusDataUnit8setValueExt(
    QModbusDataUnit *self,
    qsizetype index,
    quint16 newValue) {
  self->setValue(index, newValue);
}

//  quint16 QModbusDataUnit::value(qsizetype index) const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QModbusDataUnit5valueEx(
    const QModbusDataUnit *self,
    qsizetype index) {
  return self->value(index);
}

//  bool QModbusDataUnit::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QModbusDataUnit7isValidEv(const QModbusDataUnit *self) {
  return self->isValid();
}

//  QModbusDataUnit::~QModbusDataUnit()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QModbusDataUnitD1Ev(QModbusDataUnit *self) {
  delete self;
}
