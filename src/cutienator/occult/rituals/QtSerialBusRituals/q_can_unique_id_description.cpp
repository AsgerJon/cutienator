//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanuniqueiddescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSerialBus/qcanuniqueiddescription.h>

//  QCanUniqueIdDescription::QCanUniqueIdDescription()
extern "C" Q_DECL_EXPORT
QCanUniqueIdDescription *ritual_ZN23QCanUniqueIdDescriptionC1Ev() {
  return new QCanUniqueIdDescription();
}

//  QCanUniqueIdDescription::QCanUniqueIdDescription(const
//      QCanUniqueIdDescription &other)
extern "C" Q_DECL_EXPORT
QCanUniqueIdDescription *ritual_ZN23QCanUniqueIdDescriptionC1ERKS_(
    const QCanUniqueIdDescription *other) {
  return new QCanUniqueIdDescription(*other);
}

//  QCanUniqueIdDescription::~QCanUniqueIdDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCanUniqueIdDescriptionD1Ev(QCanUniqueIdDescription *self) {
  delete self;
}

//  bool QCanUniqueIdDescription::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QCanUniqueIdDescription7isValidEv(
    const QCanUniqueIdDescription *self) {
  return self->isValid();
}

//  QtCanBus::DataSource QCanUniqueIdDescription::source() const
extern "C" Q_DECL_EXPORT
QtCanBus::DataSource ritual_ZNK23QCanUniqueIdDescription6sourceEv(
    const QCanUniqueIdDescription *self) {
  return self->source();
}

//  void QCanUniqueIdDescription::setSource(QtCanBus::DataSource source)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCanUniqueIdDescription9setSourceEN8QtCanBus10DataSourceE(
    QCanUniqueIdDescription *self,
    QtCanBus::DataSource source) {
  self->setSource(source);
}

//  quint16 QCanUniqueIdDescription::startBit() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK23QCanUniqueIdDescription8startBitEv(
    const QCanUniqueIdDescription *self) {
  return self->startBit();
}

//  void QCanUniqueIdDescription::setStartBit(quint16 bit)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCanUniqueIdDescription11setStartBitEt(
    QCanUniqueIdDescription *self,
    quint16 bit) {
  self->setStartBit(bit);
}

//  quint8 QCanUniqueIdDescription::bitLength() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK23QCanUniqueIdDescription9bitLengthEv(
    const QCanUniqueIdDescription *self) {
  return self->bitLength();
}

//  void QCanUniqueIdDescription::setBitLength(quint8 length)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCanUniqueIdDescription12setBitLengthEh(
    QCanUniqueIdDescription *self,
    quint8 length) {
  self->setBitLength(length);
}

//  QSysInfo::Endian QCanUniqueIdDescription::endian() const
extern "C" Q_DECL_EXPORT
QSysInfo::Endian ritual_ZNK23QCanUniqueIdDescription6endianEv(
    const QCanUniqueIdDescription *self) {
  return self->endian();
}

//  void QCanUniqueIdDescription::setEndian(QSysInfo::Endian endian)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCanUniqueIdDescription9setEndianEN8QSysInfo6EndianE(
    QCanUniqueIdDescription *self,
    QSysInfo::Endian endian) {
  self->setEndian(endian);
}
