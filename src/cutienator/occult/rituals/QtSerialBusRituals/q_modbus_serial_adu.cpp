//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusadu_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, instances of templates of the
//  class: 2. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusadu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtSerialBus/QModbusPdu>

//  QModbusSerialAdu::QModbusSerialAdu(Type type, const QByteArray &data)
extern "C" Q_DECL_EXPORT
QModbusSerialAdu *ritual_ZN16QModbusSerialAduC1ENS_4TypeERK10QByteArray(
    QModbusSerialAdu::Type type,
    const QByteArray *data) {
  return new QModbusSerialAdu(type, *data);
}

//  int QModbusSerialAdu::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QModbusSerialAdu4sizeEv(const QModbusSerialAdu *self) {
  return self->size();
}

//  QByteArray QModbusSerialAdu::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QModbusSerialAdu4dataEv(
    const QModbusSerialAdu *self) {
  return new QByteArray(self->data());
}

//  int QModbusSerialAdu::rawSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QModbusSerialAdu7rawSizeEv(const QModbusSerialAdu *self) {
  return self->rawSize();
}

//  QByteArray QModbusSerialAdu::rawData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QModbusSerialAdu7rawDataEv(
    const QModbusSerialAdu *self) {
  return new QByteArray(self->rawData());
}

//  int QModbusSerialAdu::serverAddress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QModbusSerialAdu13serverAddressEv(
    const QModbusSerialAdu *self) {
  return self->serverAddress();
}

//  QModbusPdu QModbusSerialAdu::pdu() const
extern "C" Q_DECL_EXPORT
QModbusPdu *ritual_ZNK16QModbusSerialAdu3pduEv(
    const QModbusSerialAdu *self) {
  return new QModbusPdu(self->pdu());
}

//  bool QModbusSerialAdu::matchingChecksum() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QModbusSerialAdu16matchingChecksumEv(
    const QModbusSerialAdu *self) {
  return self->matchingChecksum();
}

//  quint8 QModbusSerialAdu::calculateLRC(const char *data, qint32 len)
extern "C" Q_DECL_EXPORT
quint8 ritual_ZN16QModbusSerialAdu12calculateLRCEPKci(
    const char *data,
    qint32 len) {
  return QModbusSerialAdu::calculateLRC(data, len);
}

//  quint16 QModbusSerialAdu::calculateCRC(const char *data, qint32 len)
extern "C" Q_DECL_EXPORT
quint16 ritual_ZN16QModbusSerialAdu12calculateCRCEPKci(
    const char *data,
    qint32 len) {
  return QModbusSerialAdu::calculateCRC(data, len);
}

//  QByteArray QModbusSerialAdu::create(Type type, int serverAddress, const
//      QModbusPdu &pdu, char delimiter)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QModbusSerialAdu6createENS_4TypeEiRK10QModbusPduc(
    QModbusSerialAdu::Type type,
    int serverAddress,
    const QModbusPdu *pdu,
    char delimiter) {
  return new QByteArray(
      QModbusSerialAdu::create(
          type,
          serverAddress,
          *pdu,
          delimiter));
}

//  quint16 QModbusSerialAdu::crc_reflect(quint16 data, qint32 len)
extern "C" Q_DECL_EXPORT
quint16 ritual_ZN16QModbusSerialAdu11crc_reflectEti(
    quint16 data,
    qint32 len) {
  return QModbusSerialAdu::crc_reflect(data, len);
}

//  QModbusSerialAdu::~QModbusSerialAdu()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusSerialAduD1Ev(QModbusSerialAdu *self) {
  delete self;
}

//  a QModbusPdu a ritual of QModbusSerialAdu gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QModbusSerialAdu__QModbusPdu(QModbusPdu *self) {
  delete self;
}

//  decltype(unsigned char()) QModbusSerialAdu::checksum<unsigned char>() const
extern "C" Q_DECL_EXPORT
unsigned char ritual_ZNK16QModbusSerialAdu8checksumIhEEDTcvT__EEv(const QModbusSerialAdu *self) {
  return self->checksum<unsigned char>();
}

//  decltype(unsigned short()) QModbusSerialAdu::checksum<unsigned short>() const
extern "C" Q_DECL_EXPORT
unsigned short ritual_ZNK16QModbusSerialAdu8checksumItEEDTcvT__EEv(const QModbusSerialAdu *self) {
  return self->checksum<unsigned short>();
}
